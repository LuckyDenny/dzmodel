from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('shop/',views.shop, name='shop'),
    path('shop/category/<slug:slug>/', views.category, name='category'),
    path('product/<slug:slug>/', views.product, name="product"),
]