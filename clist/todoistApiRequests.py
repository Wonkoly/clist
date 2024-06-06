import requests

class TodoistAPI:

    TODOIST_API_URL= 'https://api.todoist.com/rest/v2' #Url Api todoist 

    def __init__(self, token):
        self.token = token

        if not token:
            raise ValueError("Debes de establecer las vatiable de entorno TODOIST_API_TOKEN")

        self.header = {
            "Authorization": f"Bearer {self.token}"
        }

    def get_requests(self, rute):
        try:
            response = requests.get(f"{self.TODOIST_API_URL}/{rute}", headers=self.header)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as error:
            return []


    def post_requests(self, rute):
        #response = requests.post()
        pass

class PreRequests():

    def __init__(self):
        pass









