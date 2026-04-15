with open('arquivo.txt', 'r', encoding='UTF-8') as f1:
    conteudo1 = f1.read()

with open('meuarquivo.txt', 'r', encoding='UTF-8') as f2:
    conteudo2 = f2.read()

with open('arquivoter.txt', 'w', encoding='UTF-8') as f3:
    f3.write(conteudo1)
    f3.write('\n')
    f3.write(conteudo2)