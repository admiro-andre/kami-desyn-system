"""Vegas CLI: aplicação de terminal para o Vegas, com menu lateral de módulos.

Uso:  vegas   (ou python .claude/vegas/cli.py)
Layout: módulos à esquerda, comandos do módulo no topo e o conteúdo à direita.
Módulos: Projectos, Tasks e Rankings (os comandos do agente vegas). Só leitura: nunca altera dados no Vegas.
"""
import unicodedata
from concurrent.futures import ThreadPoolExecutor
from datetime import date

import vegas as v
from rich import box
from rich.console import Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from textual import work
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, DataTable, Footer, Header, Input, Label, ListItem, ListView, Static

ACCENT = "#D97757"

STATES = {  # value: (label, cor, ordem)
    "doing": ("Em andamento", "cyan", 0),
    "validating": ("Em Validação", "magenta", 1),
    "pending": ("Pendente", "yellow", 2),
    "idle": ("Parado", "bright_black", 3),
    "done": ("Concluído", "green", 4),
    "canceled": ("Cancelado", "red", 5),
}
PRIORITIES = {"urgent": ("Urgente", "bold red"), "high": ("Alta", "red"), "medium": ("Média", "yellow"),
              "low": ("Baixa", "bright_black")}

MODULES = [  # id, rótulo no menu
    ("projectos", "Projectos"),
    ("tasks", "Minhas tasks"),
    ("rankings", "Rankings"),
]
TOOLBARS = {  # comandos no topo de cada vista: (id, rótulo)
    "projectos": [("f-todos", "Todos"), ("f-abertos", "Em aberto"), ("f-meus", "Meus")],
    "detail": [("back", "← Voltar"), ("d-todas", "Todas"), ("d-abertas", "Em aberto"), ("d-minhas", "Minhas")],
    "tasks": [("t-todas", "Todas"), ("t-pendentes", "Pendentes"), ("t-abertas", "Em aberto")],
    "rankings": [("r-total", "Total de tasks"), ("r-peso", "Peso"), ("r-concluidas", "Concluídas"),
                 ("r-atrasadas", "Atrasadas")],
}


# ---------------------------------------------------------------- dados (cache da sessão)

class Store:
    def __init__(self):
        self.clear()

    def clear(self):
        self.projects = None
        self.details = {}

    def list(self):
        if self.projects is None:
            self.projects = v._unwrap(v.api("/dropdowns/projects"))
        return self.projects

    def all_details(self):
        missing = [p["id"] for p in self.list() if p["id"] not in self.details]
        with ThreadPoolExecutor(8) as ex:
            for pid, d in zip(missing, ex.map(lambda i: v._unwrap(v.api(f"/projects/{i}")), missing)):
                self.details[pid] = d
        return [self.details[p["id"]] for p in self.list()]

    @property
    def loaded(self):
        return self.projects is not None and all(p["id"] in self.details for p in self.projects)


# ---------------------------------------------------------------- formatação

def norm(s):
    return unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode().lower()


def name(obj):
    return (obj or {}).get("name") or "-"


def state_value(obj):
    return (obj.get("state") or {}).get("value")


def is_open(obj):
    return state_value(obj) not in ("done", "canceled")


def is_mine(task):
    return (task.get("assigned_to") or {}).get("id") == v.MY_STAFF_ID


def state_text(obj):
    label, color, _ = STATES.get(state_value(obj), ((obj.get("state") or {}).get("label", "-"), "white", 9))
    return Text(f"● {label}", style=color)


def state_order(obj):
    return STATES.get(state_value(obj), ("", "", 9))[2]


def priority_text(prio):
    value = prio.get("value") if isinstance(prio, dict) else prio
    label, color = PRIORITIES.get(value, (str(value or "-"), "white"))
    return Text(label, style=color)


