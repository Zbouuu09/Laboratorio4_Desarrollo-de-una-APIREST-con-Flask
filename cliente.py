<<<<<<< HEAD
import requests

url = "http://127.0.0.1:5000/productos"

respuesta = requests.get(url)

print("Código de estado:", respuesta.status_code)
print("Productos:")
print(respuesta.json())
=======
 
>>>>>>> 7540d9649e455e1598c72861dd28663a32f1302e
