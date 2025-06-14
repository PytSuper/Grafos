import modulo
if __name__ == "__main__":
    #probamos el grafo
    print("--- GRAFO NO DIRIGIDO ---")
    grafo = modulo.Grafo(es_dirigido=False)

    for v in ['A', 'B', 'C', 'D', 'E']:
        grafo.agregar_vertice(v)
    
    grafo.agregar_arista('A', 'B')
    grafo.agregar_arista('A', 'C')
    grafo.agregar_arista('B', 'D')
    grafo.agregar_arista('C', 'D')
    grafo.agregar_arista('D', 'E')

    grafo.imprimir_grafo()

    print("Vecinos de A:", grafo.obtener_vecinos('A'))
    print("Vecinos de D:", grafo.obtener_vecinos('D'))
    print("Vecinos de F:", grafo.obtener_vecinos('F'))  # no existe

    print("¿Existe arista A-C?", grafo.existe_arista('A', 'C'))
    print("¿Existe arista A-D?", grafo.existe_arista('A', 'D'))

    print("BFS desde A:", grafo.bfs('A'))
    print("DFS desde A:", grafo.dfs('A'))

    grafo.agregar_vertice('F')  # desconectado
    print("¿Es conexo?:", grafo.es_conexo())

    print("Camino de A a E:", grafo.encontrar_camino('A', 'E'))
    print("Camino de A a G (inexistente):", grafo.encontrar_camino('A', 'G'))

    print("\n--- GRAFO DIRIGIDO ---")
    dirigido = modulo.Grafo(es_dirigido=True)
    dirigido.agregar_arista('X', 'Y')
    dirigido.agregar_arista('Y', 'Z')
    dirigido.agregar_arista('X', 'Z')

    dirigido.imprimir_grafo()
    print("Vecinos de X:", dirigido.obtener_vecinos('X'))
    print("Vecinos de Y:", dirigido.obtener_vecinos('Y'))
