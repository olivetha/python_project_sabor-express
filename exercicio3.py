#1-Crie uma lista para cada informação a seguir:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = [Thais, Tatiana, Leonardo, Giuseppe]
anos = [1995, 2024]

#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
for numero in numeros:
    print(numero)

#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)
# O segundo argumento de da função range é exclusivo, 
# então range(1, 11) inclui números de 1 a 10) com um passo de 2 (o terceiro argumento de range). 
# Isso garante que apenas números ímpares sejam considerados.

#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente. 
for i in range(10, 0, -1):
    print(i)

#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")

#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
#Exception é uma classe base para todas as exceções em Python. 
#Capturar Exception permite lidar com qualquer tipo de exceção que possa ocorrer no bloco try. 
#O as e é opcional, mas é frequentemente usado para acessar informações detalhadas sobre a exceção, como mensagens de erro.

#7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
#ZeroDivisionError é uma exceção específica que ocorre quando há uma tentativa de divisão por zero. 
#Este bloco except é destinado a lidar especificamente com esse tipo de erro.