
from django.urls import path
from . import views

urlpatterns = [
    path('streaming-platforms',views.platforms,name="platforms")
]