def due_text(due, obj):
    if not due:
        return Text("-", style="bright_black")
    today = date.today().isoformat()
    if is_open(obj) and due < today:
        return Text(f"{due} ⚠", style="bold red")
    if is_open(obj) and due == today:
        return Text(f"{due} hoje", style="yellow")
    return Text(due)


def bar(done, total, width=10):
    if not total:
        return Text("sem tasks", style="bright_black")
    filled = round(width * done / total)
    t = Text("█" * filled, style="green")
    t.append("░" * (width - filled), style="bright_black")
    t.append(f" {done}/{total}")
    return t


def pct_bar(pct, width=6):
    filled = round(width * pct / 100)
    t = Text("█" * filled, style="green")
    t.append("░" * (width - filled), style="bright_black")
    t.append(f" {pct}%".rjust(5))
    return t


def num(n):
    return Text(str(n), justify="right")


def matches(query, *fields):
    return not query or any(norm(query) in norm(f) for f in fields)


# ---------------------------------------------------------------- vistas
# Cada vista devolve (título, colunas, linhas [(key, células)], resumo).

def view_projectos(details, flt, query):
    rows = []
    for p in sorted(details, key=lambda p: (state_order(p), p.get("end_date") or "9999")):
        tasks = p.get("tasks") or []
        mine = [t for t in tasks if is_mine(t)]
        if not matches(query, p["name"], name(p.get("client"))):
            continue
        if flt == "f-abertos" and not is_open(p):
            continue
        if flt == "f-meus" and not mine and (p.get("manager") or {}).get("id") != v.MY_STAFF_ID:
            continue
        done = sum(1 for t in tasks if state_value(t) == "done")
        rows.append((str(p["id"]), [
            Text(str(p["id"]), style="bright_black"), Text(p["name"], style="bold"), state_text(p),
            priority_text(p.get("priority")), name(p.get("client")), name(p.get("manager")),
            due_text(p.get("end_date"), p), bar(done, len(tasks)), num(len(mine) if mine else ""),
        ]))
    abertos = sum(1 for p in details if is_open(p))
    summary = f"{len(rows)} projecto(s) · {abertos} em aberto no total · Enter abre o projecto"
    cols = ["ID", "Projecto", "Estado", "Prioridade", "Cliente", "Gestor", "Fim", "Progresso", "Minhas"]
    return "Projectos", cols, rows, summary


def project_info(p):
    tasks = p.get("tasks") or []
    done = sum(1 for t in tasks if state_value(t) == "done")
    info = Table.grid(padding=(0, 2))
    info.add_column(style="bright_black")
    info.add_column()
    info.add_row("Estado", state_text(p))
    info.add_row("Prioridade", priority_text(p.get("priority")))
    info.add_row("Cliente", name(p.get("client")))
    info.add_row("Gestor", name(p.get("manager")))
    info.add_row("Equipa", name(p.get("team")))
    if p.get("tech_stack"):
        info.add_row("Tecnologias", p["tech_stack"])
    info.add_row("Período", Text.assemble(p.get("start_date") or "?", " → ", due_text(p.get("end_date"), p)))
    info.add_row("Progresso", bar(done, len(tasks), 20))
    if p.get("risks"):
        info.add_row("Riscos", p["risks"])
    parts = [info]
    if p.get("description"):
        parts += [Text(""), Text(p["description"], style="italic")]
    return Panel(Group(*parts), title=f"[bold]{p['name']}[/] [bright_black]#{p['id']}[/]", title_align="left",
                 border_style=ACCENT, box=box.ROUNDED, padding=(0, 2))


