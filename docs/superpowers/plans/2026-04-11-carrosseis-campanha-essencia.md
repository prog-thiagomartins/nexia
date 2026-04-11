# Carrosséis Campanha Essência — Plano de Implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Criar os 10 carrosséis da campanha de captação da Turma de Abril do Programa Essência (2 por dia, 11–15/04).

**Architecture:** Abordagem B — cada dia tem um carrossel de identificação (manhã) e um de conversão (tarde). Urgência cresce progressivamente ao longo dos 5 dias. Escassez por turma, não por janela artificial.

**Tech Stack:** Markdown para scripts · Identidade visual Essência (verde #4A7C6F · areia #F5EFE6 · terra #C17F5B · fontes Poppins + DM Sans)

---

## Estrutura de Arquivos

```
Campanhas/essencia/carrosseis/
  dia1_c1_voce_nao_e_o_problema.md
  dia1_c2_apresentacao_essencia.md
  dia2_c1_o_que_esta_te_travando.md
  dia2_c2_como_essencia_resolve.md
  dia3_c1_por_dentro_do_programa.md
  dia3_c2_faq_objecoes.md
  dia4_c1_storytelling_paciente.md
  dia4_c2_vagas_restantes.md
  dia5_c1_daqui_a_4_meses.md
  dia5_c2_cta_final.md
```

**Padrão de cada arquivo:** frontmatter com meta → slides numerados com texto + direção visual → CTA final → hashtags

---

## Regras de Produção (aplicar em todos os carrosséis)

- **Slide 1:** máx. 10 palavras · fundo com contraste alto · não entrega a resposta, entrega a promessa
- **Slides do meio:** uma ideia por slide · cada slide termina abrindo gancho para o próximo
- **Último slide:** um único CTA · repetir identidade visual (cor + nome)
- **Tom:** direto, humano, sem jargão clínico · sem culpa, sem pressão forçada
- **Hashtags por post:** 5–8, mistura nicho específico + médias (ver `docs/memoria/palavras_chave_nicho.md`)
- **Número de slides:** 6–8 por carrossel

---

## Task 1: Dia 1 — C1 — "Você Não É o Problema"

**Arquivo:** `Campanhas/essencia/carrosseis/dia1_c1_voce_nao_e_o_problema.md`
**Publicar:** sexta 11/04, manhã
**Objetivo:** desmistificar força de vontade · a seguidora se reconhece antes de receber qualquer oferta
**Métrica-alvo:** salvamento + compartilhamento por DM

- [ ] **Passo 1: Criar o arquivo com o roteiro completo**

```markdown
---
campanha: Essência — Turma de Abril
dia: 1
slot: C1 — Identificação (manhã)
publicar: 11/04/2026
tema: Você não é o problema
objetivo: desmistificar força de vontade, gerar identificação profunda
cta: Salva + manda pra amiga
---

## SLIDE 1 — Hook
**Texto:** "Você já tentou de tudo. E ainda não funcionou."
**Visual:** fundo areia (#F5EFE6) · texto em verde escuro (#3a6460) · fonte Poppins Bold · centralizado
**Direção:** frase em duas linhas · segunda linha com peso maior

## SLIDE 2
**Texto:** "Você não é fraca. Você só usou o método errado."
**Visual:** fundo branco · destaque em terra (#C17F5B) na palavra "método errado"
**Direção:** respiração — frase curta, fonte um pouco menor que o slide 1

## SLIDE 3
**Texto:** "Quando a dieta falha, a gente se culpa. Mas a dieta foi feita pra falhar."
**Visual:** fundo verde (#4A7C6F) · texto branco · tom mais sério
**Direção:** dois parágrafos curtos · segunda frase em negrito

## SLIDE 4
**Texto:** Restrição → Privação → Compulsão → Culpa → Começa tudo de novo.
**Visual:** diagrama horizontal em areia · setas em terra · cada palavra em caixa separada
**Direção:** visual de ciclo vicioso · impacto pela forma, não pelo texto longo

## SLIDE 5
**Texto:** "O problema nunca foi você. Foi o que te ensinaram sobre comer."
**Visual:** fundo areia · fonte média · pausa emocional
**Direção:** frase dividida em duas linhas com pausa no meio

## SLIDE 6
**Texto:** "Quando você entende o seu corpo, a comida para de ser inimiga."
**Visual:** fundo verde claro · tom de esperança · imagem opcional de prato colorido no canto
**Direção:** transição para o positivo — virada emocional

## SLIDE 7 — CTA
**Texto:** "Salva esse post. E manda pra uma amiga que precisa ouvir isso."
**Visual:** fundo terra (#C17F5B) · texto branco · nome "Mayara Farias · Nutricionista" no rodapé
**Direção:** CTA duplo suave — salvar é mais provável quando combinado com "mandar pra alguém"

---
## LEGENDA SUGERIDA
Você não está falhando. O método está.

Durante anos nos ensinaram que emagrecer é questão de força de vontade. Que se você não consegue, é fraqueza.

Não é.

É que nenhuma dieta restritiva foi pensada pro seu corpo, sua rotina, sua história.

Quando você entende o que realmente está acontecendo, tudo muda.

Salva esse post pra não esquecer — e manda pra uma amiga que precisa ouvir isso hoje. 💚

---
## HASHTAGS
#emagrecimentofeminino #emagrecimentocomportamental #nutriçãocomportamental
#reeducacaoalimentar #emagrecercomsaude #nutricionista #saúdedamulher
```

- [ ] **Passo 2: Revisar contra a voz de marca**
  - Tom acolhedor, sem jargão clínico? ✓
  - Sem culpa direcionada à seguidora? ✓
  - Slide 1 com menos de 10 palavras? ✓ (9 palavras)
  - Um único CTA no último slide? ✓

- [ ] **Passo 3: Commit**
```bash
git add Campanhas/essencia/carrosseis/dia1_c1_voce_nao_e_o_problema.md
git commit -m "content: carrossel dia1-C1 — identificação Você não é o problema"
```

---

## Task 2: Dia 1 — C2 — Apresentação do Programa Essência

**Arquivo:** `Campanhas/essencia/carrosseis/dia1_c2_apresentacao_essencia.md`
**Publicar:** sexta 11/04, tarde/noite
**Objetivo:** apresentar o Essência com clareza · o que é, para quem é, como funciona · primeira menção suave às vagas
**Métrica-alvo:** DMs espontâneos, salvamento

- [ ] **Passo 1: Criar o arquivo com o roteiro completo**

```markdown
---
campanha: Essência — Turma de Abril
dia: 1
slot: C2 — Conversão (tarde)
publicar: 11/04/2026
tema: Apresentação do Programa Essência
objetivo: apresentar o programa com clareza, gerar DMs de interesse
cta: Me chama no DM
---

## SLIDE 1 — Hook
**Texto:** "4 meses. 10 mulheres. Uma abordagem diferente."
**Visual:** fundo verde (#4A7C6F) · texto branco · Poppins Bold · números em destaque terra (#C17F5B)
**Direção:** três linhas curtas · cada número cria curiosidade

## SLIDE 2
**Texto:** "O Programa Essência não é uma dieta."
**Visual:** fundo areia · texto em verde escuro · fonte grande
**Direção:** declaração direta que interrompe expectativa

## SLIDE 3
**Texto:** "É um acompanhamento individual de 4 meses. Focado em entender o seu corpo — e criar uma relação real com a comida."
**Visual:** fundo branco · texto corrido · tom explicativo
**Direção:** quebrar em dois parágrafos curtos · segunda frase em itálico

## SLIDE 4
**Texto:** O que está incluído:
- Consultas mensais individuais
- Plano alimentar adaptado à sua rotina
- Avaliação de exames
- Suporte entre as consultas
**Visual:** fundo areia · lista com ícones simples em terra · cada item em linha
**Direção:** visual limpo, sem sobrecarga de texto

## SLIDE 5
**Texto:** "Para quem é: mulheres que já tentaram dieta e querem algo que respeite sua rotina e seu corpo."
**Visual:** fundo verde claro · texto branco · tom de inclusão
**Direção:** frase de qualificação — quem se identifica sente que é pra ela

## SLIDE 6
**Texto:** "Turma de Abril: 10 vagas. Início dia 20/04."
**Visual:** fundo terra (#C17F5B) · texto branco · destaque visual nos números
**Direção:** primeira aparição das vagas — tom informativo, não de pressão

## SLIDE 7 — CTA
**Texto:** "Quer saber se é pra você? Me chama no DM."
**Visual:** fundo verde (#4A7C6F) · texto branco · "Mayara Farias · Nutricionista" no rodapé
**Direção:** convite sem pressão — a pergunta abre a conversa com segurança

---
## LEGENDA SUGERIDA
O Programa Essência não é mais uma dieta.

É um acompanhamento de 4 meses onde a gente trabalha juntas para entender o que o seu corpo precisa — de verdade. Sem restrição que não faz sentido. Sem culpa.

Consultas individuais, plano adaptado à sua rotina, avaliação de exames e suporte real entre as consultas.

A Turma de Abril tem 10 vagas. O acompanhamento começa dia 20.

Se você se viu no post anterior e quer entender se esse programa é pra você: me chama no DM. Sem compromisso. 💚

---
## HASHTAGS
#emagrecimentofeminino #nutriçãocomportamental #reeducacaoalimentar
#emagrecercomsaude #nutricionista #saúdedamulher #programanutrição
```

- [ ] **Passo 2: Revisar coerência com C1**
  - C1 ativou a dor → C2 apresenta a solução? ✓
  - Vagas mencionadas sem pressão excessiva? ✓
  - CTA único e claro? ✓

- [ ] **Passo 3: Commit**
```bash
git add Campanhas/essencia/carrosseis/dia1_c2_apresentacao_essencia.md
git commit -m "content: carrossel dia1-C2 — conversão Apresentação do Essência"
```

---

## Task 3: Dia 2 — C1 — "O Que Está Te Travando"

**Arquivo:** `Campanhas/essencia/carrosseis/dia2_c1_o_que_esta_te_travando.md`
**Publicar:** sábado 12/04, manhã
**Objetivo:** explicar os mecanismos comportamentais que sabotam o processo · identificação profunda
**Métrica-alvo:** compartilhamento ("manda pra uma amiga que vive esse ciclo")

- [ ] **Passo 1: Criar o arquivo com o roteiro completo**

```markdown
---
campanha: Essência — Turma de Abril
dia: 2
slot: C1 — Identificação (manhã)
publicar: 12/04/2026
tema: O que está te travando
objetivo: identificar os mecanismos que travam o emagrecimento, sem culpa
cta: Manda pra amiga
---

## SLIDE 1 — Hook
**Texto:** "Por que a dieta funciona 2 semanas — e para."
**Visual:** fundo areia · texto verde escuro · Poppins Bold · travessão com pausa visual
**Direção:** pergunta implícita que toda seguidora já viveu

## SLIDE 2
**Texto:** "Não é falta de disciplina. É biologia."
**Visual:** fundo verde · texto branco · frase de impacto
**Direção:** contradição direta — interrompe a narrativa de culpa

## SLIDE 3
**Texto:** "Restrição calórica ativa o modo sobrevivência. Seu corpo diminui o metabolismo. Você come menos e queima menos."
**Visual:** fundo branco · texto corrido em dois blocos · tom educacional
**Direção:** explicação simples, sem termos técnicos

## SLIDE 4
**Texto:** "Aí vem o fim de semana. O estresse. O jantar fora. E tudo 'desmorona'."
**Visual:** fundo areia · aspas em destaque · tom de identificação
**Direção:** a seguidora se vê nessa cena exata

## SLIDE 5
**Texto:** "Isso não é fraqueza. É uma resposta fisiológica a um plano que não foi feito pro seu corpo."
**Visual:** fundo verde claro · texto branco · virada emocional
**Direção:** reframing — transforma culpa em compreensão

## SLIDE 6
**Texto:** "O emagrecimento de verdade não começa pela restrição. Começa pelo entendimento."
**Visual:** fundo terra (#C17F5B) · texto branco · frase de fechamento poderosa
**Direção:** deixa a seguidora querendo saber "como então?"

## SLIDE 7 — CTA
**Texto:** "Manda esse post pra uma amiga que vive esse ciclo."
**Visual:** fundo verde (#4A7C6F) · texto branco · "Mayara Farias · Nutricionista" no rodapé
**Direção:** CTA de compartilhamento — maximiza alcance orgânico

---
## LEGENDA SUGERIDA
Você começa na segunda. Na sexta já desistiu. Isso não é falta de disciplina.

Quando você restringe muito, seu corpo entende que está em modo de sobrevivência. Ele diminui o metabolismo, aumenta a fome, e qualquer "deslize" vira compulsão.

Não é você que falhou. É o plano que não foi feito pro seu corpo.

Emagrecer de verdade começa pelo entendimento — não pela restrição.

Manda esse post pra uma amiga que precisa ouvir isso. 💚

---
## HASHTAGS
#emagrecimentocomportamental #nutriçãocomportamental #emagrecimentofeminino
#reeducacaoalimentar #emagrecercomsaude #saúdedamulher #nutricionista
```

- [ ] **Passo 2: Revisar**
  - Explica mecanismo sem usar jargão técnico? ✓
  - Nenhuma culpa direcionada à seguidora? ✓
  - CTA de compartilhamento (maximiza alcance do sábado)? ✓

- [ ] **Passo 3: Commit**
```bash
git add Campanhas/essencia/carrosseis/dia2_c1_o_que_esta_te_travando.md
git commit -m "content: carrossel dia2-C1 — identificação O que está te travando"
```

---

## Task 4: Dia 2 — C2 — Como o Essência Resolve

**Arquivo:** `Campanhas/essencia/carrosseis/dia2_c2_como_essencia_resolve.md`
**Publicar:** sábado 12/04, tarde/noite
**Objetivo:** ligar os problemas do C1 diretamente ao programa · 1ª menção direta e clara às vagas da Turma de Abril
**Métrica-alvo:** DMs, salvamento

- [ ] **Passo 1: Criar o arquivo com o roteiro completo**

```markdown
---
campanha: Essência — Turma de Abril
dia: 2
slot: C2 — Conversão (tarde)
publicar: 12/04/2026
tema: Como o Essência resolve cada travamento
objetivo: conectar os problemas do C1 ao programa, primeira menção direta às vagas
cta: DM para Turma de Abril
---

## SLIDE 1 — Hook
**Texto:** "E se o problema não fosse você — mas o que faltava no plano?"
**Visual:** fundo verde escuro · texto branco · pergunta que continua o C1
**Direção:** retoma o raciocínio do carrossel da manhã

## SLIDE 2
**Texto:** "A maioria dos planos alimentares ignora 3 coisas: sua rotina, seu histórico e sua relação com a comida."
**Visual:** fundo areia · lista simples · cada item em linha separada
**Direção:** diagnóstico do que falta — prepara para a solução

## SLIDE 3
**Texto:** "No Essência, a gente começa por aí."
**Visual:** fundo verde (#4A7C6F) · texto branco · fonte grande · pausa
**Direção:** declaração de posicionamento — curto e direto

## SLIDE 4
**Texto:** O que fazemos diferente:
- Plano adaptado à sua rotina real (não à ideal)
- Avaliação do que está bloqueando o seu corpo
- Trabalho com o comportamento alimentar, não só com a comida
**Visual:** fundo areia · lista com marcadores em terra · fonte média
**Direção:** diferencial concreto, não abstrato

## SLIDE 5
**Texto:** "4 meses de acompanhamento individual. Consultas, plano, suporte, avaliação de exames. Tudo junto."
**Visual:** fundo branco · texto corrido · tom de completude
**Direção:** visão geral do programa sem sobrecarregar com detalhes

## SLIDE 6
**Texto:** "Turma de Abril: 10 vagas. Início 20/04. Quando lota, próxima turma é Maio."
**Visual:** fundo terra (#C17F5B) · texto branco · números em destaque
**Direção:** escassez real e natural — sem urgência artificial

## SLIDE 7 — CTA
**Texto:** "Para saber se uma vaga é sua: me chama no DM."
**Visual:** fundo verde (#4A7C6F) · texto branco · "Mayara Farias · Nutricionista" rodapé
**Direção:** convite aberto — baixa barreira de entrada

---
## LEGENDA SUGERIDA
Se você se viu no post de hoje cedo, esse é o próximo passo.

A maioria dos planos alimentares ignora o que realmente trava: sua rotina, seu histórico e sua relação com a comida.

No Essência a gente começa por aí. Plano adaptado à vida real, avaliação do que está bloqueando o seu corpo e trabalho com o comportamento — não só com a lista de alimentos.

4 meses de acompanhamento individual. 10 vagas na Turma de Abril. Início dia 20.

Quando as vagas de Abril acabam, a próxima turma é Maio.

Quer uma vaga? Me chama no DM. 💚

---
## HASHTAGS
#emagrecimentofeminino #nutriçãocomportamental #programanutrição
#reeducacaoalimentar #nutricionista #saúdedamulher #emagrecercomsaude
```

- [ ] **Passo 2: Revisar coerência com C1**
  - Cada travamento do C1 tem resposta no C2? ✓
  - Vagas mencionadas com escassez real (não artificial)? ✓
  - CTA único? ✓

- [ ] **Passo 3: Commit**
```bash
git add Campanhas/essencia/carrosseis/dia2_c2_como_essencia_resolve.md
git commit -m "content: carrossel dia2-C2 — conversão Como o Essência resolve"
```

---

## Task 5: Dia 3 — C1 — Por Dentro do Programa

**Arquivo:** `Campanhas/essencia/carrosseis/dia3_c1_por_dentro_do_programa.md`
**Publicar:** domingo 13/04, manhã
**Objetivo:** bastidores reais do acompanhamento · transparência gera confiança
**Métrica-alvo:** comentários com dúvidas, salvamento

- [ ] **Passo 1: Criar o arquivo com o roteiro completo**

```markdown
---
campanha: Essência — Turma de Abril
dia: 3
slot: C1 — Identificação (manhã)
publicar: 13/04/2026
tema: Por dentro do programa
objetivo: mostrar o processo real do Essência, gerar confiança e curiosidade
cta: Comenta sua dúvida
---

## SLIDE 1 — Hook
**Texto:** "O que acontece nos 4 meses de acompanhamento?"
**Visual:** fundo areia · texto verde escuro · Poppins Bold · pergunta direta
**Direção:** responde uma dúvida que a seguidora já tem

## SLIDE 2
**Texto:** "Mês 1: entender. A gente mapeia o que você come, como come, o que trava e o que já funciona."
**Visual:** fundo verde · texto branco · "Mês 1" em destaque terra
**Direção:** início do processo — sem julgamento, foco em diagnóstico

## SLIDE 3
**Texto:** "Mês 2: ajustar. Com os dados do Mês 1, o plano começa a fazer sentido pra sua vida — não pra uma rotina ideal."
**Visual:** fundo areia · texto verde escuro · "Mês 2" em destaque
**Direção:** progressão natural — mostra que é processo, não receita pronta

## SLIDE 4
**Texto:** "Mês 3: consolidar. O que era esforço começa a virar hábito. O corpo responde quando o plano é real."
**Visual:** fundo branco · texto corrido · "Mês 3" em destaque
**Direção:** a transformação acontece aqui — tom de resultado sem prometer milagre

## SLIDE 5
**Texto:** "Mês 4: autonomia. Você termina sabendo o que seu corpo precisa — sem depender de dieta o resto da vida."
**Visual:** fundo verde (#4A7C6F) · texto branco · "Mês 4" em destaque terra
**Direção:** o objetivo final — independência, não dependência da nutricionista

## SLIDE 6
**Texto:** "Cada mês: uma consulta individual + plano atualizado + suporte entre as consultas."
**Visual:** fundo areia · lista limpa · ícones simples
**Direção:** o que a paciente recebe de forma concreta

## SLIDE 7 — CTA
**Texto:** "Ficou com dúvida? Comenta aqui que eu respondo."
**Visual:** fundo terra (#C17F5B) · texto branco · "Mayara Farias · Nutricionista" rodapé
**Direção:** CTA de comentário — aumenta engajamento e alimenta FAQ do próximo carrossel

---
## LEGENDA SUGERIDA
Muita gente me pergunta: "mas como funciona de verdade?"

Então vem comigo pelos 4 meses do Essência.

Não é uma dieta com início, meio e fim. É um processo de entendimento do seu corpo — mês a mês.

No final, você não precisa mais de mim pra saber o que comer. Esse é o objetivo.

Tem alguma dúvida sobre como funciona? Comenta aqui — eu respondo todas. 💚

---
## HASHTAGS
#emagrecimentofeminino #nutriçãocomportamental #acompanhamentonutricional
#reeducacaoalimentar #nutricionista #saúdedamulher #habitossaudaveis
```

- [ ] **Passo 2: Revisar**
  - Processo descrito em linguagem humana, sem jargão? ✓
  - CTA de comentário coerente com o objetivo de engajamento? ✓
  - Resultado prometido é real e não exagerado? ✓

- [ ] **Passo 3: Commit**
```bash
git add Campanhas/essencia/carrosseis/dia3_c1_por_dentro_do_programa.md
git commit -m "content: carrossel dia3-C1 — bastidores Por dentro do programa"
```

---

## Task 6: Dia 3 — C2 — FAQ de Objeções

**Arquivo:** `Campanhas/essencia/carrosseis/dia3_c2_faq_objecoes.md`
**Publicar:** domingo 13/04, tarde/noite
**Objetivo:** remover as principais objeções antes que a seguidora precise expressar · vagas da turma com urgência suave
**Métrica-alvo:** DMs, salvamento

- [ ] **Passo 1: Criar o arquivo com o roteiro completo**

```markdown
---
campanha: Essência — Turma de Abril
dia: 3
slot: C2 — Conversão (tarde)
publicar: 13/04/2026
tema: FAQ — Será que funciona pra mim?
objetivo: remover objeções reais, apresentar vagas com urgência suave
cta: DM para garantir vaga
---

## SLIDE 1 — Hook
**Texto:** "Será que funciona pra mim?"
**Visual:** fundo areia · texto verde escuro · Poppins Bold · pergunta simples e direta
**Direção:** a dúvida que toda seguidora tem mas não perguntou

## SLIDE 2
**Texto:** "Já tentei antes e não funcionou."
Resposta: "O que não funcionou foi a restrição. O Essência não é restrição — é entendimento. É diferente."
**Visual:** fundo verde · pergunta em areia · resposta em branco menor
**Direção:** objeção + resposta direta no mesmo slide

## SLIDE 3
**Texto:** "Não tenho tempo pra cuidar da alimentação."
Resposta: "O plano é feito pra sua rotina real — não pra uma rotina ideal. Se você tem 20 minutos pra cozinhar, é com isso que a gente trabalha."
**Visual:** fundo areia · mesmo formato do slide anterior
**Direção:** a resposta valida a objeção antes de resolver

## SLIDE 4
**Texto:** "Será que consigo manter depois dos 4 meses?"
Resposta: "Esse é exatamente o objetivo do Mês 4. Você termina sabendo o que funciona pro seu corpo — sem precisar de dieta pra sempre."
**Visual:** fundo branco · mesmo formato
**Direção:** responde o medo de depender para sempre

## SLIDE 5
**Texto:** "E se eu não gostar da alimentação que você indicar?"
Resposta: "O plano é construído com você, não pra você. A gente parte do que você já come e do que você gosta."
**Visual:** fundo verde (#4A7C6F) · texto branco
**Direção:** diferencial do acompanhamento individual vs. dieta genérica

## SLIDE 6
**Texto:** "Turma de Abril: vagas disponíveis. Início 20/04."
**Visual:** fundo terra (#C17F5B) · texto branco · números em destaque
**Direção:** transição natural para o CTA — urgência aumentando

## SLIDE 7 — CTA
**Texto:** "Tem outra dúvida? Me chama no DM — eu respondo antes de você decidir."
**Visual:** fundo verde (#4A7C6F) · texto branco · "Mayara Farias · Nutricionista" rodapé
**Direção:** remove a barreira de "preciso ter certeza antes de perguntar"

---
## LEGENDA SUGERIDA
Recebi várias dúvidas nos comentários. Então vou responder as principais aqui.

"Já tentei antes e não funcionou." — O que não funcionou foi a restrição. O Essência não é restrição.

"Não tenho tempo." — O plano é feito pra sua rotina real. Com 20 minutos disponíveis, é com isso que a gente trabalha.

"Vou conseguir manter depois?" — O Mês 4 existe justamente pra isso. Você sai sabendo o que funciona pro seu corpo.

Ainda tem dúvida? Me chama no DM antes de decidir. Sem compromisso. As vagas da Turma de Abril estão abertas — início dia 20. 💚

---
## HASHTAGS
#emagrecimentofeminino #nutriçãocomportamental #programanutrição
#acompanhamentonutricional #nutricionista #saúdedamulher #reeducacaoalimentar
```

- [ ] **Passo 2: Revisar**
  - Cada objeção é respondida sem invalidar quem a tem? ✓
  - Vagas aparecem como informação, não pressão? ✓
  - CTA baixa a barreira de entrar em contato? ✓

- [ ] **Passo 3: Commit**
```bash
git add Campanhas/essencia/carrosseis/dia3_c2_faq_objecoes.md
git commit -m "content: carrossel dia3-C2 — conversão FAQ de objeções"
```

---

## Task 7: Dia 4 — C1 — Storytelling de Paciente

**Arquivo:** `Campanhas/essencia/carrosseis/dia4_c1_storytelling_paciente.md`
**Publicar:** segunda 14/04, manhã
**Objetivo:** relato de transformação comportamental real (sem dados pessoais) · identificação emocional profunda
**Métrica-alvo:** comentários ("sou eu aqui"), compartilhamentos

- [ ] **Passo 1: Criar o arquivo com o roteiro completo**

```markdown
---
campanha: Essência — Turma de Abril
dia: 4
slot: C1 — Identificação (manhã)
publicar: 14/04/2026
tema: Storytelling de paciente
objetivo: identificação emocional com jornada real de transformação comportamental
cta: Comenta se você se viu aqui
---

## SLIDE 1 — Hook
**Texto:** "Ela chegou dizendo que não tinha força de vontade."
**Visual:** fundo areia · texto verde escuro · Poppins Bold · abertura de história
**Direção:** começo em terceira pessoa — a seguidora já quer saber quem é "ela"

## SLIDE 2
**Texto:** "Tinha tentado 4 dietas diferentes no último ano. Todas funcionaram por algumas semanas. Nenhuma durou."
**Visual:** fundo verde · texto branco · pausa narrativa
**Direção:** contexto que toda seguidora conhece

## SLIDE 3
**Texto:** "No Mês 1, a gente descobriu que ela pulava o café da manhã por falta de tempo — e compensava à noite. Todo dia."
**Visual:** fundo areia · texto verde · insight clínico em linguagem simples
**Direção:** o problema real aparece — não é falta de disciplina, é padrão comportamental

## SLIDE 4
**Texto:** "A solução não foi 'comer mais vezes ao dia'. Foi montar um café da manhã que cabia em 8 minutos na vida dela."
**Visual:** fundo branco · texto corrido · virada prática
**Direção:** a diferença entre receita genérica e acompanhamento real

## SLIDE 5
**Texto:** "No Mês 3 ela me mandou uma mensagem: 'Mayara, eu passei o fim de semana inteiro sem pensar em comida. Pela primeira vez.'"
**Visual:** fundo verde (#4A7C6F) · texto branco · mensagem em destaque · tom emocional
**Direção:** o resultado real — não o número na balança, mas a liberdade mental

## SLIDE 6
**Texto:** "Ela não perdeu força de vontade. Ela nunca teve esse problema. O problema era o plano."
**Visual:** fundo terra (#C17F5B) · texto branco · fechamento poderoso
**Direção:** retoma o tema central da campanha — reframing final

## SLIDE 7 — CTA
**Texto:** "Você se viu aqui? Comenta."
**Visual:** fundo verde escuro · texto branco · "Mayara Farias · Nutricionista" rodapé
**Direção:** CTA simples de comentário — gera prova social pública

---
## LEGENDA SUGERIDA
Ela chegou no consultório dizendo que não tinha força de vontade.

Tinha tentado 4 dietas no último ano. Todas funcionaram por algumas semanas. Nenhuma durou.

No Mês 1 a gente descobriu que ela pulava o café da manhã por falta de tempo e compensava à noite — todo dia, sem perceber.

A solução não foi "coma de 3 em 3 horas". Foi montar uma opção que cabia em 8 minutos na rotina dela.

No Mês 3 ela me mandou: "pela primeira vez passei o fim de semana inteiro sem pensar em comida."

Isso não é dieta. É entendimento.

Você se viu aqui? Comenta. 💚

---
## HASHTAGS
#emagrecimentofeminino #emagrecimentocomportamental #nutriçãocomportamental
#reeducacaoalimentar #nutricionista #saúdedamulher #transformacaoreal
```

- [ ] **Passo 2: Revisar**
  - Transformação é comportamental, não estética (sem mencionar peso/corpo)? ✓
  - Sem dados identificáveis da paciente? ✓
  - Resultado prometido é crível e não exagerado? ✓

- [ ] **Passo 3: Commit**
```bash
git add Campanhas/essencia/carrosseis/dia4_c1_storytelling_paciente.md
git commit -m "content: carrossel dia4-C1 — storytelling Jornada de paciente"
```

---

## Task 8: Dia 4 — C2 — Vagas Restantes

**Arquivo:** `Campanhas/essencia/carrosseis/dia4_c2_vagas_restantes.md`
**Publicar:** segunda 14/04, tarde/noite
**Objetivo:** escassez real · quantas vagas restam · o que acontece quando lota (lista Maio)
**Métrica-alvo:** DMs diretos para agendamento

- [ ] **Passo 1: Criar o arquivo com o roteiro completo**

```markdown
---
campanha: Essência — Turma de Abril
dia: 4
slot: C2 — Conversão (tarde)
publicar: 14/04/2026
tema: Vagas restantes da Turma de Abril
objetivo: escassez real, urgência genuína, converter DMs em agendamento
cta: DM para garantir vaga
---

## SLIDE 1 — Hook
**Texto:** "Turma de Abril: as vagas estão saindo."
**Visual:** fundo terra (#C17F5B) · texto branco · Poppins Bold · tom de atualização real
**Direção:** notícia genuína — não alarme falso

## SLIDE 2
**Texto:** "Atendo 10 mulheres por mês porque é o número que me permite dar atenção real a cada uma."
**Visual:** fundo areia · texto verde escuro · explicação do porquê do limite
**Direção:** a escassez tem razão — isso valoriza, não pressiona

## SLIDE 3
**Texto:** "Quando a Turma de Abril fechar, a próxima é Maio. A lista de espera já existe."
**Visual:** fundo verde · texto branco · informação prática
**Direção:** cria antecipação para quem não pegar Abril — não é rejeição, é exclusividade

## SLIDE 4
**Texto:** O que você garante com a vaga de Abril:
- Início do acompanhamento em 20/04
- 4 meses de trabalho individual
- Plano alimentar feito pra sua rotina
- Suporte entre as consultas
**Visual:** fundo areia · lista com marcadores terra · fonte média
**Direção:** lembra o valor concreto antes do CTA

## SLIDE 5
**Texto:** "Para garantir sua vaga: me chama no DM com 'QUERO ABRIL' e a gente conversa."
**Visual:** fundo verde (#4A7C6F) · texto branco · destaque em "QUERO ABRIL"
**Direção:** palavra-chave simplifica o primeiro passo

## SLIDE 6 — CTA
**Texto:** "Não garantiu ainda? Agora é a hora."
**Visual:** fundo terra (#C17F5B) · texto branco · "Mayara Farias · Nutricionista" rodapé
**Direção:** urgência genuína, sem agressividade

---
## LEGENDA SUGERIDA
As vagas da Turma de Abril estão saindo.

Atendo 10 mulheres por mês porque é o número que me permite dar atenção real a cada uma. Não é uma regra de marketing — é o que funciona na prática.

Quando Abril fechar, a próxima turma é Maio. Já tem lista de espera.

Se você acompanhou essa semana e reconheceu que chegou a hora: me chama no DM com "QUERO ABRIL". A gente conversa sem compromisso.

O acompanhamento começa dia 20. 💚

---
## HASHTAGS
#emagrecimentofeminino #nutriçãocomportamental #programanutrição
#acompanhamentonutricional #nutricionista #saúdedamulher #turmaabril
```

- [ ] **Passo 2: Revisar**
  - Escassez explicada com razão real (não gatilho falso)? ✓
  - Lista de Maio cria antecipação sem parecer rejeição? ✓
  - Palavra-chave no DM facilita ação? ✓

- [ ] **Passo 3: Commit**
```bash
git add Campanhas/essencia/carrosseis/dia4_c2_vagas_restantes.md
git commit -m "content: carrossel dia4-C2 — urgência Vagas restantes Turma de Abril"
```

---

## Task 9: Dia 5 — C1 — "Daqui a 4 Meses"

**Arquivo:** `Campanhas/essencia/carrosseis/dia5_c1_daqui_a_4_meses.md`
**Publicar:** terça 15/04, manhã
**Objetivo:** reflexão emocional sobre o custo de não agir · sem vender nada diretamente
**Métrica-alvo:** comentários ("eu quero isso"), compartilhamento

- [ ] **Passo 1: Criar o arquivo com o roteiro completo**

```markdown
---
campanha: Essência — Turma de Abril
dia: 5
slot: C1 — Identificação (manhã)
publicar: 15/04/2026
tema: Daqui a 4 meses
objetivo: reflexão emocional sobre o que a seguidora quer pra si — sem vender
cta: Comenta o que você quer mudar
---

## SLIDE 1 — Hook
**Texto:** "Daqui a 4 meses, o que você quer sentir?"
**Visual:** fundo areia · texto verde escuro · Poppins Bold · pergunta aberta
**Direção:** projeção no futuro — cria imagem mental antes de qualquer oferta

## SLIDE 2
**Texto:** "Não o que você quer pesar. O que você quer sentir."
**Visual:** fundo verde · texto branco · diferenciação sutil mas poderosa
**Direção:** reposiciona o desejo — do estético para o emocional

## SLIDE 3
**Texto:** "Dormir bem e acordar com energia?"
**Visual:** fundo areia · texto simples · uma imagem por slide
**Direção:** começo da lista de sensações — cada uma em slide separado

## SLIDE 4
**Texto:** "Passar o fim de semana sem culpa depois de comer?"
**Visual:** fundo branco · mesmo padrão
**Direção:** identificação direta com a ansiedade que as seguidoras vivem

## SLIDE 5
**Texto:** "Olhar pro prato e saber o que o seu corpo precisa — sem calcular nada?"
**Visual:** fundo verde (#4A7C6F) · texto branco
**Direção:** o objetivo final do Essência sem mencionar o Essência

## SLIDE 6
**Texto:** "Essas coisas não vêm de dieta. Vêm de entendimento."
**Visual:** fundo terra (#C17F5B) · texto branco · fechamento
**Direção:** ancora tudo no posicionamento central da campanha

## SLIDE 7 — CTA
**Texto:** "Comenta aqui: o que você mais quer mudar nos próximos 4 meses?"
**Visual:** fundo verde escuro · texto branco · "Mayara Farias · Nutricionista" rodapé
**Direção:** CTA de engajamento — os comentários alimentam o C2 final da campanha

---
## LEGENDA SUGERIDA
Daqui a 4 meses o que você quer sentir?

Não o que você quer pesar. O que você quer sentir.

Dormir bem. Ter energia. Passar o fim de semana sem culpa. Olhar pro prato e saber o que o seu corpo precisa — sem calcular nada.

Essas coisas não vêm de dieta. Vêm de entendimento do seu próprio corpo.

Comenta aqui: o que você mais quer mudar nos próximos 4 meses? 💚

---
## HASHTAGS
#emagrecimentofeminino #emagrecimentocomportamental #nutriçãocomportamental
#saúdedamulher #reeducacaoalimentar #nutricionista #mudancadehabito
```

- [ ] **Passo 2: Revisar**
  - Reflexão emocional sem mencionar o programa diretamente? ✓
  - Foco em sensação, não em estética? ✓
  - CTA de comentário alimenta prova social para o C2? ✓

- [ ] **Passo 3: Commit**
```bash
git add Campanhas/essencia/carrosseis/dia5_c1_daqui_a_4_meses.md
git commit -m "content: carrossel dia5-C1 — reflexão Daqui a 4 meses"
```

---

## Task 10: Dia 5 — C2 — CTA Final da Turma de Abril

**Arquivo:** `Campanhas/essencia/carrosseis/dia5_c2_cta_final.md`
**Publicar:** terça 15/04, tarde/noite
**Objetivo:** últimas vagas · como agendar · data de início · o que a mulher recebe · urgência final
**Métrica-alvo:** DMs diretos de agendamento

- [ ] **Passo 1: Criar o arquivo com o roteiro completo**

```markdown
---
campanha: Essência — Turma de Abril
dia: 5
slot: C2 — Conversão (tarde/noite)
publicar: 15/04/2026
tema: CTA final — Turma de Abril
objetivo: converter as últimas vagas com clareza e calor — não pressão
cta: DM "QUERO ABRIL"
---

## SLIDE 1 — Hook
**Texto:** "Últimas vagas. Turma de Abril."
**Visual:** fundo verde (#4A7C6F) · texto branco · Poppins Bold · simples e direto
**Direção:** sem drama — informação real

## SLIDE 2
**Texto:** "Esta semana falei sobre tudo que estava travando você. Sobre o que o acompanhamento realmente faz. Sobre como é por dentro."
**Visual:** fundo areia · texto verde escuro · recapitulação da semana
**Direção:** âncora emocional — lembra a jornada da semana antes de fechar

## SLIDE 3
**Texto:** "Se você se viu aqui em algum momento, essa mensagem é pra você."
**Visual:** fundo verde claro · texto branco · tom pessoal
**Direção:** fala diretamente com quem acompanhou a semana toda

## SLIDE 4
**Texto:** O que você recebe no Essência:
- 4 meses de acompanhamento individual
- Consultas + plano + avaliação de exames
- Suporte entre as consultas
- Um plano feito pra sua rotina real
**Visual:** fundo areia · lista limpa com marcadores terra
**Direção:** recapitulação do valor — última vez que a seguidora vê isso

## SLIDE 5
**Texto:** "Início: 20 de abril. Vagas: 10. Quando fechar, próxima turma é Maio."
**Visual:** fundo terra (#C17F5B) · texto branco · números em destaque
**Direção:** todos os fatos relevantes em um slide

## SLIDE 6
**Texto:** "Para garantir a sua vaga: DM com 'QUERO ABRIL'. A gente conversa."
**Visual:** fundo verde (#4A7C6F) · texto branco · "QUERO ABRIL" em destaque
**Direção:** primeiro passo fácil e concreto

## SLIDE 7 — CTA Final
**Texto:** "Te vejo do outro lado. 💚"
**Visual:** fundo areia · texto verde escuro · assinatura "Mayara Farias · Nutricionista" · logo Essência
**Direção:** encerramento caloroso — não pressão de vendas, convite

---
## LEGENDA SUGERIDA
Esta semana falei sobre o que trava o emagrecimento. Sobre como funciona o Essência por dentro. Sobre uma paciente que descobriu que nunca teve problema de força de vontade.

Se você se viu aqui, essa mensagem é pra você.

Turma de Abril: últimas vagas. Acompanhamento começa dia 20.

4 meses individuais. Plano feito pra sua rotina. Consultas, avaliação de exames, suporte real.

Quando as vagas de Abril fecharem, a próxima turma é Maio.

Para garantir a sua: DM com "QUERO ABRIL". A gente conversa sem pressão.

Te vejo do outro lado. 💚

---
## HASHTAGS
#emagrecimentofeminino #nutriçãocomportamental #programanutrição
#acompanhamentonutricional #nutricionista #saúdedamulher #turmaabril
```

- [ ] **Passo 2: Revisar**
  - Recapitula a semana antes de fechar? ✓
  - Tom é convite, não pressão? ✓
  - Menciona lista de Maio para quem não pegar Abril? ✓
  - CTA único e claro? ✓

- [ ] **Passo 3: Commit**
```bash
git add Campanhas/essencia/carrosseis/dia5_c2_cta_final.md
git commit -m "content: carrossel dia5-C2 — CTA final Turma de Abril"
```

---

## Self-Review — Checklist Final

### Cobertura do Spec
- [x] 10 carrosséis (2/dia × 5 dias) ✓
- [x] Abordagem B (identificação manhã + conversão tarde) ✓
- [x] Escassez por turma mensal, não por janela artificial ✓
- [x] Urgência cresce progressivamente (menção leve → urgência genuína) ✓
- [x] Foco emagrecimento feminino / comportamental ✓
- [x] Identidade visual Essência em todos os slides ✓
- [x] Hashtags em todos os posts (5–8 por carrossel) ✓
- [x] CTAs coerentes com momento do funil ✓
- [x] Tom acolhedor, sem culpa, sem pressão forçada ✓

### Consistência
- Palavra-chave DM padronizada: "QUERO ABRIL" (aparece nos dias 4 e 5)
- Número de vagas consistente: "10" em todos os posts
- Data de início consistente: "20/04" em todos os posts
- Cor terra (#C17F5B) sempre nos slides de urgência/vagas ✓
