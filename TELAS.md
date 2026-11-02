# Telas do Kami

Gerado de `kami-screens.js`. **Não editar à mão**: altera o registo e volta a gerar.
Protótipo: `kami-app.html#/<rota>`. Vista geral: `kami-telas.html`. Cada tela do protótipo traz `data-screen="<ID>"` no elemento raiz.

## Como pedir uma tela ao Claude (Angular)
> Implementa **CLI-03** em Angular usando `kami-theme.css` (tokens `--evo-*`) e os componentes de `kami-components.css`. Segue o protótipo em `kami-app.html#/c/cart`.

Convenções: componentes *standalone*, uma pasta por tela em `src/app/features/<pasta>`, rotas com `loadComponent`, estado de pedido/carrinho num serviço com signals. Cores, raios e tipografia só por `var(--evo-*)` e `var(--kami-*)`.

## Índice
| ID | Tela | Rota do protótipo | Rota Angular | Componente | Pasta |
|---|---|---|---|---|---|
| ENT-01 | Splash | `#/a/splash` | `/` | `SplashPage` | `auth/splash` |
| ENT-02 | Entrar | `#/a/login` | `/entrar` | `LoginPage` | `auth/login` |
| ENT-03 | Recuperar palavra-passe | `#/a/recuperar` | `/recuperar` | `RecoverPage` | `auth/recover` |
| ENT-04 | Registo, passo 1: conta | `#/a/registo` | `/registo` | `RegisterAccountPage` | `auth/register/account` |
| ENT-05 | Registo, passo 2: restaurante | `#/a/registo-restaurante` | `/registo/restaurante` | `RegisterRestaurantPage` | `auth/register/restaurant` |
| ENT-06 | Registo, passo 3: plano | `#/a/registo-plano` | `/registo/plano` | `RegisterPlanPage` | `auth/register/plan` |
| ENT-07 | Registo concluído | `#/a/registo-ok` | `/registo/concluido` | `RegisterDonePage` | `auth/register/done` |
| LND-01 | Landing Kami (para restaurantes) | `#/l/kami` | `/` | `HomePage` | `marketing/home` |
| LND-02 | Landing do restaurante (página pública) | `#/l/restaurante` | `/:slug` | `RestaurantLandingPage` | `public/restaurant` |
| CLI-01 | Menu | `#/c/menu` | `/:slug/menu` | `MenuPage` | `public/order/menu` |
| CLI-02 | Detalhe do produto | `#/c/produto` | `/:slug/produto/:id` | `ProductPage` | `public/order/product` |
| CLI-03 | Carrinho | `#/c/cart` | `/:slug/carrinho` | `CartPage` | `public/order/cart` |
| CLI-04 | Finalizar pedido | `#/c/checkout` | `/:slug/finalizar` | `CheckoutPage` | `public/order/checkout` |
| CLI-05 | Pedido enviado | `#/c/confirmacao` | `/:slug/pedido/:id/enviado` | `OrderSentPage` | `public/order/sent` |
| CLI-06 | Acompanhar pedido | `#/c/track` | `/:slug/pedido/:id` | `TrackPage` | `public/order/track` |
| CLI-07 | Restaurante fechado | `#/c/fechado` | `/:slug/fechado` | `ClosedPage` | `public/order/closed` |
| CLI-08 | Fora da zona de entrega | `#/c/foradazona` | `/:slug/fora-da-zona` | `OutOfZonePage` | `public/order/out-of-zone` |
| MES-00 | Ler QR Code | `#/m/ler` | `/ler` | `QrScanPage` | `public/table/scan` |
| MES-00b | Escrever o código da mesa | `#/m/codigo` | `/codigo` | `TableCodePage` | `public/table/code` |
| MES-01 | Entrada por QR Code | `#/m/scan` | `/:slug/mesa/:token` | `TableStartPage` | `public/table/start` |
| MES-01c | Convidar amigos (modal) | `#/m/convidar` | `(diálogo sobre /:slug/mesa/:token)` | `TableInviteDialog` | `public/table/invite-dialog` |
| MES-01b | Mesa já ocupada (aviso) | `#/m/ocupada` | `/:slug/mesa/:token` (estado) | `TableStartPage` | `public/table/start` |
| MES-02 | Menu da mesa | `#/m/menu` | `/:slug/mesa/:token/menu` | `TableMenuPage` | `public/table/menu` |
| MES-02s | Pesquisa (mesa) | `#/m/pesquisa` | `(diálogo sobre /:slug/mesa/:token/menu)` | `MenuSearchDialog` | `public/shared/menu-search-dialog` |
| MES-03 | Detalhe do produto (mesa) | `#/m/produto` | `/:slug/mesa/:token/produto/:id` | `TableProductPage` | `public/table/product` |
| MES-04 | Carrinho da mesa | `#/m/cart` | `/:slug/mesa/:token/carrinho` | `TableCartPage` | `public/table/cart` |
| MES-05 | Pedidos do atendimento | `#/m/session` | `/:slug/mesa/:token/pedidos` | `TableSessionPage` | `public/table/session` |
| MES-06 | Atendimento encerrado | `#/m/encerrado` | `/:slug/mesa/:token/encerrado` | `TableClosedPage` | `public/table/closed` |
| BO-01 | Pedidos (quadro) | `#/b/pedidos` | `/admin/pedidos` | `OrdersBoardPage` | `admin/orders/board` |
| BO-11 | Modal: novo pedido (som + aceitar) | `#/b/novo-pedido` | `(diálogo sobre /admin/pedidos)` | `NewOrderDialog` | `admin/orders/new-order-dialog` |
| BO-02 | Detalhe do pedido | `#/b/pedido` | `/admin/pedidos/:id` | `OrderDetailPage` | `admin/orders/detail` |
| BO-03 | Histórico de pedidos | `#/b/historico` | `/admin/historico` | `OrdersHistoryPage` | `admin/orders/history` |
| BO-04 | Mesas e atendimentos | `#/b/mesas` | `/admin/mesas` | `TablesPage` | `admin/tables` |
| BO-05 | Produtos | `#/b/produtos` | `/admin/produtos` | `ProductsPage` | `admin/catalog/products` |
| BO-06 | Categorias | `#/b/categorias` | `/admin/categorias` | `CategoriesPage` | `admin/catalog/categories` |
| BO-07 | Zonas de entrega | `#/b/zonas` | `/admin/zonas` | `DeliveryZonesPage` | `admin/delivery-zones` |
| BO-08 | Equipa | `#/b/equipa` | `/admin/equipa` | `TeamPage` | `admin/team` |
| BO-09 | Plano e facturação | `#/b/plano` | `/admin/plano` | `BillingPage` | `admin/billing` |
| BO-10 | Definições | `#/b/definicoes` | `/admin/definicoes` | `SettingsPage` | `admin/settings` |
| PLT-01 | Visão geral da plataforma | `#/p/dashboard` | `/plataforma` | `PlatformDashboardPage` | `platform/dashboard` |
| PLT-02 | Restaurantes | `#/p/restaurantes` | `/plataforma/restaurantes` | `RestaurantsPage` | `platform/restaurants` |
| PLT-03 | Detalhe do restaurante | `#/p/restaurante` | `/plataforma/restaurantes/:id` | `RestaurantDetailPage` | `platform/restaurant-detail` |
| PLT-04 | Planos | `#/p/planos` | `/plataforma/planos` | `PlansPage` | `platform/plans` |

