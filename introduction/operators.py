

#Operadores aritméticos

produto_1 = 10
produto_2 = 20

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

x = 10 + 5 * 4
print(x)

# Operadores de comparação

saldo = 200
saque = 200

print(saldo == saque)
print(saldo != saque)
print(saldo > saque)
print(saldo >= saque)
print(saldo < saque)
print(saldo <= saque)

# Operadores de atribuição

saldo = 20
print(saldo)

saldo = 2
print(saldo)

saldo += 10
print(saldo)

saldo -= 5
print(saldo)

saldo /= 10
print(saldo)

saldo // 5
print(saldo)

saldo //= 5
print(saldo)

saldo ** 2
print(saldo)

saldo %= 3
print(saldo)

saldo *= 3
print(saldo)

# Operadores lógicos

#AND = para ser True tudo tem que ser True
#OR = para ser True apenas um tem que ser True

print(True and True)
print(True and False)
print (False and False)
print(True or True)
print(True or False)
print (False or False)


saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(exp_2)

#Operadores de identidade

saldo = 1000
limite = 1000

print(saldo is limite)
print (saldo is not limite)

#Operadores de associação

#curso = "Curso de Python"
#frutas = ["laranja", "uva", "limão"]
#saques = [1500,100]

#"Phyton" in curso
#>>> True

#"maçã" not in frutas>>> True

frutas = ["limão", "uva"]

print("laranja" in frutas)
print("limão"  not in frutas)


