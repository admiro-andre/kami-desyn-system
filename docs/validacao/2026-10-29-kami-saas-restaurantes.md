# Avaliação: Kami — Plataforma SaaS de Gestão de Restaurantes

**Suposições assumidas:** mercado = Luanda; persona = dono ou gerente de restaurante pequeno/médio (2–15 funcionários); sem preço definido, sem clientes e sem entrevistas feitas `[Suposição]`. O repositório contém só protótipo front-end (design system, telas em HTML/CSS/JS), sem backend `[Facto]`.
**Frase de valor:** Para donos de restaurantes em Luanda que recebem pedidos desorganizados por WhatsApp, chamada e papel, o Kami entrega uma página própria com menu e pedidos (mesa e delivery) num só painel, em vez de caderno, menu em PDF e WhatsApp.
**Trabalho a fazer:** Quando um cliente quer pedir comida (na mesa ou à distância), o dono quer receber o pedido completo, correto e sem o perder, para vender mais sem erros nem comissões de terceiros.

## Veredicto: VALIDAR PRIMEIRO
**Índice de Pagamento:** Hoje 44/100 → Com cimento 70/100
O maior problema: o README é uma especificação de requisitos sem comprador, sem dor provada e sem preço; "menu digital por QR" é uma commodity freemium global. O cimento mais importante: apontar a uma dor aguda e estreita (pedidos de delivery e levantamento que hoje chegam por WhatsApp) e ligar-se ao WhatsApp em vez de o substituir. Próximo passo: 12 entrevistas e pré-venda com sinal antes de construir o backend.

## Inventário de funcionalidades
| Módulo | O que faz | Motivo de compra | Evidência | Decisão |
|---|---|---|---|---|
| Gestão SaaS (planos, trial 30 dias, limites) | Subscrições Start/Premium | Nenhum (é do fornecedor) | `README-KAMI.md` §6, RG-03..07 | Fora do MVP (cobrar à mão) |
| Página pública + URL personalizável | Menu partilhável por WhatsApp | Conveniência | README §7 | Dentro |
| Catálogo (categorias, preço, até 5 fotos) | Menu atualizável | Conveniência | README §8 | Dentro (fotos opcionais, 1 por produto) |
| Carrinho | Pedido pelo cliente | Conveniência | README §9 | Dentro |
| Pedidos online: levantamento e delivery com geolocalização | Recebe pedidos à distância | Solução (dor maior) | README §10 | Dentro (pin ou texto; sem polígonos) |
| Pedidos presenciais por QR e sessões de mesa | Pedido na mesa | Experiência/Conveniência | README §11 | Fora (fase 2): dor menor, regras de sessão por definir |
| Back-office com alerta visual e sonoro, repetição | Não perder pedidos | Solução | README §12 | Dentro (versão simples) |
| Estimativas de tempo | Prevê preparação/entrega | Experiência | README §13 | Fora |
| Protótipo visual | Telas e design system | n/a | `kami-app.html`, `kami-screens.js`, `kami-components.css`, `TELAS.md` | Aproveitar |

Estado de execução `[Facto]`: não existe backend, base de dados, multi-tenant nem pagamentos no repositório.

## Mapa da dor
| Dimensão | Avaliação |
|---|---|
| Frequência | Diária, em horas de pico, se o restaurante já recebe pedidos remotos; para o menu em si a dor é rara `[Suposição]` |
| Intensidade | Pedidos perdidos, errados ou atrasados, clientes que não voltam. Sem episódios documentados ainda |
| Custo | Ver estimativa abaixo `[Estimativa]` |
| Consciência | Baixa para "menu digital"; média para "perco pedidos no WhatsApp" `[Suposição]` |
| Solução atual (e custo) | Menu em papel/PDF, pedidos por WhatsApp e telefone, caderno. Custo direto ≈ 0; o custo real é a perda invisível. Apps de delivery cobram comissão (valor não encontrado) |

