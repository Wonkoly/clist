import os
import click as cl
from todoistApiRequests import TodoistAPI

"""
Clase de comandos para tratar las requests de la API de Todoist
"""
class CmdAPI:

    def __init__(self):
        self.todoist_api = TodoistAPI(os.getenv('TODOIST_API_TOKEN'))

    #------------------------------------------------------------------
    # TASKS COMMANDS
    
    # TASKS LIST
    def list_tasks(self):
        tasks = self.todoist_api.get_requests(rute="tasks")
        for task in tasks:
            cl.echo(cl.style(task['content'], fg='yellow'))


    # TASKS ADD
    def add_task(self, content, description=""):
        data = {
            "content" : content,
            "description" : description
        }
        new_task = self.todoist_api.post_requests(rute="tasks",data=data)


#------------------------------------------------------------------
# PROJECTS COMMANDS
    def list_projects(self):
        projects = self.todoist_api.get_requests(rute="projects")
        for project in projects:
            print(project['name'])
