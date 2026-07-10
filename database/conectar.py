import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def connect_db(base: str = "main"):
    if base == "main":
        prefix = "DB"
    elif base == "replica":
        prefix = "DBL"
    elif base == "separada":
        prefix = "DBS"
    else:
        raise ValueError("Base no válida. Usa 'main', 'replica' o 'separada'.")

    host = os.getenv(f"{prefix}_HOST")
    port = os.getenv(f"{prefix}_PORT")
    user = os.getenv(f"{prefix}_USER")
    password = os.getenv(f"{prefix}_PASSWORD")
    database = os.getenv(f"{prefix}_NAME")

    return mysql.connector.connect(
        host=host,
        port=int(port) if port else 3306,
        user=user,
        password=password,
        database=database,
    )

def connect_main():
    return connect_db("main")

def connect_replica():
    return connect_db("replica")

def connect_separada():
    return connect_db("separada")

if __name__ == "__main__":
    conexion = connect_main()
    conexion.close()
    print("Conexión principal exitosa")

