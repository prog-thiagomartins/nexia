# Landing Page + Quiz — Plano de Implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ajustar a landing page do Programa Essência para o novo funil — remover o preço, trocar os CTAs para "Quero entender meu perfil", e substituir o formulário de triagem por um quiz de 5 perguntas que envia o perfil da pessoa pro WhatsApp da Mayara ao final.

**Architecture:** Tudo acontece em um único arquivo HTML (`Campanhas/essencia/landing page/index.html`). O quiz substitui a seção `#triagem` atual. CSS e JS são adicionados inline no mesmo arquivo, seguindo o padrão já existente.

**Tech Stack:** HTML, CSS, JavaScript vanilla — sem dependências externas.

---

## Arquivo modificado

- `Campanhas/essencia/landing page/index.html` — único arquivo alterado

---

## Task 1: Remover o preço e atualizar a seção de investimento

**Contexto:** A seção `sec-preco` (linha ~744) exibe o valor R$1.497 e condições de pagamento. Precisamos remover o preço visível e atualizar o texto da sessão diagnóstica (era gratuita de 40 min, agora é R$97 e 30 min) e o CTA.

**Files:**
- Modify: `Campanhas/essencia/landing page/index.html` (seção sec-preco, ~linha 744)

- [ ] **Substituir o conteúdo da preco-card**

Localizar o bloco atual (linhas 748–764) e substituir por:

```html
    <div class="preco-card">
      <div class="preco-nome">Programa Essência · 4 meses</div>
      <ul class="preco-lista">
        <li>4 consultas de 60–90 minutos</li>
        <li>2 entregáveis personalizados</li>
        <li>2 check-ins de acompanhamento</li>
        <li>Mapeamento de perfil comportamental</li>
        <li>Linha cronológica individualizada</li>
        <li>Alta ao final dos 4 meses</li>
      </ul>
      <div class="preco-cashback">
        <strong>Começa com uma sessão diagnóstica de 30 min</strong> — para mapear seu perfil antes de qualquer coisa.
      </div>
      <a href="#quiz" class="btn-primary">Quero entender meu perfil</a>
    </div>
```

- [ ] **Atualizar o título da seção** (linha ~747)

Trocar:
```html
    <h2 class="section-title">Tudo que você precisa<br>para começar de verdade</h2>
```
Por:
```html
    <h2 class="section-title">Um programa feito<br>para o seu perfil</h2>
```

- [ ] **Remover CSS não mais usado**

Localizar e remover as regras `.preco-valor` e `.preco-parcela` no bloco de CSS (linhas ~357–361):
```css
    .preco-valor {
```
e
```css
    .preco-parcela {
```
(remover cada regra completa, do seletor até o `}` fechador)

- [ ] **Commit**

```bash
git add "Campanhas/essencia/landing page/index.html"
git commit -m "feat: remove preco da landing e atualiza sessao diagnostica"
```

---

## Task 2: Atualizar todos os CTAs da página

**Contexto:** Existem 3 CTAs que apontam para `#triagem` com textos variados. Todos precisam apontar para `#quiz` com o texto unificado "Quero entender meu perfil".

**Files:**
- Modify: `Campanhas/essencia/landing page/index.html`

- [ ] **Atualizar CTA do hero** (linha ~486)

Trocar:
```html
    <a href="#triagem" class="btn-primary">Quero saber se é pra mim</a>
```
Por:
```html
    <a href="#quiz" class="btn-primary">Quero entender meu perfil</a>
```

- [ ] **Atualizar CTA da seção final** (linha ~839)

Trocar:
```html
    <a href="#triagem" class="btn-white">Quero preencher o formulário</a>
```
Por:
```html
    <a href="#quiz" class="btn-white">Quero entender meu perfil</a>
```

- [ ] **Atualizar copy da seção final** (linhas ~835–838)

Trocar:
```html
    <p class="cta-body">
      Preencha o formulário abaixo. Vou analisar o seu caso e entrar em contato
      para marcarmos a sua sessão diagnóstica gratuita.
    </p>
```
Por:
```html
    <p class="cta-body">
      Responda algumas perguntas rápidas. Com base no seu perfil, você recebe sua análise personalizada na sessão diagnóstica com a Mayara.
    </p>
```

- [ ] **Commit**

