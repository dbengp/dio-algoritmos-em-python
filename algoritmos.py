# Algoritmo 1: Busca Binária
def busca_binaria(arr, alvo):
    esquerda, direita = 0, len(arr) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if arr[meio] == alvo:
            return meio
        elif arr[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

# Algoritmo 2: Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Algoritmo 3: Fibonacci Recursivo
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Algoritmo 4: Verificação de Números Primos
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Algoritmo 5: Dijkstra (Caminho Mínimo em Grafos)
import heapq

def dijkstra(grafo, inicio):
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[inicio] = 0
    fila = [(0, inicio)]
    
    while fila:
        distancia_atual, vertice_atual = heapq.heappop(fila)
        if distancia_atual > distancias[vertice_atual]:
            continue
        for vizinho, peso in grafo[vertice_atual].items():
            distancia = distancia_atual + peso
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(fila, (distancia, vizinho))
    return distancias

# Função Principal (main)
def main():
    print("=== Demonstração dos Algoritmos ===")

    # 1. Busca Binária
    lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15]
    alvo = 7
    indice = busca_binaria(lista_ordenada, alvo)
    print(f"\n1. Busca Binária: O valor {alvo} está no índice {indice} da lista {lista_ordenada}.")

    # 2. Bubble Sort
    lista_desordenada = [64, 34, 25, 12, 22, 11, 90]
    lista_ordenada = bubble_sort(lista_desordenada.copy())
    print(f"\n2. Bubble Sort: Lista original: {lista_desordenada}. Lista ordenada: {lista_ordenada}.")

    # 3. Fibonacci Recursivo
    n = 10
    fib = fibonacci(n)
    print(f"\n3. Fibonacci Recursivo: O {n}º número de Fibonacci é {fib}.")

    # 4. Verificação de Números Primos
    numero = 29
    if eh_primo(numero):
        print(f"\n4. Verificação de Primos: {numero} é um número primo.")
    else:
        print(f"\n4. Verificação de Primos: {numero} não é um número primo.")

    # 5. Dijkstra (Caminho Mínimo em Grafos)
    grafo = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    inicio = 'A'
    distancias = dijkstra(grafo, inicio)
    print(f"\n5. Dijkstra: Distâncias mínimas a partir de {inicio}: {distancias}.")

# Executar a função main
if __name__ == "__main__":
    main()