**Dor anual estimada:** ~3,2 milhões Kz/ano por restaurante `[Estimativa]`. Pressupostos: 600 pedidos remotos/mês, 5% perdidos ou errados, ticket médio 6.000 Kz → 30 × 6.000 = 180.000 Kz/mês × 12 = 2,16 M Kz; mais 1 h/dia de pessoal ao telefone (30 h × 3.000 Kz/h = 90.000 Kz/mês × 12 = 1,08 M Kz). Valores a validar nas entrevistas; com preço de 20.000 Kz/mês (240.000 Kz/ano) o rácio seria ~13×, perto do mínimo de 10×.
**Classificação:** Vitamina (menu/QR) com uma fatia Analgésico (pedidos de delivery e levantamento). Só a fatia analgésica sustenta a venda.

## Os 3 motivos de compra
| Motivo | Nota | Justificação |
|---|---|---|
| Solução | 2/5 | Dor plausível mas não provada; sem entrevistas nem pagamento `[Suposição]`. Sem evidência não passa de 3 |
| Conveniência | 3/5 | Poupa tempo ao atender pedidos, mas exige que clientes e equipa mudem de hábito e que o restaurante carregue o menu |
| Experiência | 3/5 | "Parecer profissional" com página própria e link partilhável; sem prova de que o dono valoriza |
**Motivo dominante:** Conveniência (pedidos organizados e sem perdas).
**Alavanca mais fraca da equação de valor:** probabilidade percebida e tempo até ao resultado. O dono não acredita que os clientes vão usar o link em vez do WhatsApp, e o ganho só aparece depois de o menu estar carregado.

## Pagariam?
**Sim, se** provarem que reduzem pedidos perdidos/errados ou substituem comissões de apps de delivery. Quem paga: o dono. Quem usa: funcionário de balcão. Âncora: custo atual ≈ 0 em dinheiro; perdas e horas ao telefone como na estimativa. Rácio valor/preço: ~13× a 20 mil Kz/mês `[Estimativa]`, apertado. Faixa inicial `[Suposição]`: 15 a 35 mil Kz/mês, com setup incluído; confirmar com as 4 perguntas de preço nas entrevistas. Meio de pagamento: transferência e Multicaixa Express `[Verificar]` a adoção do Express como meio B2B.

## Vertentes de negócio
| Vertente | Nota | Problema principal |
|---|---|---|
| Persona | 2/5 | "Restaurantes" é amplo: cantina, takeaway, restaurante com mesas e hotel têm dores diferentes |
| Concorrência e substitutos | 2/5 | QR menu é commodity freemium (Cafe QR £9,99–14,99/mês, Qroda US$8–20, AhaarScan ₹399/mês, MenuForma freemium); local: Tupuca, Koxito; e o substituto "WhatsApp + PDF" é grátis |
| Diferenciação defensável | 2/5 | Nada no README é difícil de copiar; a vantagem possível é localização (Kz, Multicaixa, WhatsApp, suporte humano) |
| Distribuição | 1/5 | Sem canal definido |
| Retenção | 3/5 | Uso diário se for o canal de pedidos; abandono se o cliente final não o adotar |
| Modelo de negócio/unit economics | 2/5 | Preços "por definir"; pagamentos fora da plataforma; setup manual tem custo |
| Execução | 3/5 | Design pronto, nenhum backend; multi-tenant, tempo real e geolocalização são trabalho sério |
| Timing | 3/5 | Digitalização e facturação electrónica criam momento de mudança, mas não obrigam o restaurante a ter pedidos online |
| Riscos | 2/5 | Dependência de rede e energia, notificação sonora exige painel aberto, câmbio nos custos cloud |

## Lacunas e cimento

### 1. Persona vaga e dor não provada — Gravidade: Alta | Esforço: Baixo
- **Porque trava vendas:** o README serve "restaurantes" em geral; sem episódio concreto de perda, o dono vê o Kami como vitamina.
- **Cimento:** nicho de entrada = restaurantes e takeaways em Luanda que já fazem delivery ou levantamento e recebem pedidos por WhatsApp (10–30 pedidos/dia). Entrevistar 12 antes de qualquer linha de backend. Falar de "pedidos perdidos" e não de "menu digital".
- **Cimento técnico:** nenhum; não escrever código.
- **Como provar:** 12 entrevistas — sucesso se ≥ 60% descrevem um episódio recente de pedido perdido ou errado sem indução e ≥ 40% já gastaram dinheiro ou tempo a resolvê-lo.

