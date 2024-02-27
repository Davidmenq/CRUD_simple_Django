#Las rutas tambi'en se pueden crear en el archivo views.py, o como en este caso, en un archivo independiente
from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class TaskViewSet(viewsets.ModelViewSet): #Un viewset es un conjunto de vistas que forman un crud completo para la ruta creada
    queryset = Task.objects.all() #Es igual a la tabla que quiero importar
    permission_classes = [permissions.AllowAny] #Permite acceder a todos sin pasar por un proceso de atenticaci'on
    serializer_class = TaskSerializer #Viene de la clase serializer que creada

    #Cuando queremos hacer nuestras propias operaciones personalizadas a parte del CRUD por defecto se agrega un ACTION mediante una funcion
    @action(detail=True, methods=['post'])
    def done(self, request, pk=None):
        task = self.get_object() #Obtiene una 'unica tarea basada en el ID
        task.done = not task.done #Cambia el valor por el contrario, si est'a en true lo cambia a false y viceversa
        task.save()
        return Response({
            'status': 'task done' if task.done else 'task undone' 
        }, status = status.HTTP_200_OK)
