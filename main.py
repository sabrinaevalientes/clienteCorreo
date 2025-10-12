#clases a definir: usuario, mensaje, carpeta, servidorcorreo
from servidor import ServidorCorreo
from usuario import Usuario
from carpeta import Carpeta


# Ejemplo de uso mínimo
if __name__ == "__main__":
    servidor = ServidorCorreo()

    #Creamos usuarios
    u1 = Usuario("luna@mail.com", "Luna")
    u2 = Usuario("pepito@mail.com", "Pepito")
    servidor.agregar_usuario(u1)
    servidor.agregar_usuario(u2)

    #Enviamos mensajes
    servidor.enviar_mensaje(u1, u2, "Holii", "Buenas tardes. Como esta?")
    servidor.enviar_mensaje(u2, u1, "Re: Holaa", "Muy buenas. Todo bien. Gracias por preguntar")

    print("Usuarios registrados:")
    for u in servidor.listar_usuarios():
        print(u)
    
    print("\nMensajes de Pepito en 'Recibidos':")
    for msg in u2.listar_mensajes("Recibidos"):
        print(msg)


    print("\nEstructura de carpetas:")
    c1 = Carpeta("Bandeja de entrada")
    c2 = Carpeta("Trabajo")
    c3 = Carpeta("Clientes")
    c1.agregar_subcarpeta(c2)
    c2.agregar_subcarpeta(c3)
    c1.listar_subcarpetas()


    #Probamos mover un mensaje de una carpeta a otra
    print("\nMoviendo mensaje de Recibidos a Trabajo....")
    carpeta_recibidos = next((c for c in u2.carpetas if c.nombre == "Recibidos"), None)
    carpeta_trabajo = Carpeta("Trabajo")
    u2.agregar_carpeta(carpeta_trabajo)

    if carpeta_recibidos and carpeta_recibidos.mover_mensaje("Holii", carpeta_trabajo):
        print("Mensaje movido correctamente")
    else:
        print("No se encontro el mensaje para moveer")

    print("\nMensajes en 'Trabajo':")
    for msg in carpeta_trabajo.listar_mensajes():
        print(msg)

    print("\nBusqueda recursiva por asunto:")
    resultados_asunto = carpeta_trabajo.buscar_mensajes_por_asunto("Holii")
    for r in resultados_asunto:
        print(r)

    print("\nBusqueda recursiva por remitente:")
    resultados_remitente = carpeta_trabajo.buscar_mensajes_por_remitente("luna@mail.com")
    for r in resultados_remitente:
        print(r)

