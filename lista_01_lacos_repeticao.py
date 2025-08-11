# 1. Imprimir números de 1 a 10 usando for
print("1. Números de 1 a 10:")
for i in range(1, 11):
    print(i)

# 2. Imprimir números de 10 a 1 usando while
print("\n2. Números de 10 a 1:")
i = 10
while i >= 1:
    print(i)
    i -= 1

# 3. Perguntar o nome e imprimir 5 vezes
print("\n3. Nome impresso 5 vezes:")
nome = input("Digite seu nome: ")
for i in range(5):
    print(nome)

# 4. Imprimir números pares de 0 a 20
print("\n4. Números pares de 0 a 20:")
for i in range(0, 21, 2):
    print(i)

# 5. Pedir senha até digitar "1234"
print("\n5. Verificação de senha:")
while True:
    senha = input("Digite a senha: ")
    if senha == "1234":
        print("Acesso permitido!")
        break

# 6. Ler 5 números e imprimir a soma
print("\n6. Soma de 5 números:")
soma = 0
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    soma += num
print("Soma total:", soma)

# 7. Pular números ímpares entre 1 e 10
print("\n7. Números pares de 1 a 10 usando continue:")
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)

# 8. Ler números até digitar 0 e contar quantos foram digitados
print("\n8. Contagem de números digitados (0 para parar):")
contador = 0
while True:
    num = int(input("Digite um número (0 para parar): "))
    if num == 0:
        break
    contador += 1
print("Quantidade de números digitados:", contador)

# 9. Tabuada de um número
print("\n9. Tabuada de um número:")
n = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")