## Entrada

### ENT-01, Splash
- Protótipo: `kami-app.html#/a/splash` (ecrã de telemóvel, 400x800)
- Angular: `auth/splash` → `SplashPageComponent`, rota `/`
- Dados: sessão (token)
- Navega para: ENT-02

### ENT-02, Entrar
- Protótipo: `kami-app.html#/a/login` (ecrã largo, 1280x800)
- Angular: `auth/login` → `LoginPageComponent`, rota `/entrar`
- Dados: email, palavra-passe
- Navega para: BO-01, PLT-01, ENT-03, ENT-04

### ENT-03, Recuperar palavra-passe
- Protótipo: `kami-app.html#/a/recuperar` (ecrã largo, 1280x800)
- Angular: `auth/recover` → `RecoverPageComponent`, rota `/recuperar`
- Dados: email
- Navega para: ENT-02

### ENT-04, Registo, passo 1: conta
- Protótipo: `kami-app.html#/a/registo` (ecrã largo, 1280x800)
- Angular: `auth/register/account` → `RegisterAccountPageComponent`, rota `/registo`
- Dados: nome, email, telefone, palavra-passe, termos
- Navega para: ENT-05, ENT-02

### ENT-05, Registo, passo 2: restaurante
- Protótipo: `kami-app.html#/a/registo-restaurante` (ecrã largo, 1280x800)
- Angular: `auth/register/restaurant` → `RegisterRestaurantPageComponent`, rota `/registo/restaurante`
- Dados: nome, slug, zona, horário, tipos de pedido
- Navega para: ENT-06

