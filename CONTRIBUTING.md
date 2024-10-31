
# Contribuindo com o Projeto Testify

Obrigado por seu interesse em contribuir com o **Testify**! Este guia irá ajudá-lo a começar e a entender como podemos trabalhar juntos para melhorar este projeto.

## Como Contribuir

### 1. Faça um Fork do Projeto

Se você quiser contribuir, o primeiro passo é fazer um **fork** deste repositório para o seu GitHub. Isso criará uma cópia do projeto na sua conta.

### 2. Clone o Repositório

Clone o repositório que você acabou de criar:

```bash
git clone https://github.com/seu-usuario/testify.git
```

### 3. Crie uma Branch para Suas Alterações

Crie uma branch para suas alterações, utilizando um nome descritivo que explique a sua modificação:

```bash
git checkout -b minha-feature
```

### 4. Faça Suas Modificações

Implemente suas melhorias ou correções de bugs no código.

### 5. Teste Suas Alterações

Antes de enviar seu código, execute os testes para garantir que tudo funciona corretamente:

```bash
# Execute os testes unitários (se aplicável)
python -m unittest
```

### 6. Padrão de Commits Semânticos

Utilize o padrão de commits semânticos ao fazer seus commits. Isso facilita a leitura do histórico de commits e ajuda a identificar rapidamente o que cada commit faz.

| Tipo de Commit | Descrição                                                            | Exemplo                                          |
| ---------------|----------------------------------------------------------------------|--------------------------------------------------|
| `feat`         | Adiciona uma nova funcionalidade ao projeto.                         | `feat: adicionar suporte para testes numéricos`  |
| `fix`          | Corrige um bug ou problema no projeto.                               | `fix: corrigir erro na função de ataque`         |
| `docs`         | Atualiza ou cria documentação.                                       | `docs: atualizar README com novas instruções`    |
| `style`        | Modifica apenas a aparência ou formatação, sem mudar a funcionalidade.| `style: ajustar indentação no arquivo principal` |
| `refactor`     | Refatora o código sem alterar a funcionalidade.                      | `refactor: reorganizar lógica de ataques`        |
| `test`         | Adiciona ou modifica testes no projeto.                              | `test: adicionar testes para classe Hero`        |
| `chore`        | Atualiza tarefas de build ou configurações.                          | `chore: atualizar dependências`                  |

### 7. Envie Suas Alterações

Faça um commit das suas alterações:

```bash
git commit -m "feat: descrição curta da feature"
```

Envie suas alterações para o GitHub:

```bash
git push origin minha-feature
```

### 8. Abra um Pull Request

Por fim, abra um **pull request** explicando as alterações que você fez. Um mantenedor irá revisar seu código e aprová-lo ou sugerir melhorias.

---

## Regras de Conduta

Ao contribuir, por favor, mantenha uma postura respeitosa e amigável. Todos os colaboradores devem seguir o nosso [Código de Conduta](./CODE_OF_CONDUCT.md).

---

Obrigado novamente por contribuir com o **Testify**! Seu apoio é muito importante.
