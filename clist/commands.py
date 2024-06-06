import os
from todoistApiRequests import TodoistAPI

class CmdAPI:

    def __init__(self):
        self.todoist_api = TodoistAPI(os.getenv('TODOIST_API_TOKEN'))

    def list_projects(self):
        projects = self.todoist_api.get_requests(rute="projects")
        for project in projects:
            print(project['name'])
 
    def list_tasks(self):
        tasks = self.todoist_api.get_requests(rute="tasks")
        for task in tasks:
            print(task['content'])