### 2. Alternativa grátis "suficiente" — WhatsApp + menu em PDF — Gravidade: Alta | Esforço: Médio
- **Porque trava vendas:** o dono já recebe pedidos por WhatsApp de graça. Uma página mais bonita não justifica mensalidade.
- **Cimento:** integrar em vez de substituir. O cliente monta o carrinho na página Kami e o botão "Enviar pedido" abre o WhatsApp do restaurante com a mensagem formatada (itens, total, morada), e o pedido fica em simultâneo registado no painel. O painel vende o que o WhatsApp não faz: histórico, relatório do dia em Kz, alertas de pedido não tratado, preço único atualizado.
- **Cimento técnico:** criar endpoint `POST /pedidos` com estado `novo` + geração de link `https://wa.me/<n>?text=...` no carrinho (`kami-screens.js` / telas do carrinho); painel de pedidos com lista e estado; ~4 dias.
- **Como provar:** piloto de 14 dias em 10 restaurantes — sucesso se ≥ 3 pagam o primeiro mês e ≥ 30% dos pedidos remotos passam pelo link.

### 3. Monetização indefinida e sem fluxo de pagamento — Gravidade: Alta | Esforço: Médio
- **Porque trava vendas:** o README não tem preços nem processo de cobrança (RG-07 exclui pagamentos). Sem preço não há teste de compra.
- **Cimento:** testar já no piloto: mensalidade 20.000 Kz (setup incluído) paga por transferência ou Multicaixa Express, com 30 dias de teste só depois de um sinal simbólico de 5.000 Kz. No painel, registar o método de pagamento de cada pedido (numerário, TPA, Express, transferência) e entregar um relatório de caixa diário por WhatsApp; essa reconciliação é a "dor que se vende".
- **Cimento técnico:** campos `pago` e `metodo_pagamento` no pedido; relatório diário (tarefa agendada); ~2–3 dias. Cobrança do Kami à mão (fatura e transferência) no início.
- **Como provar:** pré-venda — sucesso se ≥ 20% das conversas qualificadas pagam sinal e ≥ 3 pagamentos reais.

### 4. Distribuição inexistente — Gravidade: Alta | Esforço: Médio
- **Porque trava vendas:** sem canal, a aquisição vira visitas porta a porta; o custo de aquisição supera a mensalidade.
- **Cimento:** (a) distribuidores e grossistas de bebidas e produtos que visitam restaurantes, com 20% de comissão recorrente nos 12 primeiros meses; (b) 20 gabinetes de contabilidade que atendem restaurantes, com a mesma comissão; (c) grupos de WhatsApp e Facebook de empresários da restauração em Luanda; (d) ligação aos restaurantes por contacto direto (Instagram, Google Maps) com demo ao vivo de 10 minutos.
- **Cimento técnico:** campo `origem/parceiro` no registo do restaurante e relatório de comissões; ~1 dia.
- **Como provar:** 10 abordagens a distribuidores + 30 a restaurantes em 2 semanas — sucesso se um canal gera ≥ 5 conversas qualificadas e ≥ 1 parceiro aceita indicar.

### 5. Execução pesada e infraestrutura frágil — Gravidade: Média | Esforço: Alto
- **Porque trava vendas:** o README planeia 6 módulos (multi-tenant, QR e sessões, geolocalização, tempo real, estimativas); sem backend, o primeiro cliente pagante demoraria meses. Em Luanda, o alerta sonoro só funciona com o painel aberto, rede estável e energia.
- **Cimento:** MVP concierge: antes de construir o backend, página estática gerada a partir do menu do cliente, pedidos por WhatsApp e folha partilhada, painel manual por parte da equipa Kami. Depois, MVP real reduzido (ver "Versão reforçada"). PWA leve e otimizada para Android de gama baixa; alerta por WhatsApp/notificação push se o painel estiver fechado; modo offline para o painel.
- **Cimento técnico:** cortar do MVP: QR e sessões de mesa (RPQ-*), estimativas (RT-*), planos e limites (RG-03/06), polígonos de zonas; manter 1 tenant por restaurante com `restaurante_id` em todas as tabelas (RN-01); usar mapas e pagamentos por integração e não construir. Estimativa grosseira MVP real: 25–35 dias.
- **Como provar:** primeiro cliente pagante servido por concierge antes de existir backend; depois, sessão de teste completa num telemóvel de entrada de gama com 3G fraco.

