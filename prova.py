"""Considere uma lista de números inteiros 
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Utilizando as funções map(),filter() e reduce(), escreva um código que execute as seguintes operações:
Função map() para obter uma nova lista com o quadrado de cada número da lista numeros
Função filter() para obter uma nova lista com números pares da lista numeros
Função reduce()  para obter a soma de todos os números da lista numeros
Qual o resultado obtido após a execução das operações acima?
"""
from functools import reduce
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

func_map = list(map(lambda num: num**2, numeros))
func_filter = list(filter(lambda num: num % 2 == 0, numeros))
func_reduce = (reduce(lambda num, num2: num + num2, numeros))


print(f'O retorno da func "map" é: \n{func_map}')
print(f'o retorno da func "filter" é: \n{func_filter}')
print(f'o retorno da func "reduce" é: \n{func_reduce}')