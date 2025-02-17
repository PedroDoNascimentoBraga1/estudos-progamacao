def armazenar(informacao,linha):
    with open('dados.txt', 'r') as arquivo:
        conteudo = arquivo.readlines()

    while linha >= len(conteudo):
        conteudo.append("\n")

    conteudo[linha - 1] = f"{informacao}\n"

    with open('dados.txt','w') as arquivo:
        arquivo.writelines(conteudo)

        
def ler(linha):
    with open('dados.txt', 'r') as arquivo:
        conteudo = arquivo.readlines()
        return(conteudo[linha - 1])

    
for x in range (101):
    print(ler(x))