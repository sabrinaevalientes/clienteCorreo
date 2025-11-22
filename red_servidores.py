from collections import deque

class GrafoServidor:
    def __init__(self):
        # adjacency list: {nombre_servidor: [vecinos]}
        self._ady = {}

    def agregar_servidor(self, nombre: str) -> None:
        self._ady.setdefault(nombre, [])

    def conectar(self, a: str, b: str) -> None:
        self._ady.setdefault(a, [])
        self._ady.setdefault(b, [])
        if b not in self._ady[a]:
            self._ady[a].append(b)
        if a not in self._ady[b]:
            self._ady[b].append(a)

    def bfs(self, inicio: str, objetivo: str):
        # retorna camino más corto (lista de nodos) o None
        if inicio not in self._ady or objetivo not in self._ady:
            return None
        q = deque([inicio])
        padre = {inicio: None}
        while q:
            nodo = q.popleft()
            if nodo == objetivo:
                # reconstruir camino
                camino = []
                cur = nodo
                while cur:
                    camino.append(cur)
                    cur = padre[cur]
                return list(reversed(camino))
            for v in self._ady[nodo]:
                if v not in padre:
                    padre[v] = nodo
                    q.append(v)
        return None

    def dfs(self, inicio: str, objetivo: str):
        visited = set()
        path = []
        def _dfs(n):
            if n == objetivo:
                path.append(n)
                return True
            visited.add(n)
            for v in self._ady.get(n, []):
                if v not in visited:
                    if _dfs(v):
                        path.append(n)
                        return True
            return False
        if inicio not in self._ady or objetivo not in self._ady:
            return None
        if _dfs(inicio):
            return list(reversed(path))
        return None
