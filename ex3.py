pala = input("Digite sua palavra: ")

with open('arquivoter.txt', 'r', encoding='UTF-8') as file:
    encontrada = False
    for linha in file:
        if pala.lower() in linha.lower():
            encontrada = True
            break  

if encontrada:
    print("Encontrada")
else:
    print("Não encontrada")
