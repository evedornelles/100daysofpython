frutas = ["laranja", "maca", "uva"]

frutas = []

letras = list("python")

numeros = list(range(10))

carro = ["Ferrari", "F8", 420000, 2020, 2900, "São Paulo", True]

#Acesso direto

frutas = ["maçã", "laranja", "uva", "pera"]

print(frutas[0])  # maçã
print(frutas[2])  # uva

#Indices negativos

frutas = ["maçã", "laranja", "uva", "pera"]

print(frutas[-1])  # pera
print(frutas[-3])  # laranja

#Matriz

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"