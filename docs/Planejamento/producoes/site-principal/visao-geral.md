# Visão Geral — Site Principal (mayarafarias.com.br)

**Domínio:** mayarafarias.com.br
**Status:** No ar em **v0** · https://mayarafarias.com.br (13/abr/2026)
**Progresso:** 90%
**Deploy:** Netlify (projeto helpful-wisp-833428)

## Objetivo

Página única (hub) que serve duas funções:
1. **Link da bio do Instagram** — destino limpo, mobile-first, com escolha óbvia
2. **Chamariz pro Google e descoberta** — SEO local + entidade Mayara, ranqueando por "nutricionista comportamental Ubatuba", "nutricionista gestantes online", "diabetes gestacional"

## Estrutura aprovada (em brainstorm)

1. **Hero** — foto + nome + tagline + cidade + atendimento online
2. **Sobre Mayara** — narrativa real (residência → gestantes → processo próprio → "entendimento, não dieta")
3. **Especialidades** — chips estáticos (chips viram link só quando a página existir)
4. **Caminhos** — 3 cards: Programa Essência (featured) + Acompanhamento Gestacional + Consulta Avulsa
5. **Instagram** — CTA secundário, fora dos cards (canal, não serviço)
6. **FAQ** — 4-6 perguntas com FAQPage schema
7. **Footer** — NAP completo (Name/Address/Phone) + sameAs Insta

## Stack técnica

- HTML estático (mesmo padrão da Essência)
- Deploy: Netlify (novo projeto separado de mayarafarias-essencia)
- Schema markup: Person + MedicalBusiness + FAQPage
- Open Graph + Twitter cards
- Identidade visual: paleta Essência (verde-dark/terra/areia + Poppins/DM Sans)

## Observações pendentes (não inventar)

- ⚠️ **Formação acadêmica** — não documentado no workspace. Não citar até Mayara confirmar (graduação, ano, universidade).
- ⚠️ **Pós-graduação / especializações** — não documentado. NÃO é "Nutrição Comportamental" (foi alucinação minha em iteração anterior).
- ⚠️ **Anos de experiência** — não documentado.
- ⚠️ **Foto profissional** — usar `imagens/Sessão fotos Nutri/Sessão de fotos 2025/25012025-IMG_1137.jpg` na hero.

## Fora do escopo (v0)

- Blog (decidido — manutenção alta, ela já posta no Insta)
- Múltiplas páginas internas (futuro: criar pillars `/diabetes-gestacional` e `/nutricao-comportamental` quando fizer sentido)
- Sistema de agendamento (WhatsApp resolve)
- Formulário de contato (WhatsApp resolve)
