from django.urls import path
from blog import views


namespace = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
]
