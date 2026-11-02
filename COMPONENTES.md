# Componentes Kami

Catálogo dos componentes usados nas telas do `kami-design-system-v2.html`. Cada componente aparece com uma demonstração na subsecção **Componentes mobile**, na secção *Mobile — Fluxo do cliente online* (`#m-componentes`).

Regras gerais:

- As cores, os raios e as sombras vêm só dos tokens em `:root` (ver `kami-theme.css` e a secção *Tokens & Paleta*). Não se usam cores escritas à mão.
- A fonte é Nunito em toda a aplicação.
- No mobile, o botão principal (`.m-cta`) é sempre castanho-escuro (`--on-surface`), nunca laranja. Há só um por ecrã e fica no fundo (`.m-bottom`).
- Os botões circulares (`.circ`) também usam fundo `--on-surface` e ícone branco.
- A opção escolhida tem borda ou fundo `--on-surface`. Só os estados já concluídos do pedido (ecrã 11) são verdes (`--success`). O passo em curso fica laranja (`--primary`).
- O mesmo nome de acção mantém-se em todo o fluxo. Por exemplo, "Enviar pedido" aparece tanto no levantamento como na entrega.

## Mobile — fluxo do cliente online

Telas: 1 página do restaurante · 2 menu · 3 pesquisa · 4 produtos da categoria · 5 produto adicionado · 6 detalhe do produto · 7 carrinho · 8 finalizar (levantar) · 9 finalizar com entrega · 10 pedido enviado · 11 acompanhar pedido.

