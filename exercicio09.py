'''
9)	Fazer um algoritmo que pergunte 1 número e apresente:
a)	O próprio número
b)	O quadrado deste número
c)	A raiz quadrada deste número
'''

import math

num = int(input("Aqui você deve inserir o número que você deseja trabalhar: "))

a = num
b = num * num
c = math.sqrt(num)

print("Esse é o número que você inseriu:", a)
print("Esse é o quadrado do número:", b )
print("Essa é a raiz quadrada do seu número:", c)