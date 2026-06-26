<<<<<<< HEAD
<<<<<<< HEAD
from flask import Flask, jsonify, request

app = Flask(__name__)

productos = [
    {
        "codigo": 201,
        "producto": "Teclado mecánico RGB",
        "precio": 45.00,
        "stock": 12
    },
    {
        "codigo": 202,
        "producto": "Mouse inalámbrico",
        "precio": 18.50,
        "stock": 25
    },
    {
        "codigo": 203,
        "producto": "Monitor LED 24",
        "precio": 165.00,
        "stock": 8
    }
]

@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "Bienvenido a la API de TecnoMarket"
    })

@app.route("/productos", methods=["GET"])
def obtener_productos():
    return jsonify(productos)

@app.route("/productos/<int:codigo>", methods=["GET"])
def obtener_producto(codigo):

    for producto in productos:
        if producto["codigo"] == codigo:
            return jsonify(producto)

    return jsonify({
        "mensaje": "Producto no encontrado"
    }), 404

@app.route("/productos", methods=["POST"])
def agregar_producto():

    datos = request.get_json()

    if not datos:
        return jsonify({
            "mensaje": "Debe enviar un JSON"
        }), 400

    nuevo_codigo = productos[-1]["codigo"] + 1

    nuevo_producto = {
        "codigo": nuevo_codigo,
        "producto": datos["producto"],
        "precio": datos["precio"],
        "stock": datos["stock"]
    }

    productos.append(nuevo_producto)

    return jsonify(nuevo_producto), 201

if __name__ == "__main__":
    app.run(debug=True)
=======
 
>>>>>>> 7540d9649e455e1598c72861dd28663a32f1302e
=======
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Catálogo de datos inicial simulado en memoria
productos = [
    {"codigo": 201, "nombre": "Teclado mecánico RGB", "precio": 45.00, "stock": 12},
    {"codigo": 202, "nombre": "Mouse inalámbrico", "precio": 18.50, "stock": 25},
    {"codigo": 203, "nombre": "Monitor LED 24\"", "precio": 165.00, "stock": 8}
]

# Contador para autogenerar el código de nuevos productos
siguiente_codigo = 204

@app.route('/productos', methods=['GET'])
def obtener_productos():
    """Consulta del catálogo completo"""
    return jsonify(productos), 200

@app.route('/productos/<int:codigo>', methods=['GET'])
def obtener_producto(codigo):
    """Consulta de un producto específico por código"""
    producto = next((p for p in productos if p["codigo"] == codigo), None)
    if producto is None:
        abort(404, description=f"Producto con código {codigo} no encontrado.")
    return jsonify(producto), 200

@app.route('/productos', methods=['POST'])
def registrar_producto():
    """Registro de nuevos productos con código autogenerado"""
    global siguiente_codigo
    
    if not request.json:
        abort(400, description="La petición debe incluir un cuerpo JSON.")
        
    datos = request.json
    
    # Validaciones de los campos requeridos obligatoriamente
    if 'nombre' not in datos or 'precio' not in datos or 'stock' not in datos:
        abort(400, description="Faltan campos obligatorios: nombre, precio y stock.")
        
    nuevo_producto = {
        "codigo": siguiente_codigo,
        "nombre": datos['nombre'],
        "precio": float(datos['precio']),
        "stock": int(datos['stock'])
    }
    
    productos.append(nuevo_producto)
    siguiente_codigo += 1  # Incrementa para el próximo producto
    
    return jsonify(nuevo_producto), 201

# --- DESAFÍOS ADICIONALES (Opcionales para puntos extra) ---

@app.route('/productos/<int:codigo>', methods=['PUT'])
def actualizar_producto(codigo):
    """Actualizar precio o stock de un producto existente"""
    producto = next((p for p in productos if p["codigo"] == codigo), None)
    if producto is None:
        abort(404, description=f"Producto con código {codigo} no encontrado.")
        
    datos = request.json or {}
    if 'precio' in datos:
        producto['precio'] = float(datos['precio'])
    if 'stock' in datos:
        producto['stock'] = int(datos['stock'])
        
    return jsonify(producto), 200

@app.route('/productos/<int:codigo>', methods=['DELETE'])
def eliminar_producto(codigo):
    """Eliminar un producto del catálogo"""
    global productos
    producto = next((p for p in productos if p["codigo"] == codigo), None)
    if producto is None:
        abort(404, description=f"Producto con código {codigo} no encontrado.")
        
    productos = [p for p in productos if p["codigo"] != codigo]
    return jsonify({"mensaje": f"Producto {codigo} eliminado correctamente."}), 200

if __name__ == '__main__':
    # Ejecuta el servidor local en el puerto 5000 con autoreload activado
    app.run(debug=True, port=5000)
>>>>>>> 1f3caf87bb22b65fa8dec45a03f682ece24572d0
