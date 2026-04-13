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

## Hoje (12/abr) — V3: refinamento copywriting + storytelling

### Seção nova
- [x] Seção **"O caminho"** (entre Mayara e Oferta) com 3 passos: Quiz gratuito · Sessão diagnóstica R$97 · O processo (duração sob medida). Esclarece que os passos são um único caminho, não produtos concorrentes. Passo 2 tangibiliza entrega ("Você sai com: mapeamento do perfil + diagnóstico + direções pra aplicar já").

### Caminho D reforçado
- [x] Crença 1: "O Essência começa do zero" → "O trabalho começa do zero" (remove lock-in do flagship)
- [x] Passo 3 do Caminho: "O acompanhamento" → "O processo" (evita confusão com "alta/autonomia" da Oferta)

### Copywriting refinado
- [x] "Você tem alta" → "Você caminha sozinha" (tira jargão clínico, mais metafórico)
- [x] Item 4 da lista de dor: frase longa enxugada ("Cansada de cada tentativa que não durou")
- [x] Fechamento da seção Dor: removida autopergunta "Será que com ela vai ser diferente?" que reforçava dúvida
- [x] Hero badge: "Programa Essência · Mayara Farias · Nutricionista" → "Essência · por Mayara Farias"
- [x] Quiz sub: "Clique na opção que mais combina..." → "Responda com honestidade. Não existe resposta certa."
- [x] Offer item 5: "Seu cérebro vai ter um objetivo claro" → "Você vai ter um objetivo claro" (tira tom técnico/robótico)
- [x] Caixinha R$97: removida repetição "Mapeamento do seu perfil antes de qualquer coisa" (já tem como item da oferta)
- [x] Depoimento da Crença 2: legenda "Paciente · Consulta · Ubatuba" → "Paciente · Ubatuba, SP"
- [x] FAQ 1: explicado o "atendimento online" sem citar ferramenta ("link por WhatsApp, abre no navegador, sem instalação")
- [x] FAQ 4: prazo flexível em função da sessão diagnóstica (respeita caminho D)
- [x] Prova social: subtítulo "Mensagens reais, sem edição" como ponte entre Oferta e depoimentos
- [x] Cite da Mayara: "É minha entender o que te impede" → "É minha, de entender o que te impede e conduzir isso com você" (ritmo melhor, sugestão da Mayara)

### Em-dashes (tratamento anti-IA)
- [x] ~24 em-dashes substituídos caso a caso por vírgula, ponto, dois pontos ou parênteses. Texto ficou mais humano, menos "cheiro de IA". Exceção mantida: hero subtitle (único em-dash preservado pelo peso rhetórico da primeira impressão).
- [x] Decisão registrada em insights.md: "Evitar em-dashes em texto corrido"

### Deploy
- [x] **Deploy V3 em produção (12/abr, commit 48c3f0d)** em https://essencia.mayarafarias.com.br

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
