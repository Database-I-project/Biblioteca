import mysql.connector as mysql
import os

def clear():
    os.system('cls' if os.name== 'nt' else 'clear')

def insert_user(nombre,apellido,dni,telefono,email):
    try:
        con=mysql.connect(
        host="localhost",
        port=3306,
        user="root",
        database="biblioteca")

        if con.is_connected():
            cur=con.cursor()
            query="""INSERT INTO USUARIOS(nombre,apellido,dni,telefono,email) VALUES (%s,%s,%s,%s,%s)"""
            values=(nombre,apellido,dni,telefono,email)
            cur.execute(query,values)
            con.commit()
            print("Datos cargados correctamente.")
    except Exception as e:
        print(f"Error al insertar datos: {e}")

    finally:
        if con.is_connected():
            cur.close()
            con.close()

def insert_book(titulo,autor,genero,año_publicacion):
    try:
        con=mysql.connect(
        host="localhost",
        port=3306,
        user="root",
        database="biblioteca")

        if con.is_connected():
            cur=con.cursor()
            query="""INSERT INTO INVENTARIO(titulo,autor,genero_id,año_publicacion) VALUES (%s,%s,%s,%s)"""
            values=(titulo,autor,genero,año_publicacion)
            cur.execute(query,values)
            con.commit()
            print("Datos cargados correctamente.")
    except Exception as e:
        print(f"Error al insertar datos: {e}")

    finally:
        if con.is_connected():
            cur.close()
            con.close()

def insert_genre(genero,descripcion):
    try:
        con=mysql.connect(
        host="localhost",
        port=3306,
        user="root",
        database="biblioteca")

        if con.is_connected():
            cur=con.cursor()
            query="""INSERT INTO GENEROS(genero,descripcion) VALUES (%s,%s)"""
            values=(genero,descripcion)
            cur.execute(query,values)
            con.commit()
            print("Datos cargados correctamente.")
    except Exception as e:
        print(f"Error al insertar datos: {e}")

    finally:
        if con.is_connected():
            cur.close()
            con.close()

def insert_loan(libro,usuario):
    try:
        con=mysql.connect(
        host="localhost",
        port=3306,
        user="root",
        database="biblioteca")

        if con.is_connected():
            cur=con.cursor()
            query="""INSERT INTO PRESTAMOS(libro_id,usuario_id) VALUES (%s,%s)"""
            values=(libro,usuario)
            cur.execute(query,values)
            con.commit()
            print("Datos cargados correctamente.")
    except Exception as e:
        print(f"Error al insertar datos: {e}")

    finally:
        if con.is_connected():
            cur.close()
            con.close()
            
def main_menu():
    clear()
    print("====== MENÚ ======")
    print("1. Agregar")
    print("2. Actualizar")
    print("3. Estado")
    print("4. Salir")
    print("===============================")

def menu_agregar():
    clear()
    print("====== AGREGAR ======")
    print("1. Agregar Usuario")
    print("2. Agregar Libro")
    print("3. Agregar Género")
    print("4. Agregar Préstamo")
    print("5. Volver")
    print("===============================")
    opcion = input("Seleccione una opción: ")

    if opcion=='1':
        while True:
            nombre=input("Ingrese el nombre del usuario: ")
            apellido=input("Ingrese el apellido del usuario: ")
            dni=input("Ingrese el dni del usuario: ")
            telefono=input("Ingrese el telefono del usuario: ")
            email=input("Ingrese el email del usuario: ")
            if dni is "" or apellido is "" or  nombre is "":
                print("Datos inválidos, por favor ingrese de nuevo.")
            else:
                insert_user(nombre,apellido,dni,telefono,email)
                break
    elif opcion == '2':
        while True: 
            titulo=input("Ingrese el titulo del libro: ")
            autor=input("Ingrese el autor del libro: ")
            genero=input("Ingrese el id del genero: (1)Drama (2)Terror (3)Ciencia-Ficcion (4)Fantasia (5)Romance (6)Misterio (7)Aventura (8)Historico: ")
            año_publicacion=input("Ingrese el año de publicacion: ")
            if titulo is "" or autor is "" or genero is "":
                print("Datos invalidos, por favor ingrese de nuevo.")
            else:
                insert_book(titulo,autor,genero,año_publicacion)
                break
    elif opcion == '3':
        while True:
            genero=input("Ingrese el genero: ")
            descripcion=("Ingrese una descripcion: ")
            if genero is "" :
                print("Datos invalidos, por favor ingrese de nuevo")
            else:
                insert_genre(genero, descripcion)
                break
    elif opcion == '4':
        while True:
            libro=input("Ingrese el ID del libro: ")
            usuario=("Ingrese el ID de usuario: ")
            if libro is "" or usuario is "":
                print("Datos invalidos, por favor ingrese de nuevo")
            else:
                insert_loan(libro,usuario)
                break
    elif opcion == '5':
        return
    
def main():
    while True:
        main_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_agregar()
            break
        elif opcion == '2':
            clear()
            print("====== ACTUALIZAR ======")
            print("1. Actualizar Usuario")
            print("2. Actualizar Libro")
            print("3. Actualizar Género")
            print("4. Actualizar Préstamo")
            print("5. Volver")
            print("===============================")
        elif opcion == '3':
            clear()
            print("====== ESTADO ======")
            print("1. Estado Usuario")
            print("2. Estado Libro")
            print("3. Volver")
            print("===============================")
        elif opcion == '4':
            input("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

main()
    
