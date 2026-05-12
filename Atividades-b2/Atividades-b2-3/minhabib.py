# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#                  FATEC São Caetano do Sul                 
#                       Atividade B2-3                      
#                   Tiago Bondezan Bazani                   
#                Objetivo: Árvore Binária (AINDA PRECISA SER FEITO, TROQUEI O ARQUIVO PARA UM NÃO PRONTO!!!!!               
#                          12.05.2026                       
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class No:
        def __init__(self, valor):
                self.valor = valor
                self.esq = None
                self.dir = None

class ArvoreBST:
        def __init__(self, raiz=None):
                self.raiz = raiz
        
        def analisar_arvore(self): pass
                
        def imprimir_nos_internos(self): pass        
        
        def imprimir_folhas(self): pass

        def imprimir_niveis(self): pass

        def calcular_altura(self, no): pass

        def calcular_profundidade(self, valor): pass

        def imprimir_ancestrais(self, valor): pass

        def imprimir_descendentes(self, valor): pass
