"""Método para escrever em arquivos txt, com isso é possivel criar arquivos <com memória>"""

with open('livro-de-dados.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
print(conteudo)

conteudo[0] = "teste \n"

print(conteudo)

with open('livro-de-dados.txt','w') as arquivo:
    arquivo.writelines(conteudo)