| Componente | Classes | Onde | Regra |
|---|---|---|---|
| Moldura do ecrã | `.phone-stage` `.stage-nav` `.phone-label` `.phone-step` `.phone` | Todas | Fundo amarelo (`--sun`) com desenhos de comida a 20 %. Cabeçalho branco em cima, depois o indicador "(n) Nome do ecrã", depois o painel branco. Só para a apresentação; não vai para a aplicação. |
| Moldura com capa | `.phone-stage.stage-cover` | 1 | Sem cabeçalho: a capa do restaurante ocupa o topo. |
| Botão circular | `.circ` `.circ-sm` `.circ-light` | Todas | 40 px (34 px no `-sm`). `-light` = fundo branco, usado sobre imagens. |
| Cabeçalho do ecrã | `.m-nav` `.m-nav-mid > small` | 2–11 | Voltar à esquerda, título e subtítulo ao centro, acção à direita. O subtítulo diz o contexto (modo, contagem, mesa). |
| Pesquisa | `.stage-modal` `.m-backdrop` `.m-search-foot` `.m-search` `.m-search-bar` `.m-search-field` `.m-search-clear` `.m-search-cancel` `.m-search-count` `.m-search-list` `mark` | 3 (online), 7 (mesa) | Abre ao tocar na lupa do cabeçalho. O fundo desfocado e escurecido cobre o ecrã inteiro, incluindo cabeçalho e margens; só o painel fica visível. O painel desce do topo com o campo já focado. Os resultados aparecem enquanto se escreve (sem distinguir acentos) e a parte que coincide fica realçada a amarelo. Cada resultado mostra a categoria e adiciona ao carrinho sem fechar a pesquisa; o botão "Ver carrinho" fica no rodapé do painel. "Fechar" ou tocar fora volta ao ecrã anterior. |
| Título de entrada | `.m-hero h2 > strong` | 2 | Peso 400 e 900 na mesma frase. |
| Tabs de categoria | `.m-chips` `.m-chip` `.m-chip.active` | 2, 4, 5 | Deslizam na horizontal. A activa tem fundo `--on-surface`. Texto centrado. Quando é o primeiro elemento do painel, leva 14 px de espaço em cima. |
| Bloco de categoria | `.m-section` `.m-sec-head` `.m-sec-c-orange` / `-amber` / `-green` `.m-sec-link` | 2 | Uma cor suave por categoria. Mostra os 2 primeiros produtos e "Ver todos (n)". |
| Linha de produto | `.m-prod` `.m-prod-img` `.m-prod-info` `.m-prod-name` `.m-prod-desc` `.m-prod-price` | 2 | Usada dentro do bloco de categoria. |
| Cartão de produto | `.m-card` `.m-card.added` `.m-card-row` `.m-noimg` | 3, 4, 5 | O preço e o botão de adicionar ficam na mesma linha. `.added` = contorno escuro quando o produto já está no carrinho. Sem foto, mostra a inicial do nome. |
| Botão adicionar | `.m-add` | 2, 3, 4, 5, 11 | Ao tocar, junta 1 unidade sem sair da lista e transforma-se em `.m-step-sm`. |
| Contador pequeno | `.m-step-sm` | 3, 5, 7 | − quantidade +. Se chegar a 0, volta a ser `.m-add`. |
| Contador grande | `.m-stepper` | 6 | Quantidade no detalhe do produto. |
| Aviso temporário | `.m-toast` | 5 | Aparece por cima do botão do carrinho e desaparece ao fim de 3 s. "Desfazer" retira o produto. |
| Botão principal | `.m-cta` `.m-cta.bar > span + em` `.m-cta.ghost` | Todas | `.bar` mostra o valor à direita. `.ghost` serve para a acção secundária. Fica sempre dentro de `.m-bottom`. |
| Capa do restaurante | `.lnd-cover` `.lnd-head` `.lnd-logo` `.lnd-name` `.lnd-tagline` `.lnd-open` | 1 | Imagem de capa com o botão de partilhar. O logótipo sobrepõe-se à capa. Indica se está aberto e a que horas fecha. |
| Informações | `.lnd-facts` | 1 | Morada e horário, com ícones. |
| Forma de recebimento (página do restaurante) | `.lnd-modes` `.lnd-mode.pick` / `.deliv` `.on` | 1 | Levantar ou Entrega. Só pré-selecciona; pode mudar-se no Finalizar. A opção escolhida tem borda escura. |
| Ler QR Code (página do restaurante) | `.lnd-scan` `.lnd-scan-ico` `.lnd-scan-btn` | 1 | Bloco escuro "Estás no restaurante?" com o botão amarelo "Ler QR Code", que abre o leitor do fluxo na mesa. Fica antes da forma de recebimento. |
| Mais pedidos | `.lnd-pop` `.lnd-pop-item` | 1 | Lista horizontal. |
| Galeria de fotos | `.m-photo` `.m-dots > i.on` | 6 | Até 5 fotos por produto (fotos são opcionais). |
| Linha do carrinho | `.m-cart-item` `.m-rm` | 7 | Mostra a observação do produto. O lixo remove o produto. |
| Resumo de valores | `.m-summary` `.m-summary .tot` | 7–10 | A última linha (`.tot`) é o total. |
| Forma de recebimento (finalizar) | `.m-seg > span.on` | 8, 9 | Levantar / Entrega. A opção escolhida tem fundo escuro. |
| Campos de texto | `.field` `.field-label` `.field-opt` `.input` `.input-ph` `.textarea` `.field-hint` | 6, 8, 9 | Partilhados com o back-office. Pede-se só nome e telemóvel; o cliente não cria conta. |
| Forma de pagamento | `.m-pay` `.m-pay-opt.on` `.m-radio` `.m-pay-ico` | 8, 9 | Dinheiro, Multicaixa (TPA) ou Transferência. A escolhida tem borda e rádio escuros. Ícone de 36 px (cantos de 9 px) entre o rádio e o texto: Multicaixa = `imagem-references/mcx.webp`; Dinheiro e Transferência = símbolos `#pay-cash` e `#pay-transfer` no sprite, com o mesmo formato (quadrado arredondado, fundo sólido, desenho branco e nome em baixo). Só informa o restaurante; no MVP o pagamento não passa pela plataforma. |
| Mapa e morada | `.m-map` `.m-map-zone` `.m-map-pin` `.m-addr` `.m-zone-ok` `.m-link` | 9 (`.m-addr` também no 8) | A zona de entrega aparece a tracejado. O cliente confirma o ponto ou escreve a morada à mão. |
| À espera de aceitação | `.m-wait` `.m-linkbox` | 10 | O anel roda até o restaurante aceitar (pára se o utilizador pedir menos movimento). O link do pedido substitui a conta. |
| Estimativa e estados | `.m-estimate` `.timeline` `.tl-item` `.tl-dot.done` / `.now` / `.wait` | 11 | Concluído = verde, em curso = laranja, por fazer = vazio. A estimativa só aparece depois de o restaurante aceitar o pedido. |
| Sugestão de novo pedido | `.m-again` `.m-again-item` | 11 | Aparece com o botão "Fazer outro pedido". O novo pedido é separado do actual. |

Fotos: só para a apresentação, as imagens de produtos, capa, galeria e leitor estão em `assets/fotos/` (descarregadas uma vez da Foodish API) e entram como `background` com `center/cover` sobre `--canvas`. A capa leva por cima um degradê escuro (`--on-surface` a 45 % → transparente) para o botão de partilhar se ver. O "Frango grelhado" fica sem foto de propósito, para mostrar `.m-noimg`. Na aplicação real as fotos vêm do catálogo do restaurante.

Ícones: sprite SVG no topo do HTML (`<use href="#i-nome"/>`), traço de 2 px. Dentro de um elemento usa-se `.ico`; dentro de `.circ` o `<svg>` não leva classe. Ícones disponíveis: `x flash qr keyboard orders history table box team map billing settings home bell search back filter plus minus check cart pin pinfill clock platform share copy trash bag scooter locate`.

## Mobile — fluxo na mesa (QR Code)

Telas: 1 ler QR Code · 2 escrever o código · 3 entrada na mesa · 4 convidar amigos · 5 mesa já ocupada · 6 menu da mesa · 7 pesquisa · 8 detalhe do produto · 9 carrinho da mesa · 10 pedidos do atendimento · 11 atendimento encerrado.

