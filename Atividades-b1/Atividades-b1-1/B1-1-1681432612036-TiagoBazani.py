"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
"                  FATEC São Caetano do Sul                 "
"                       Atividade B1-1                      "
"                   Tiago Bondezan Bazani                   "
"                Objetivo: Catalogo de Filmes               "
"                          24.02.2026                       "
"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="

catalogo = {}
def adicionar_filme(id_filme, titulo, diretor):
    if id_filme in catalogo:
        print("ID já existe!")
    else:
        catalogo[id_filme] = {"titulo": titulo, "diretor": diretor}

def buscar_filme(id_filme):
    return catalogo.get(id_filme, "Filme não encontrado")

def remover_filme(id_filme):
    catalogo.pop(id_filme, None)
    print ("Filme removido!")

def listar_todos():
    if not catalogo:
        print("\nO catálogo está vazio.")
    else:
        print("\nCatálogo de Filmes:")
        for id_f, dados in catalogo.items():
            print(f"ID: {id_f} | Título: {dados['titulo']} | Diretor: {dados['diretor']}")

adicionar_filme("1", "Parasita", "Bong Joon-ho")
adicionar_filme("2", "Clube da Luta", "David Fincher")
adicionar_filme("3", "Forrest Gump", "Robert Zemeckis")
adicionar_filme("4", "Interestelar", "Christopher Nolan")
adicionar_filme("5", "Cidade de Deus", "Fernando Meirelles")



"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
"Em caso de dúvidas, entre em contato:                      "
"Tiago Bazani - tiagobondezanbazani@gmail.com               "
"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="