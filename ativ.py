#1.Escreva um programa que imprima os números de 1 a 10 usando o for.
numero = 1
for numero in range (1,11):
    print(numero)

#2.Escreva um programa que imprima os números de 10 a 1 usando while.
contador = 1
while contador <= 10:
    print(contador)
    contador += 1

#3.Crie um programa que pergunte o nome do usuário e o imprima 5 vezes.
nome = input("Digite o seu nome:")
for _ in range(5):
    print(nome)

#4.Imprima os números pares de 0 a 20 usando for com range().
numero = 1
for numero in range (1,21):
    print(numero)

#5.Crie um programa que pergunte ao usuário uma senha e só saia do loop se ele digitar "1234".
#senha = "1234"
#while 

#6.Crie um programa que peça 5 números e imprima a soma total.
numero1 = float(input(f"insira o primeiro número:"))
numero2 = float(input(f"insira o segundo número:"))
numero3 = float(input(f"insira o terceiro número:"))
numero4 = float(input(f"insira o quarto número:"))
numero5 = float(input(f"insira o quinto número:"))
