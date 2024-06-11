import requests

"""
Clase TodoistAPI:
Se encarga de comunicarse por el protocolo HTTP a la API de Todoist con la finalidad de realizar 
solicitudes GET, POST, PUT y DELETE para manipualar las tareas y proyectos de una cuenta activa
cargando el API_TOKEN.
"""
class TodoistAPI:

    TODOIST_API_URL= 'https://api.todoist.com/rest/v2' #Url Api todoist 

    def __init__(self, token):
        self.token = token

        if not token:
            raise ValueError("Debes de establecer las vatiable de entorno TODOIST_API_TOKEN")

        self.header = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type" : "application/json"
        }

    #-------------------------------------------------------------------
    # GET Requests:
    def get_requests(self, rute):
        try:
            response = requests.get(f"{self.TODOIST_API_URL}/{rute}", headers=self.header)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as error:
            return [] 

    #-------------------------------------------------------------------
    # POST Requests:
    def post_requests(self, rute, data):
        response = requests.post(
            f"{self.TODOIST_API_URL}/{rute}", 
            headers=self.header, 
            json=data
        )
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code()

class PreRequests():

    def __init__(self):
        pass









