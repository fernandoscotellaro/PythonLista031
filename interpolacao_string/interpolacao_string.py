nome = input("Digite aqui o seu primeiro nome:")
idade = int(input("Digite aqui a sua idade:"))

#print("Olá,", nome, "!")
#print("Tudo bem com você?")
#print("Caramba", nome, "! Você tem", idade, "anos mesmo? \nNem parece.")


#print("Olá, {}!".format(nome))
#print("Tudo bem com você?")
#print("Caramba", nome, "! Você tem", idade, "anos mesmo? Nem parece.".format(nome, idade))


print("Olá, {}!".format(nome))
print("Tudo bem com você?")

print("Caramba", nome, "! Você tem", idade, "anos mesmo? Nem parece.".format(nome, idade))
print(f"Caramba {nome}! Você tem {idade} anos mesmo? Nem parece") #resultado: Caramba fernando! Você tem 16 anos? Nem parece
print(f"Caramba {nome}! Você tem {idade} anos mesmo? \nNem parece.")