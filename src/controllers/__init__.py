# Importa todos los controllers para facilitar su uso
from .estudiante_controller import EstudianteController
from .docente_controller import DocenteController
from .admin_controller import AdminController

# Lista de lo que se puede importar con "from src.controllers import *"
__all__ = [
  'EstudianteController',
  'DocenteController', 
  'AdminController'
]