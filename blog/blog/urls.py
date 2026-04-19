from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('post/<slug:slug>/', views.post, name="post"),
    path('category/<slug:slug>/', views.category, name="category"),
]