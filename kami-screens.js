/* Registo único das telas do Kami.
   Fonte de verdade para: kami-app.html (protótipo), kami-telas.html (canvas) e TELAS.md (spec para Angular).
   Cada tela tem uma referência estável (ENT-01, CLI-03, BO-05...). Ao pedir uma tela ao Claude, usa a referência.
   rota   = hash do protótipo (kami-app.html#/<rota>)
   ang    = pasta/componente/rota sugeridos para o projecto Angular
   vai    = referências das telas para onde esta navega
   dados  = o que a tela lê ou escreve */
window.KAMI_SCREENS = [
  // ---- Entrada
  { id: 'ENT-01', rota: 'a/splash', nome: 'Splash', area: 'Entrada', tipo: 'phone', ang: ['auth/splash', 'SplashPage', '/'], vai: ['ENT-02'], dados: 'sessão (token)' },
  { id: 'ENT-02', rota: 'a/login', nome: 'Entrar', area: 'Entrada', tipo: 'web', ang: ['auth/login', 'LoginPage', '/entrar'], vai: ['BO-01', 'PLT-01', 'ENT-03', 'ENT-04'], dados: 'email, palavra-passe' },
  { id: 'ENT-03', rota: 'a/recuperar', nome: 'Recuperar palavra-passe', area: 'Entrada', tipo: 'web', ang: ['auth/recover', 'RecoverPage', '/recuperar'], vai: ['ENT-02'], dados: 'email' },
  { id: 'ENT-04', rota: 'a/registo', nome: 'Registo, passo 1: conta', area: 'Entrada', tipo: 'web', ang: ['auth/register/account', 'RegisterAccountPage', '/registo'], vai: ['ENT-05', 'ENT-02'], dados: 'nome, email, telefone, palavra-passe, termos' },
  { id: 'ENT-05', rota: 'a/registo-restaurante', nome: 'Registo, passo 2: restaurante', area: 'Entrada', tipo: 'web', ang: ['auth/register/restaurant', 'RegisterRestaurantPage', '/registo/restaurante'], vai: ['ENT-06'], dados: 'nome, slug, zona, horário, tipos de pedido' },
  { id: 'ENT-06', rota: 'a/registo-plano', nome: 'Registo, passo 3: plano', area: 'Entrada', tipo: 'web', ang: ['auth/register/plan', 'RegisterPlanPage', '/registo/plano'], vai: ['ENT-07'], dados: 'plano (Start | Premium)' },
  { id: 'ENT-07', rota: 'a/registo-ok', nome: 'Registo concluído', area: 'Entrada', tipo: 'web', ang: ['auth/register/done', 'RegisterDonePage', '/registo/concluido'], vai: ['BO-01'], dados: '' },
  // ---- Landing
  { id: 'LND-01', rota: 'l/kami', nome: 'Landing Kami (para restaurantes)', area: 'Landing', tipo: 'web', ang: ['marketing/home', 'HomePage', '/'], vai: ['ENT-04', 'ENT-02'], dados: 'planos (estático)' },
  { id: 'LND-02', rota: 'l/restaurante', nome: 'Landing do restaurante (página pública)', area: 'Landing', tipo: 'web', ang: ['public/restaurant', 'RestaurantLandingPage', '/:slug'], vai: ['CLI-01', 'CLI-07'], dados: 'Restaurante, horário, estado aberto/fechado' },
  // ---- Cliente online
  { id: 'CLI-01', rota: 'c/menu', nome: 'Menu', area: 'Cliente online', tipo: 'phone', ang: ['public/order/menu', 'MenuPage', '/:slug/menu'], vai: ['CLI-02', 'CLI-03', 'CLI-07'], dados: 'Categoria[], Produto[], modo (levantamento | entrega), Carrinho' },
  { id: 'CLI-02', rota: 'c/produto', nome: 'Detalhe do produto', area: 'Cliente online', tipo: 'phone', ang: ['public/order/product', 'ProductPage', '/:slug/produto/:id'], vai: ['CLI-01'], dados: 'Produto, quantidade, observação' },
  { id: 'CLI-03', rota: 'c/cart', nome: 'Carrinho', area: 'Cliente online', tipo: 'phone', ang: ['public/order/cart', 'CartPage', '/:slug/carrinho'], vai: ['CLI-04', 'CLI-01'], dados: 'Carrinho, observação do pedido' },
  { id: 'CLI-04', rota: 'c/checkout', nome: 'Finalizar pedido', area: 'Cliente online', tipo: 'phone', ang: ['public/order/checkout', 'CheckoutPage', '/:slug/finalizar'], vai: ['CLI-05', 'CLI-08', 'CLI-03'], dados: 'modo, nome, telefone, local de entrega, zona, taxa' },
  { id: 'CLI-05', rota: 'c/confirmacao', nome: 'Pedido enviado', area: 'Cliente online', tipo: 'phone', ang: ['public/order/sent', 'OrderSentPage', '/:slug/pedido/:id/enviado'], vai: ['CLI-06'], dados: 'Pedido (número, total)' },
  { id: 'CLI-06', rota: 'c/track', nome: 'Acompanhar pedido', area: 'Cliente online', tipo: 'phone', ang: ['public/order/track', 'TrackPage', '/:slug/pedido/:id'], vai: ['CLI-01'], dados: 'Pedido.estado (novo, em preparação, pronto, concluído), estimativa' },
  { id: 'CLI-07', rota: 'c/fechado', nome: 'Restaurante fechado', area: 'Cliente online', tipo: 'phone', ang: ['public/order/closed', 'ClosedPage', '/:slug/fechado'], vai: ['LND-02'], dados: 'horário, estado aberto/fechado' },
  { id: 'CLI-08', rota: 'c/foradazona', nome: 'Fora da zona de entrega', area: 'Cliente online', tipo: 'phone', ang: ['public/order/out-of-zone', 'OutOfZonePage', '/:slug/fora-da-zona'], vai: ['CLI-04'], dados: 'local, zonas de entrega' },
  // ---- Cliente na mesa
  { id: 'MES-01', rota: 'm/scan', nome: 'Entrada por QR Code', area: 'Cliente na mesa', tipo: 'phone', ang: ['public/table/start', 'TableStartPage', '/:slug/mesa/:token'], vai: ['MES-02', 'MES-06'], dados: 'Mesa, atendimento activo' },
  { id: 'MES-02', rota: 'm/menu', nome: 'Menu da mesa', area: 'Cliente na mesa', tipo: 'phone', ang: ['public/table/menu', 'TableMenuPage', '/:slug/mesa/:token/menu'], vai: ['MES-03', 'MES-04', 'MES-05'], dados: 'Produto[], Carrinho, Atendimento' },
  { id: 'MES-03', rota: 'm/produto', nome: 'Detalhe do produto (mesa)', area: 'Cliente na mesa', tipo: 'phone', ang: ['public/table/product', 'TableProductPage', '/:slug/mesa/:token/produto/:id'], vai: ['MES-02'], dados: 'Produto, quantidade, observação' },
  { id: 'MES-04', rota: 'm/cart', nome: 'Carrinho da mesa', area: 'Cliente na mesa', tipo: 'phone', ang: ['public/table/cart', 'TableCartPage', '/:slug/mesa/:token/carrinho'], vai: ['MES-05', 'MES-02'], dados: 'Carrinho, observação' },
  { id: 'MES-05', rota: 'm/session', nome: 'Pedidos do atendimento', area: 'Cliente na mesa', tipo: 'phone', ang: ['public/table/session', 'TableSessionPage', '/:slug/mesa/:token/pedidos'], vai: ['MES-02'], dados: 'Pedido[] do atendimento, total da mesa' },
  { id: 'MES-06', rota: 'm/encerrado', nome: 'Atendimento encerrado', area: 'Cliente na mesa', tipo: 'phone', ang: ['public/table/closed', 'TableClosedPage', '/:slug/mesa/:token/encerrado'], vai: ['MES-01'], dados: 'Atendimento.estado' },
  // ---- Back-office
  { id: 'BO-01', rota: 'b/pedidos', nome: 'Pedidos (quadro)', area: 'Back-office', tipo: 'desk', ang: ['admin/orders/board', 'OrdersBoardPage', '/admin/pedidos'], vai: ['BO-02', 'BO-11'], dados: 'Pedido[] por estado, som, aberto/fechado' },
  { id: 'BO-11', rota: 'b/novo-pedido', nome: 'Modal: novo pedido (som + aceitar)', area: 'Back-office', tipo: 'desk', ang: ['admin/orders/new-order-dialog', 'NewOrderDialog', '(diálogo sobre /admin/pedidos)'], vai: ['BO-01'], dados: 'Pedido novo, tempo de preparação' },
  { id: 'BO-02', rota: 'b/pedido', nome: 'Detalhe do pedido', area: 'Back-office', tipo: 'desk', ang: ['admin/orders/detail', 'OrderDetailPage', '/admin/pedidos/:id'], vai: ['BO-01', 'BO-03'], dados: 'Pedido, cronologia, cliente' },
  { id: 'BO-03', rota: 'b/historico', nome: 'Histórico de pedidos', area: 'Back-office', tipo: 'desk', ang: ['admin/orders/history', 'OrdersHistoryPage', '/admin/historico'], vai: ['BO-02'], dados: 'Pedido[] (filtros: estado, data)' },
  { id: 'BO-04', rota: 'b/mesas', nome: 'Mesas e atendimentos', area: 'Back-office', tipo: 'desk', ang: ['admin/tables', 'TablesPage', '/admin/mesas'], vai: ['BO-02'], dados: 'Mesa[], Atendimento, QR Code' },
  { id: 'BO-05', rota: 'b/produtos', nome: 'Produtos', area: 'Back-office', tipo: 'desk', ang: ['admin/catalog/products', 'ProductsPage', '/admin/produtos'], vai: ['BO-06'], dados: 'Produto[], 0 a 5 fotografias' },
  { id: 'BO-06', rota: 'b/categorias', nome: 'Categorias', area: 'Back-office', tipo: 'desk', ang: ['admin/catalog/categories', 'CategoriesPage', '/admin/categorias'], vai: ['BO-05'], dados: 'Categoria[] (ordem)' },
  { id: 'BO-07', rota: 'b/zonas', nome: 'Zonas de entrega', area: 'Back-office', tipo: 'desk', ang: ['admin/delivery-zones', 'DeliveryZonesPage', '/admin/zonas'], vai: [], dados: 'Zona[] (polígono, taxa, activa)' },
  { id: 'BO-08', rota: 'b/equipa', nome: 'Equipa', area: 'Back-office', tipo: 'desk', ang: ['admin/team', 'TeamPage', '/admin/equipa'], vai: [], dados: 'Funcionário[] (função, permissões)' },
  { id: 'BO-09', rota: 'b/plano', nome: 'Plano e facturação', area: 'Back-office', tipo: 'desk', ang: ['admin/billing', 'BillingPage', '/admin/plano'], vai: [], dados: 'Plano, uso, facturas' },
  { id: 'BO-10', rota: 'b/definicoes', nome: 'Definições', area: 'Back-office', tipo: 'desk', ang: ['admin/settings', 'SettingsPage', '/admin/definicoes'], vai: [], dados: 'Restaurante, horário, tipos de pedido' },
  // ---- Plataforma (SaaS)
  { id: 'PLT-01', rota: 'p/dashboard', nome: 'Visão geral da plataforma', area: 'Plataforma', tipo: 'desk', ang: ['platform/dashboard', 'PlatformDashboardPage', '/plataforma'], vai: ['PLT-02'], dados: 'métricas, registos recentes' },
  { id: 'PLT-02', rota: 'p/restaurantes', nome: 'Restaurantes', area: 'Plataforma', tipo: 'desk', ang: ['platform/restaurants', 'RestaurantsPage', '/plataforma/restaurantes'], vai: ['PLT-03'], dados: 'Restaurante[] (plano, estado)' },
  { id: 'PLT-03', rota: 'p/restaurante', nome: 'Detalhe do restaurante', area: 'Plataforma', tipo: 'desk', ang: ['platform/restaurant-detail', 'RestaurantDetailPage', '/plataforma/restaurantes/:id'], vai: ['PLT-02'], dados: 'Restaurante, plano, estado, pedidos recentes' },
  { id: 'PLT-04', rota: 'p/planos', nome: 'Planos', area: 'Plataforma', tipo: 'desk', ang: ['platform/plans', 'PlansPage', '/plataforma/planos'], vai: [], dados: 'Plano[] (Start, Premium; valores por definir)' },
];
