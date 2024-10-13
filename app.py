from flask import Flask, render_template, request, redirect, url_for, flash
from estudiante import get_db_connection
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necesario para mensajes flash (personaliza este valor)

# Ruta de inicio - lista de estudiantes
@app.route('/', methods=['GET'])
def index():
    conn = get_db_connection()
    try:
        estudiantes = conn.execute('SELECT * FROM alumnos').fetchall()
    except Exception as e:
        flash(f'Error al obtener los estudiantes: {e}', 'error')
        estudiantes = []  # Si hay error, al menos devolvemos una lista vacía
    finally:
        conn.close()
    return render_template('index.html', estudiantes=estudiantes)

# Ruta para ver un solo estudiante
@app.route('/estudiantes/<int:id>', methods=['GET'])
def get_one_estudiante(id):
    conn = get_db_connection()
    try:
        estudiante = conn.execute('SELECT * FROM alumnos WHERE id = ?', (id,)).fetchone()
        if estudiante is None:
            flash('Estudiante no encontrado', 'error')
            return redirect(url_for('index'))
    finally:
        conn.close()
    return render_template('estudiante.html', estudiante=estudiante)

# Ruta para crear un nuevo estudiante (GET para formulario, POST para insertar)
@app.route('/estudiantes/create', methods=['GET', 'POST'])
def create_one_estudiante():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        aprobado = True if 'aprobado' in request.form else False
        nota = request.form.get('nota')

        # Validación de entrada
        if not nombre or not apellido:
            flash('Nombre y apellido son requeridos', 'error')
            return render_template('create.html')

        try:
            nota = float(nota)
        except ValueError:
            flash('La nota debe ser un número', 'error')
            return render_template('create.html')

        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO alumnos (nombre, apellido, aprobado, nota, fecha) VALUES (?, ?, ?, ?, ?)',
                         (nombre, apellido, aprobado, nota, fecha))
            conn.commit()
            flash('Estudiante creado exitosamente', 'success')
        except Exception as e:
            flash(f'Error al crear el estudiante: {e}', 'error')
        finally:
            conn.close()

        return redirect(url_for('index'))

    return render_template('create.html')

# Ruta para editar un estudiante
@app.route('/estudiantes/edit/<int:id>', methods=['GET', 'POST'])
def edit_one_estudiante(id):
    conn = get_db_connection()
    estudiante = conn.execute('SELECT * FROM alumnos WHERE id = ?', (id,)).fetchone()

    if estudiante is None:
        flash('Estudiante no encontrado', 'error')
        return redirect(url_for('index'))

    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        aprobado = True if 'aprobado' in request.form else False
        nota = request.form.get('nota')

        # Validación de entrada
        if not nombre or not apellido:
            flash('Nombre y apellido son requeridos', 'error')
            return render_template('edit.html', estudiante=estudiante)

        try:
            nota = float(nota)
        except ValueError:
            flash('La nota debe ser un número', 'error')
            return render_template('edit.html', estudiante=estudiante)

        try:
            conn.execute('UPDATE alumnos SET nombre = ?, apellido = ?, aprobado = ?, nota = ? WHERE id = ?',
                         (nombre, apellido, aprobado, nota, id))
            conn.commit()
            flash('Estudiante actualizado exitosamente', 'success')
        except Exception as e:
            flash(f'Error al actualizar el estudiante: {e}', 'error')
        finally:
            conn.close()

        return redirect(url_for('index'))

    return render_template('edit.html', estudiante=estudiante)

# Ruta para eliminar un estudiante
@app.route('/estudiantes/delete/<int:id>', methods=['POST'])
def delete_one_estudiante(id):
    conn = get_db_connection()
    try:
        conn.execute('DELETE FROM alumnos WHERE id = ?', (id,))
        conn.commit()
        flash('Estudiante eliminado exitosamente', 'success')
    except Exception as e:
        flash(f'Error al eliminar el estudiante: {e}', 'error')
    finally:
        conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