### ENT-06, Registo, passo 3: plano
- Protótipo: `kami-app.html#/a/registo-plano` (ecrã largo, 1280x800)
- Angular: `auth/register/plan` → `RegisterPlanPageComponent`, rota `/registo/plano`
- Dados: plano (Start | Premium)
- Navega para: ENT-07

### ENT-07, Registo concluído
- Protótipo: `kami-app.html#/a/registo-ok` (ecrã largo, 1280x800)
- Angular: `auth/register/done` → `RegisterDonePageComponent`, rota `/registo/concluido`
- Dados: nenhum
- Navega para: BO-01

## Landing

### LND-01, Landing Kami (para restaurantes)
- Protótipo: `kami-app.html#/l/kami` (ecrã largo, 1280x800)
- Angular: `marketing/home` → `HomePageComponent`, rota `/`
- Dados: planos (estático)
- Navega para: ENT-04, ENT-02

### LND-02, Landing do restaurante (página pública)
- Protótipo: `kami-app.html#/l/restaurante` (ecrã largo, 1280x800)
- Angular: `public/restaurant` → `RestaurantLandingPageComponent`, rota `/:slug`
- Dados: Restaurante, horário, estado aberto/fechado
- Navega para: CLI-01, CLI-07

## Cliente online

### CLI-01, Menu
- Protótipo: `kami-app.html#/c/menu` (ecrã de telemóvel, 400x800)
- Angular: `public/order/menu` → `MenuPageComponent`, rota `/:slug/menu`
- Dados: Categoria[], Produto[], modo (levantamento | entrega), Carrinho
- Navega para: CLI-02, CLI-03, CLI-07

### CLI-02, Detalhe do produto
- Protótipo: `kami-app.html#/c/produto` (ecrã de telemóvel, 400x800)
- Angular: `public/order/product` → `ProductPageComponent`, rota `/:slug/produto/:id`
- Dados: Produto, quantidade, observação
- Navega para: CLI-01

### CLI-03, Carrinho
- Protótipo: `kami-app.html#/c/cart` (ecrã de telemóvel, 400x800)
- Angular: `public/order/cart` → `CartPageComponent`, rota `/:slug/carrinho`
- Dados: Carrinho, observação do pedido
- Navega para: CLI-04, CLI-01

### CLI-04, Finalizar pedido
- Protótipo: `kami-app.html#/c/checkout` (ecrã de telemóvel, 400x800)
- Angular: `public/order/checkout` → `CheckoutPageComponent`, rota `/:slug/finalizar`
- Dados: modo, nome, telefone, local de entrega, zona, taxa
- Navega para: CLI-05, CLI-08, CLI-03

### CLI-05, Pedido enviado
- Protótipo: `kami-app.html#/c/confirmacao` (ecrã de telemóvel, 400x800)
- Angular: `public/order/sent` → `OrderSentPageComponent`, rota `/:slug/pedido/:id/enviado`
- Dados: Pedido (número, total)
- Navega para: CLI-06

