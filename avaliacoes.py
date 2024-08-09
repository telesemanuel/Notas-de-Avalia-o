import os

# Solicita ao usuário o número de avaliações
quantidade_notas = int(input("Digite o número de avaliações: "))

# Inicializa a soma das notas
soma_notas = 0

# Coleta as notas e as soma
for i in range(quantidade_notas):
    nota = float(input(f"Digite a nota da avaliação {i+1}: "))
    soma_notas += nota
    os.system("cls")
    print("\nAvaliação Concluida.\n")

os.system("cls")

# Calcula a média
media = soma_notas / quantidade_notas

# Exibe a média
print(f"A média das notas é: {media:.2f}")