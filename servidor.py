from typing import List
from usuario import Usuario
from mensaje import Mensaje

class ServidorCorreo: 
    def __init__(self):
        self._usuarios: List[Usuario] = []

    @property
    def usuarios(self) -> List[Usuario]:
        return self._usuarios

    def agregar_usuario(self, usuario: Usuario) -> None:
        self._usuarios.append(usuario)

    def enviar_mensaje(self, emisor: Usuario, receptor: Usuario, asunto: str, cuerpo: str) -> None:
        mensaje = Mensaje(emisor, receptor, asunto, cuerpo)
        receptor.recibir_mensaje(mensaje)

    def listar_usuarios(self) -> List[str]:
        return [str(u) for u in self._usuarios]