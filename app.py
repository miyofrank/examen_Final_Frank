from flask import Flask, render_template, request, redirect, url_for
from db import get_db_connection
from datetime import datetime

app = Flask(__name__)

# Ruta de inicio - lista de estudiantes
@app.route('/', methods=['GET'])
def index():
    conn = get_db_connection()
    estudiantes = conn.execute('SELECT * FROM alumnos').fetchall()
    conn.close()
    return render_template('index.html', estudiantes=estudiantes)

# Ruta para ver un solo estudiante
@app.route('/estudiantes/<int:id>', methods=['GET'])
def get_one_estudiante(id):
    conn = get_db_connection()
    estudiante = conn.execute('SELECT * FROM alumnos WHERE id = ?', (id,)).fetchone()
    conn.close()
    if estudiante is None:
        return 'Estudiante no encontrado', 404
    return render_template('estudiante.html', estudiante=estudiante)

# Ruta para crear un nuevo estudiante (GET para formulario, POST para insertar)
@app.route('/estudiantes/create', methods=['GET', 'POST'])
def create_one_estudiante():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        aprobado = True if 'aprobado' in request.form else False
        nota = float(request.form['nota'])
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if not nombre or not apellido:
            return 'Nombre y apellido son requeridos', 400

        conn = get_db_connection()
        conn.execute('INSERT INTO alumnos (nombre, apellido, aprobado, nota, fecha) VALUES (?, ?, ?, ?, ?)',
                     (nombre, apellido, aprobado, nota, fecha))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template('create.html')

# Ruta para editar un estudiante
@app.route('/estudiantes/edit/<int:id>', methods=['GET', 'POST'])
def edit_one_estudiante(id):
    conn = get_db_connection()
    estudiante = conn.execute('SELECT * FROM alumnos WHERE id = ?', (id,)).fetchone()

    if estudiante is None:
        return 'Estudiante no encontrado', 404

    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        aprobado = True if 'aprobado' in request.form else False
        nota = float(request.form['nota'])

        if not nombre or not apellido:
            return 'Nombre y apellido son requeridos', 400

        conn.execute('UPDATE alumnos SET nombre = ?, apellido = ?, aprobado = ?, nota = ? WHERE id = ?',
                     (nombre, apellido, aprobado, nota, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('edit.html', estudiante=estudiante)

# Ruta para eliminar un estudiante
@app.route('/estudiantes/delete/<int:id>', methods=['POST'])
def delete_one_estudiante(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM alumnos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
