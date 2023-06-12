from django.urls import path
from . import views

# url config method
urlpatterns = [
    path('hello/', views.say_hello)
]