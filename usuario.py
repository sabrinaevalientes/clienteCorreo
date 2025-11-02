from typing import List
from carpeta import Carpeta
from collections import deque
from mensaje import Mensaje

class Usuario:
    def __init__(self, email: str, nombre_usuario: str):
        self._email = email
        self._nombre_usuario = nombre_usuario
        self._carpetas: List[Carpeta] = []
        self._filtros: dict[str, str] = {}
        self._cola_urgentes = deque()
    
    @property
    def email(self) -> str:
        return self._email
    
    @property
    def nombre_usuario(self) -> str:
        return self._nombre_usuario
    
    @property
    def carpetas(self) -> List['Carpeta']:
        return self._carpetas
    
    def agregar_carpeta(self, carpeta: 'Carpeta') -> None:
        self._carpetas.append(carpeta)

    def agregar_filtro(self, palabra_clave: str, nombre_carpeta: str) -> None:
        #Agrega un filtro automático: si el asunto contiene la palabra clave,
        #el mensaje se guarda directamente en la carpeta indicada.
        self._filtros[palabra_clave.lower()] = nombre_carpeta
        print(f"Filtro agregado: '{palabra_clave}' -> '{nombre_carpeta}'")

    def recibir_mensaje(self, mensaje: Mensaje, urgente: bool = False) -> None:
        #Recibe un mensaje.
        #Si es urgente, se guarda en la cola de prioridades.
        #Si no, aplica los filtros automaticos definidos por el usuarioo

        if urgente:
            self._cola_urgentes.appendleft(mensaje)  # Los urgentes se atienden primero
            print(f"Advertencia! Mensaje urgente agregado a la cola: {mensaje.asunto}")
            return

        # Verificar si el mensaje cumple con algún filtro automático
        carpeta_destino = None
        for palabra, carpeta_nombre in self._filtros.items():
            if palabra in mensaje.asunto.lower():
                carpeta_destino = next(
                    (c for c in self._carpetas if c.nombre == carpeta_nombre), None)
                if not carpeta_destino:
                    carpeta_destino = Carpeta(carpeta_nombre)
                    self.agregar_carpeta(carpeta_destino)
                break  # Si coincide con un filtro, se detiene la busqueda

        # Si no se encontro un filtro que aplique, va a "Recibidos"
        if not carpeta_destino:
            carpeta_destino = next(
                (c for c in self._carpetas if c.nombre == "Recibidos"), None)
            if not carpeta_destino:
                carpeta_destino = Carpeta("Recibidos")
                self.agregar_carpeta(carpeta_destino)

        carpeta_destino.agregar_mensaje(mensaje)
    
    def listar_mensajes(self, nombre_carpeta: str):
        #Lista todos los mensajes de una carpeta por nombre
        carpeta = next((c for c in self._carpetas if c.nombre == nombre_carpeta), None)
        if carpeta:
            return carpeta.listar_mensajes()
        return[]
    
    #--urgentes--
    
    def atender_urgente(self):

        # Atiende el mensaje más urgente (el primero en la cola).
        # Lo elimina de la cola al atenderlo.

        if self._cola_urgentes:
            mensaje = self._cola_urgentes.popleft()
            print(f"Atendiendo mensaje urgente: {mensaje.asunto}")
            return mensaje
        else:
            print("No hay mensajes urgentes pendientes.")
            return None

    def listar_urgentes(self):
        #Muestra los mensajes actualmente en la cola de urgentes.
        if not self._cola_urgentes:
            print("No hay mensajes urgentes.")
        else:
            print("Mensajes urgentes en cola:")
            for m in list(self._cola_urgentes):
                print(f" ! {m.asunto}")

    def __str__(self):
        return f"Usuario - {self._nombre_usuario}, {self._email}"
