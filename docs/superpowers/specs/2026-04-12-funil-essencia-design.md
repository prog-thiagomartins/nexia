# Design: Funil de Conversão — Programa Essência

**Data:** 2026-04-12
**Status:** Aprovado para implementação

---

## Contexto

A Mayara está construindo sua estrutura digital do zero. Hoje as pacientes chegam pelo Instagram e vão direto pro WhatsApp, sem qualificação. O objetivo é criar um sistema completo de conversão que:

- Qualifique leads antes de ocupar o tempo da Mayara e da estagiária
- Gere 10 novas pacientes/mês no Programa Essência (R$1.497)
- Não desperdice nenhum lead — redireciona quem não é perfil Essência para a consulta avulsa (R$350)
- Reduza no-show na sessão diagnóstica

---

## Abordagem Escolhida: Funil com Quiz de Elegibilidade

```
[Instagram]
     ↓
[Landing Page]
     ↓
CTA: "Quero entender meu perfil"
     ↓
[Quiz — 5 perguntas, ~2 min]
     ↓
"Seu perfil está pronto. Agende sua sessão diagnóstica."
     ↓
[WhatsApp com contexto do quiz — visível só para a Mayara]
[Automação manda horários disponíveis]
[Pessoa escolhe horário + paga R$97]
[Sequência anti-no-show ativa]
     ↓
[Sessão Diagnóstica — Mayara já conhece o perfil, decide o caminho junto com a cliente]
     ↓
        ┌── Essência R$1.497 (R$97 abatido)
        └── Consulta avulsa R$350 (R$97 abatido) — ou outro caminho que fizer sentido
```

---

## O funil como processo de vendas

| Etapa | O que acontece | Onde |
|---|---|---|
| **Quebra gelo** | Conteúdo do Instagram cria familiaridade — a pessoa chega já sabendo quem é a Mayara | Reels, stories, carrosséis |
| **Apresentação** | A landing apresenta o programa, o método e a profissional | Landing page |
| **Mapeamento de perfil** | Quiz coleta o contexto da pessoa — preenchido sem pressão, no próprio ritmo | Quiz (5 perguntas) |
| **Apresentação contextualizada** | WhatsApp com perfil em mãos — a resposta parece feita pra aquela pessoa | WhatsApp pós-quiz |
| **Sinal de intenção** | Pagamento de R$97 é o micro-comprometimento — quem paga já decidiu que quer resolver | Agendamento + pagamento |
| **Apresentação do método** | Sessão diagnóstica — Mayara apresenta o caminho personalizado com base no que foi mapeado | Sessão 30 min |
| **Indicações** | A cliente pode indicar até 5 pessoas — não obrigatório, mas gera desconto. Os contatos recebem uma abordagem ativa respeitosa mostrando como o trabalho funciona | Sessão — antes do bloco financeiro |
| **Apresentação financeira** | Preço revelado após a entrega de clareza, no momento de maior valor percebido | Sessão — bloco 4 |
| **Fechamento** | Pagamento acontece ainda na sessão | PIX ou link na sessão |

---

## Princípio central

**A triagem é invisível para a cliente.** Toda pessoa que completa o quiz vai para a sessão diagnóstica — sem exceção. O quiz é inteligência interna: Mayara chega na sessão já sabendo o perfil provável, mas a sessão em si define o caminho real. Às vezes o que parecia consulta avulsa vira Essência. Às vezes o contrário. A decisão é tomada junto, na conversa.

A cliente nunca sabe que foi "triada". Para ela, existe só um caminho: quiz → sessão diagnóstica.

---

## Componentes

### 1. Landing Page

**O que muda na landing atual:**
- CTA principal passa de "ir pro WhatsApp" para "Quero entender meu perfil" (abre o quiz)
- O botão flutuante do WhatsApp permanece para quem preferir contato direto
- **Preço removido da landing** — a pessoa não vê R$1.497 antes de estar aquecida. O valor é revelado apenas após a sessão diagnóstica, quando já entendeu o programa e confia na Mayara

**O que não muda:**
- Estrutura, copy e identidade visual da landing

---

### 2. Quiz de Elegibilidade

**Princípio:** as perguntas parecem descoberta, não triagem. A pessoa sente que está se conhecendo — não sendo avaliada.

