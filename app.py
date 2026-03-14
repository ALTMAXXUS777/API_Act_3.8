from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configuración de SQLite local
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de la Base de Datos
class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255), nullable=True)
    estado = db.Column(db.String(50), default='Pendiente') # Ejemplo: Pendiente, En proceso, Completada

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'estado': self.estado
        }

# Crear tablas automáticamente al inicio
with app.app_context():
    db.create_all()

# ==========================================================
# RUTAS DE LA API (CRUD)
# ==========================================================

# 0. Ruta de Bienvenida (GET /)
@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'mensaje': '¡Bienvenido a la API de Tareas!',
        'instrucciones': 'Accede a /tareas para ver todas las tareas o utiliza POST, PUT y DELETE para interactuar con ellas.'
    }), 200

# 1. Crear Tarea (POST /tareas)
@app.route('/tareas', methods=['POST'])
def crear_tarea():
    data = request.get_json()
    
    # Validar que al menos venga el título
    if not data or not data.get('titulo'):
        return jsonify({'error': 'El campo "titulo" es obligatorio'}), 400
    
    nueva_tarea = Tarea(
        titulo=data.get('titulo'),
        descripcion=data.get('descripcion', ''),
        estado=data.get('estado', 'Pendiente')
    )
    
    db.session.add(nueva_tarea)
    db.session.commit()
    
    return jsonify(nueva_tarea.to_dict()), 201

# 2. Consultar todas las Tareas (GET /tareas)
@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    tareas = Tarea.query.all()
    lista_tareas = [tarea.to_dict() for tarea in tareas]
    return jsonify(lista_tareas), 200

# 3. Actualizar una Tarea (PUT /tareas/<id>)
@app.route('/tareas/<int:id>', methods=['PUT'])
def actualizar_tarea(id):
    tarea = Tarea.query.get(id)
    if not tarea:
        return jsonify({'error': 'Tarea no encontrada'}), 404
        
    data = request.get_json()
    
    if 'titulo' in data:
        tarea.titulo = data['titulo']
    if 'descripcion' in data:
        tarea.descripcion = data['descripcion']
    if 'estado' in data:
        tarea.estado = data['estado']
        
    db.session.commit()
    return jsonify(tarea.to_dict()), 200

# 4. Eliminar una Tarea (DELETE /tareas/<id>)
@app.route('/tareas/<int:id>', methods=['DELETE'])
def eliminar_tarea(id):
    tarea = Tarea.query.get(id)
    if not tarea:
        return jsonify({'error': 'Tarea no encontrada'}), 404
        
    db.session.delete(tarea)
    db.session.commit()
    return jsonify({'mensaje': 'Tarea eliminada exitosamente'}), 200

if __name__ == '__main__':
    # Ejecuta el servidor en modo desarrollo
    app.run(debug=True, port=5000)
