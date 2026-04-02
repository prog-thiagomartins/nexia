# Workflow: Landing Page Builder

## Objetivo

Criar landing pages animadas e de alto valor comercial usando Claude Code como orquestrador, com Anime.js e GSAP para animações, seguindo um processo estruturado e reproduzível.

## Inputs Necessários

- `project_name`: Nome do projeto/produto
- `goal`: Objetivo da página (captura de leads, venda direta, evento, etc.)
- `sections`: Lista de seções desejadas (hero, benefícios, depoimentos, CTA, etc.)
- `style_reference`: URL ou descrição visual de referência (opcional)
- `images`: Imagens prontas ou instrução para gerar via `image_generation_pipeline.md`

## Ferramentas

- Claude Code (orquestrador principal)
- Anime.js — animações de entrada, contadores, efeitos de texto
- GSAP — scroll horizontal, efeitos magnéticos de mouse, parallax

## Processo

### Passo 1 — Definir estrutura da página

Antes de escrever qualquer código, defina com o usuário:

1. Quais seções a página terá e em que ordem
2. Qual o CTA principal (botão, formulário, link)
3. Paleta de cores e tipografia (ou extrair de referência)
4. Se haverá scroll horizontal (efeito favorito do criador — funciona bem para features/pilares)

Documente isso em `.tmp/lp_brief_<project_name>.md` antes de prosseguir.

### Passo 2 — Scaffolding do projeto

Crie a estrutura de arquivos:

```
<project_name>/
├── index.html
├── css/
│   └── styles.css
├── js/
│   ├── animations.js    # Anime.js — animações de entrada
│   ├── scroll.js        # GSAP — scroll horizontal e parallax
│   └── magnetic.js      # Efeito magnético do mouse
├── images/
│   └── (geradas via image_generation_pipeline.md)
└── assets/
    └── (fontes, ícones)
```

Inclua Anime.js e GSAP via CDN no `<head>` do HTML:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
```

### Passo 3 — Construir HTML e CSS

1. Construa o HTML semântico de cada seção
2. Aplique CSS base: layout, cores, tipografia, responsividade mobile
3. Adicione classes de animação (`data-animate`, `data-scroll`) nos elementos que serão animados — deixe os efeitos para o próximo passo

**Regra:** Mobile-first. A página deve funcionar bem no celular antes de qualquer animação.

### Passo 4 — Implementar animações

Implemente em camadas, testando cada uma antes de avançar:

**Camada 1 — Entrada (Anime.js)**
```js
// Exemplo: fade + slide up nos elementos com data-animate
anime({
  targets: '[data-animate]',
  opacity: [0, 1],
  translateY: [30, 0],
  duration: 800,
  delay: anime.stagger(100),
  easing: 'easeOutExpo'
});
```

**Camada 2 — Scroll horizontal (GSAP)**
```js
// Para seções de features/pilares
gsap.registerPlugin(ScrollTrigger);
gsap.to(".horizontal-track", {
  x: () => -(document.querySelector(".horizontal-track").scrollWidth - window.innerWidth),
  ease: "none",
  scrollTrigger: {
    trigger: ".horizontal-section",
    pin: true,
    scrub: 1,
    end: () => "+=" + document.querySelector(".horizontal-track").scrollWidth
  }
});
```

**Camada 3 — Efeito magnético do mouse**
```js
// Botões e elementos interativos seguem o cursor
document.querySelectorAll('.magnetic').forEach(el => {
  el.addEventListener('mousemove', (e) => {
    const rect = el.getBoundingClientRect();
    const x = e.clientX - rect.left - rect.width / 2;
    const y = e.clientY - rect.top - rect.height / 2;
    el.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px)`;
  });
  el.addEventListener('mouseleave', () => {
    el.style.transform = 'translate(0, 0)';
  });
});
```

### Passo 5 — Imagens

Se as imagens ainda não estiverem prontas, execute `image_generation_pipeline.md` agora e aplique os arquivos gerados na pasta `images/`.

### Passo 6 — Revisão final

Checklist antes de considerar a página pronta:

- [ ] Abre corretamente no mobile e no desktop
- [ ] Animações não travam em dispositivos mais lentos
- [ ] CTA está visível acima da dobra (sem scroll)
- [ ] Scroll horizontal funciona com trackpad e touch
- [ ] Imagens têm fundo removido onde necessário
- [ ] Nenhum erro no console do navegador

## Outputs

- Pasta `<project_name>/` com todos os arquivos da landing page
- Página funcional, animada e responsiva
- Pronta para deploy via `deploy_site.md`

## Edge Cases

| Situação | Como lidar |
|---|---|
| GSAP ScrollTrigger não funciona | Verificar se o plugin foi registrado com `gsap.registerPlugin(ScrollTrigger)` |
| Animações lentas no mobile | Reduzir `duration` e desativar efeito magnético em touch devices (`'ontouchstart' in window`) |
| Imagens sem fundo disponíveis | Executar `image_generation_pipeline.md` antes de continuar |
| Cliente quer CMS | Escopo diferente — esse workflow é para páginas estáticas de alta performance |

## Referências do Vídeo

- Canal: Mateus Dias — "CLAUDE CODE + NANO BANANA PRO = Sites de R$10.000"
- Bibliotecas usadas em produção: Anime.js + GSAP
- Efeito scroll horizontal validado em páginas reais com boa taxa de conversão
