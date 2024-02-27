from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta: #Permite describir en que modelo estoy basandome
        model = Task
        fields = ('id', 'title', 'description', 'done', 'created_at') #Datos que utilizo para convertirlo de datos de python a json
        read_only_fields = ('id', 'created_at') #Campos que no son modificadoss