#clases a definir: usuario, mensaje, carpeta, servidorcorreo
from typing import List, Optional

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

    def __str__(self):
        return f"Usuario - {self._nombre_usuario}, {self._email}"

class Mensaje:
    def __init__(self, emisor: Usuario, receptor: Usuario, asunto: str, cuerpo: str):
        self._emisor = emisor 
        self._receptor = receptor 
        self._asunto = asunto 
        self._cuerpo = cuerpo 

    @property
    def emisor(self) -> Usuario:
        return self._emisor

    @property
    def receptor(self) -> Usuario:
        return self._receptor

    @property
    def asunto(self) -> str:
        return self._asunto
    
    @property
    def cuerpo(self) -> str:
        return self._cuerpo

    def __str__(self):
        return f"De: {self._emisor.email} | Para: {self._receptor.email} | Asunto: {self._asunto} | Cuerpo: {self._cuerpo}"

class Carpeta:
    def __init__(self, nombre: str):
        self._nombre = nombre 
        self._mensajes: List[Mensaje] = []

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def mensajes(self) -> List[Mensaje]:
        return self._mensajes

    def agregar_mensaje(self, mensaje: Mensaje) -> None:
        self._mensajes.append(mensaje)

    def listar_mensajes(self) -> List[str]:
        return [str(m) for m in self._mensajes]

    def __str__(self):
        return f"Carpeta -> {self._nombre}, {len(self._mensajes)} mensajes)"

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
        # Recientes del receptor
        recientes = next((c for c in receptor.carpetas if c.nombre == "Recientes"), None)
        if recientes:
            recientes.agregar_mensaje(mensaje)
        else:
            nueva = Carpeta("Recientes")
            nueva.agregar_mensaje(mensaje)
            receptor.agregar_carpeta(nueva)

    def listar_usuarios(self) -> List[str]:
        return [str(u) for u in self._usuarios]
    

# Ejemplo de uso mínimo
if __name__ == "__main__":
    servidor = ServidorCorreo()

    u1 = Usuario("luna@mail.com", "Luna")
    u2 = Usuario("pepito@mail.com", "Pepito")
    servidor.agregar_usuario(u1)
    servidor.agregar_usuario(u2)

    servidor.enviar_mensaje(u1, u2, "Holii", "Buenas tardes. Como esta?")
    servidor.enviar_mensaje(u2, u1, "Re: Holaa", "Muy buenas. Todo bien. Gracias por preguntar")

    print("Usuarios:", servidor.listar_usuarios())
    for c in u2.carpetas:
        print("Carpeta:", c)
        print(c.listar_mensajes())