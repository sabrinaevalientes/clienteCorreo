from servidor import ServidorCorreo
from usuario import Usuario
from carpeta import Carpeta
from red_servidores import GrafoServidor

def pausar():
    input("\nPresione ENTER para continuar...")

def mostrar_menu():
    print("\n=== Cliente de Correo - CLI ===")
    print("1. Crear usuario")
    print("2. Listar usuarios")
    print("3. Enviar mensaje")
    print("4. Ver carpetas de un usuario")
    print("5. Ver mensajes de una carpeta")
    print("6. Crear carpeta para un usuario")
    print("7. Mover mensaje entre carpetas")
    print("8. Agregar filtro automático")
    print("9. Ver urgentes de un usuario")
    print("10. Atender urgente")
    print("11. Gestionar red de servidores (Grafo)")
    print("0. Salir")
    return input("Seleccione una opción: ")

# --- Submenú de grafos ---
def menu_grafos(grafo: GrafoServidor):
    while True:
        print("\n--- Redes de Servidores (Grafo) ---")
        print("1. Agregar servidor")
        print("2. Conectar servidores")
        print("3. Mostrar ruta (BFS)")
        print("4. Mostrar ruta (DFS)")
        print("0. Volver")
        op = input("Opción: ")

        if op == "1":
            nombre = input("Nombre del servidor: ")
            grafo.agregar_servidor(nombre)
            print("Servidor agregado.")
        elif op == "2":
            a = input("Servidor A: ")
            b = input("Servidor B: ")
            grafo.conectar(a, b)
            print("Servidores conectados.")
        elif op == "3":
            inicio = input("Inicio: ")
            fin = input("Destino: ")
            camino = grafo.bfs(inicio, fin)
            print("Ruta BFS:", camino if camino else "No hay camino.")
        elif op == "4":
            inicio = input("Inicio: ")
            fin = input("Destino: ")
            camino = grafo.dfs(inicio, fin)
            print("Ruta DFS:", camino if camino else "No hay camino.")
        elif op == "0":
            return
        else:
            print("Opción inválida.")

        pausar()


# --- CLI principal ---
def main():
    servidor = ServidorCorreo()
    grafo = GrafoServidor()

    print("Bienvenido al Cliente de Correo CLI\n")

    while True:
        op = mostrar_menu()

        # --- Crear usuario ---
        if op == "1":
            email = input("Email: ")
            nombre = input("Nombre: ")
            usuario = Usuario(email, nombre)
            servidor.agregar_usuario(usuario)
            print("Usuario creado correctamente.")
            pausar()

        # --- Listar usuarios ---
        elif op == "2":
            print("\nUsuarios registrados:")
            for u in servidor.listar_usuarios():
                print(" -", u)
            pausar()

        # --- Enviar mensaje ---
        elif op == "3":
            em = input("Email del emisor: ")
            re = input("Email del receptor: ")
            asunto = input("Asunto: ")
            cuerpo = input("Cuerpo: ")
            urg = input("¿Urgente? (s/n): ").lower() == "s"

            emisor = next((u for u in servidor.usuarios if u.email == em), None)
            receptor = next((u for u in servidor.usuarios if u.email == re), None)

            if not emisor or not receptor:
                print("Alguno de los usuarios no existe.")
            else:
                servidor.enviar_mensaje(emisor, receptor, asunto, cuerpo, urgente=urg)
                print("Mensaje enviado con éxito.")

            pausar()

        # --- Ver carpetas ---
        elif op == "4":
            email = input("Email del usuario: ")
            usuario = next((u for u in servidor.usuarios if u.email == email), None)

            if not usuario:
                print("Usuario no encontrado.")
            else:
                print("\nCarpetas de", usuario.nombre_usuario)
                for c in usuario.carpetas:
                    print(" -", c.nombre)

            pausar()

        # --- Ver mensajes de una carpeta ---
        elif op == "5":
            email = input("Email del usuario: ")
            carpeta = input("Nombre carpeta: ")

            usuario = next((u for u in servidor.usuarios if u.email == email), None)
            if not usuario:
                print("Usuario no encontrado.")
            else:
                mensajes = usuario.listar_mensajes(carpeta)
                if not mensajes:
                    print("No hay mensajes.")
                else:
                    print("\n--- Mensajes ---")
                    for m in mensajes:
                        print(m)

            pausar()

        # --- Crear carpeta ---
        elif op == "6":
            email = input("Email usuario: ")
            usuario = next((u for u in servidor.usuarios if u.email == email), None)
            if not usuario:
                print("Usuario no encontrado.")
            else:
                nombre = input("Nombre de la nueva carpeta: ")
                usuario.agregar_carpeta(Carpeta(nombre))
                print("Carpeta creada.")

            pausar()

        # --- Mover mensaje ---
        elif op == "7":
            email = input("Email usuario: ")
            usuario = next((u for u in servidor.usuarios if u.email == email), None)

            if not usuario:
                print("Usuario no encontrado.")
            else:
                asunto = input("Asunto del mensaje a mover: ")
                origen = input("Carpeta origen: ")
                destino = input("Carpeta destino: ")

                carpeta_origen = next((c for c in usuario.carpetas if c.nombre == origen), None)
                carpeta_destino = next((c for c in usuario.carpetas if c.nombre == destino), None)

                if not carpeta_origen or not carpeta_destino:
                    print("Alguna carpeta no existe.")
                else:
                    if carpeta_origen.mover_mensaje(asunto, carpeta_destino):
                        print("Mensaje movido con éxito.")
                    else:
                        print("No se encontró el mensaje.")

            pausar()

        # --- Filtros automáticos ---
        elif op == "8":
            email = input("Email usuario: ")
            usuario = next((u for u in servidor.usuarios if u.email == email), None)

            if not usuario:
                print("Usuario no encontrado.")
            else:
                palabra = input("Palabra clave: ")
                destino = input("Carpeta destino: ")
                usuario.agregar_filtro(palabra, destino)
                print("Filtro agregado.")

            pausar()

        # --- Ver urgentes ---
        elif op == "9":
            email = input("Email usuario: ")
            usuario = next((u for u in servidor.usuarios if u.email == email), None)

            if not usuario:
                print("Usuario no encontrado.")
            else:
                usuario.listar_urgentes()

            pausar()

        # --- Atender urgente ---
        elif op == "10":
            email = input("Email usuario: ")
            usuario = next((u for u in servidor.usuarios if u.email == email), None)

            if not usuario:
                print("Usuario no encontrado.")
            else:
                usuario.atender_urgente()

            pausar()

        # --- Grafos ---
        elif op == "11":
            menu_grafos(grafo)

        # --- Salir ---
        elif op == "0":
            print("Saliendo del sistema... ¡Hasta luego!")
            break

        else:
            print("Opción inválida.")
            pausar()


if __name__ == "__main__":
    main()
