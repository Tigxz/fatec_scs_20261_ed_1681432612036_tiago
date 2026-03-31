# Atividade B1-3
# Simulador HP12c - Pilha RPN com Menu
# Disciplina: Estruturas de Dados - Fatec SCS
# Autor: Tiago Bondezan Bazani
# Data: 2026

def inicializar():
    return [0, 0, 0, 0]

def empilhar(pilha, valor):
    pilha[3] = pilha[2]
    pilha[2] = pilha[1]
    pilha[1] = pilha[0]
    pilha[0] = valor
    mostrar_pilha(pilha)
    return pilha

def desempilhar(pilha):
    x = pilha[0]
    pilha[0] = pilha[1]
    pilha[1] = pilha[2]
    pilha[2] = pilha[3]
    pilha[3] = 0
    return pilha, x

def operar(pilha, operador):
    pilha, a = desempilhar(pilha)
    pilha, b = desempilhar(pilha)

    if operador == '+':
        resultado = b + a
    elif operador == '-':
        resultado = b - a
    elif operador == '*':
        resultado = b * a
    elif operador == '/':
        if a == 0:
            print("Erro: divisão por zero não é permitido")
            resultado = 0
        else:
            resultado = b / a
    else:
        print("Erro: operador inválido ->", operador)
        resultado = 0

    pilha = empilhar(pilha, resultado)
    return pilha

def mostrar_pilha(pilha):
    print(f"D: {pilha[3]} | C: {pilha[2]} | B: {pilha[1]} | A: {pilha[0]}")

def avaliar_rpn(pilha, expressao):
    tokens = expressao.split()
    for token in tokens:
        if token.isdigit():
            pilha = empilhar(pilha, float(token))
        else:
            pilha = operar(pilha, token)
    return pilha, pilha[0]


pilha = inicializar()

while True:
    print("\n-=-=-=-=-=-=- MENU CALCULADORA HP12c -=-=-=-=-=-=-")
    print("1 - Zerar pilha")
    print("2 - Empilhar número")
    print("3 - Calcular expressão")
    print("4 - Mostrar pilha")
    print("0 - Sair")
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")


    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        pilha = inicializar()
        print("Pilha zerada!")
    elif opcao == "2":
        valor = float(input("Digite o número: "))
        pilha = empilhar(pilha, valor)
    elif opcao == "3":
        expressao = input("Digite a expressão RPN: ")
        pilha, resultado = avaliar_rpn(pilha, expressao)
        print(f"O resultado da expressão algébrica é: {resultado}")
    elif opcao == "4":
        mostrar_pilha(pilha)
    elif opcao == "0":
        print("Encerrando calculadora...")
        break
    else:
        print("Opção inválida, tente novamente.")


# Em caso de dúvidas, entre em contato:                      
# Tiago Bondezan Bazani - tiagobondezanbazani@gmail.com               