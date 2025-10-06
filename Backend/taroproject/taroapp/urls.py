from django.urls import path,include
from .views import TaroViewSet
from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'taro',TaroViewSet,basename='taro')
urlpatterns = [
    path("api/", include(router.urls)),

]
