import sqlite3

def get_db_connection():
    conn = sqlite3.connect('alumnos.db')
    conn.row_factory = sqlite3.Row  # Para que las filas sean accesibles como diccionarios
    return conn
