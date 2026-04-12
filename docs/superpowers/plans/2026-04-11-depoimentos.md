# Depoimentos Landing Page — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Substituir todos os placeholders de depoimentos por conteúdo real na landing page do Programa Essência.

**Architecture:** Modificação direta do `index.html` — novo CSS para cards de imagem, troca dos placeholders de texto nas seções de crença, e substituição completa da grade de prova social por cards com prints de WhatsApp. Imagens copiadas para subpasta `depoimentos/` dentro da landing page.

**Tech Stack:** HTML, CSS (sem dependências externas)

---

## Mapa de arquivos

| Ação | Arquivo |
|------|---------|
| Criar | `Campanhas/essencia/landing page/depoimentos/` (pasta + 5 imagens copiadas) |
| Modificar | `Campanhas/essencia/landing page/index.html` — CSS + HTML |

---

### Task 1: Copiar imagens para a pasta da landing page

**Files:**
- Create: `Campanhas/essencia/landing page/depoimentos/` (5 arquivos)

- [ ] **Step 1: Criar pasta e copiar as 5 imagens**

```bash
mkdir -p "Campanhas/essencia/landing page/depoimentos"
cp "imagens/depoimentos/image.png"  "Campanhas/essencia/landing page/depoimentos/image.png"
cp "imagens/depoimentos/image2.png" "Campanhas/essencia/landing page/depoimentos/image2.png"
cp "imagens/depoimentos/image3.png" "Campanhas/essencia/landing page/depoimentos/image3.png"
cp "imagens/depoimentos/image4.jpeg" "Campanhas/essencia/landing page/depoimentos/image4.jpeg"
cp "imagens/depoimentos/image5.jpeg" "Campanhas/essencia/landing page/depoimentos/image5.jpeg"
```

- [ ] **Step 2: Verificar que os 5 arquivos estão na pasta**

```bash
ls "Campanhas/essencia/landing page/depoimentos/"
```

Esperado: `image.png  image2.png  image3.png  image4.jpeg  image5.jpeg`

- [ ] **Step 3: Commit**

```bash
git add "Campanhas/essencia/landing page/depoimentos/"
git commit -m "assets: adiciona prints de depoimentos na landing page Essência"
```

---

### Task 2: Adicionar CSS dos cards de imagem

**Files:**
- Modify: `Campanhas/essencia/landing page/index.html` — bloco CSS de `.prova-img-card`

Localizar no CSS o bloco `/* ════ PROVA SOCIAL ════ */` e adicionar logo após as regras existentes de `.prova-mosaic` o seguinte CSS:

- [ ] **Step 1: Adicionar `align-items: start` ao `.prova-mosaic` existente**

Localizar:
```css
.prova-mosaic { display: grid; grid-template-columns: repeat(3,1fr); gap: 18px; }
```
Trocar por:
```css
.prova-mosaic { display: grid; grid-template-columns: repeat(3,1fr); gap: 18px; align-items: start; }
```

- [ ] **Step 2: Adicionar CSS do card de imagem**

Inserir após a linha `.prova-card:nth-child(5) .prova-card-loc { ... }`:

```css
/* Cards de imagem — depoimentos reais */
.prova-img-card {
  background: var(--branco);
  border-radius: 12px;
  border-top: 3px solid var(--verde);
  overflow: hidden;
  box-shadow: 0 2px 14px rgba(0,0,0,.08);
  break-inside: avoid;
}
.prova-img-header {
  background: #f5f5f5;
  padding: 8px 14px;
  display: flex;
  align-items: center;
}
.prova-img-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #25D366;
}
.prova-img-card img {
  width: 100%;
  height: auto;
  display: block;
}
```

- [ ] **Step 2: Verificar que o CSS não quebrou nada**

Abrir `Campanhas/essencia/landing page/index.html` no navegador. A seção de prova social ainda mostra os 6 cards de texto placeholder — isso é esperado (o HTML ainda não foi trocado).

---

### Task 3: Substituir depo-card da Crença 1

**Files:**
- Modify: `Campanhas/essencia/landing page/index.html` — seção `sec-crenca-1`

- [ ] **Step 1: Localizar o depo-card placeholder**

Encontrar o bloco:
```html
<div class="depo-card">
  <blockquote>
    "[Inserir depoimento real de paciente que chegou com essa mesma crença e transformou o resultado. Pode ser um print de WhatsApp ou texto com permissão da paciente.]"
  </blockquote>
  <div class="depo-autor">
    <div class="depo-avatar">M</div>
    <div class="depo-info">
      <strong>Paciente do Programa Essência</strong>
      <span>Ubatuba, SP</span>
    </div>
  </div>
</div>
```

- [ ] **Step 2: Substituir pelo depoimento real**

