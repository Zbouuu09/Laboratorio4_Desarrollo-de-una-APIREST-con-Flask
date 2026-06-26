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