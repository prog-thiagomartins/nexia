# Design: Depoimentos — Landing Page Essência

**Data:** 2026-04-11  
**Contexto:** Landing page do Programa Essência (`Campanhas/essencia/landing page/index.html`)

---

## Objetivo

Substituir todos os placeholders de depoimentos por conteúdo real, usando os 5 prints de WhatsApp disponíveis em `imagens/depoimentos/`.

---

## Imagens disponíveis

| Arquivo | Dimensões | Conteúdo resumido |
|---------|-----------|-------------------|
| image.png | 590×1020 | Dani — menos estufada, mais energia, intestino ok |
| image2.png | 456×499 | Autoestima, leveza, estresse diminuiu |
| image3.png | 539×674 | "Injeção de ânimo", voltou a sentir prazer em cozinhar |
| image4.jpeg | 448×202 | Energia de 30% foi para 90% com vitaminas |
| image5.jpeg | 590×521 | "Não preciso fazer maluquice", "nutri amiga" |

---

## Seção 1 — Crença 1: Quebrando o ciclo

**Localização:** `div.depo-card` dentro de `section.sec-crenca-1`

**Ação:** Substituir o blockquote placeholder pelo texto extraído de `image3.png`.

**Texto:**
> "A sua consulta, mesmo online, foi uma injeção de ânimo para mim. Era como se tivesse batendo papo com uma amiga. Voltei a sentir prazer em preparar as minhas refeições e comer bem. Recomendaria super você."

**Autor:** Paciente do Programa Essência  
**Avatar:** inicial "C" (nome não identificado, usar inicial genérica)

---

## Seção 2 — Crença 2: Sobre força de vontade

**Localização:** `div.depo-card` dentro de `section.sec-crenca-2`

**Ação:** Substituir o blockquote placeholder pelo texto extraído de `image5.jpeg`.

**Texto:**
> "Eu amei o atendimento — sua energia e alegria. A gente consegue ficar à vontade. Eu não preciso fazer maluquice pra alcançar o que eu quero. 1000 se todos tivessem uma nutri amiga assim."

**Autor:** Paciente · Consulta  
**Avatar:** inicial "A"

---

## Seção 3 — Prova Social: Resultados reais

**Localização:** `div.prova-mosaic` dentro de `section.sec-prova`

### Layout

- Substituir os 6 `div.prova-card` de texto por 5 cards de imagem
- Grid: `repeat(3, 1fr)`, `gap: 18px`, `align-items: start`
- Mobile (≤1024px): `grid-template-columns: 1fr`

### Estilo do card (`.prova-img-card`)

```
fundo: branco (#FAFAFA)
border-radius: 12px
border-top: 3px solid var(--verde)
overflow: hidden
box-shadow: 0 2px 14px rgba(0,0,0,.08)
```

### Cabeçalho do card (`.prova-img-header`)

```
background: #f5f5f5
padding: 8px 14px
contém: bolinha verde (8px, #25D366) — sem texto
```

### Imagem

```
width: 100%
height: auto
display: block
```

### Ordem dos cards

1. image.png
2. image2.png
3. image3.png
4. image4.jpeg
5. image5.jpeg

### Arquivos

Copiar as 5 imagens para:  
`Campanhas/essencia/landing page/depoimentos/`

Referências no HTML usam caminho relativo: `./depoimentos/image.png` etc.

---

## CSS a remover

Os estilos `.prova-card`, `.prova-stars`, `.prova-card-autor`, `.prova-card-loc` podem ser removidos ou mantidos comentados — não serão mais usados após a troca.

---

## Extensibilidade

Para adicionar novos depoimentos no futuro: basta inserir um novo `div.prova-img-card` com a imagem dentro de `.prova-mosaic`. O grid acomoda automaticamente.

---

## Fora de escopo

- Edição ou recorte das imagens
- Animações ou lightbox ao clicar
- Nomes reais das pacientes (privacidade)
