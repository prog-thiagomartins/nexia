# Concluído — Landing Page

## Hoje (12/abr) — Quiz personalizado + fluxo + marketing

- [x] Quiz personalizado por perfil (4 perfis via P1) — copy dinâmica + mensagem WhatsApp personalizada com todas as respostas + CTA suave "me fala mais sobre a sessão"
- [x] Todos os botões da página passam pela ponte `#cta-final` antes do quiz (aquecimento obrigatório)
- [x] Pontes do quiz reescritas com entregáveis concretos (entender travamento + mapear perfil + centrar o Essência)
- [x] R$97 vira crédito no Essência — seção Preço ajustada
- [x] Removida linguagem de saída ("sem compromisso", "independente de fechar")
- [x] Tirado "em 4 meses" do hero (ficou genérico, não da descrição do produto)
- [x] Lista de dor: "Quer emagrecer para ser mais feliz" → "Começa na segunda e desiste na quarta" (padrão comportamental)
- [x] Fechamento da dor: removida autopergunta que reforçava dúvida ("Será que com ela vai ser diferente?")
- [x] FAQ item 3 reescrito: "se não puder continuar" (abria porta pra desistência) → "se tiver um imprevisto" (flexibilidade operacional + reforço do fim definido)
- [x] Funil em formato D — abertura sutil pra consulta pontual: pontes do quiz sem citar "Essência" explícito, FAQ ganha item "e se eu só precisar de uma consulta pontual?", decisão final pivotada na sessão
- [x] Edge cases da mensagem WhatsApp: "nada ainda" vira frase dedicada; barras "/" viram vírgulas em listas da P3

## Hoje (12/abr) — Estrutura e assets

- [x] Mosaico de prova social substituído — 8 prints (3 Google + 5 WhatsApp) em grid balanceado por altura
- [x] Imagens reorganizadas em `imagens/{hero, sobre, depoimentos, arquivo}/` com nomes descritivos
- [x] Arquivos órfãos removidos (`css/`, `js/`, `preview-whatsapp-depo.html`)
- [x] Hero refeito pra não grudar imagem/texto em desktop intermediário (1025-1200px): grid 50/50 + `cover` na foto + padding adequado + breakpoint extra pra larguras apertadas
- [x] Caixinha R$97 da seção Preço: traço virou quebra de linha (leitura mais limpa)
- [x] `netlify.toml` criado na raiz com `publish = "Campanhas/essencia/landing page"` (antes o deploy publicava a raiz inteira do workspace — expunha coisas)
- [x] Pasta `imagens/arquivo/` movida pra fora da pasta de deploy (depoimentos antigos não vão mais pro ar)
- [x] Teste do quiz validado nos 4 perfis (A, B, C, D) — título, corpo, ponte, mensagem WhatsApp todos corretos
- [x] Edge case P3: "Nada ainda" marcado junto com outros itens agora filtra o "Nada ainda" (só dispara a frase "primeira vez buscando" quando é a única opção)
- [x] Removida linha "Você será atendida pelo WhatsApp" no resultado do quiz (redundante com o botão "Continuar pelo WhatsApp")
- [x] Seção Preço: tirado "Sem compromisso com o programa" do resultado do quiz (era linguagem de saída que tinha escapado)
- [x] Botão do resultado do quiz: "Agendar minha sessão" → "Continuar pelo WhatsApp" (alinha com o tom da mensagem "me fala mais sobre")
- [x] **Deploy Netlify em produção (12/abr, commit 0104f10)** — substituiu a V1 em https://essencia.mayarafarias.com.br. Publicado só a pasta da landing (9 arquivos), resto do workspace segue privado.

## Antes de hoje

- [x] Hero reescrito com fio narrativo (headline → sub → CTA)
- [x] Credenciais no hero (CRN 64803 + Nutrição Comportamental)
- [x] Seção Mayara na posição correta (depois das Crenças)
- [x] R$97 visível na página e no resultado do quiz
- [x] Análise CRO documentada

## Observações

**Pontos de abandono resolvidos** (da análise CRO):
- Hero sem proposta de valor concreta → resolvido
- Seção Mayara fora de posição → resolvido
- Preço oculto criava ansiedade → resolvido (R$97 visível)
- Resultado do quiz genérico → resolvido (4 perfis dinâmicos + WhatsApp personalizado)
- Prova social com imagens ilegíveis → resolvido (8 prints novos em grid balanceado)
