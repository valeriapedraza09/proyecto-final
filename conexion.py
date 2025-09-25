import mysql.connector

def conectar_recetas():
    """
    Establece la conexión a la base de datos recetas_db.
    """
    try:
        # Configuración de la conexión a la base de datos de recetas
        conex = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Reemplaza con tu contraseña
            database="recetas_db",
            port="3306"       # Cambia el puerto si es necesario
        )
        if conex.is_connected():
            print("Conexión exitosa a la base de datos recetas_db.")
            return conex
        else:
            return None
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None