def view_detail(p, flt, query):
    tasks = p.get("tasks") or []
    rows = []
    for t in sorted(tasks, key=lambda t: (state_order(t), t.get("due_date") or "9999")):
        if flt == "d-abertas" and not is_open(t):
            continue
        if flt == "d-minhas" and not is_mine(t):
            continue
        if not matches(query, t["name"], name(t.get("assigned_to"))):
            continue
        rows.append((str(t["id"]), [
            Text(str(t["id"]), style="bright_black"), Text(("⚡ " if t.get("is_urgent") else "") + t["name"]),
            Text(name(t.get("assigned_to")), style=f"bold {ACCENT}" if is_mine(t) else ""), state_text(t),
            priority_text(t.get("priority")), num(t.get("weight") or "-"), due_text(t.get("due_date"), t),
            name(t.get("sprint")),
        ]))
    done = sum(1 for t in tasks if state_value(t) == "done")
    summary = f"{len(tasks)} task(s) · {done} concluída(s) · {len(tasks) - done} por concluir · Esc volta"
    cols = ["ID", "Task", "Responsável", "Estado", "Prioridade", "Peso", "Prazo", "Sprint"]
    return f"Projectos › {p['name']}", cols, rows, summary


def view_tasks(details, flt, query):
    tasks = v._sort(v.my_tasks(details))
    rows = []
    for t in tasks:
        if flt == "t-pendentes" and state_value(t) != "pending":
            continue
        if flt == "t-abertas" and not is_open(t):
            continue
        if not matches(query, t["name"], t["project"]["name"]):
            continue
        rows.append((str(t["id"]), [
            Text(str(t["id"]), style="bright_black"), t["name"], t["project"]["name"], state_text(t),
            priority_text(t.get("priority")), num(t.get("weight") or "-"), due_text(t.get("due_date"), t),
            Text("sim", style="bold red") if t.get("is_urgent") else "",
        ]))
    abertas = [t for t in tasks if is_open(t)]
    late = [t for t in abertas if (t.get("due_date") or "9999") < date.today().isoformat()]
    summary = f"{len(tasks)} task(s) · {len(tasks) - len(abertas)} concluída(s) · {len(abertas)} em aberto"
    if late:
        summary += f" · {len(late)} atrasada(s) ⚠"
    cols = ["ID", "Task", "Projecto", "Estado", "Prioridade", "Peso", "Prazo", "Urgente"]
    return "Minhas tasks", cols, rows, summary


def view_rankings(details, flt, query):
    stats = v._ranking_stats(details)
    if flt == "r-peso":
        stats.sort(key=lambda r: (-r["peso_total"], -r["concluidas"], r["name"]))
        cols = ["#", "Nome", "Peso total", "Peso concluído", "Total", "Abertas", "Concluídas"]
        cells = lambda r: [r["peso_total"], r["peso_concluido"], r["total"], r["abertas"], r["concluidas"]]
        title = "Rankings › Peso"
    elif flt == "r-concluidas":
        stats.sort(key=lambda r: (-r["concluidas"], -r["peso_concluido"], r["name"]))
        cols = ["#", "Nome", "Concluídas", "Peso concluído", "Total", "Taxa"]
        cells = lambda r: [r["concluidas"], r["peso_concluido"], r["total"],
                           pct_bar(round(100 * r["concluidas"] / r["total"]) if r["total"] else 0)]
        title = "Rankings › Concluídas"
    elif flt == "r-atrasadas":
        for r in stats:
            r["taxa_atraso"] = round(100 * r["atrasadas"] / r["abertas"]) if r["abertas"] else 0
        stats.sort(key=lambda r: (-r["atrasadas"], -r["taxa_atraso"], r["name"]))
        cols = ["#", "Nome", "Atrasadas", "Abertas", "Taxa", "Peso atrasado", "Atraso máx (dias)"]
        cells = lambda r: [r["atrasadas"], r["abertas"], pct_bar(r["taxa_atraso"]), r["peso_atrasado"],
                           r["max_dias_atraso"]]
        title = "Rankings › Atrasadas"
    else:
        stats.sort(key=lambda r: (-r["total"], r["name"]))
        cols = ["#", "Nome", "Total", "Abertas", "Concluídas", "Canceladas"]
        cells = lambda r: [r["total"], r["abertas"], r["concluidas"], r["canceladas"]]
        title = "Rankings › Total de tasks"
    rows, me = [], None
    for i, r in enumerate(stats, 1):
        mine = r["name"].startswith("Admiro")
        me = i if mine else me
        style = f"bold {ACCENT}" if mine else ""
        row = [Text(str(i), style="bright_black"), Text(r["name"], style=style)]
        row += [c if isinstance(c, Text) else Text(str(c), justify="right", style=style) for c in cells(r)]
        rows.append((r["name"], row))
    summary = f"{len(stats)} pessoa(s)" + (f" · está em {me}.º lugar" if me else "")
    return title, cols, rows, summary


