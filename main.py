# main.py

from conexion import conectar_recetas
from funciones import (
    obtener_recetas, 
    insertar_receta, 
    actualizar_dificultad_receta, 
    eliminar_receta
)

if __name__ == "__main__":
    conex = conectar_recetas()

    if conex:
        # --- Demostración de modificación de datos ---
        
        # Ejemplo 1: Insertar una nueva receta
        print("\n--- Insertando una nueva receta ---")
        # El ID 101 se asignará automáticamente si es el siguiente.
        insertar_receta(conex, "Sandwich de queso", "Derrite queso en pan tostado.", 5, "Muy fácil", 1)

        # Ejemplo 2: Actualizar la dificultad de la receta que acabamos de crear (ID 101)
        print("\n--- Actualizando la dificultad de una receta ---")
        actualizar_dificultad_receta(conex, 101, "Fácil")
        
        # Ejemplo 3: Eliminar la receta que acabamos de crear
        print("\n--- Eliminando la receta que acabamos de crear ---")
        eliminar_receta(conex, 101)
        
        # --- Demostración de consultas (SELECT) ---

        lista_recetas = obtener_recetas(conex)
        if lista_recetas:
            print("\nResultados de la tabla 'RECETAS':")
            for receta in lista_recetas:
                print(receta)
        else:
            print("No se encontraron registros de recetas o hubo un error.")
        
        # Cierra la conexión al finalizar
        conex.close()
        print("\nConexión a la base de datos cerrada.")