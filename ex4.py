with open('arquivoter.txt', 'r', encoding='UTF-8') as file:
    texto = file.read()
    pala = texto.lower().split()
    po = sorted(pala)
    for i in po:
        print(i)