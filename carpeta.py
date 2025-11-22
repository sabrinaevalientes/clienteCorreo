from typing import List
from mensaje import Mensaje

class Carpeta:
    def __init__(self, nombre: str):
        self._nombre = nombre 
        self._mensajes: List[Mensaje] = []
        self._subcarpetas: List['Carpeta'] = []

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def mensajes(self) -> List[Mensaje]:
        return self._mensajes

    @property
    def subcarpetas(self) -> List['Carpeta']:
        return self._subcarpetas

    def agregar_mensaje(self, mensaje: Mensaje) -> None:
        self._mensajes.append(mensaje)

    def listar_mensajes(self) -> List[str]:
        return [str(m) for m in self._mensajes]
    
    def agregar_subcarpeta(self, carpeta: 'Carpeta') -> None:
        self._subcarpetas.append(carpeta)

    def listar_subcarpetas(self, nivel=0) -> None:
        print("  " * nivel + f"- {self._nombre}")
        for sub in self._subcarpetas:
            sub.listar_subcarpetas(nivel + 1)

    def mover_mensaje(self, asunto: str, carpeta_destino: 'Carpeta') -> bool:
        for mensaje in self._mensajes:
            if mensaje.asunto.lower() == asunto.lower():
                carpeta_destino.agregar_mensaje(mensaje)
                self._mensajes.remove(mensaje)
                return True
        for sub in self._subcarpetas:
            if sub.mover_mensaje(asunto, carpeta_destino):
                return True
        return False

    def buscar_mensajes_por_asunto(self, texto: str) -> List[Mensaje]:
        resultados: List[Mensaje] = [m for m in self._mensajes if texto.lower() in m.asunto.lower()]
        for sub in self._subcarpetas:
            resultados.extend(sub.buscar_mensajes_por_asunto(texto))
        return resultados

    def buscar_mensajes_por_remitente(self, email_remitente: str) -> List[Mensaje]:
        resultados: List[Mensaje] = [m for m in self._mensajes if m.emisor.email.lower() == email_remitente.lower()]
        for sub in self._subcarpetas:
            resultados.extend(sub.buscar_mensajes_por_remitente(email_remitente))
        return resultados

    def __str__(self):
        return f"Carpeta -> {self._nombre}, {len(self._mensajes)} mensajes"
