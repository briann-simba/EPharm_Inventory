from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/',views.hello_world),
    path('',views.hello_world)
]