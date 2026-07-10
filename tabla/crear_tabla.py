from database.conectar import connect_main

def crear_main():
    conexion = connect_main()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS activos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                placa VARCHAR(50) NOT NULL,
                numero_serie VARCHAR(100),
                activo VARCHAR(45),
                ip VARCHAR(45),
                sede VARCHAR(100),
                area VARCHAR(100)
            )
            """
        )
        conexion.commit()
        print("Tabla 'activos' creada correctamente en la base main")
    except Exception as e:
        conexion.rollback()
        print(f"Error al crear la tabla: {e}")
    finally:
        cursor.close()
        conexion.close()

if __name__ == "__main__":
    crear_main()

# Solo genera la main.
