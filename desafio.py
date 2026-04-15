with open ('meuarquivo.txt', 'w', encoding='UTF-8') as file:
    nome = input('Digite seu nome: ')
    file.write('Olá, mundo!\n')
    file.write('Este é um arquivo de texto\n')
    file.write(f'Criado por {nome}\n')

with open("meuarquivo.txt", "r", encoding="UTF-8") as arquivo:
    while True:
        linha = arquivo.readline()
        if not linha:
            break
        print(linha)
