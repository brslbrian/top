#abrir arquivo para escrita
with open('arquivo.txt', 'w', encoding='UTF-8') as file:
    file.write('Olá, mundo!\n')
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')


#abrir um arquivo para leitura e escrita 
with open('arquivo.txt', 'r+') as file:
    conteudo = file.read()
    file.write('\nAdicionando mais conteudo. ')

#abrir um arquivo para anexo
with open('arquivo.txt', 'a') as file:
    file.write('\nMais uma linha no final do arquivo')

#Abre o arquivo no modo de leitura ('r')
with open('arquivo.txt', 'r') as file:
    #Le todo o conteudo do arquivo
    conteudo = file.read()
    print(conteudo)

#Abre o arquivo no modo de leitura ('r')
with open('arquivo.txt', 'r') as file:
    #le a primeira linha do arquivo
    linha1 = file.readline()
    #le a segunda linha do arquivo
    linha2 = file.readline()
    #le a terceira linha do arquivo
    linha3 = file.readline()
    print(linha1)
    print(linha2)
    print(linha3)