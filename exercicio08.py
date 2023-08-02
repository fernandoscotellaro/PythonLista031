'''
8)	Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o valor do consumo médio do automóvel, em quilômetros por litro.
'''

distancia = float(input("Qual a distância percorrida pelo automóvel na viagem? KM:"))
consumo = float(input("Quantos KM o automóvel percorre com um litro de gasolina?"))

bill = distancia / consumo

print("O valor de litros que o automóvel utilizou foi de: ", bill)
