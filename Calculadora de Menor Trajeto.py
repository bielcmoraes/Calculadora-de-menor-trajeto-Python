import networkx as nx
import matplotlib.pyplot as plt

# Função que gera o objeto Graph e constroi sua representação visual
def GerarGrafo(grafoDic):
    # Cria um objeto grafo
    grafo = nx.Graph()

    # Cria as Edges no objeto grafo com base no grafo-dicionario passado como parâmetro
    for key in grafoDic:
        for i in grafoDic[key]:
            grafo.add_edge(key, i[0], weight=i[1])

    # Desenha o grafo
    nx.draw(grafo, with_labels=True,  node_size=5000)
    plt.show()


# Função que adiciona nós ao grafo principal
def AdicionarNodle(cidade1, cidade2, distancia, graph):
    # Verifica se a chave já existe e caso não exista cria uma lista interna
    if cidade1 not in graph:
        graph[cidade1] = []
    # Adiciona a dupla cidade distancia 
    graph[cidade1].append([cidade2, distancia])
    # Retorna o gafo alterado
    return graph


# Função que gera a sequencia do menor caminho entre A e B
def MenorCaminho(graph, start, end):
    # Cria um objeto grafo
    grafo = nx.Graph()
    grafoAux = nx.Graph()

    # Cria as Edges no objeto grafo com base no grafo-dicionario passado como parâmetro
    for key in graph:
        for i in graph[key]:
            grafo.add_edge(key, i[0], weight=i[1])

    # Chama a função de menor caminho de Dijkstra
    menorPath = nx.dijkstra_path(grafo, start, end)

    for i in range(len(menorPath) - 1):
        grafoAux.add_edge(menorPath[i], menorPath[i+1])

    nx.draw(grafoAux, with_labels=True,  node_size=5000)
    plt.show()


# View da função de cadastrar mais cidades     
def solicitarDadosCadastroCidades():
    sairMenu = False
    while not sairMenu:
        try:
            print("\n---------------ADICIONAR CIDADES--------------\n")
            cidade1 = input("Nome da 1º cidade: ").strip()
            cidade2 = input("Nome da 2º cidade: ").strip()
            if len(cidade1) > 0 and len(cidade2) > 0:
                distancia = float(input(f"Distância entre '{cidade1}' e '{cidade2}': "))
            else:
                print("Nome(s) da(s) cidade(s) não pode(m) ser vazio(s)!")
                continue
        except ValueError:
            print("\nInformação inválida. Tente novamente!")
        else:
            return cidade1, cidade2, distancia


# View da função de distância mínima
def solicitarDadosDistanciaMinima():
    sairMenu = False
    while not sairMenu:
        try:
            print("\n-------CALCULAR DISTÂNCIA ENTRE CIDADES-------\n")
            cidade1 = input("Nome da 1º cidade: ").strip()
            cidade2 = input("Nome da 2º cidade: ").strip()
            if len(cidade1) <= 0 and len(cidade2) <= 0:
                print("\nNome(s) da(s) cidade(s) não pode(m) ser vazio(s)!")
                continue
        except ValueError:
            print("\nInformação inválida. Tente novamente!")
        else:
            return cidade1, cidade2

# ------------------------------------------------Fim da secção de funções-------------------------------------------------------#

# Grafo principal
# graph = {"Ichu":[["Serrinha", 33],["Coité", 40],["Tanquinho", 40]], "Serrinha":[["Coité", 30], ["Ichu", 30], ["Trevo", 50]], "Tanquinho":[["Trevo", 20]], "Trevo":[["Feira", 30]]}
graph = {"Ichu":[["Serrinha", 28],["Coité", 40],["Tanquinho", 30]], "Serrinha":[["Coité", 30], ["Ichu", 28], ["Trevo", 46]], "Tanquinho":[["Trevo", 18]], "Trevo":[["Feira", 25]]}
# graph = {}

# Menu principal
sairMenu = False
while not sairMenu:
    try:
        print("\n-----------------MENU INICIAL-----------------\n")
        print("[1] -> Cadastrar cidades")
        print("[2] -> Calcular menor distância entre cidades")
        print("[3] -> Gerar Grafo")
        print("[4] -> Sair")
        opcao = int(input("\nOpção desejada: "))

    except ValueError:
        print("Opção inválida. Tente novamente!")
    else:
        if opcao == 1:
            cidade1, cidade2, distancia = solicitarDadosCadastroCidades()
            AdicionarNodle(cidade1, cidade2, distancia, graph)
            print("\nInformação adicionada!")

        elif opcao == 2:
            inicial, final = solicitarDadosDistanciaMinima()
            MenorCaminho(graph, inicial, final)

        elif opcao == 3:
            GerarGrafo(graph)

        elif opcao == 4:
            sairMenu = True
            print("Saindo!")
            quit()