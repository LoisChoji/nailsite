from django.urls import path
from . import views

app_name ='NailPolishes'

urlpatterns = [
    path('<int:nail_id>/',views.detail, name ='detail'), 
    path('', views.nails, name = 'home-page'),
    path('<int:nail_id>/yourchoice/', views.yourchoice, name = 'yourchoice'),
]