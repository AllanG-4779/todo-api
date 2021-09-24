from rest_framework import routers
# from .api import ItemViewSet
# from django.urls import path
from .views import ItemManipulationViews

router = routers.DefaultRouter()

router.register("tasks/todo", ItemManipulationViews, "items")

urlpatterns = router.urls