# Concluído — Site Principal

## Hoje (13/abr/2026) — v0 no ar

### Brainstorm
- [x] Spec da hub escrito (visao-geral.md): hub raiz como porta de entrada da marca + chamariz SEO
- [x] 3 mockups visuais comparados (V1 Clean / V2 Imersivo / V3 Editorial) — escolhido **V1 Clean** como base por equilibrar bio-link e densidade SEO
- [x] Skills marketing-ops consultadas: site-architecture (URL/anchor/NAP) + schema-markup (Person + MedicalBusiness + FAQPage)

### Conteúdo (sem invenções, fonte autoritativa nos arquivos)
- [x] Tagline aprovada: "Ajudo mulheres a comerem de verdade — com saúde, energia e sem culpa. E gestantes a ter uma gravidez tranquila."
- [x] Bio Sobre: aproveitada da landing Essência (residência → gestantes → "não entrego dieta, entrego entendimento")
- [x] 3 caminhos: Programa Essência (featured) + Acompanhamento Gestacional (R$2.000) + Consulta Avulsa (R$350, com badge "+30 dias suporte WhatsApp")
- [x] FAQ com 4 perguntas (com FAQPage schema)
- [x] Faixa Instagram com CTA "Quer me conhecer melhor?"
- [x] Removido CRN visível no header (mantido apenas no Person schema)

### Design
- [x] Identidade Essência aplicada (verde-dark/terra/areia + Poppins/DM Sans/Playfair Italic)
- [x] Hero com foto sessão jan/2025 (IMG_1137)
- [x] Sobre com foto sessão jan/2025 (IMG_1313) circular
- [x] Responsividade trabalhada em 4 breakpoints (1200/1024/768/480)
- [x] Padding elástico no hero pra manter background full-width sem comprimir conteúdo

### SEO
- [x] Title + meta description otimizados (keyword + nicho + local)
- [x] Open Graph + Twitter cards completos
- [x] Canonical
- [x] Schema JSON-LD: Person + MedicalBusiness + FAQPage
- [x] sameAs apontando pro Instagram (entidade)
- [x] NAP completo no footer (Ubatuba + WhatsApp)

### Deploy
- [x] Pasta `Campanhas/site-principal/` criada com index.html + imagens/{hero,sobre}/
- [x] Deploy via `netlify deploy --prod --site=edd8eb93-55d5-4b38-b8db-7d15479b3cfd` (projeto helpful-wisp-833428)
- [x] **No ar em https://mayarafarias.com.br** (13/abr/2026)
