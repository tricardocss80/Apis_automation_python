import requests
import unittest


class Apitest(unittest.TestCase):
    def test001_modificar_todos_los_datos_en_post(self):
        req = requests.put('http://jsonplaceholder.typicode.com/posts/1',
                           {'title': 'prueba', 'body': 'Hola mundo y algo mas', 'User id': 1})
        print(req.status_code)
        self.assertEqual(req.status_code, 200)

    def test002_modificar_titulo_de_post(self):
        req = requests.patch('http://jsonplaceholder.typicode.com/posts/1', {'title': 'otra prueba'})
        print('Status')
        self.assertEqual(req.status_code, 200)


if __name__ == '__main__':
    unittest.main()