```bash
git add "Campanhas/essencia/landing page/index.html"
git commit -m "feat: unifica CTAs para o quiz"
```

---

## Task 3: Substituir a seção de triagem pelo quiz

**Contexto:** A seção atual `id="triagem"` (linha ~845) tem um formulário simples que manda dados pro WhatsApp. Vamos substituir inteiramente por um quiz de 5 perguntas com uma tela de resultado final.

**Fluxo do quiz:**
1. Perguntas aparecem uma de cada vez — clique na opção avança automaticamente
2. Indicador de progresso (Pergunta 1 de 5)
3. Tela final: "Seu perfil está pronto" + botão que abre WhatsApp com resumo das respostas

**Files:**
- Modify: `Campanhas/essencia/landing page/index.html`

- [ ] **Substituir toda a seção `#triagem`**

Localizar o bloco (linha ~844 até linha ~882):
```html
<!-- ══════════════ 12. FORMULÁRIO DE TRIAGEM ══════════════ -->
<section id="triagem">
  ...
</section>
```

Substituir por:

```html
<!-- ══════════════ 12. QUIZ ══════════════ -->
<section id="quiz">
  <div class="container-narrow">
    <div class="quiz-header">
      <span class="section-tag">Seu perfil</span>
      <h2 class="section-title">Algumas perguntas rápidas</h2>
      <p class="quiz-sub">Clique na opção que mais combina com você. Leva menos de 2 minutos.</p>
    </div>

    <div class="quiz-card" id="quiz-card">

      <!-- PROGRESS -->
      <div class="quiz-progress" id="quiz-progress">
        <div class="quiz-progress-bar" id="quiz-progress-bar"></div>
      </div>
      <div class="quiz-step-label" id="quiz-step-label">Pergunta 1 de 5</div>

      <!-- PERGUNTAS -->
      <div id="quiz-perguntas">

        <!-- P1 -->
        <div class="quiz-pergunta active" data-p="1">
          <p class="quiz-enunciado">Qual dessas frases mais descreve você hoje?</p>
          <div class="quiz-opcoes">
            <button class="quiz-opcao" data-p="1" data-v="Ja tentei varias dietas e sempre volto para onde estava">Já tentei várias dietas e sempre volto para onde estava</button>
            <button class="quiz-opcao" data-p="1" data-v="Sei o que devo comer mas nao consigo colocar em pratica">Sei o que devo comer, mas não consigo colocar em prática</button>
            <button class="quiz-opcao" data-p="1" data-v="Tenho uma relacao dificil com a comida - ansiedade culpa compulsao">Tenho uma relação difícil com a comida — ansiedade, culpa ou compulsão</button>
            <button class="quiz-opcao" data-p="1" data-v="Quero emagrecer sem abrir mao de ter uma vida normal">Quero emagrecer sem abrir mão de ter uma vida normal</button>
          </div>
        </div>

        <!-- P2 -->
        <div class="quiz-pergunta" data-p="2">
          <p class="quiz-enunciado">Há quanto tempo você está tentando resolver isso?</p>
          <div class="quiz-opcoes">
            <button class="quiz-opcao" data-p="2" data-v="Menos de 6 meses">Menos de 6 meses</button>
            <button class="quiz-opcao" data-p="2" data-v="Entre 6 meses e 2 anos">Entre 6 meses e 2 anos</button>
            <button class="quiz-opcao" data-p="2" data-v="Mais de 2 anos">Mais de 2 anos</button>
            <button class="quiz-opcao" data-p="2" data-v="A vida toda">A vida toda</button>
          </div>
        </div>

        <!-- P3 -->
        <div class="quiz-pergunta" data-p="3">
          <p class="quiz-enunciado">O que você já tentou antes?</p>
          <p class="quiz-multi-hint">Pode selecionar mais de uma opção.</p>
          <div class="quiz-opcoes">
            <button class="quiz-opcao quiz-multi" data-p="3" data-v="Dieta restritiva / low carb / jejum">Dieta restritiva / low carb / jejum</button>
            <button class="quiz-opcao quiz-multi" data-p="3" data-v="Acompanhamento nutricional">Acompanhamento nutricional</button>
            <button class="quiz-opcao quiz-multi" data-p="3" data-v="Reeducacao alimentar por conta propria">Reeducação alimentar por conta própria</button>
            <button class="quiz-opcao quiz-multi" data-p="3" data-v="Apps de contagem de calorias">Apps de contagem de calorias</button>
            <button class="quiz-opcao quiz-multi" data-p="3" data-v="Nada ainda, esse seria meu primeiro passo">Nada ainda, esse seria meu primeiro passo</button>
          </div>
          <button class="quiz-avancar" id="quiz-avancar-p3" onclick="avancarP3()">Continuar →</button>
        </div>

        <!-- P4 -->
        <div class="quiz-pergunta" data-p="4">
          <p class="quiz-enunciado">Como você se descreveria em relação a compromissos?</p>
          <div class="quiz-opcoes">
            <button class="quiz-opcao" data-p="4" data-v="Sou consistente quando acredito no que estou fazendo">Sou consistente quando acredito no que estou fazendo</button>
            <button class="quiz-opcao" data-p="4" data-v="Comeco bem mas perco o fio com o tempo">Começo bem mas perco o fio com o tempo</button>
            <button class="quiz-opcao" data-p="4" data-v="Preciso de acompanhamento para me manter no caminho">Preciso de acompanhamento para me manter no caminho</button>
            <button class="quiz-opcao" data-p="4" data-v="Depende muito do meu estado emocional">Depende muito do meu estado emocional</button>
          </div>
        </div>

        <!-- P5 -->
        <div class="quiz-pergunta" data-p="5">
          <p class="quiz-enunciado">O que você mais quer ao final de 4 meses?</p>
          <div class="quiz-opcoes">
            <button class="quiz-opcao" data-p="5" data-v="Emagrecer de forma definitiva">Emagrecer de forma definitiva</button>
            <button class="quiz-opcao" data-p="5" data-v="Parar de ter uma relacao de culpa com a comida">Parar de ter uma relação de culpa com a comida</button>
            <button class="quiz-opcao" data-p="5" data-v="Entender meu corpo e minhas escolhas">Entender meu corpo e minhas escolhas</button>
            <button class="quiz-opcao" data-p="5" data-v="Ter mais energia e disposicao no dia a dia">Ter mais energia e disposição no dia a dia</button>
          </div>
        </div>

      </div><!-- /quiz-perguntas -->

      <!-- RESULTADO -->
      <div id="quiz-resultado" style="display:none; text-align:center; padding: 16px 0;">
        <div class="quiz-resultado-icon">✦</div>
        <h3 class="quiz-resultado-titulo">Seu perfil está pronto.</h3>
        <p class="quiz-resultado-corpo">Para receber sua análise personalizada com a Mayara, agende sua sessão diagnóstica.</p>
        <a id="quiz-btn-wa" href="#" class="btn-primary" target="_blank">Agendar minha sessão</a>
        <p class="quiz-resultado-nota">Você será atendida pelo WhatsApp.</p>
      </div>

    </div><!-- /quiz-card -->
  </div>
</section>
```

