from dados import armazenar,ler

class Tipo_transicao:
    def __init__(self, tipo, linha):
        self.tipo = tipo
        self.linha = linha
    
    
def transicao(descricao , valor , data, tipo , linha):
    saldo = valor + int(ler(1))
    armazenar(f"Saldo atual: {str(saldo),1}")
    


transicao("Salário",1450,"01/02/25",5,5)