**Pergunta 1 — Identificação do perfil comportamental**
> "Qual dessas frases mais descreve você hoje?"
- Já tentei várias dietas e sempre volto para onde estava
- Sei o que devo comer, mas não consigo colocar em prática
- Tenho uma relação difícil com a comida — como por ansiedade, culpa ou compulsão
- Quero emagrecer mas sem abrir mão de ter uma vida normal

**Pergunta 2 — Tempo de dor**
> "Há quanto tempo você está tentando resolver isso?"
- Menos de 6 meses
- Entre 6 meses e 2 anos
- Mais de 2 anos
- A vida toda

**Pergunta 3 — Histórico de tentativas** *(multi-seleção)*
> "O que você já tentou antes?"
- Dieta restritiva / low carb / jejum
- Acompanhamento nutricional
- Reeducação alimentar por conta própria
- Apps de contagem de calorias
- Nada ainda, esse seria meu primeiro passo

**Pergunta 4 — Comprometimento**
> "Como você se descreveria em relação a compromissos?"
- Sou consistente quando acredito no que estou fazendo
- Começo bem mas perco o fio com o tempo
- Preciso de acompanhamento para me manter no caminho
- Depende muito do meu estado emocional

**Pergunta 5 — Alinhamento de expectativa**
> "O que você mais quer ao final de 4 meses?"
- Emagrecer de forma definitiva
- Parar de ter uma relação de culpa com a comida
- Entender meu corpo e minhas escolhas
- Ter mais energia e disposição no dia a dia

---

### 3. Lógica de Triagem (interna — invisível para a cliente)

Toda pessoa vai para a sessão diagnóstica. O quiz apenas informa a Mayara sobre o perfil provável antes da sessão começar.

| Perfil identificado no quiz | O que a Mayara chega sabendo |
|---|---|
| Dor recorrente + já tentou + busca mudança comportamental | Provável Essência |
| Primeira tentativa / busca solução pontual | Provável consulta avulsa — mas a sessão pode mudar isso |
| Qualquer perfil | A decisão final é sempre tomada na sessão, junto com a cliente |

A consulta avulsa não é descarte — é porta de entrada. Muita cliente que começa por ali evolui para o Essência.

---

### 4. Tela de Resultado do Quiz

**O resultado nunca aparece na tela.** Isso cria um loop aberto — a curiosidade puxa a pessoa para a próxima etapa.

**Perfil Essência:**
> "Seu perfil está pronto. Para receber sua análise personalizada com a Mayara, agende sua sessão diagnóstica."
> [botão: Agendar minha sessão]

**Todos os perfis recebem a mesma tela de resultado:**
> "Seu perfil está pronto. Para receber sua análise personalizada com a Mayara, agende sua sessão diagnóstica."
> [botão: Agendar minha sessão]

---

### 5. Estrutura da Sessão Diagnóstica (30 min)

**Princípio:** a cliente paga R$97 e sai com algo concreto — independente de fechar qualquer plano. O valor é real, não um argumento de venda. Isso é o que justifica o preço e elimina a percepção de "consulta de vendas disfarçada".

**Meta da sessão:** cliente fecha um plano e paga ainda na chamada. Se não fechar, sai com clareza suficiente pra querer voltar.

---

**Bloco 1 — Espelho (5 min)**
Mayara abre com o que viu no quiz. A cliente se sente vista antes de dizer uma palavra.
> "Pelo que você compartilhou, você está tentando resolver isso há [X tempo], já tentou [Y abordagem] e o que mais trava é [Z]. Isso está certo?"

Esse momento cria confiança imediata — Mayara chegou preparada.

---

**Bloco 2 — Diagnóstico real (15 min)**
Mayara aprofunda com perguntas específicas pra identificar o bloqueio central: comportamental, emocional, de conhecimento ou de contexto de vida. Não é anamnese clínica — é entender *por que* as tentativas anteriores não funcionaram.

---

**Bloco 3 — Entrega de clareza (5 min)**
Independente do que vier depois, a cliente sai com isso:
- **Onde ela está:** o diagnóstico em uma frase clara
- **O que está travando:** o bloqueio principal identificado
- **O que moveria o ponteiro:** a direção concreta