# ---------------------------------------------------------------- aplicação

class VegasApp(App):
    TITLE = "Vegas"
    SUB_TITLE = "Evolium"
    CSS = f"""
    Screen {{ layout: vertical; }}
    #body {{ height: 1fr; }}
    #sidebar {{ width: 26; border-right: tall {ACCENT}; padding: 1 0; }}
    #sidebar-title {{ color: $text-muted; text-style: bold; padding: 0 2 1 2; }}
    #modules {{ background: transparent; height: auto; }}
    #modules > ListItem {{ padding: 0 2; background: transparent; }}
    #modules > ListItem.-highlight {{ background: {ACCENT} 30%; }}
    #modules:focus > ListItem.-highlight {{ background: {ACCENT}; color: white; text-style: bold; }}
    #user {{ dock: bottom; color: $text-muted; padding: 0 2; }}
    #main {{ padding: 0 1; }}
    #toolbar {{ height: auto; padding: 1 0 0 0; }}
    #toolbar Button {{ margin-right: 1; }}
    #toolbar .spacer {{ width: 1fr; }}
    #search {{ width: 32; }}
    #heading {{ text-style: bold; color: {ACCENT}; padding: 1 0 0 0; }}
    #info {{ height: auto; display: none; padding: 1 0 0 0; }}
    #table {{ height: 1fr; margin-top: 1; }}
    #summary {{ height: 1; color: $text-muted; }}
    """
    BINDINGS = [
        Binding("q", "quit", "Sair"),
        Binding("r", "refresh", "Actualizar"),
        Binding("slash", "focus_search", "Pesquisar"),
        Binding("escape", "back", "Voltar"),
        Binding("1", "module(0)", "Projectos", show=False),
        Binding("2", "module(1)", "Tasks", show=False),
        Binding("3", "module(2)", "Rankings", show=False),
    ]

    def __init__(self):
        super().__init__()
        self.store = Store()
        self.module = "projectos"
        self.project_id = None
        self.filters = {"projectos": "f-todos", "detail": "d-todas", "tasks": "t-todas", "rankings": "r-total"}
        self.query_text = ""
        self.toolbar_key = None
        self.error = None

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Horizontal(id="body"):
            with Vertical(id="sidebar"):
                yield Label("MÓDULOS", id="sidebar-title")
                yield ListView(*[ListItem(Label(label), id=f"mod-{mid}") for mid, label in MODULES], id="modules")
                yield Label("", id="user")
            with Vertical(id="main"):
                yield Horizontal(id="toolbar")
                yield Static("", id="heading")
                yield Static("", id="info")
                yield DataTable(id="table", cursor_type="row", zebra_stripes=True)
                yield Static("", id="summary")
        yield Footer()

    async def on_mount(self):
        await self.build_toolbar()
        self.load()

    # -------------------------------------------------- carregamento

    @work(thread=True, exclusive=True)
    def load(self, force=False):
        self.call_from_thread(self.set_loading, True)
        try:
            if force:
                self.store.clear()
            user = v._unwrap(v.api("/user")).get("name")
            self.store.all_details()
            self.error = None
        except Exception as e:  # sem ligação, token inválido, etc.
            user, self.error = None, str(getattr(e, "reason", e))
        self.call_from_thread(self.loaded, user)

    def set_loading(self, value):
        self.query_one("#table").loading = value

    def loaded(self, user):
        self.set_loading(False)
        if user:
            self.query_one("#user", Label).update(f"● {user}")
            self.sub_title = user
        self.render_view()
        if self.error:
            self.notify(f"Sem ligação ao Vegas: {self.error}", severity="error", timeout=8)

    # -------------------------------------------------- vista

    @property
    def view_key(self):
        return "detail" if self.module == "projectos" and self.project_id else self.module

    async def build_toolbar(self):
        key = self.view_key
        if key == self.toolbar_key:
            return
        self.toolbar_key = key
        bar = self.query_one("#toolbar")
        await bar.remove_children()
        widgets = [Button(label, id=bid, compact=True, variant="primary" if bid == self.filters[key] else "default")
                   for bid, label in TOOLBARS[key]]
        widgets.append(Static(classes="spacer"))
        if key != "rankings":
            widgets.append(Input(value=self.query_text, placeholder="/ Pesquisar…", id="search", compact=True))
        widgets.append(Button("↻ Actualizar", id="refresh", compact=True))
        await bar.mount_all(widgets)

    def render_view(self):
        table = self.query_one("#table", DataTable)
        info = self.query_one("#info", Static)
        key = self.view_key
        info.display = key == "detail"
        if not self.store.loaded:
            self.query_one("#heading", Static).update(dict(MODULES)[self.module])
            self.query_one("#summary", Static).update("A carregar…" if not self.error else "Sem dados. Prima r.")
            table.clear(columns=True)
            return
        details = self.store.all_details()
        flt = self.filters[key]
        if key == "detail":
            p = self.store.details[self.project_id]
            info.update(project_info(p))
            title, cols, rows, summary = view_detail(p, flt, self.query_text)
        else:
            fn = {"projectos": view_projectos, "tasks": view_tasks, "rankings": view_rankings}[key]
            title, cols, rows, summary = fn(details, flt, self.query_text)
        self.query_one("#heading", Static).update(title)
        self.query_one("#summary", Static).update(summary)
        table.clear(columns=True)
        table.add_columns(*cols)
        for row_key, cells in rows:
            table.add_row(*cells, key=row_key)
        if not rows:
            self.query_one("#summary", Static).update("Nada para mostrar com este filtro.")

    async def change_view(self, module=None, project_id=...):
        if module is not None:
            self.module = module
        if project_id is not ...:
            self.project_id = project_id
        self.query_text = ""
        await self.build_toolbar()
        self.render_view()

    # -------------------------------------------------- eventos

    async def on_list_view_highlighted(self, event: ListView.Highlighted):
        if event.item is not None:
            module = event.item.id.removeprefix("mod-")
            if module != self.module:
                await self.change_view(module, None)

    async def on_list_view_selected(self, event: ListView.Selected):
        self.query_one("#table").focus()

    async def on_button_pressed(self, event: Button.Pressed):
        bid = event.button.id
        if bid == "refresh":
            self.action_refresh()
        elif bid == "back":
            await self.action_back()
        else:
            self.filters[self.view_key] = bid
            for b in self.query("#toolbar Button"):
                if b.id not in ("refresh", "back"):
                    b.variant = "primary" if b.id == bid else "default"
            self.render_view()

    def on_input_changed(self, event: Input.Changed):
        self.query_text = event.value
        self.render_view()

    async def on_data_table_row_selected(self, event: DataTable.RowSelected):
        if self.view_key == "projectos" and event.row_key.value:
            await self.change_view(project_id=int(event.row_key.value))
            self.query_one("#table").focus()

    # -------------------------------------------------- acções

    def action_refresh(self):
        self.notify("A actualizar os dados do Vegas…", timeout=2)
        self.load(force=True)

    async def action_back(self):
        if self.view_key == "detail":
            await self.change_view(project_id=None)
            self.query_one("#table").focus()

    def action_focus_search(self):
        for i in self.query("#search"):
            i.focus()

    def action_module(self, index):
        self.query_one("#modules", ListView).index = index


if __name__ == "__main__":
    VegasApp().run()