### 6. Fiscalidade e confiança — Gravidade: Média | Esforço: Médio
- **Porque trava vendas:** a facturação electrónica por software certificado AGT é obrigatória em fases e deverá chegar aos regimes Geral e Simplificado em 2027 `[Pesquisado]` `[Verificar]` (uma fonte indica 21 de setembro de 2026 para o regime simplificado). Um pedido do Kami não é uma fatura; o dono pode recear que o Kami complique a conformidade. Pagamento adiantado a empresa nova também gera desconfiança.
- **Cimento:** posicionar o Kami como canal de pedidos e dizer claramente que não emite faturas; integrar com ou recomendar um software certificado (por exemplo Vendus/Cegid) em vez de construir faturação. Reverter o risco: 30 dias de teste com devolução, contrato simples sobre dados e exportação do menu e dos pedidos. Verificar calendário com um contabilista.
- **Cimento técnico:** exportação CSV de pedidos e do catálogo (~1 dia); página de termos com propriedade e exportação de dados (~0,5 dia).
- **Como provar:** parecer de um contabilista local e taxa de aceitação do piloto — sucesso se ≥ 50% dos que recebem o piloto aceitam.

## Versão reforçada
**Nova frase de valor:** Para restaurantes e takeaways de Luanda com delivery próprio, que perdem pedidos entre o WhatsApp e o telefone, o Kami junta cada pedido num painel, com alerta, relatório de caixa do dia e link próprio para partilhar, sem comissão por pedido, em vez do caderno e do grupo de WhatsApp.
**Nicho de entrada:** restaurantes e takeaways em Luanda com 10–30 pedidos remotos por dia e entrega feita por pessoal próprio.
**MVP — Dentro (≤ 5):** (1) página pública com URL e menu; (2) carrinho que envia pedido para o painel e para o WhatsApp do restaurante; (3) painel de pedidos com alerta sonoro e repetição de aviso, estados simples (novo, aceite, pronto, entregue, cancelado); (4) registo de pagamento e relatório de caixa diário por WhatsApp; (5) localização do cliente por pin ou texto, confirmada pelo restaurante.
**MVP — Fora:** QR por mesa e sessões (dor menor, regras por resolver); estimativas de tempo (Experiência, não compra); planos Start/Premium e limites (cobrar à mão); polígonos de zonas (usar lista de bairros); 5 fotos por produto (1 chega); pagamentos online integrados (RG-07 mantém-se).
**Oferta:** "Em 48 horas tem o seu menu e o link de pedidos no ar, com o setup feito por nós. Durante 30 dias vê quantos pedidos recebeu e quanto vendeu, em Kz. Se não receber pelo menos 10 pedidos pelo link, devolvemos o sinal." Inclui setup, carregamento do menu, QR do link para o balcão, formação em vídeo curto no WhatsApp. Bónus: relatório semanal por WhatsApp.
**Preço e cobrança:** sinal de 5.000 Kz para reservar vaga; depois 20.000 Kz/mês (faixa a testar 15–35 mil), anual adiantado com 2 meses de desconto; transferência bancária ou Multicaixa Express; revisão anual com cláusula cambial.
**Primeiros 10 clientes:** (1) lista de 50 restaurantes/takeaways do nicho (Instagram, Google Maps, rede pessoal); (2) 10 distribuidores e 10 gabinetes de contabilidade com comissão de 20%; (3) grupos de WhatsApp de restauração. Mensagem pronta no ficheiro de kit (`2026-10-29-kami-saas-restaurantes-kit.md`).

