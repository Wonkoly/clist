import click
from commands import CmdAPI


#-------------------------------------------------------------------
# Comando principar de la app
@click.group()
def cli():
    """Herramienta de gestion de tareas con Todoist mediante CLI."""
    pass

#-------------------------------------------------------------------
# TASK subgrupo de comandos para la gestion de tareas
@cli.group()
def task():
    """Gestion de tareas."""     
    pass

# TASK: add [Comando para agregar tareas]
@task.command()
@click.argument('content')
@click.option('-d', '--description', help='Coloque una descripcion de la tarea.')
def add(content, description):
    new_task = CmdAPI()
    new_task.add_task(content, description)

@task.command()
@click.option('-f', '--filter', help='Filtrar por estado de la tarea.')
def list(filter):
    tasks = CmdAPI()
    tasks.list_tasks()


#-------------------------------------------------------------------
# PROJECTS subgrupo de comandos para la gestion de proyectos
@cli.group()
def project():
    """Gestion de proyectos."""
    pass




if __name__ == '__main__':
    cli()
