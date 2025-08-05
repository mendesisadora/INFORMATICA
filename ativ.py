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

#Crie um programa que pergunte ao usuário uma senha e só saia do loop se ele digitar "1234".
#senha = "1234"
#while 

#6.Crie um programa que peça 5 números e imprima a soma total.
numero1 = input("insira o primeiro número:")
numero2 = input("insira o segundo número:")
numero3 = input("insira o terceiro número:")
numero4 = input("insira o quarto número:")
numero5 = input("insira o quinto número:")
soma = numero1+numero2+numero3+numero4+numero5
print(soma)