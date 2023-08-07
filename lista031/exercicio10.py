'''
10)	Fazer um algoritmo que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula prestação	=	valor	+	(valor	x	(taxa	:	100)	x	tempo	em	dias).
'''

valor = float(input("Qual o valor da sua prestação? R$"))
atraso = int(input("Quantos dias de atraso tem a sua prestação?"))
taxa = float(input("Qual é a taxa de atraso em porcentagem? "))

conta = valor + (valor * (taxa / 100) * atraso)

print("Esse é o valor da sua conta com a soma dos dias de prestação cobrados pelo atraso do pagamento: R$", conta)