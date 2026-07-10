# Probar si la base si se conecta.

import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def test():
    try:
        conexion = mysql.connector.connect(
            host = os.getenv("DBS_HOST"),
            port=int(os.getenv("DBS_PORT")),
            user=os.getenv("DBS_USER"),
            password=os.getenv("DBS_PASSWORD"),
            database=os.getenv("DBS_NAME")
        )
        print("Conexion exitosa!")
        conexion.close()
    except Exception as e:
        print(f"Error al conectar: {e}")

if __name__ == "__main__":
    test()
