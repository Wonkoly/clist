from setuptools import setup, find_packages

setup(
    #Nombre de la app
    name='clist',
    #Version de la app
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Click',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'todoist_cli = clist.cli:cli',
        ],
    },
)