```html
<div class="depo-card">
  <blockquote>
    "A sua consulta, mesmo online, foi uma injeção de ânimo para mim. Era como se tivesse batendo papo com uma amiga. Voltei a sentir prazer em preparar as minhas refeições e comer bem. Recomendaria super você."
  </blockquote>
  <div class="depo-autor">
    <div class="depo-avatar">C</div>
    <div class="depo-info">
      <strong>Paciente do Programa Essência</strong>
      <span>Online</span>
    </div>
  </div>
</div>
```

- [ ] **Step 3: Verificar visualmente**

Abrir a página no navegador, rolar até "Quebrando o ciclo" — o card deve mostrar o texto real, sem aspas duplas de placeholder.

---

### Task 4: Substituir depo-card da Crença 2

**Files:**
- Modify: `Campanhas/essencia/landing page/index.html` — seção `sec-crenca-2`

- [ ] **Step 1: Localizar o depo-card placeholder**

Encontrar o bloco:
```html
<div class="depo-card">
  <blockquote>
    "[Inserir depoimento de paciente que fala sobre o acolhimento, sobre ter se sentido entendida, sobre o suporte emocional que fez diferença — não só sobre o número na balança.]"
  </blockquote>
  <div class="depo-autor">
    <div class="depo-avatar">A</div>
    <div class="depo-info">
      <strong>Paciente do Programa Essência</strong>
      <span>Online</span>
    </div>
  </div>
</div>
```

- [ ] **Step 2: Substituir pelo depoimento real**

```html
<div class="depo-card">
  <blockquote>
    "Eu amei o atendimento — sua energia e alegria. A gente consegue ficar à vontade. Eu não preciso fazer maluquice pra alcançar o que eu quero. 1000 se todos tivessem uma nutri amiga assim."
  </blockquote>
  <div class="depo-autor">
    <div class="depo-avatar">A</div>
    <div class="depo-info">
      <strong>Paciente · Consulta</strong>
      <span>Ubatuba, SP</span>
    </div>
  </div>
</div>
```

- [ ] **Step 3: Verificar visualmente**

Abrir a página no navegador, rolar até "Sobre força de vontade" — o card deve mostrar o texto real.

- [ ] **Step 4: Commit tasks 3 e 4**

```bash
git add "Campanhas/essencia/landing page/index.html"
git commit -m "content: depoimentos reais nas seções Crença 1 e Crença 2"
```

---

### Task 5: Substituir a grade de Prova Social por cards de imagem

**Files:**
- Modify: `Campanhas/essencia/landing page/index.html` — seção `sec-prova`

- [ ] **Step 1: Localizar o bloco prova-mosaic**

Encontrar o bloco inteiro:
```html
<div class="prova-mosaic">
  <div class="prova-card">
    ...
  </div>
  ... (6 cards no total)
</div>
```

- [ ] **Step 2: Substituir pelos 5 cards de imagem**

```html
<div class="prova-mosaic">
  <div class="prova-img-card">
    <div class="prova-img-header"><div class="prova-img-dot"></div></div>
    <img src="./depoimentos/image.png" alt="Depoimento de paciente">
  </div>
  <div class="prova-img-card">
    <div class="prova-img-header"><div class="prova-img-dot"></div></div>
    <img src="./depoimentos/image2.png" alt="Depoimento de paciente">
  </div>
  <div class="prova-img-card">
    <div class="prova-img-header"><div class="prova-img-dot"></div></div>
    <img src="./depoimentos/image3.png" alt="Depoimento de paciente">
  </div>
  <div class="prova-img-card">
    <div class="prova-img-header"><div class="prova-img-dot"></div></div>
    <img src="./depoimentos/image4.jpeg" alt="Depoimento de paciente">
  </div>
  <div class="prova-img-card">
    <div class="prova-img-header"><div class="prova-img-dot"></div></div>
    <img src="./depoimentos/image5.jpeg" alt="Depoimento de paciente">
  </div>
</div>
```

- [ ] **Step 3: Atualizar regra mobile do prova-mosaic**

Localizar no media query `@media (max-width: 1024px)`:
```css
.prova-mosaic { grid-template-columns: 1fr; }
```
Confirmar que essa regra já existe — ela cobre tanto os cards antigos quanto os novos automaticamente.

- [ ] **Step 4: Verificar visualmente**

Abrir a página no navegador:
- Desktop: 3 colunas com os 5 prints, alturas naturais, borda verde no topo de cada card
- Mobile (redimensionar janela abaixo de 1024px): 1 coluna, imagens empilhadas

- [ ] **Step 5: Commit final**

```bash
git add "Campanhas/essencia/landing page/index.html"
git commit -m "content: seção prova social com prints reais de depoimentos WhatsApp"
```
