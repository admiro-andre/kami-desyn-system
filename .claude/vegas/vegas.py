"""CLI de acesso ao Vegas (gestão de projectos/tasks da Evolium).

Uso:  python .claude/vegas/vegas.py <comando> [--json] [--cache]
      --cache  mostra o resultado guardado da última consulta, sem chamar a API (imediato)
Comandos: ver COMMANDS no fim do ficheiro (registo também em .claude/agent-memory/vegas/commands.md).
"""
import concurrent.futures as cf
import contextlib
import io
import json
import sys
import urllib.error
import urllib.request
from datetime import date, datetime
from pathlib import Path

BASE = "https://api-vegas-v2.evoubuntu.it.ao/api/v1"
ROOT = Path(__file__).resolve().parents[2]
CRED_FILE = ROOT / "credencial-vegas.txt"
TOKEN_FILE = Path(__file__).with_name(".token")
CACHE_DIR = Path(__file__).with_name("cache")
MY_STAFF_ID = 11  # Admiro Tunguno André (Admiro Alfredo)

sys.stdout.reconfigure(encoding="utf-8")


def _creds():
    data = {}
    for line in CRED_FILE.read_text(encoding="utf-8").splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip().lower()] = v.strip()
    return data["email"], data["senha"]


def _request(method, path, body=None, token=None):
    req = urllib.request.Request(BASE + path, method=method)
    req.add_header("Accept", "application/json")
    req.add_header("User-Agent", "vegas-cli/1.0")  # o default Python-urllib leva 403
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    payload = None
    if body is not None:
        req.add_header("Content-Type", "application/json")
        payload = json.dumps(body).encode()
    with urllib.request.urlopen(req, payload, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def login():
    email, password = _creds()
    token = _request("POST", "/login", {"email": email, "password": password})["token"]
    TOKEN_FILE.write_text(token, encoding="utf-8")
    return token


def api(path):
    token = TOKEN_FILE.read_text(encoding="utf-8").strip() if TOKEN_FILE.exists() else login()
    try:
        return _request("GET", path, token=token)
    except urllib.error.HTTPError as e:
        if e.code != 401:
            raise
        return _request("GET", path, token=login())


def _unwrap(d):
    return d.get("data", d) if isinstance(d, dict) else d


def project_details():
    """Detalhe (com tasks) de todos os projectos."""
    projects = _unwrap(api("/dropdowns/projects"))
    with cf.ThreadPoolExecutor(8) as ex:
        return list(ex.map(lambda p: _unwrap(api(f"/projects/{p['id']}")), projects))


def my_tasks(details=None):
    tasks = []
    for proj in details if details is not None else project_details():
        for t in proj.get("tasks") or []:
            if (t.get("assigned_to") or {}).get("id") == MY_STAFF_ID:
                t["project"] = {"id": proj["id"], "name": proj["name"]}
                tasks.append(t)
    return tasks


PRIORITY_ORDER = {"urgent": 0, "high": 1, "medium": 2, "low": 3}


def _sort(tasks):
    return sorted(tasks, key=lambda t: (
        not t.get("is_urgent"),
        t.get("due_date") or "9999",
        PRIORITY_ORDER.get((t.get("priority") or {}).get("value"), 9),
    ))


def _print(tasks, as_json):
    tasks = _sort(tasks)
    if as_json:
        print(json.dumps(tasks, ensure_ascii=False, indent=1))
        return
    today = date.today().isoformat()
    print(f"{len(tasks)} task(s)\n")
    print("| ID | Task | Projecto | Estado | Prioridade | Prazo | Urgente |")
    print("|---|---|---|---|---|---|---|")
    for t in tasks:
        due = t.get("due_date") or "-"
        late = " ⚠ atrasada" if due != "-" and due < today and t["state"]["value"] not in ("done", "canceled") else ""
        print(f"| {t['id']} | {t['name']} | {t['project']['name']} | {t['state']['label']} | "
              f"{(t.get('priority') or {}).get('label', '-')} | {due}{late} | {'sim' if t.get('is_urgent') else ''} |")


def cmd_task(as_json):
    _print(my_tasks(), as_json)


def cmd_task_pendente(as_json):
    _print([t for t in my_tasks() if t["state"]["value"] == "pending"], as_json)


def _ranking_stats(details=None):
    stats = {}
    today = date.today().isoformat()
    for proj in details if details is not None else project_details():
        for t in proj.get("tasks") or []:
            a = t.get("assigned_to") or {}
            key = a.get("name") or "(sem atribuição)"
            r = stats.setdefault(key, {"name": key, "total": 0, "abertas": 0, "concluidas": 0, "canceladas": 0,
                                       "peso_total": 0, "peso_concluido": 0, "atrasadas": 0, "peso_atrasado": 0,
                                       "max_dias_atraso": 0})
            peso = t.get("weight") or 0
            r["total"] += 1
            r["peso_total"] += peso
            st = t["state"]["value"]
            if st == "done":
                r["concluidas"] += 1
                r["peso_concluido"] += peso
            elif st == "canceled":
                r["canceladas"] += 1
            else:
                r["abertas"] += 1
                due = t.get("due_date")
                if due and due[:10] < today and st not in ("done", "canceled"):
                    r["atrasadas"] += 1
                    r["peso_atrasado"] += peso
                    dias = (date.today() - date.fromisoformat(due[:10])).days
                    r["max_dias_atraso"] = max(r["max_dias_atraso"], dias)
    return list(stats.values())


def cmd_ranking(as_json):
    rows = sorted(_ranking_stats(), key=lambda r: (-r["total"], r["name"]))
    if as_json:
        print(json.dumps(rows, ensure_ascii=False, indent=1))
        return
    print("| # | Nome | Total | Abertas | Concluídas | Canceladas |")
    print("|---|---|---|---|---|---|")
    for i, r in enumerate(rows, 1):
        print(f"| {i} | {r['name']} | {r['total']} | {r['abertas']} | {r['concluidas']} | {r['canceladas']} |")


def cmd_ranking_peso(as_json):
    rows = sorted(_ranking_stats(), key=lambda r: (-r["peso_total"], -r["concluidas"], r["name"]))
    if as_json:
        print(json.dumps(rows, ensure_ascii=False, indent=1))
        return
    print("| # | Nome | Peso total | Peso concluído | Total | Abertas | Concluídas | Canceladas |")
    print("|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(rows, 1):
        print(f"| {i} | {r['name']} | {r['peso_total']} | {r['peso_concluido']} | {r['total']} | "
              f"{r['abertas']} | {r['concluidas']} | {r['canceladas']} |")


def cmd_rank_concluida(as_json):
    rows = sorted(_ranking_stats(), key=lambda r: (-r["concluidas"], -r["peso_concluido"], r["name"]))
    for r in rows:
        r["taxa"] = round(100 * r["concluidas"] / r["total"]) if r["total"] else 0
    if as_json:
        print(json.dumps(rows, ensure_ascii=False, indent=1))
        return
    print("| # | Nome | Concluídas | Peso concluído | Total | Taxa de conclusão |")
    print("|---|---|---|---|---|---|")
    for i, r in enumerate(rows, 1):
        print(f"| {i} | {r['name']} | {r['concluidas']} | {r['peso_concluido']} | {r['total']} | {r['taxa']}% |")


def cmd_rank_atrasada(as_json):
    rows = _ranking_stats()
    for r in rows:
        r["taxa_atraso"] = round(100 * r["atrasadas"] / r["abertas"]) if r["abertas"] else 0
    rows.sort(key=lambda r: (-r["atrasadas"], -r["taxa_atraso"], r["name"]))
    if as_json:
        print(json.dumps(rows, ensure_ascii=False, indent=1))
        return
    print("| # | Nome | Atrasadas | Abertas | % abertas atrasadas | Peso atrasado | Atraso máx (dias) |")
    print("|---|---|---|---|---|---|---|")
    for i, r in enumerate(rows, 1):
        print(f"| {i} | {r['name']} | {r['atrasadas']} | {r['abertas']} | {r['taxa_atraso']}% | "
              f"{r['peso_atrasado']} | {r['max_dias_atraso']} |")


COMMANDS = {
    "ranking": cmd_ranking,
    "ranking-peso": cmd_ranking_peso,
    "rank-concluida": cmd_rank_concluida,
    "rank-atrasada": cmd_rank_atrasada,
    "task": cmd_task,
    "task-pendente": cmd_task_pendente,
}


def _cache_file(cmd, as_json):
    return CACHE_DIR / f"{cmd}{'.json' if as_json else ''}.txt"


def run(cmd, as_json):
    """Corre o comando, guarda o resultado em cache e imprime-o."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        COMMANDS[cmd](as_json)
    out = buf.getvalue()
    CACHE_DIR.mkdir(exist_ok=True)
    _cache_file(cmd, as_json).write_text(out, encoding="utf-8")
    print(out, end="")


def show_cache(cmd, as_json):
    # a resposta completa do agente (tabela + resumo) tem preferência sobre a saída crua
    answer = CACHE_DIR / f"{cmd}.md"
    f = answer if not as_json and answer.exists() else _cache_file(cmd, as_json)
    if not f.exists():
        print(f"Sem cache para '{cmd}'.")
        sys.exit(2)
    when = datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
    if not as_json:
        print(f"_cache de {when}_\n")
    print(f.read_text(encoding="utf-8"), end="")


if __name__ == "__main__":
    flags = {"--json", "--cache"}
    args = [a for a in sys.argv[1:] if a not in flags]
    if not args or args[0] not in COMMANDS:
        print("Comandos: " + ", ".join(COMMANDS))
        sys.exit(1)
    as_json = "--json" in sys.argv
    if "--cache" in sys.argv:
        show_cache(args[0], as_json)
    else:
        run(args[0], as_json)