### CLI-06, Acompanhar pedido
- Protótipo: `kami-app.html#/c/track` (ecrã de telemóvel, 400x800)
- Angular: `public/order/track` → `TrackPageComponent`, rota `/:slug/pedido/:id`
- Dados: Pedido.estado (novo, em preparação, pronto, concluído), estimativa
- Navega para: CLI-01

### CLI-07, Restaurante fechado
- Protótipo: `kami-app.html#/c/fechado` (ecrã de telemóvel, 400x800)
- Angular: `public/order/closed` → `ClosedPageComponent`, rota `/:slug/fechado`
- Dados: horário, estado aberto/fechado
- Navega para: LND-02

### CLI-08, Fora da zona de entrega
- Protótipo: `kami-app.html#/c/foradazona` (ecrã de telemóvel, 400x800)
- Angular: `public/order/out-of-zone` → `OutOfZonePageComponent`, rota `/:slug/fora-da-zona`
- Dados: local, zonas de entrega
- Navega para: CLI-04

## Cliente na mesa

### MES-01, Entrada por QR Code
- Protótipo: `kami-app.html#/m/scan` (ecrã de telemóvel, 400x800)
- Angular: `public/table/start` → `TableStartPageComponent`, rota `/:slug/mesa/:token`
- Dados: Mesa, atendimento activo
- Navega para: MES-02, MES-06

### MES-02, Menu da mesa
- Protótipo: `kami-app.html#/m/menu` (ecrã de telemóvel, 400x800)
- Angular: `public/table/menu` → `TableMenuPageComponent`, rota `/:slug/mesa/:token/menu`
- Dados: Produto[], Carrinho, Atendimento
- Navega para: MES-03, MES-04, MES-05

### MES-03, Detalhe do produto (mesa)
- Protótipo: `kami-app.html#/m/produto` (ecrã de telemóvel, 400x800)
- Angular: `public/table/product` → `TableProductPageComponent`, rota `/:slug/mesa/:token/produto/:id`
- Dados: Produto, quantidade, observação
- Navega para: MES-02

### MES-04, Carrinho da mesa
- Protótipo: `kami-app.html#/m/cart` (ecrã de telemóvel, 400x800)
- Angular: `public/table/cart` → `TableCartPageComponent`, rota `/:slug/mesa/:token/carrinho`
- Dados: Carrinho, observação
- Navega para: MES-05, MES-02

### MES-05, Pedidos do atendimento
- Protótipo: `kami-app.html#/m/session` (ecrã de telemóvel, 400x800)
- Angular: `public/table/session` → `TableSessionPageComponent`, rota `/:slug/mesa/:token/pedidos`
- Dados: Pedido[] do atendimento, total da mesa
- Navega para: MES-02

### MES-06, Atendimento encerrado
- Protótipo: `kami-app.html#/m/encerrado` (ecrã de telemóvel, 400x800)
- Angular: `public/table/closed` → `TableClosedPageComponent`, rota `/:slug/mesa/:token/encerrado`
- Dados: Atendimento.estado
- Navega para: MES-01

## Back-office

### BO-01, Pedidos (quadro)
- Protótipo: `kami-app.html#/b/pedidos` (ecrã largo, 1280x800)
- Angular: `admin/orders/board` → `OrdersBoardPageComponent`, rota `/admin/pedidos`
- Dados: Pedido[] por estado, som, aberto/fechado
- Navega para: BO-02, BO-11

### BO-11, Modal: novo pedido (som + aceitar)
- Protótipo: `kami-app.html#/b/novo-pedido` (ecrã largo, 1280x800)
- Angular: `admin/orders/new-order-dialog` → `NewOrderDialogComponent`, rota `(diálogo sobre /admin/pedidos)`
- Dados: Pedido novo, tempo de preparação
- Navega para: BO-01

