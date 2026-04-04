# Architecture Reference

Documento de referência para guiar o agente na construção de aplicações profissionais com Claude Code. Leia este arquivo antes de qualquer implementação.

---

## Estrutura de Pastas (por comportamento)

Organize o projeto por **página → comportamento**, não por tipo de arquivo.

```
src/
  pages/
    <page-name>/
      <behavior-name>/    ← cada comportamento isolado aqui
        index.tsx         ← componente principal do comportamento
        hooks.ts          ← lógica local do comportamento
        types.ts          ← tipos específicos deste comportamento
  components/             ← componentes reutilizáveis entre páginas
  lib/                    ← utilitários, clientes de API, helpers
  server/                 ← toda lógica de negócio e acesso a dados
```

**Regra:** Quando um behavior precisa ser modificado, apenas a pasta daquele behavior é tocada. Isso evita que mexer em uma coisa quebre outra.

---

## Regra de Segurança: Thin Client / Fat Server

### O que o front end PODE fazer
- Capturar interações do usuário (cliques, inputs, formulários)
- Chamar endpoints do back end
- Exibir a resposta recebida
- Gerenciar estado visual (loading, erro, sucesso)

### O que o front end NUNCA pode fazer
- Conter regras de negócio (ex: "se admin, mostrar X")
- Validar permissões (isso é responsabilidade do back end)
- Armazenar ou expor chaves de API, tokens ou secrets
- Fazer chamadas diretas ao banco de dados

### O que o back end é responsável por
- Toda validação de permissão e autenticação
- Toda lógica de negócio
- Todo acesso a dados (banco, APIs externas)
- Retornar apenas o que o front end precisa exibir

> **Por quê:** Tudo no front end é acessível com dois cliques no navegador. Qualquer segredo ou regra de negócio exposta no front end é uma vulnerabilidade.

---

## Regras de Implementação

### Reutilização antes de recriar
Antes de criar qualquer componente, hook, função ou modelo:
1. Pesquise na base de código se já existe algo equivalente
2. Se existir, importe — não recrie
3. Se precisar de variação, estenda o existente

### Padrões comprovados antes de inventar
Antes de implementar uma integração externa ou algoritmo:
1. Consulte a documentação oficial da dependência
2. Use o padrão documentado
3. Não invente soluções quando há uma estabelecida

### Tarefas pequenas
- Nunca implemente mais de um comportamento por sessão
- Se a tarefa parece grande, quebre antes de executar
- Contexto limpo = performance melhor

### Arquivos explícitos
- Sempre liste os arquivos a criar ou modificar antes de implementar
- Não toque em arquivos fora da lista
- Se descobrir que outro arquivo precisa mudar, pare e informe

---

## Checklist antes de implementar

- [ ] Pesquisei se o componente/função já existe na codebase?
- [ ] A lógica de negócio está no back end, não no front end?
- [ ] Nenhuma chave ou secret está no front end?
- [ ] Os arquivos a modificar estão listados explicitamente?
- [ ] Estou seguindo o padrão de isolamento por behavior?
