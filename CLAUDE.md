# Kami

Plataforma SaaS de gestão de restaurantes. O objectivo é desenhar **todas as telas da aplicação** — página pública e pedidos do cliente (online e na mesa), back-office (do login às configurações) e administração da plataforma — e não apenas o design system.

## Ficheiros de referência

- `README-KAMI.md` — requisitos aprovados. Pontos "Por definir" não são requisitos.
- `kami-design-system-v2.html` — design system e telas actuais. É aqui que se trabalha.
- `COMPONENTES.md` — **catálogo de todos os componentes e das suas classes**. Consultar antes de criar um componente novo, e actualizar sempre que se acrescenta ou altera um.
- `TELAS.md` — índice de telas (ENT, LND, CLI, MES, BO, PLT).
- `kami-theme.css` / `variable-tokens.md` — tokens de cor, raio e tipografia.
- `assets/fotos/` e `assets/js/` — fotos e scripts usados pelas telas, guardados localmente. Imagens novas vão para `assets/fotos/`; não apontar para URLs externos.

## Regras de trabalho

- **Sempre que houver um pedido de design ou alteração de telas, executar primeiro a skill `/frontend-design`** e seguir as suas orientações.

- Editar o `kami-design-system-v2.html` directamente; não publicar o artefacto, salvo pedido.
- Usar só os tokens da paleta Kami e a fonte Nunito.
- Cada tela mobile segue a moldura: cabeçalho branco, indicador "(n) Nome da tela", painel branco. Sem notas explicativas por cima das telas.
- Antes de dar uma tela por concluída, verificar o resultado com uma captura do Chrome em modo headless.