- [ ] **Commit**

```bash
git add "Campanhas/essencia/landing page/index.html"
git commit -m "feat: substitui formulario de triagem pelo quiz de 5 perguntas"
```

---

## Task 4: Adicionar CSS do quiz

**Contexto:** O quiz tem elementos novos (card, opções, barra de progresso, resultado) que precisam de estilo. Inserir antes do fechamento `</style>` no `<head>`.

**Files:**
- Modify: `Campanhas/essencia/landing page/index.html` (bloco `<style>` no `<head>`)

- [ ] **Remover a regra CSS antiga `#triagem`**

Localizar no bloco `<style>` a linha:
```css
    #triagem { background: var(--areia); }
```
E remover — o `#quiz` já tem essa regra no CSS novo abaixo.

- [ ] **Inserir CSS do quiz antes de `</style>`**

```css
    /* ════ QUIZ ════ */
    #quiz { background: var(--areia); }
    .quiz-header { text-align: center; margin-bottom: 40px; }
    .quiz-sub { font-size: 16px; color: var(--text-muted); margin-top: 8px; }

    .quiz-card {
      background: white; border-radius: 20px;
      padding: 40px 44px; max-width: 600px; margin: 0 auto;
      box-shadow: 0 4px 32px rgba(0,0,0,.07);
    }

    .quiz-progress {
      height: 4px; background: var(--areia-dark);
      border-radius: 2px; margin-bottom: 10px;
    }
    .quiz-progress-bar {
      height: 4px; background: var(--verde);
      border-radius: 2px; width: 20%;
      transition: width .35s ease;
    }
    .quiz-step-label {
      font-size: 12px; font-weight: 600; letter-spacing: .08em;
      text-transform: uppercase; color: var(--text-muted);
      margin-bottom: 28px;
    }

    .quiz-pergunta { display: none; }
    .quiz-pergunta.active { display: block; }

    .quiz-enunciado {
      font-family: 'Poppins', sans-serif;
      font-size: clamp(17px, 2.2vw, 21px); font-weight: 700;
      color: var(--verde-dark); line-height: 1.35; margin-bottom: 24px;
    }
    .quiz-multi-hint {
      font-size: 13px; color: var(--text-muted); margin: -16px 0 20px;
    }

    .quiz-opcoes { display: flex; flex-direction: column; gap: 12px; }
    .quiz-opcao {
      text-align: left; background: var(--areia);
      border: 2px solid transparent; border-radius: 12px;
      padding: 16px 20px; font-size: 15px; line-height: 1.5;
      color: var(--text); cursor: pointer;
      transition: border-color .15s, background .15s;
    }
    .quiz-opcao:hover { border-color: var(--verde-light); background: #f0f7f5; }
    .quiz-opcao.selecionada { border-color: var(--verde); background: #e8f4f1; }

    .quiz-avancar {
      margin-top: 20px; background: var(--terra); color: white;
      border: none; border-radius: 100px; padding: 14px 36px;
      font-family: 'Poppins', sans-serif; font-size: 14px; font-weight: 700;
      text-transform: uppercase; letter-spacing: .04em; cursor: pointer;
      transition: background .2s;
    }
    .quiz-avancar:hover { background: var(--terra-dark); }

    .quiz-resultado-icon {
      font-size: 32px; color: var(--terra); margin-bottom: 16px;
    }
    .quiz-resultado-titulo {
      font-family: 'Poppins', sans-serif;
      font-size: clamp(22px, 3vw, 30px); font-weight: 800;
      color: var(--verde-dark); margin-bottom: 16px;
    }
    .quiz-resultado-corpo {
      font-size: 17px; color: var(--text-mid); line-height: 1.7;
      margin-bottom: 32px; max-width: 420px; margin-left: auto; margin-right: auto;
    }
    .quiz-resultado-nota {
      font-size: 13px; color: var(--text-muted); margin-top: 16px;
    }

    @media (max-width: 600px) {
      .quiz-card { padding: 28px 20px; }
    }
```

