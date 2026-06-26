import requests

BASE_URL = "http://127.0.0.1:5000/productos"

def probar_api():
    print("=== 1. OBTENER TODO EL CATÁLOGO ===")
    response = requests.get(BASE_URL)
    print(f"Status Code: {response.status_code}")
    print(response.json())
    print("-" * 50)

    print("\n=== 2. OBTENER UN PRODUCTO EXISTENTE (Código 202) ===")
    response = requests.get(f"{BASE_URL}/202")
    print(f"Status Code: {response.status_code}")
    print(response.json())
    print("-" * 50)

    print("\n=== 3. OBTENER UN PRODUCTO INEXISTENTE (Código 999) ===")
    response = requests.get(f"{BASE_URL}/999")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 404:
        print("Éxito: Error 404 capturado correctamente conforme a la rúbrica.")
    print(response.json())
    print("-" * 50)

    print("\n=== 4. REGISTRAR UN NUEVO PRODUCTO ===")
    nuevo_prod = {
        "nombre": "Audífonos Gamer Pro",
        "precio": 59.99,
        "stock": 15
    }
    response = requests.post(BASE_URL, json=nuevo_prod)
    print(f"Status Code: {response.status_code} (Debe ser 201 - Created)")
    print(response.json())
    print("-" * 50)

    print("\n=== 5. VERIFICAR QUE SE AGREGÓ AL CATÁLOGO ===")
    response = requests.get(BASE_URL)
    print(f"Status Code: {response.status_code}")
    print(f"Total productos en catálogo actual: {len(response.json())}")
    print("-" * 50)

if __name__ == '__main__':
    print("Asegúrate de tener ejecutando 'app.py' en otra terminal antes de correr este script.\n")
    try:
        probar_api()
    except requests.exceptions.ConnectionError:
        print("ERROR CRÍTICO: No se pudo conectar con la API. ¿Olvidaste encender app.py?") 
