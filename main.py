from my_test_ify import my_test_ify

# Inicialização das funções do módulo testify
core, report = my_test_ify()

# O teste de igualdade é implicitamente chamado quando o quarto parâmetro de core é omitido.
core(1, 1, "Testando igualdade de inteiros")
core("Hello", "Hello", "Testando igualdade de strings")
core(4.0, 4.1, "Testando igualdade de números com ponto flutuante")

from my_test_ify.assertive import (greater_than, less_than, not_equals,
                                   raises_exception)
from my_test_ify.exceptions import TestFunctionError

core(1, 3, "Testando desigualdade de inteiros", not_equals)
core(3, 2, "Testando se é maior que", greater_than)
core(2, 3, "Testando se é menor que", less_than)

def func (a: int):
    raise TestFunctionError("Teste de exceção")

# O quinto parâmetro de core é uma lista ou dicionario de argumentos que são passados pela função testada. Neste caso, a função `func`.
core(TestFunctionError, func, "test8", raises_exception, [1]) # O ultimo parâmetro é uma lista de argumentos que são passados pela função testada.
core(TestFunctionError, func, "test8", raises_exception, {'a':1}) # O ultimo parâmetro é um dicionario de argumentos que são passados pela função testada.
core(TestFunctionError, func, "test8", raises_exception) # O ultimo parâmetro é um dicionario de argumentos que são passados pela função testada.


print(report.report()) # Imprime o relatório de testes
print(report.failure_stack()[0]) # Imprime o stack da primeira falha, caso haja falhas. Se não houver falhas, imprime "No failures".
print(report.summary()) # Imprime o resumo dos testes
