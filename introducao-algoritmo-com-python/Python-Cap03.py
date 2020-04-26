'''
Em Python temos os Seguinte tipos de Variaveis mais usadas: integer,float ou decimal ,string ,bool.

integer (numeros inteiros: 7,-85,32500,...,etc);
float ou decimal (7.8,25000.95,...,etc)
string (todos os valores entre aspas duplas "");
bool (retorna valores logicos (treu ou false));

Operadores Relacionais em Python
== (igualdade)
> (Maior)
< (Menor)
!= (Difrente)
>= (Maior ou igual)
<= (Menor ou igual)
'''
#Exemplo do uso de Operadores Relacionais
print("Exemplo 3.1")
a = 1.0
b = 5
c = 3
d = 1
 
print(a == b)
print(b > a)
print(c != a)
print(c <= b)
print(a == d)
print(b >= c)


print("////////////////////////////////////")
'''
Operadores Relacionais tambem podem ser utilizados junto de variaveis do tipo logico
'''
print("Exemplo 3.2")

nota = 8
media = 7
aprovado = (nota > media) #A vairavel  aprovado ela vai receber o resultado da comparacao logica recebendo (true or false)

print("Voce foi aprovado",aprovado)

print("////////////////////////////////////")

'''
Operadores logicos
and (e)
not (nao)
or (ou)

Descricao:

O operador (not) é unario ou seja so precisa de um operando
ele é conhecido como operador inverso pois ele transforma um valor verdadeiro em falso e vice-versa;

Ja os outro dois and e or sao operadores binarios precisao de dois operandos
o (and) ele so resulta em verdadeiro se os dois operadores forem verdadeiros caso contrario sera sempre falso;
o (or) ele sempre sera verdadeiro se somente um de seus operadores forem verdadeiros.
'''
print("Exemplo 3.3")

print("Operador not")
#Exemplo do operador not
print(not False)
print(not True)

print("Operador and")
#Exemplo do operador and
print(True and True)
print(True and False)

print("Operador or")
#Exemplo do operador or
print(True or False)
print(True or True)
print(False or True)
print(False or False)
 

