from rest_framework import routers
from .api import TaskViewSet

router = routers.DefaultRouter()

router.register('api/tasks', TaskViewSet, 'tasks' ) #Registra la ruta, la clase que se ejecuta y el nombre que se le da a la ruta

urlpatterns = router.urls #Es un arreglo que le dice que router.urls tiene los valores que se registraron

