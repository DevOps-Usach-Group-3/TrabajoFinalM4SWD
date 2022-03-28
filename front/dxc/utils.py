import requests

BASE_URL = 'http://back:8080/rest/msdxc/{tipo}?sueldo={sueldo}&ahorro={ahorro}'

def get_response(sueldo, ahorro, tipo):
    url = BASE_URL.format(tipo=tipo, sueldo=sueldo, ahorro=ahorro)

    response = requests.get(url).json()

    return response
