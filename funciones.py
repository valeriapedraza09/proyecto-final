import mysql.connector

def obtener_recetas(conexion):
    """
    Obtiene las primeras 10 recetas de la base de datos.
    """
    if not conexion:
        return None
    try:
        cursor = conexion.cursor()
        query = "SELECT ID_RECETA, titulo, dificultad FROM RECETAS LIMIT 120"
        cursor.execute(query)
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
    except mysql.connector.Error as err:
        print(f"Error al ejecutar la consulta para obtener recetas: {err}")
        return None

def insertar_receta(conexion, titulo, instrucciones, tiempo, dificultad, id_categoria):
    """
    Inserta una nueva receta en la tabla RECETAS.
    """
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        query = "INSERT INTO RECETAS (titulo, instrucciones, tiempo_preparacion, dificultad, ID_CATEGORIA) VALUES (%s, %s, %s, %s, %s)"
        datos = (titulo, instrucciones, tiempo, dificultad, id_categoria)
        cursor.execute(query, datos)
        
        # Confirmar los cambios
        conexion.commit()
        print(f"Receta '{titulo}' insertada con éxito.")
        cursor.close()
        return True
    except mysql.connector.Error as err:
        print(f"Error al insertar la receta: {err}")
        conexion.rollback()
        return False

def actualizar_dificultad_receta(conexion, id_receta, nueva_dificultad):
    """
    Actualiza la dificultad de una receta.
    """
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        query = "UPDATE RECETAS SET dificultad = %s WHERE ID_RECETA = %s"
        datos = (nueva_dificultad, id_receta)
        cursor.execute(query, datos)
        
        # Confirmar los cambios
        conexion.commit()
        print(f"Dificultad de la receta con ID {id_receta} actualizada a '{nueva_dificultad}'.")
        cursor.close()
        return True
    except mysql.connector.Error as err:
        print(f"Error al actualizar la dificultad: {err}")
        conexion.rollback()
        return False

def eliminar_receta(conexion, id_receta):
    """
    Elimina una receta de la tabla RECETAS.
    """
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        query = "DELETE FROM RECETAS WHERE ID_RECETA = %s"
        cursor.execute(query, (id_receta,))
        
        # Confirmar los cambios
        conexion.commit()
        print(f"Receta con ID {id_receta} eliminada con éxito.")
        cursor.close()
        return True
    except mysql.connector.Error as err:
        print(f"Error al eliminar la receta: {err}")
        conexion.rollback()
        return False