### BO-02, Detalhe do pedido
- Protótipo: `kami-app.html#/b/pedido` (ecrã largo, 1280x800)
- Angular: `admin/orders/detail` → `OrderDetailPageComponent`, rota `/admin/pedidos/:id`
- Dados: Pedido, cronologia, cliente
- Navega para: BO-01, BO-03

### BO-03, Histórico de pedidos
- Protótipo: `kami-app.html#/b/historico` (ecrã largo, 1280x800)
- Angular: `admin/orders/history` → `OrdersHistoryPageComponent`, rota `/admin/historico`
- Dados: Pedido[] (filtros: estado, data)
- Navega para: BO-02

### BO-04, Mesas e atendimentos
- Protótipo: `kami-app.html#/b/mesas` (ecrã largo, 1280x800)
- Angular: `admin/tables` → `TablesPageComponent`, rota `/admin/mesas`
- Dados: Mesa[], Atendimento, QR Code
- Navega para: BO-02

### BO-05, Produtos
- Protótipo: `kami-app.html#/b/produtos` (ecrã largo, 1280x800)
- Angular: `admin/catalog/products` → `ProductsPageComponent`, rota `/admin/produtos`
- Dados: Produto[], 0 a 5 fotografias
- Navega para: BO-06

### BO-06, Categorias
- Protótipo: `kami-app.html#/b/categorias` (ecrã largo, 1280x800)
- Angular: `admin/catalog/categories` → `CategoriesPageComponent`, rota `/admin/categorias`
- Dados: Categoria[] (ordem)
- Navega para: BO-05

### BO-07, Zonas de entrega
- Protótipo: `kami-app.html#/b/zonas` (ecrã largo, 1280x800)
- Angular: `admin/delivery-zones` → `DeliveryZonesPageComponent`, rota `/admin/zonas`
- Dados: Zona[] (polígono, taxa, activa)
- Navega para: fim de fluxo

### BO-08, Equipa
- Protótipo: `kami-app.html#/b/equipa` (ecrã largo, 1280x800)
- Angular: `admin/team` → `TeamPageComponent`, rota `/admin/equipa`
- Dados: Funcionário[] (função, permissões)
- Navega para: fim de fluxo

### BO-09, Plano e facturação
- Protótipo: `kami-app.html#/b/plano` (ecrã largo, 1280x800)
- Angular: `admin/billing` → `BillingPageComponent`, rota `/admin/plano`
- Dados: Plano, uso, facturas
- Navega para: fim de fluxo

### BO-10, Definições
- Protótipo: `kami-app.html#/b/definicoes` (ecrã largo, 1280x800)
- Angular: `admin/settings` → `SettingsPageComponent`, rota `/admin/definicoes`
- Dados: Restaurante, horário, tipos de pedido
- Navega para: fim de fluxo

## Plataforma

### PLT-01, Visão geral da plataforma
- Protótipo: `kami-app.html#/p/dashboard` (ecrã largo, 1280x800)
- Angular: `platform/dashboard` → `PlatformDashboardPageComponent`, rota `/plataforma`
- Dados: métricas, registos recentes
- Navega para: PLT-02

### PLT-02, Restaurantes
- Protótipo: `kami-app.html#/p/restaurantes` (ecrã largo, 1280x800)
- Angular: `platform/restaurants` → `RestaurantsPageComponent`, rota `/plataforma/restaurantes`
- Dados: Restaurante[] (plano, estado)
- Navega para: PLT-03

### PLT-03, Detalhe do restaurante
- Protótipo: `kami-app.html#/p/restaurante` (ecrã largo, 1280x800)
- Angular: `platform/restaurant-detail` → `RestaurantDetailPageComponent`, rota `/plataforma/restaurantes/:id`
- Dados: Restaurante, plano, estado, pedidos recentes
- Navega para: PLT-02

### PLT-04, Planos
- Protótipo: `kami-app.html#/p/planos` (ecrã largo, 1280x800)
- Angular: `platform/plans` → `PlansPageComponent`, rota `/plataforma/planos`
- Dados: Plano[] (Start, Premium; valores por definir)
- Navega para: fim de fluxo
