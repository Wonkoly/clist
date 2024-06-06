import click
from .todoistApiRequests import TodoistAPI


@click.group()
def cli():
    """Herramienta de gestion de tareas con todoist mediante CLI"""
    pass

@click.command()
def ls():
    """Lista las tareas """     
    pass

if __name__ == '__main__':
    cli()