- [ ] **Commit**

```bash
git add "Campanhas/essencia/landing page/index.html"
git commit -m "feat: adiciona CSS do quiz"
```

---

## Task 5: Adicionar JavaScript do quiz

**Contexto:** O quiz precisa de lógica para avançar entre perguntas, atualizar o progresso, lidar com multi-seleção na P3, e montar a mensagem do WhatsApp com o resumo das respostas. Inserir antes do fechamento `</script>` no final do arquivo.

**Files:**
- Modify: `Campanhas/essencia/landing page/index.html` (bloco `<script>` no final)

- [ ] **Remover a função `enviarTriagem` antiga**

Localizar no bloco `<script>` a função completa:
```javascript
  function enviarTriagem(e) {
```
E deletar do `function enviarTriagem` até o `}` fechador — ela não é mais usada.

- [ ] **Inserir JS do quiz antes de `</script>` (no final do arquivo)**

```javascript
  // ── QUIZ ──
  const quizRespostas = {};
  let quizPasso = 1;
  const TOTAL_PASSOS = 5;
  const WA_NUMERO = '5512991734388';

  function quizAtualizarProgresso() {
    const pct = (quizPasso / TOTAL_PASSOS) * 100;
    document.getElementById('quiz-progress-bar').style.width = pct + '%';
    document.getElementById('quiz-step-label').textContent =
      'Pergunta ' + quizPasso + ' de ' + TOTAL_PASSOS;
  }

  function quizAvancar(p) {
    const atual = document.querySelector('.quiz-pergunta.active');
    const prox = document.querySelector('.quiz-pergunta[data-p="' + (p + 1) + '"]');
    if (atual) atual.classList.remove('active');
    if (prox) {
      quizPasso = p + 1;
      quizAtualizarProgresso();
      prox.classList.add('active');
    } else {
      quizMostrarResultado();
    }
  }

  function quizMostrarResultado() {
    document.getElementById('quiz-perguntas').style.display = 'none';
    document.getElementById('quiz-progress').style.display = 'none';
    document.getElementById('quiz-step-label').style.display = 'none';
    const resultado = document.getElementById('quiz-resultado');
    resultado.style.display = 'block';

    const r = quizRespostas;
    const msg = encodeURIComponent(
      'Oi Mayara! Acabei de fazer o quiz do Essencia.\n\n' +
      'Meu perfil:\n' +
      '- ' + (r[1] || '') + '\n' +
      '- Ha quanto tempo: ' + (r[2] || '') + '\n' +
      '- Ja tentei: ' + (r[3] || '') + '\n' +
      '- Comprometimento: ' + (r[4] || '') + '\n' +
      '- Objetivo: ' + (r[5] || '') + '\n\n' +
      'Quero agendar minha sessao diagnostica.'
    );
    document.getElementById('quiz-btn-wa').href =
      'https://wa.me/' + WA_NUMERO + '?text=' + msg;
  }

  // Cliques nas opções de resposta única (P1, P2, P4, P5)
  document.querySelectorAll('.quiz-opcao:not(.quiz-multi)').forEach(function(btn) {
    btn.addEventListener('click', function() {
      const p = parseInt(this.getAttribute('data-p'));
      quizRespostas[p] = this.getAttribute('data-v');
      quizAvancar(p);
    });
  });

  // Cliques nas opções multi-seleção (P3)
  document.querySelectorAll('.quiz-opcao.quiz-multi').forEach(function(btn) {
    btn.addEventListener('click', function() {
      this.classList.toggle('selecionada');
      const selecionadas = document.querySelectorAll('.quiz-opcao.quiz-multi.selecionada');
      document.getElementById('quiz-avancar-p3').style.display =
        selecionadas.length > 0 ? 'inline-block' : 'none';
    });
  });

  function avancarP3() {
    const selecionadas = document.querySelectorAll('.quiz-opcao.quiz-multi.selecionada');
    const valores = Array.from(selecionadas).map(function(b) {
      return b.getAttribute('data-v');
    });
    quizRespostas[3] = valores.join(', ');
    quizAvancar(3);
  }

  // Esconder botão "Continuar" da P3 inicialmente
  document.addEventListener('DOMContentLoaded', function() {
    var btn = document.getElementById('quiz-avancar-p3');
    if (btn) btn.style.display = 'none';
  });
```

