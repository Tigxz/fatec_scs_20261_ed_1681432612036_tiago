'''
*---------------------------------------------------------------*
*       Fatec São Caetano do Sul                                *
*       Atividade B2-2                                          *
*       Autor: Tiago Bondezan Bazani                            *
*       Objetivo: Gerenciar uma ordem de impressão seguindo     *
*       os conceitos de fila                                    *
*                                                               *  
*       data: 30/04/2026                                        *
*---------------------------------------------------------------*
'''

class FilaImpressao: 
    def __init__(self):
        self.fila_administracao = []
        self.fila_alunos = []
        self.fila_geral = []

    def adicionar_arquivo(self, usuario, nome_arquivo, quantidade_paginas):
        documento = {
            "arquivo": nome_arquivo, 
            "paginas": quantidade_paginas
        }

        tipo_usuario = usuario.lower()
        
        if tipo_usuario in ['adm', 'administrador', 'admin']:
            self.fila_administracao.append(documento)
            print(f"Documento '{nome_arquivo}' adicionado à fila de Administração")
        elif tipo_usuario in ['aluno', 'alunos']:
            self.fila_alunos.append(documento)
            print(f"Documento '{nome_arquivo}' adicionado à fila de Alunos")
        else:
            print("Tipo de usuário inválido.")

    def reorganizar_fila(self):
        if not self.fila_administracao and not self.fila_alunos:
            print("Filas vazias")
            return

        if len(self.fila_geral) == 0:
            self.fila_geral.extend(self.fila_administracao)
            self.fila_geral.extend(self.fila_alunos)
            self.fila_administracao.clear()
            self.fila_alunos.clear()
            print("Fila Geral organizada (Administração primeiro)!")
        else:
            print("Ainda existe itens na Fila Geral.")

    def consumir_fila(self):  
        if len(self.fila_geral) > 0:
            documento_atual = self.fila_geral.pop(0)
            print(f"Imprimindo...\nArquivo: '{documento_atual['arquivo']}' | Páginas: {documento_atual['paginas']}")
        else:
            print("Fila Geral vazia. Reorganize antes de imprimir.")

    def exibir_listas(self):
        print("\n--- STATUS DAS FILAS ---")
        self.mostrar_sublista("Fila de Administração", self.fila_administracao)
        self.mostrar_sublista("Fila de Alunos", self.fila_alunos)
        self.mostrar_sublista("Fila Geral", self.fila_geral)

    def mostrar_sublista(self, nome_da_lista, lista):
        if lista:  
            print(f"{nome_da_lista}:")
            for doc in lista:
                print(f"  - {doc['arquivo']} ({doc['paginas']} págs)")
        else:
            print(f"{nome_da_lista} está vazia")

sistema = FilaImpressao()
while True:
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("SISTEMA DE FILA DE IMPRESSÃO")
    print("1 - Adicionar arquivo")
    print("2 - Consumir fila (Imprimir)")
    print("3 - Listar estado das filas")
    print("4 - Reorganizar fila")
    print("0 - Sair")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")


    opcao = input("Escolha: ")

    if opcao == '1':
        user = input("Tipo (adm/aluno): ").strip()
        nome_arq = input("Nome do arquivo: ").strip()
        try:
            paginas = int(input("Quantidade de páginas: "))
            sistema.adicionar_arquivo(user, nome_arq, paginas)
        except ValueError:
            print("ERRO: Quantidade de páginas deve ser um número inteiro.")

    elif opcao == '2':
        sistema.consumir_fila()

    elif opcao == '3':
        sistema.exibir_listas()

    elif opcao == '4':
        sistema.reorganizar_fila()
        
    elif opcao == '0':
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida.")

#----------------------------------------------------------------------------------------------------------------#

'''
*---------------------------------------------------------------*
*                                                               * 
* Qualquer dúvida, por favor, entre em contato:                 *
* Tiagobondezanbazani@gmail.com                                 *
*                                                               * 
*---------------------------------------------------------------*
'''