Reutiliza os componentes do fluxo online (cabeçalho, tabs, blocos de categoria, linha de produto, contadores, galeria, linha do carrinho, resumo, botão principal, fundo desfocado `.stage-modal` + `.m-backdrop`, pesquisa `.m-search`). Diferenças: o subtítulo do cabeçalho é sempre "Mesa n"; não há forma de recebimento, nome, telemóvel nem forma de pagamento; o botão de envio chama-se "Enviar pedido", como no fluxo online.

| Componente | Classes | Onde | Regra |
|---|---|---|---|
| Leitor de QR Code | `.m-cam` `.m-cam-hint` `.m-cam-frame` `.m-cam-line` `.m-cam-actions` | 1 | Imagem da câmara a ocupar o painel. Fora do quadrado escurece (`--on-surface` a 68 %). Cantos em `--sun`; a linha amarela percorre o quadrado (pára com menos movimento). Lanterna num `.circ-light`. |
| QR Code | `.m-qr[data-qr]` `.m-qr-card` `.m-qr-tag` | 1, 4 | Gerado no browser pela `qrcode-generator` (cópia local em `assets/js/qrcode.min.js`) a partir do endereço em `data-qr`, nível de correcção Q, cor `--on-surface` sobre branco. O cartão leva por baixo a etiqueta "Mesa n" em `--sun`. |
| Código da mesa | `.m-code` `.m-code span.cur` `.m-code i` `.m-code-where` | 2 | Alternativa ao QR Code (README RPQ-10), para câmara avariada ou código ilegível. 6 caixas (3 + 3, com traço ao meio), letras e números, sem distinguir maiúsculas. A caixa activa tem borda escura e cursor. Um desenho do cartão da mesa mostra onde o código está impresso (por baixo do QR Code). "Entrar na mesa" fica desactivado (`.m-cta[disabled]`) até o código estar completo. |
| Botão "escrever código" | `.m-cta.ghost` + `#i-keyboard` | 1 | No fundo do leitor. Leva ao ecrã 2. |
| Modal centrado | `.m-sheet` `.m-sheet-head` `.m-sheet-note` | 4 | Sobre `.m-backdrop` que cobre o ecrã inteiro. Título, fechar (`.circ-sm` com `#i-x`), texto, conteúdo e um botão principal. |
| Dois botões no fundo | `.m-bottom-2` | 3 | Acção secundária (`.m-cta.ghost`) por cima da principal. Ícone dentro do botão com `.ico`. |
| Número da mesa | `.m-tent` `.m-tent.busy` | 3, 5 | Elemento de destaque do fluxo: lembra o cartão com o número da mesa. Número a 84 px, peso 900. `.busy` esbate o número e usa `--warning-s` quando a mesa já tem atendimento aberto. |
| Faixa do atendimento | `.m-session` `.m-session-dot` | 6 | Fundo `--success-s`. Diz a hora de abertura e leva aos pedidos já feitos ("Pedidos (n)"). |
| Pedido do atendimento | `.m-order` `.m-order.is-served` `.m-order-head` `.m-order-note` `.m-order-foot` | 10 | Um cartão por pedido, o mais recente em cima. Estado com `.badge`: À espera (`b-new`), Em preparação (`b-prep`, com o tempo numa `.m-order-note`), Servido (`b-ready`, cartão esbatido). O tempo só aparece depois de a cozinha aceitar. |
| Nota informativa | `.m-info` `.m-info.warn` | 3, 5, 9, 11 | Uma frase que explica a regra. `.warn` quando a acção está bloqueada. |
| Fim do atendimento | `.m-done` | 11 | O atendimento é fechado por um funcionário no back-office. Depois disso já não se enviam pedidos; para voltar a pedir, lê-se o QR Code de novo. |

Regras de sessão (README 11.1): uma mesa só tem um atendimento aberto de cada vez. Quem abriu o atendimento pode convidar amigos (ecrã 4; README 11.2): o QR Code de convite leva ao mesmo atendimento e deixa de funcionar quando o atendimento fecha. Quem lê o QR Code da mesa sem convite, com a mesa ocupada, vê o ecrã 5 e só pode ver o menu. "Pedir a conta" (ecrã 10) é uma proposta ainda por validar.

Estados (README 12.2): `A_ESPERA` → `EM_PREPARACAO` → `PRONTO` → `ENTREGUE`. Na mesa, os rótulos são À espera (`b-new`), Em preparação (`b-prep`), Pronto e Servido (`b-ready`, o cartão fica esbatido em `ENTREGUE`). Online: À espera, Em preparação, Pronto para levantar ou A caminho, Entregue.

## Back-office

Componentes já desenhados nas secções *Back-office* do mesmo ficheiro: shell de 3 zonas (`.bo-shell`, `.bo-rail`, `.bo-sidebar`, `.bo-header`, `.bo-content`), Modo Pedido (`.bo-shell.bo-focus`), navegação (`.rail-item`, `.bo-nav`), botões (`.btn` `.btn-p` / `-s` / `-ghost` / `-d` / `-sm` / `-lg`), campos, `.toggle`, `.check`, `.tabs`, talões de pedido (`.ticket` e estados), `.badge`, `.tbl`, `.mesa`, `.alert`, `.modal`. Esta lista será detalhada quando o back-office for revisto.
