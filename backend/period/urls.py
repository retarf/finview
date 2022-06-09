from django.urls import path
from period import views


app_name = 'period'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:period_name>/', views.detail, name='detail'),
]
