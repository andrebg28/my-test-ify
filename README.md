# Test.py - Micro-Framework de Testes para Projetos de Bootcamp

## Descrição

O Test.py foi criado como um micro-framework de testes minimalista, visando atender aos requisitos de projetos em bootcamps sem a necessidade de instalar dependências adicionais. A ferramenta oferece uma implementação direta para testes de igualdade entre valores, especialmente útil para valores str e int.

## Propósito

O Test.py surgiu com o objetivo de facilitar a validação de funções e métodos nos desafios de código dos bootcamps. Ele permite testar de forma rápida e automatizada o retorno das funções, fornecendo segurança para refatorações e acelerando o desenvolvimento. Como o framework é leve e não depende de instalações extras, ele pode ser executado pelos avaliadores sem necessidade de configuração adicional.

## Funcionalidades Principais

- Testes de Igualdade: O foco principal é testar se o retorno das funções é igual ao valor esperado.
- Mensagens de Resultado: Exibe uma mensagem indicando o sucesso ou falha dos testes.
- Simplicidade e Portabilidade: Implementado como uma classe estática com métodos de classe, o Test.py não precisa de instância e não possui complexidade adicional.

## Exemplo de Uso

```python

from Test import Test

Test.assert_equals("Hello", "Hello", "Testando igualdade de strings")
Test.assert_equals(42, 42, "Testando igualdade de inteiros")

Test.print_summary()
```

## Estrutura e Decisões de Design

Optou-se pela implementação com métodos de classe estáticos para evitar a criação de instâncias e manter a simplicidade. Mesmo com limitações de modularidade, essa abordagem foi adequada para resolver o problema imediato e atender ao propósito específico.

## Limitações

Embora tenha sido desenvolvido sem planos iniciais de expansão, o uso contínuo do Test.py levou à ideia de uma versão mais modular e extensível, permitindo novos tipos de teste. Isso resultou na criação de um projeto evolutivo chamado testify, que incorpora boas práticas de POO, SOLID, e padrões de design.
