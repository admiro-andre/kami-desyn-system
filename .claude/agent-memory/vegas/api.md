# API do Vegas

Base: `https://api-vegas-v2.evoubuntu.it.ao/api/v1` (Laravel, respostas JSON em pt)
Cliente: `.claude/vegas/vegas.py`. Usa sempre um `User-Agent` próprio, porque o default `Python-urllib` leva **403**.

## Autenticação
- `POST /login` `{email, password}` devolve `{token, user, permissions, colaborador}`
- Header: `Authorization: Bearer <token>`. Token em cache em `.claude/vegas/.token`; ao receber 401, faz login de novo.
- Permissões do Admiro: clients/projects/teams/staff/departments.viewAny, tasks.manage, sprints.manage, ...

## Endpoints conhecidos (GET)
| Endpoint | Conteúdo |
|---|---|
| `/dropdowns/projects` | lista de projectos (sem tasks): id, name, state, priority, client, manager, team, datas |
| `/dropdowns/staff` | colaboradores. **Contém dados sensíveis (salário, BI, docs). Expor só id/name.** |
| `/projects` | lista de projectos |
| `/projects/{id}` | projecto + `tasks[]` + `task_stats` (total/completed/in_progress/pending) |
| `/dashboard` | perfil collaborator: contagem das minhas tasks por estado, overdue, equipa, sprint activa, `todo_tasks` |
| `/user` | utilizador autenticado |

Não existem (404): `/tasks`, `/tasks/{id}`, `/my-tasks`, `/sprints`, `/projects/{id}/tasks`, `/dropdowns/tasks`, `/dropdowns/sprints`.
Por isso, **as minhas tasks obtêm-se percorrendo `/projects/{id}` e filtrando `assigned_to.id == 11`.** Valida-se pelo total em `/dashboard`.

## Formato de uma task
`id, name, description, state{value,label}, priority{value,label}, complexity, value, weight, story_points, value_points,
is_urgent, due_date, start_date, finished_at, validating_at, rejected_count, was_transported, transported_at,
sprint{id,name,status}, assigned_to{id,name}, created_at, updated_at`

## Estados (task.state.value)
`pending` Pendente · `doing` Em andamento · `validating` Em Validação · `idle` Parado · `canceled` Cancelado · `done` Concluído
Os projectos usam os mesmos valores. Prioridade: `low`, `medium`, `high` (pode haver `urgent`).
