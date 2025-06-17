import json
# Archivo donde se guardarán los datos
archivo_usuarios = 'usuarios.json'
def mostrar_menu():
    print("\n=== MENÚ CRUD DE USUARIOS ===")
    print("1. Crear usuario")
    print("2. Leer usuarios")
    print("3. Actualizar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")
def cargar_usuarios():
    try:
        with open(archivo_usuarios, 'r') as archivo:
            datos = json.load(archivo)
            if isinstance(datos, list):
                return datos
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
def guardar_usuarios(usuarios):
    with open(archivo_usuarios, 'w') as archivo:
        json.dump(usuarios, archivo, indent=4)
def iniciar_programa():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ").strip()  # Usar strip para limpiar espacios
        if opcion == '1':
            crear_usuario()
        elif opcion == '2':
            leer_usuarios()
        elif opcion == '3':
            actualizar_usuario()
        elif opcion == '4':
            eliminar_usuario()
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
# Opción 1: Crear usuario
def crear_usuario():
    usuarios = cargar_usuarios()
    nombre = input("Ingrese el nombre del usuario: ").strip()
    edad = input("Ingrese la edad del usuario: ").strip()
    if not nombre or not edad:
        print("Error: El nombre y la edad no pueden estar vacíos.")
        return
    for usuario in usuarios:
        if usuario['nombre'].lower() == nombre.lower():
            print("Error: El usuario ya existe.")
            return
    nuevo_usuario = {
        "nombre": nombre,
        "edad": edad
    }
    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)
    print(f"Usuario {nombre} creado exitosamente.")
# Opción 2: Leer usuarios
def leer_usuarios():
    usuarios = cargar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    print("\n=== Lista de Usuarios ===")
    for idx, usuario in enumerate(usuarios, start=1):
        print(f"{idx}. Nombre: {usuario['nombre']}, Edad: {usuario['edad']}")
# Opción 3: Actualizar usuario
def actualizar_usuario():
    usuarios = cargar_usuarios()
    if not usuarios:
        print("No hay usuarios para actualizar.")
        return
    print("\n=== Lista de Usuarios ===")
    for idx, usuario in enumerate(usuarios, start=1):
        print(f"{idx}. Nombre: {usuario['nombre']}, Edad: {usuario['edad']}")
    try:
        seleccion = int(input("Ingresa el número del usuario que quieres actualizar: "))
        if 1 <= seleccion <= len(usuarios):
            nuevo_nombre = input("Ingresa el nuevo nombre: ").strip()
            nueva_edad = input("Ingresa la nueva edad: ").strip()
            if not nuevo_nombre or not nueva_edad:
                print("Error: Los campos no pueden estar vacíos.")
                return
            usuarios[seleccion - 1]['nombre'] = nuevo_nombre
            usuarios[seleccion - 1]['edad'] = nueva_edad
            guardar_usuarios(usuarios)
            print("Usuario actualizado correctamente.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Error: Debes ingresar un número válido.")
# Opción 4: Eliminar usuario
def eliminar_usuario():
    usuarios = cargar_usuarios()
    if not usuarios:
        print("No hay usuarios para eliminar.")
        return
    print("\n=== Lista de Usuarios ===")
    for idx, usuario in enumerate(usuarios, start=1):
        print(f"{idx}. Nombre: {usuario['nombre']}, Edad: {usuario['edad']}")
    try:
        seleccion = int(input("Ingresa el número del usuario que quieres eliminar: "))
        if 1 <= seleccion <= len(usuarios):
            usuarios.pop(seleccion - 1)  # Eliminar el usuario
            guardar_usuarios(usuarios)
            print("Usuario eliminado correctamente.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Error: Debes ingresar un número válido.")
# Iniciamos el programa
iniciar_programa()
