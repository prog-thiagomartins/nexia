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
        ┌── Perfil Essência ──→ "Seu perfil está pronto. Agende sua sessão diagnóstica."
        │                              ↓
        │                    [WhatsApp com contexto do quiz]
        │                    [Automação manda horários disponíveis]
        │                    [Pessoa escolhe horário + paga R$97]
        │                    [Sequência anti-no-show ativa]
        │                              ↓
        │                    [Sessão Diagnóstica — Mayara revela o perfil]
        │                              ↓
        │                    [Fechamento Essência — R$97 abatido]
        │
        └── Perfil Consulta ──→ "Um bom ponto de partida pra você é uma consulta."
                                [WhatsApp → agendamento → R$350]
```

---

## Componentes

### 1. Landing Page

**O que muda na landing atual:**
- CTA principal passa de "ir pro WhatsApp" para "Quero entender meu perfil" (abre o quiz)
- O botão flutuante do WhatsApp permanece para quem preferir contato direto
- A sessão de preço mantém o valor R$1.497, mas o caminho de entrada é pelo quiz

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

### 3. Lógica de Triagem

| Perfil | Critério | Destino |
|---|---|---|
| **Essência** | Dor recorrente + já tentou antes + busca mudança comportamental | Sessão diagnóstica R$97 → Essência R$1.497 |
| **Essência (mediano)** | Interessada mas expectativa ainda se formando | Sessão diagnóstica R$97 → Essência R$1.497 |
| **Consulta avulsa** | Primeira tentativa / quer solução pontual | Consulta avulsa R$350 |

Ninguém recebe um "não". Quem não é perfil Essência agora recebe um caminho real — a consulta avulsa é porta de entrada e pode converter para Essência no futuro.

---

### 4. Tela de Resultado do Quiz

**O resultado nunca aparece na tela.** Isso cria um loop aberto — a curiosidade puxa a pessoa para a próxima etapa.

**Perfil Essência:**
> "Seu perfil está pronto. Para receber sua análise personalizada com a Mayara, agende sua sessão diagnóstica."
> [botão: Agendar minha sessão]

**Perfil Consulta:**
> "Com base no que você compartilhou, um bom ponto de partida é uma consulta individual. Você sai com um plano alimentar personalizado e suporte por 30 dias."
> [botão: Quero agendar]

---

### 5. Fluxo WhatsApp — Sessão Diagnóstica

**Mensagem pré-preenchida (enviada pela pessoa):**
> "Oi! Acabei de fazer o quiz do Essência. Quero agendar minha sessão diagnóstica."
*(o contexto do quiz chega junto — via parâmetros na URL ou mensagem estruturada)*

**Resposta automática imediata:**
> "Oi [nome]! Vi seu perfil aqui — faz muito sentido. Aqui estão os horários disponíveis: [link Calendly/Cal.com]. Escolha o que funciona melhor pra você."

**Após escolher o horário:**
> "Perfeito! Para confirmar sua sessão, o investimento é de R$97 — esse valor é abatido integralmente se você iniciar o Essência. [link de pagamento]"

**Após pagamento confirmado:**
> "Tudo certo! Sua sessão está confirmada para [data e hora]. Em 40 minutos você vai entender exatamente o que está travando sua relação com a comida — e sair com clareza do que faz sentido pra você agora. Qualquer dúvida, é só me chamar aqui."

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
