# Plataforma SaaS de Gestão de Restaurantes

> Documento de visão do projecto e levantamento de requisitos aprovados — versão inicial.

## Índice

- [1. Descrição do projecto](#1-descrição-do-projecto)
- [2. Objectivos](#2-objectivos)
- [3. Utilizadores do sistema](#3-utilizadores-do-sistema)
- [4. Organização funcional](#4-organização-funcional)
- [5. Requisitos gerais do SaaS](#5-requisitos-gerais-do-saas)
- [6. Planos Start e Premium](#6-planos-start-e-premium)
- [7. Página pública do restaurante](#7-página-pública-do-restaurante)
- [8. Gestão de produtos](#8-gestão-de-produtos)
- [9. Carrinho de compras](#9-carrinho-de-compras)
- [10. Pedidos online](#10-pedidos-online)
- [11. Pedidos presenciais por QR Code](#11-pedidos-presenciais-por-qr-code)
- [12. Back-office e notificações](#12-back-office-e-notificações)
- [13. Estimativas de preparação e entrega](#13-estimativas-de-preparação-e-entrega)
- [14. Regras de negócio transversais](#14-regras-de-negócio-transversais)
- [15. Resumo dos módulos](#15-resumo-dos-módulos)
- [16. Pontos por definir](#16-pontos-por-definir)
- [17. Decisões-chave aprovadas](#17-decisões-chave-aprovadas)

---

## 1. Descrição do projecto

O projecto consiste no desenvolvimento de uma plataforma **SaaS (Software as a Service)** para a gestão de restaurantes, com foco na digitalização da apresentação de menus, recepção de pedidos, gestão do atendimento presencial e gestão de pedidos online.

A plataforma permitirá que diferentes restaurantes utilizem o mesmo sistema, cada um com o seu próprio espaço de gestão, catálogo de produtos, mesas, pedidos, configurações e página pública. Os dados e as operações de cada estabelecimento deverão permanecer isolados dos restantes.

O sistema terá dois canais principais de pedidos:

1. **Pedidos presenciais:** o cliente encontra-se dentro do restaurante, lê o QR Code associado à mesa, consulta o menu e realiza o pedido a partir do seu dispositivo.
2. **Pedidos online:** o cliente acede à página pública do restaurante através de um endereço partilhável, consulta o menu e faz um pedido para levantamento no estabelecimento ou entrega ao domicílio.

A plataforma terá um **back-office** para os funcionários e responsáveis do restaurante gerirem pedidos, produtos, mesas, sessões de atendimento e configurações do estabelecimento.

O modelo comercial será baseado em planos de subscrição, inicialmente designados **Start** e **Premium**, com limites de utilização e funcionalidades a definir. Está previsto um período experimental de 30 dias. No MVP, os pagamentos não serão processados directamente pela plataforma.

## 2. Objectivos

- Digitalizar a consulta do menu e a realização de pedidos.
- Permitir que os restaurantes recebam pedidos presenciais e online através de uma única plataforma.
- Reduzir a dependência de menus físicos e da anotação manual dos pedidos.
- Identificar automaticamente a mesa associada a um pedido presencial.
- Controlar o início e o fim do atendimento de cada mesa através de sessões.
- Facilitar a gestão e o acompanhamento dos pedidos pelo back-office.
- Informar o cliente sobre o tempo estimado de preparação e, quando aplicável, de entrega.
- Permitir que cada restaurante tenha uma presença digital própria através de uma página pública com endereço personalizável.
- Disponibilizar uma solução SaaS para vários restaurantes, mantendo os respectivos dados e configurações separados.
- Oferecer planos comerciais adequados a estabelecimentos com necessidades diferentes.

## 3. Utilizadores do sistema

### 3.1. Cliente

Poderá consultar o menu, escolher produtos, realizar pedidos, seleccionar levantamento ou entrega e consultar a estimativa temporal apresentada pelo sistema.

### 3.2. Funcionário do restaurante

Poderá receber e tratar pedidos, acompanhar o atendimento e encerrar sessões de mesas no back-office, de acordo com as permissões atribuídas.

### 3.3. Gestor ou responsável do restaurante

Poderá gerir produtos, preços, fotografias, mesas, sessões, zonas de entrega e configurações do estabelecimento.

### 3.4. Administrador da plataforma

Será responsável pela administração geral do SaaS, incluindo estabelecimentos, planos, subscrições e limites de utilização.

## 4. Organização funcional

A plataforma será organizada nos seguintes módulos:

1. **Gestão SaaS:** estabelecimentos, subscrições, planos e limites de utilização.
2. **Pedidos online:** página pública, menu, carrinho, levantamento e entrega.
3. **Pedidos presenciais:** QR Codes por mesa, sessões de atendimento e pedidos associados às mesas.
4. **Catálogo de produtos:** criação e gestão de produtos, categorias, preços, descrições e fotografias.
5. **Gestão de pedidos:** recepção, notificações, confirmação e acompanhamento dos pedidos.
6. **Estimativas temporais:** cálculo inicial com tempos base definidos pela equipa e possibilidade de evolução futura com dados históricos.

Os módulos online e presencial são distintos e devem ser tratados como fluxos diferentes, embora utilizem o mesmo catálogo e back-office.

## 5. Requisitos gerais do SaaS

| ID | Requisito | Descrição / regra |
|---|---|---|
| RG-01 | Modelo SaaS | A plataforma será disponibilizada como serviço para vários restaurantes. |
| RG-02 | Suporte multiempresa | Cada estabelecimento terá os seus dados e configurações separados dos restantes. |
| RG-03 | Planos comerciais | Existirão inicialmente os planos Start e Premium. |
| RG-04 | Período experimental | Está previsto um período de teste de 30 dias. |
| RG-05 | Gestão centralizada | A plataforma terá uma área administrativa para gerir estabelecimentos, subscrições e limites dos planos. |
| RG-06 | Limites por plano | A quantidade de contas de utilizador permitidas dependerá do plano contratado. |
| RG-07 | Pagamentos externos | No MVP, os pagamentos não serão processados directamente pela plataforma; o processo ficará fora do sistema. |

## 6. Planos Start e Premium

### 6.1. Decisão aprovada

Os dois planos incluirão os dois principais canais de pedidos. O plano Start não deverá impedir um restaurante de receber pedidos online nem de utilizar QR Codes nas mesas.

| Funcionalidade | Start | Premium |
|---|---|---|
| Pedidos online | Incluído | Incluído |
| Pedidos presenciais por QR Code | Incluído | Incluído |
| Página pública do restaurante | Incluída | Incluída |
| Gestão de produtos e pedidos | Incluída | Incluída |
| Limites de utilização | A definir | A definir |
| Funcionalidades avançadas | Diferenciação por definir | Diferenciação por definir |

A diferenciação comercial deverá privilegiar limites de utilização e funcionalidades avançadas, sem bloquear os dois módulos principais no plano Start.

### 6.2. Por definir

- Preços das subscrições.
- Limites exactos de utilização por plano.
- Quantidade de contas de utilizador permitidas em cada plano.
- Funcionalidades exclusivas do Premium.
- Regras de activação, renovação e expiração das subscrições.

## 7. Página pública do restaurante

| ID | Requisito | Descrição / regra |
|---|---|---|
| RP-01 | Página pública individual | Cada restaurante terá uma página pública própria. |
| RP-02 | URL personalizável | O estabelecimento poderá escolher um identificador para o endereço, desde que esteja disponível. |
| RP-03 | Endereço partilhável | O endereço poderá ser partilhado com clientes, por exemplo, através do WhatsApp e das redes sociais. |
| RP-04 | Menu digital | A página permitirá consultar os produtos disponibilizados pelo restaurante. |
| RP-05 | Realização de pedidos | O cliente poderá seleccionar produtos e avançar para a realização do pedido. |

Exemplo ilustrativo de endereço:

`https://dominio-do-saas.ao/restaurante-quilamba`

O domínio definitivo ainda não foi escolhido. O endereço acima é apenas um exemplo.

## 8. Gestão de produtos

| ID | Requisito | Descrição / regra |
|---|---|---|
| RP-06 | Nome obrigatório | Cada produto deverá ter um nome. |
| RP-07 | Preço obrigatório | Cada produto deverá ter um preço definido. |
| RP-08 | Categoria obrigatória | Cada produto deverá estar associado a uma categoria. |
| RP-09 | Descrição opcional | O restaurante poderá cadastrar um produto sem descrição. |
| RP-10 | Fotografias opcionais | Um produto poderá ser publicado sem fotografia. |
| RP-11 | Limite de fotografias | Cada produto poderá ter entre zero e cinco fotografias. |
| RP-12 | Incentivo visual | O sistema poderá apresentar um aviso a incentivar a adição de fotografias, sem impedir a publicação. |
| RP-13 | Histórico de preços | A alteração do preço de um produto só afectará pedidos futuros. |
| RP-14 | Preservação dos pedidos anteriores | Os pedidos já realizados manterão os preços aplicáveis no momento da sua realização. |

### 8.1. Snapshot dos dados do pedido

Foi aprovada a utilização do conceito de **snapshot** para preservar os valores históricos dos pedidos.

Quando o cliente finaliza um pedido, o sistema deverá guardar os dados comerciais relevantes daquele momento, incluindo o preço unitário e a quantidade de cada produto. Alterações posteriores ao catálogo não deverão modificar os valores dos pedidos anteriores.

**Exemplo:**

- Preço no momento do pedido: 3.000 Kz.
- Novo preço definido posteriormente: 3.500 Kz.
- O pedido antigo continuará a apresentar 3.000 Kz.
- Os pedidos futuros utilizarão o novo preço de 3.500 Kz.

Esta regra protege a integridade do histórico dos pedidos, dos totais e dos relatórios financeiros.

## 9. Carrinho de compras

| ID | Requisito | Descrição / regra |
|---|---|---|
| RC-01 | Adicionar produtos | O cliente poderá adicionar produtos ao carrinho. |
| RC-02 | Editar quantidades | O cliente poderá aumentar ou diminuir a quantidade dos produtos seleccionados. |
| RC-03 | Remover produtos | O cliente poderá retirar produtos do carrinho antes de finalizar. |
| RC-04 | Rever antes de finalizar | O cliente poderá rever e corrigir o carrinho antes de submeter o pedido. |

O cliente deverá ter oportunidade de rever o carrinho e ajustar os produtos e as respectivas quantidades antes da finalização.

## 10. Pedidos online

O módulo online destina-se a clientes que acedem à página pública do restaurante, independentemente de estarem fisicamente no estabelecimento.

| ID | Requisito | Descrição / regra |
|---|---|---|
| RO-01 | Pedidos online | O cliente poderá realizar pedidos através da página pública. |
| RO-02 | Levantamento | O cliente poderá seleccionar o levantamento do pedido no estabelecimento. |
| RO-03 | Entrega ao domicílio | O cliente poderá solicitar a entrega do pedido na sua localização. |
| RO-04 | Gestão das entregas | No MVP, as entregas serão geridas pelo próprio estabelecimento, através dos seus funcionários. |
| RO-05 | Confirmação da morada | Na opção de entrega, o cliente deverá rever e confirmar a localização antes de submeter o pedido. |
| RO-06 | Levantamento sem QR Code | No fluxo online de levantamento, o cliente não terá de indicar uma mesa nem utilizar um QR Code. |

### 10.1. Recolha e validação da localização

A abordagem aprovada privilegia a recolha automática da localização, evitando obrigar o cliente a escrever toda a morada.

Fluxo previsto:

1. O cliente solicita a utilização da sua localização.
2. O sistema tenta obter as coordenadas através do dispositivo, mediante autorização do cliente.
3. O sistema compara a localização com as zonas de entrega definidas pelo restaurante.
4. O cliente revê a localização e confirma-a ou corrige-a.
5. Se a localização automática não estiver disponível ou não permitir validar a zona, deverá existir uma alternativa manual e possibilidade de confirmação pelo restaurante.

Cada restaurante poderá definir as zonas onde realiza entregas. O sistema deverá ajudar a determinar se a localização do cliente está abrangida.

**Por definir:** método técnico de configuração das zonas, por exemplo, polígonos geográficos, raios ou áreas predefinidas.

## 11. Pedidos presenciais por QR Code

Este módulo destina-se ao cliente que está dentro do restaurante, se senta numa mesa, consulta o menu através de um QR Code e realiza o pedido no seu dispositivo.

| ID | Requisito | Descrição / regra |
|---|---|---|
| RPQ-01 | QR Code por mesa | Cada mesa terá um QR Code próprio. |
| RPQ-02 | Identificação do restaurante | O QR Code deverá identificar o restaurante correspondente. |
| RPQ-03 | Identificação da mesa | A leitura do QR Code permitirá ao sistema identificar automaticamente a mesa. |
| RPQ-04 | Acesso ao menu | O QR Code encaminhará o cliente para o menu do restaurante associado à mesa. |
| RPQ-05 | Abertura da sessão | A leitura do QR Code deverá permitir ao cliente iniciar uma sessão de atendimento para aquela mesa. |
| RPQ-06 | Associação dos pedidos | Os pedidos realizados durante a sessão deverão ficar associados à respectiva sessão e mesa. |
| RPQ-07 | Controlo da sessão | O sistema deverá permitir acompanhar o início e o fim do atendimento. |
| RPQ-08 | Encerramento pelo funcionário | Um funcionário autorizado poderá encerrar a sessão através do back-office. |
| RPQ-09 | Convite para a mesma sessão | Quem abriu a sessão poderá convidar outras pessoas da mesa através de um QR Code de convite, para consultarem o menu e fazerem pedidos na mesma sessão. |
| RPQ-10 | Código manual da mesa | Cada mesa terá também um código curto (6 letras e números), impresso por baixo do QR Code no cartão da mesa. Se a câmara não funcionar ou o QR Code não for lido, o cliente poderá escrever esse código para entrar na mesa, com o mesmo efeito da leitura do QR Code. |

### 11.1. Regras para sessões activas

Foram aprovadas as seguintes regras:

- Uma mesa só poderá ter uma sessão de atendimento activa de cada vez.
- Se um cliente ler o QR Code de uma mesa que já tem uma sessão activa, o sistema não deverá criar automaticamente uma segunda sessão.
- O sistema deverá apresentar um aviso de que já existe uma sessão activa naquela mesa.
- O funcionário poderá encerrar a sessão existente através do back-office.
- O início e o fim das sessões deverão ser controlados para evitar misturar pedidos de atendimentos diferentes.

**Exemplo:** a Mesa 4 tem uma sessão activa. Se outro cliente ler o QR Code da Mesa 4, o sistema detecta a sessão existente e apresenta um aviso em vez de criar outra sessão.

### 11.2. Convidar amigos para a mesma sessão

Aprovado em 2026-11-02. Resolve o caso de várias pessoas sentadas na mesma mesa que querem pedir cada uma do seu telemóvel.

- Depois de abrir a sessão, o cliente pode tocar em **"Convidar amigos"**. O sistema mostra um **QR Code de convite** e o respectivo link, que pode ser partilhado.
- O convite é diferente do QR Code da mesa. Quem o lê **entra na sessão já aberta**: consulta o menu e faz pedidos que ficam associados à mesma mesa e à mesma sessão.
- O QR Code da mesa continua a seguir as regras de 11.1. Quem o lê com a mesa ocupada e **sem convite** vê o aviso e não pode encomendar. O aviso explica que pode pedir o convite a quem abriu a mesa.
- O convite **deixa de funcionar quando a sessão é encerrada**. Uma nova sessão gera um convite novo.
- Todos os pedidos feitos por convidados contam para o total da mesa.

**Por definir:** como atender um cliente novo, que não conhece quem abriu a sessão, quando a sessão anterior continua activa sem ter sido encerrada.

## 12. Back-office e notificações

O back-office será o ponto de controlo operacional do restaurante.

| ID | Requisito | Descrição / regra |
|---|---|---|
| RB-01 | Recepção de pedidos | Os pedidos submetidos pelos clientes deverão chegar ao back-office. |
| RB-02 | Actualização em tempo real | A equipa deverá receber novos pedidos sem depender de actualizações manuais da página. |
| RB-03 | Notificação visual | A chegada de um novo pedido deverá gerar um pop-up ou aviso visual. |
| RB-04 | Notificação sonora | O sistema deverá emitir um som para chamar a atenção da equipa. |
| RB-05 | Confirmação manual | O pedido deverá aguardar a confirmação da equipa antes de avançar para o estado seguinte. |
| RB-06 | Repetição dos avisos | Se ninguém tratar o pedido, o aviso visual e sonoro deverá repetir-se periodicamente. |
| RB-07 | Gestão de sessões | O back-office deverá permitir aos funcionários autorizados encerrar sessões de atendimento das mesas. |

### 12.1. Repetição das notificações

O sistema deverá voltar a alertar a equipa enquanto o pedido continuar sem tratamento, de acordo com as regras de notificação a definir.

Ainda não foram aprovados:

- O intervalo entre avisos, por exemplo, dois ou três minutos.
- As condições exactas para parar a repetição.
- O comportamento das notificações quando o back-office não está aberto.

### 12.2. Estados do pedido

Aprovado em 2026-11-02. Os pedidos online e os pedidos na mesa usam os mesmos quatro estados, sempre por esta ordem:

| Estado | Significado | O cliente vê (online) | O cliente vê (mesa) | Passa para |
|---|---|---|---|---|
| `A_ESPERA` | O pedido chegou ao back-office e aguarda que a equipa o aceite (RB-05, RN-03). Ainda não há estimativa. | À espera | À espera | `EM_PREPARACAO` |
| `EM_PREPARACAO` | A equipa aceitou o pedido. A partir daqui o cliente vê o tempo estimado (RT-01). | Em preparação | Em preparação | `PRONTO` |
| `PRONTO` | O pedido está pronto. | Pronto para levantar (levantamento) ou A caminho (entrega) | Pronto | `ENTREGUE` |
| `ENTREGUE` | O pedido chegou ao cliente. É o estado final. | Entregue | Servido | — |

- As transições só avançam, uma de cada vez, e são feitas pela equipa no back-office.
- A estimativa de preparação só existe a partir de `EM_PREPARACAO`. Na entrega ao domicílio, o tempo de deslocação conta a partir de `PRONTO` (RT-05).

**Por definir:** recusa e cancelamento de pedidos (se são estados próprios, em que momento são permitidos e quem os pode fazer).

## 13. Estimativas de preparação e entrega

O sistema deverá ajudar o cliente a perceber quanto tempo poderá faltar para o pedido ficar pronto ou ser entregue e ajudar a equipa a organizar o trabalho. A inspiração funcional foi a apresentação de estimativas de tempo em aplicações de transporte.

| ID | Requisito | Descrição / regra |
|---|---|---|
| RT-01 | Estimativa após aceitação | O tempo estimado só deverá ser apresentado depois de o restaurante aceitar o pedido. |
| RT-02 | Tempo base de preparação | A equipa poderá definir um tempo de preparação para os produtos. |
| RT-03 | Estimativa para o cliente | O cliente deverá poder consultar a estimativa temporal do pedido aceite. |
| RT-04 | Utilidade operacional | A estimativa deverá ajudar a equipa do restaurante a organizar a preparação dos pedidos. |
| RT-05 | Separação dos tempos | O tempo de preparação deverá ser distinto do tempo de entrega. |
| RT-06 | Evolução futura | O sistema poderá utilizar dados históricos para melhorar as estimativas numa versão posterior. |

### 13.1. Abordagem prevista para o MVP

- A equipa define o tempo base de preparação dos produtos.
- Após aceitar o pedido, o sistema utiliza essa configuração para apresentar uma estimativa.
- Quando existir entrega ao domicílio, o tempo de preparação não deverá ser confundido com o tempo de deslocação do entregador.
- A estimativa poderá evoluir futuramente com base em dados reais.

**Machine Learning não fará parte desta primeira versão.** A utilização de um modelo para aprender com os tempos reais foi discutida, mas ficou para uma versão posterior, para evitar aumentar a complexidade do MVP.

**Por definir:** cálculo para pedidos com vários produtos, influência das quantidades, cálculo do tempo de entrega e forma de apresentar actualizações ao cliente.

## 14. Regras de negócio transversais

| ID | Regra | Aplicação |
|---|---|---|
| RN-01 | Separação entre restaurantes | Os dados e as operações de cada restaurante devem permanecer isolados dos restantes estabelecimentos. |
| RN-02 | Preservação histórica | Alterações ao catálogo não devem modificar os dados comerciais dos pedidos anteriores. |
| RN-03 | Confirmação antes de avançar | Um novo pedido deve aguardar a intervenção da equipa antes de avançar no fluxo de processamento. |
| RN-04 | Identificação da mesa | Os pedidos presenciais devem estar associados à mesa e à sessão correspondentes. |
| RN-05 | Uma sessão activa por mesa | O sistema não deverá criar uma segunda sessão enquanto existir outra activa na mesma mesa. |
| RN-06 | Separação dos fluxos | Pedidos presenciais por QR Code e pedidos online devem ser tratados como módulos distintos. |
| RN-07 | Flexibilidade comercial | Os planos Start e Premium devem disponibilizar os dois módulos de pedidos. |
| RN-08 | Estimativas separadas | O tempo de preparação e o tempo de entrega devem ser tratados separadamente. |

## 15. Resumo dos módulos

### Módulo 1 — Gestão SaaS
Gestão de restaurantes, planos Start e Premium, período experimental de 30 dias, contas e limites por plano.

### Módulo 2 — Pedidos online
Página pública, URL personalizável, catálogo, carrinho, levantamento, entrega e recolha da localização.

### Módulo 3 — Pedidos presenciais
QR Code por mesa, identificação automática, sessões de atendimento e associação dos pedidos às mesas.

### Módulo 4 — Catálogo de produtos
Gestão de nomes, preços, categorias, descrições e até cinco fotografias por produto, com preservação do histórico dos preços.

### Módulo 5 — Gestão de pedidos
Recepção em tempo real, notificações visuais e sonoras, confirmação manual e repetição periódica dos avisos.

### Módulo 6 — Estimativas temporais
Tempos base definidos pela equipa, apresentação após aceitação e possibilidade de evolução com dados históricos.

## 16. Pontos por definir

Os pontos abaixo permanecem em aberto e não devem ser tratados como requisitos aprovados até serem discutidos e validados.

| Área | Decisão em falta |
|---|---|
| Planos | Preços, limites exactos de contas e funcionalidades exclusivas do Premium. |
| Produtos | Comportamento para produtos esgotados, incluindo disponibilidade e visibilidade no menu. |
| Sessões | Como tratar o cliente que encontra uma sessão activa pertencente a um atendimento anterior e não tem convite. |
| Notificações | Intervalo de repetição, condições de paragem e comportamento quando o back-office não está aberto. |
| Pedidos | Recusa e cancelamento de pedidos: se são estados próprios, quando são permitidos e quem os pode fazer. |
| Estimativas | Fórmula para calcular o tempo de pedidos com vários produtos e a estimativa de entrega. |
| Entregas | Método definitivo de configuração e validação geográfica das zonas de entrega. |
| Pagamentos | Processo operacional para registar ou confirmar pagamentos efectuados fora da plataforma. |
| Segurança | Perfis de acesso, permissões e regras de autenticação para funcionários e gestores. |
| Administração | Detalhes da gestão de subscrições, activação e expiração do período experimental. |

## 17. Decisões-chave aprovadas

- Os pedidos online e os pedidos presenciais por QR Code estarão disponíveis nos planos Start e Premium.
- Cada restaurante terá uma página pública com endereço personalizável.
- Cada mesa terá o seu próprio QR Code e o sistema controlará as sessões de atendimento.
- O carrinho permitirá editar quantidades e remover produtos.
- Os pedidos online permitirão levantamento e entrega ao domicílio.
- A localização poderá ser obtida automaticamente, com alternativa manual.
- Cada produto poderá ter até cinco fotografias, sem obrigatoriedade de adicionar imagens.
- Os preços dos pedidos anteriores serão preservados através de snapshots.
- Os novos pedidos terão notificações visuais e sonoras, com repetição periódica.
- As estimativas começarão com tempos base definidos pela equipa; o Machine Learning ficará para uma versão posterior.
- Cada mesa tem, além do QR Code, um código manual de 6 caracteres como alternativa à câmara.
- Quem abre a sessão de uma mesa pode convidar outras pessoas para a mesma sessão através de um QR Code de convite, válido até a sessão ser encerrada.
- Os pedidos passam pelos estados `A_ESPERA`, `EM_PREPARACAO`, `PRONTO` e `ENTREGUE`, por esta ordem.

---

## Estado do documento

Este README reúne a visão do projecto e os requisitos aprovados durante o levantamento inicial. Os pontos identificados como **“Por definir”** permanecem em aberto e deverão ser validados antes de se considerar a especificação completa.

**Próximo passo recomendado:** rever os requisitos, corrigir eventuais divergências e depois transformar o levantamento numa especificação formal com identificadores, prioridades, critérios de aceitação e estado de aprovação.