Exemplo real:
> "O que está travando não é falta de informação — você já sabe muito. É que toda vez que o estresse aumenta, a comida vira regulação emocional. O trabalho aqui não é dieta, é construir outra ferramenta pra esses momentos."

Isso tem valor por si só. A cliente pagou R$97 e recebeu uma percepção que ela não tinha.

---

**Bloco 4 — Proposta natural (5 min)**
O fechamento flui do diagnóstico — não é uma virada de chave pra "venda".
> "Dado o que a gente mapeou hoje, aqui está o que faz sentido pra você agora..."

Mayara propõe o caminho (Essência ou consulta avulsa), explica o porquê, e **o pagamento acontece na sessão** — via PIX ou link enviado no WhatsApp. O R$97 já pago é abatido.

Se a cliente precisar de um dia pra decidir, tudo bem — ela já recebeu valor real e tem clareza do próximo passo.

---

**Mensagem pré-preenchida (enviada pela pessoa):**
> "Oi! Acabei de fazer o quiz do Essência. Quero agendar minha sessão diagnóstica."
*(o contexto do quiz chega junto — via parâmetros na URL ou mensagem estruturada)*

**Resposta automática imediata:**
> "Oi [nome]! Vi seu perfil aqui — faz muito sentido. Aqui estão os horários disponíveis: [link Calendly/Cal.com]. Escolha o que funciona melhor pra você."

**Após escolher o horário:**
> "Perfeito! Para confirmar sua sessão, o investimento é de R$97 — esse valor é abatido integralmente se você iniciar o Essência. [link de pagamento]"

**Após pagamento confirmado:**
> "Tudo certo! Sua sessão está confirmada para [data e hora]. Em 30 minutos você vai entender exatamente o que está travando sua relação com a comida — e sair com clareza do que faz sentido pra você agora. Qualquer dúvida, é só me chamar aqui."

---

### 6. Sequência Anti-No-Show

| Momento | Ação | Canal |
|---|---|---|
| Ao agendar | "Confirme respondendo SIM" | WhatsApp |
| 48h antes | Lembrete leve + reforço do que vai receber na sessão | WhatsApp |
| 24h antes | "Confirma presença amanhã às [hora]?" — precisa responder | WhatsApp |
| 2h antes | Lembrete final | WhatsApp |
| No-show | Mensagem de reagendamento (não de cobrança) | WhatsApp |

Quem responde "SIM" duas vezes raramente desaparece. O comprometimento é progressivo.

---

### 7. Sistema WhatsApp — Estagiária + IA Copiloto

**Princípio:** a estagiária conduz, a IA sugere. Nada é cópia e cola — a comunicação é sempre da Mayara.

**O que a IA fornece:**
- Sugestão de tom e temas baseada no perfil do quiz
- Scripts para as situações mais comuns (dúvida sobre preço, pedido de desconto, reagendamento, objeções)
- Alerta quando a conversa sinaliza objeção não tratada

**Situações com script definido:**
- Primeiro contato após quiz
- Dúvida sobre o que é a sessão diagnóstica
- "Está caro" / pedido de desconto
- Cancelamento / pedido de reagendamento
- Após a sessão — follow-up de fechamento
- Lead que sumiu — reativação suave

*(os scripts são desenvolvidos em etapa separada)*

---

## O que este design não cobre (próximas etapas)

- Implementação técnica do quiz (ferramenta: Typeform, Tally ou página HTML customizada)
- Integração quiz → WhatsApp (parâmetros UTM ou Zapier)
- Configuração da automação de agenda (Calendly ou Cal.com)
- Configuração do link de pagamento (Stripe, Hotmart ou PIX automatizado)
- Desenvolvimento dos scripts completos de WhatsApp
- Configuração da IA copiloto (ferramenta a definir)

---

## Métricas para acompanhar

| Métrica | O que indica |
|---|---|
| Taxa de conclusão do quiz | Qualidade do quiz — muito abandono = perguntas longas ou intimidadoras |
| Taxa de conversão quiz → agendamento | Força do resultado + CTA |
| Taxa de conversão agendamento → pagamento R$97 | Clareza do valor da sessão |
| Taxa de comparecimento | Eficácia da sequência anti-no-show |
| Taxa de fechamento sessão → Essência | Qualidade da triagem do quiz |
| Taxa de conversão perfil consulta → agendamento | Força do redirecionamento |
