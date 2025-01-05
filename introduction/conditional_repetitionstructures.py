#Indentação e blocos

def sacar(valor):
    saldo = 500

    if saldo >= valor: #4 espaços
        print("Valor sacado!") #8 espaços (boa convenção)
        print("Retire o seu dinheiro na boca do caixa")

    print("obrigado por ser nosso cliente")


sacar (1000)

#Estruturas condicionais

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("Maior de idade, pode tirar a CNH")

else:
    print("Ainda não pode tirar a CNH")

    
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas")
else:
    print("Ainda não pode tirar a CNH")

#Estrutura condicional alinhada

conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Não foi possível realizar o saque!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente")