## Suposições críticas por validar
1. Os restaurantes-alvo recebem volume relevante de pedidos remotos e perdem alguns (sem isto, não há dor).
2. Os clientes finais usam o link em vez de mandar mensagem livre por WhatsApp.
3. O dono paga 15–35 mil Kz/mês e por transferência ou Express.
4. Um canal (distribuidor ou contabilista) traz restaurantes a custo baixo.
5. O alerta funciona de forma fiável com rede e energia reais.
6. Calendário e requisitos AGT para o regime Geral e Simplificado `[Verificar]`.
7. As comissões das apps de delivery locais (não encontradas) justificam o argumento "sem comissão".

## Plano de validação — 14 dias
| Dia | Teste | Critério de sucesso |
|---|---|---|
| 1–5 | 12 entrevistas com o guião (restaurantes e takeaways do nicho) | ≥ 60% descrevem pedido perdido/errado recente; ≥ 40% já gastaram dinheiro ou tempo; 4 perguntas de preço com faixa entre "boa compra" e "caro" |
| 2–6 | Mensagem em 5 grupos de WhatsApp/Facebook da restauração com diagnóstico grátis de pedidos | ≥ 10 respostas, ≥ 5 conversas qualificadas |
| 3–8 | 10 abordagens a distribuidores e 10 a gabinetes de contabilidade | ≥ 2 reuniões, ≥ 1 aceita indicar com comissão |
| 5–10 | Landing page + pré-reserva com sinal de 5.000 Kz (Express/transferência) | ≥ 20% das conversas qualificadas pagam sinal; ≥ 3 sinais |
| 8–14 | Piloto concierge com 3–5 restaurantes (página + WhatsApp + folha) | ≥ 60% ativos na 2.ª semana; ≥ 50% aceitam pagar o 1.º mês |
**Regra de decisão:** Se os números forem atingidos → construir o MVP mínimo (25–35 dias) para o nicho; se houver dor mas ninguém pagar → rever preço, quem paga e canal (lacunas 3 e 4) e testar a oferta "sem comissão"; se houver pagamento mas pouco uso → rever adoção e retenção (alerta, formação, relatório diário); se a dor não se confirmar → redirecionar para **delivery sem comissão por WhatsApp para takeaways e dark kitchens** (primeiro teste: 5 takeaways pagam 15.000 Kz/mês por 30 dias).

## Fontes pesquisadas
- [Cafe QR (Capterra)](https://www.capterra.ca/software/1243391/Cafe-QR) — £9,99/£14,99/£39 por local/mês `[Pesquisado]`
- [Qroda (GetApp)](https://www.getapp.co.uk/software/2141897/qroda) — US$8–20/mês
- [AhaarScan (Software Advice)](https://www.softwareadvice.com.au/software/560297/Ahaar-Scan) — ₹399/mês, sem comissão por pedido
- [Menu Tiger](https://www.menutiger.com/pt/features/qrcode-menu-restaurants) — plano grátis, pagos US$38–119
- [MenuForma](https://creati.ai/pt/ai-tools/menuforma/) — freemium, mesa, levantamento e entrega
- [Tupuca (Ver Angola)](https://www.verangola.net/va/pt/092016/Gastronomia/5748/Do-funge-ao-sushi-a-Tupuca-é-a-primeira-empresa-angolana-de-entrega-de-refeições-ao-domicílio.htm) — delivery em Luanda desde 2016
- [Koxito](https://mwm.ai/apps/koxito/6476457749) — app de delivery angolana, 2024
- [Vendus — facturação electrónica Angola](https://www.vendus.pt/blog/faturacao-eletronica-obrigatoria-angola/) e [Abreu Advogados 2026](https://abreuadvogados.com/wp-content/uploads/2026/02/NL-Novidades-Fiscais-e-Legais-para-o-ano-de-2026-PT.pdf) — calendário faseado, Decreto Presidencial 71/25

Não encontrei comissões das apps de delivery angolanas nem fornecedores locais de menu QR; não os inventei. Pesquisas feitas em modo padrão; os preços são de diretórios de terceiros e podem estar desatualizados.
