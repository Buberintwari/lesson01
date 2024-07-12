from django.urls import path # type: ignore
from . import views

app_name ='users'

urlpatterns = [
    path('register/', views.register_view, name="register"),
   
]