- [ ] **Commit**

```bash
git add "Campanhas/essencia/landing page/index.html"
git commit -m "feat: adiciona logica do quiz e mensagem WhatsApp com perfil"
```

---

## Task 6: Verificar e testar no browser

**Contexto:** Não há testes automatizados para HTML. A verificação é manual abrindo o arquivo no navegador.

- [ ] **Abrir o arquivo no browser**

```bash
start "Campanhas/essencia/landing page/index.html"
```
Ou abrir via VS Code Live Server.

- [ ] **Verificar lista de checagem visual**

- [ ] Página abre sem erros no console (F12)
- [ ] CTA do hero diz "Quero entender meu perfil" e faz scroll até o quiz
- [ ] Seção de preço não exibe R$1.497
- [ ] Seção de preço exibe a lista de benefícios + texto da sessão diagnóstica
- [ ] CTA da seção final diz "Quero entender meu perfil"
- [ ] Seção quiz exibe pergunta 1 com barra de progresso
- [ ] Clicar em uma opção avança para pergunta 2
- [ ] Pergunta 3 permite multi-seleção e só avança ao clicar "Continuar →"
- [ ] Após pergunta 5, aparece tela de resultado
- [ ] Botão "Agendar minha sessão" abre WhatsApp com mensagem contendo as respostas
- [ ] Botão flutuante do WhatsApp continua funcionando

- [ ] **Commit final**

```bash
git add "Campanhas/essencia/landing page/index.html"
git commit -m "feat: landing page v2 — quiz de perfil e funil diagnostica"
```

---

## Próximo plano

Após aprovação desta landing: **Plano 2 — Sistema WhatsApp** (automação de agenda, pagamento R$97, sequência anti-no-show, scripts + IA copiloto).
