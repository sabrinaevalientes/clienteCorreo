from typing import List
from carpeta import Carpeta

class Usuario:
    def __init__(self, email: str, nombre_usuario: str):
        self._email = email
        self._nombre_usuario = nombre_usuario
        self._carpetas: List[Carpeta] = []
    
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

    def recibir_mensaje(self, mensaje):
        carpeta_recibidos = next((c for c in self._carpetas if c.nombre == "Recibidos"), None)
        if not carpeta_recibidos:
            carpeta_recibidos = Carpeta("Recibidos")
            self.agregar_carpeta(carpeta_recibidos)
        carpeta_recibidos.agregar_mensaje(mensaje)
    
    def listar_mensajes(self, nombre_carpeta: str):
        carpeta = next((c for c in self._carpetas if c.nombre == nombre_carpeta), None)
        if carpeta:
            return carpeta.listar_mensajes()
        return[]

    def __str__(self):
        return f"Usuario - {self._nombre_usuario}, {self._email}"
