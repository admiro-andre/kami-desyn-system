---
name: vegas
description: Consulta o Vegas (projectos/tasks da Evolium) através do subagent vegas. Usar com /vegas <comando>, por exemplo /vegas task (todas as minhas tasks), /vegas task-pendente (as pendentes), /vegas ranking (quem tem mais tasks atribuídas), /vegas ranking-peso (ranking pelo peso das tasks) ou /vegas rank-concluida (quem concluiu mais tasks).
argument-hint: <comando> (task | task-pendente | ranking | ranking-peso | rank-concluida | ...)
---

O utilizador pediu: `/vegas $ARGUMENTS`

Se `$ARGUMENTS` vier vazio, mostra os comandos registados em `.claude/agent-memory/vegas/commands.md` e não chames o agente.

## 1. Mostrar o cache de imediato
Na mesma mensagem, faz estas duas chamadas em paralelo:
- Bash: `python .claude/vegas/vegas.py $ARGUMENTS --cache`
- Agent com `subagent_type: "vegas"` e o prompt:
  "Executa o comando /vegas `$ARGUMENTS`. Segue a tua memória em .claude/agent-memory/vegas/."

Se o Bash devolver um resultado (código 0), mostra-o ao utilizador tal como está, incluindo a linha `_cache de ..._`.
Termina com uma única linha discreta, por exemplo: `_a actualizar em segundo plano…_`. Não digas mais nada.

Se não houver cache (código 2), diz apenas que a consulta está a correr e espera pelo agente.

## 2. Quando o agente responder
- **Havia cache e os dados são iguais** (mesmos números na tabela): responde só com `_✓ actualizado, sem alterações_`.
- **Havia cache e os dados mudaram:** escreve `_↻ actualizado_` e, logo a seguir, a tabela e o resumo do agente, sem os reescrever. Não comentes as diferenças a não ser que sejam relevantes para o Admiro, e nesse caso numa só linha.
- **Não havia cache:** mostra a tabela e o resumo devolvidos pelo agente, sem os reescrever.
