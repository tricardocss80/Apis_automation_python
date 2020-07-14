import requests


# Enviar una consulta y traerme el stats y todos los contenidos
req = requests.get('https://jsonplaceholder.typicode.com/comments?postId=1')
print('Status ')
print(req.status_code)
print('Content')
print(req.content)

# Enviar una consulta y traerme solo el status y el head
req = requests.head('https://jsonplaceholder.typicode.com/comments?postId=1')
print('Status ')
print(req.status_code)
print('Content')
print(req.content)

# Enviar datos y me devuelve el status
req = requests.post('https://jsonplaceholder.typicode.com/posts/', {'title': 'prueba', 'body': 'Hola mundo', 'User id': 1})
print('Status ')
print(req.status_code)

# Eliminar datos y me devuelve el status
req = requests.delete('http://jsonplaceholder.typicode.com/posts/1')
print('Status')
print(req.status_code)

# Modificar todos los datos y me devuelve el status
req = requests.put('http://jsonplaceholder.typicode.com/posts/1', {'title': 'prueba', 'body': 'Hola mundo y algo mas', 'User id': 1})
print('Status')
print(req.status_code)

# Modificar solo una parte de los datos y me devuelve el status
req = requests.patch('http://jsonplaceholder.typicode.com/posts/1', {'title': 'otra prueba'})
print('Status')
print(req.status_code)
