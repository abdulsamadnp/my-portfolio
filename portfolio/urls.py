from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.home,),
    path('', views.mhome, name="mhome"),
    ]
