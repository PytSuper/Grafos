import collections

class Grafo:
    def __init__(self, es_dirigido=False):
        self.grafo = {}
        self.es_dirigido = es_dirigido
    
    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = {}  # Changed from set() to {}
            print(f"Vertice '{vertice}' agregado.")
        else:
            print(f"Vertice '{vertice}' ya existe.")
    
    def agregar_arista(self, u, v, peso=1):
        if u not in self.grafo:
            self.agregar_vertice(u)
        if v not in self.grafo:
            self.agregar_vertice(v)

        # Arista de u a v con peso
        self.grafo[u][v] = peso
        if not self.es_dirigido:
            self.grafo[v][u] = peso

    
    def obtener_vecinos(self, vertice):
        if vertice in self.grafo:
            return list(self.grafo[vertice])  # Convertir a lista para devolver
        return []  # Si el vertice no existe, no tiene vecinos
    
    def existe_arista(self, desde, hasta):
        return hasta in self.grafo.get(desde, [])
    
    def bfs(self, inicio):#Búsqueda en Amplitud
        visitados = set()  # Conjunto para guardar los vertices ya visitados
        cola = collections.deque()  # Cola para los vertices a visitar
        
        # Empezar el recorrido desde el vertice inicial
        cola.append(inicio)
        visitados.add(inicio)
        
        recorrido = []  # Lista para almacenar el orden de visita
        
        while cola:
            vertice_actual = cola.popleft()  # Sacar el primer elemento de la cola
            recorrido.append(vertice_actual)
            print(f"Visitando: {vertice_actual}")
            
            # Añadir a la cola los vecinos no visitados
            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        return recorrido
    
    def dfs(self, inicio):  #Búsqueda en Profundidad
        visitados = set()
        recorrido = []
        
        def __dfs_recursivo(vertice):
            visitados.add(vertice)
            recorrido.append(vertice)
            print(f"Visitando: {vertice}")
            
            for vecino in self.obtener_vecinos(vertice):
                if vecino not in visitados:
                    __dfs_recursivo(vecino)
        
        # Iniciar el DFS desde el vértice dado
        __dfs_recursivo(inicio)
        return recorrido
    
    def imprimir_grafo(self):
        print("\n--- Representación del Grafo ---")
        for vertice, vecinos in self.grafo.items():
            print(f"{vertice}: {',  '.join(vecinos)}")
        print("---")
    
    def imprimir_grafo(self): #imprime vecinos y sus pesos
        print("\n--- Representación del Grafo ---")
        for vert, vecinos in self.grafo.items():
            if vecinos:
                detalles = ", ".join(f"{v}(peso={p})" for v, p in vecinos.items())
            else:
                detalles = "(sin vecinos)"
            print(f"{vert}: {detalles}")
        print("---")

    def es_conexo(self):
        if not self.grafo:
            return True
        
        # Tomar el primer vértice para iniciar el BFS/DFS
        primer_vertice = next(iter(self.grafo))
        
        # Realizar un BFS desde el primer vértice
        recorrido_bfs = self.bfs(primer_vertice)
        return len(recorrido_bfs) == len(self.grafo)
    
    def encontrar_camino(self, inicio, fin):
        if inicio not in self.grafo or fin not in self.grafo:
            print(f"Error: '{inicio}' o '{fin}' no existen en el grafo.")
            return []

        visitados = {inicio}
        padres = {inicio: None}
        cola = collections.deque([inicio])

        while cola:
            actual = cola.popleft()
            if actual == fin:
                # Reconstruir camino desde el final hacia el inicio
                camino = []
                while actual is not None:
                    camino.append(actual)
                    actual = padres[actual]
                return camino[::-1]

            for vecino in self.obtener_vecinos(actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = actual
                    cola.append(vecino)

        return []  # No hay camino

