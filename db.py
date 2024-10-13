import sqlite3

def get_db_connection():
    conn = sqlite3.connect('alumnos.db')
    conn.row_factory = sqlite3.Row  # Para acceder a los datos como diccionarios
    return conn
