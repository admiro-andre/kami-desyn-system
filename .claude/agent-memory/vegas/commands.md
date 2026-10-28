# Comandos /vegas

Execução: `python .claude/vegas/vegas.py <comando> [--json]`. Cada comando é uma função `cmd_<nome>` em `COMMANDS`.
Neste ambiente (Windows) o atalho `python` não está disponível (abre a Microsoft Store). Usar `py -3 .claude/vegas/vegas.py <comando>` em vez disso.
Para adicionar um comando: implementar em vegas.py, depois registar aqui.
Cache: cada execução guarda a saída em `.claude/vegas/cache/<comando>.txt` (`.json.txt` com `--json`). O agente guarda a resposta final em `cache/<comando>.md`.
`--cache` mostra o último resultado sem chamar a API (prefere o `.md`); sai com código 2 se não houver cache.

| Comando | Descrição | Implementação |
|---|---|---|
| `task` | Lista todas as minhas tasks | `my_tasks()`, ordenadas (urgente, prazo, prioridade); marca ⚠ as atrasadas |
| `task-pendente` | Lista as minhas tasks pendentes | `my_tasks()` filtrado por `state.value == "pending"` |
| `ranking` | Ranking por pessoa atribuída, todos os staff: total/abertas/concluídas/canceladas, ordenado pelo total de tasks | `_ranking_stats()`: percorre `/projects/{id}` de todos os projectos e agrupa por `assigned_to.name`; abertas = estado diferente de done/canceled |
| `rank-concluida` | Ranking por tasks concluídas, todos os staff: concluídas, peso concluído, total e taxa de conclusão. Ordenado por concluídas, depois peso concluído | `_ranking_stats()`; taxa = concluídas / total |
| `ranking-peso` | Ranking por pessoa atribuída com pesos: peso total, peso concluído e contagens. Ordenado por peso total, depois por concluídas | `_ranking_stats()`; peso = soma de `weight` (null conta 0) |
| `rank-atrasada` | Ranking por tasks atrasadas, todos os staff: atrasadas, abertas, % abertas atrasadas, peso atrasado, atraso máximo (dias). Ordenado por atrasadas, depois pela taxa de atraso | `_ranking_stats()`; atrasada = `due_date` < hoje e estado fora de done/canceled (mesma regra do ⚠ em `task`); taxa = atrasadas / abertas |

### Resumo do `rank-atrasada`
Diz quem tem mais tasks atrasadas, quem tem a maior taxa de atraso (atrasadas/abertas) e a posição do Admiro.
Como as tasks do Admiro são prioridade, nomeia as atrasadas dele (id, nome, dias de atraso), não só o rank — usar `my_tasks()` com o mesmo filtro (`due_date < hoje` e estado fora de done/canceled).

## CLI (`vegas`)
`vegas.cmd` na raiz abre `.claude/vegas/cli.py`, uma aplicação de terminal em ecrã inteiro (Textual + rich, ver `requirements.txt`). Só leitura.
Layout: menu lateral de módulos à esquerda (Projectos, Minhas tasks, Rankings), comandos do módulo no topo (filtros, pesquisa, actualizar) e o conteúdo à direita.
- Projectos: filtros Todos / Em aberto / Meus; Enter abre o detalhe (ficha + tasks, filtros Todas / Em aberto / Minhas); Esc volta.
- Minhas tasks: Todas / Pendentes / Em aberto (= comandos `task` e `task-pendente`).
- Rankings: Total de tasks / Peso / Concluídas (= `ranking`, `ranking-peso`, `rank-concluida`).
Teclas: 1-3 mudam de módulo, `/` pesquisa, `r` actualiza, `q` sai. Os dados ficam em cache durante a sessão.
Usa as funções do `vegas.py` (`my_tasks`, `_ranking_stats`). Um comando novo do agente deve ganhar também um botão/vista no `cli.py` (`TOOLBARS` e a função `view_*`).
