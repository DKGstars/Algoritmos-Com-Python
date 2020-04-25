print("Tipos de operacoes Aritimeticas em Python:")
print("Exercicio:2.1")
'''
Cap2 Converta as seguintes expressões matemáticas para que possam ser
calculadas usando o interpretador Python.
1)10 + 20 × 30
2)4**2 ÷ 30
3)(9**4 + 2) × 6 - 1
'''
print((10 + 20) * 30)
print((4 ** 2) / 30)
print((9 ** 4 + 2) * (6 - 1))
print("/////////////////////////////////////")

print("Exercicio:2.2")
'''
Exercício 2.2 Digite a seguinte expressão no interpretador:
4)10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2
Tente resolver o mesmo cálculo, usando apenas lápis e papel. Observe como a
prioridade das operações é importante.
'''
print((10 % 3) * (10 ** 2 + 1) - (10 * 4 / 2))
print("/////////////////////////////////////")

print("Conceitos de variaveis e atribuicao:")
#Em python para atribuir valores a variaveis usamos o sinal de(=)
#Em python as variaveis podem ser declaradas implicitamente 
print("Exempol 01")
a = 5 #modo implicito
b = 8

print(a + b)

print("Exemplo 02")
salario01 = 1500
aumento01 = 5

print(salario01 + (salario01 * aumento01 / 100))
print("/////////////////////////////////////")

print("Exercicios Finais do Capitulo02")
'''
1)Faça um programa que exiba seu nome na tela.
2)Escreva um programa que exiba o resultado de 2a × 3b, onde a vale
3 e b vale 5.
3)Modifique o primeiro programa, listagem 2.7, de forma a calcular a
soma de três variáveis.
4)Modifique o programa da listagem 2.11, de forma que ele calcule um
aumento de 15% para um salário de R$ 750.
'''
print("Exercicio 1:")

print("Lucas Augusto")

print("Exercicio 2:")

a = 3
b = 5

print(2*a * 3*b)

print("Exercicio 3:")

a = 3
b = 5
c = 9

print(a + b + c)

print("Exercicio 4:")

salario02 = 750
aumento02 = 15

print(salario02 + (salario02 + aumento02 / 100))
print("//////////////FIM-CAP2///////////////")