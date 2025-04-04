from django.urls import path

from products import views

urlpatterns = [
    path('hello/', views.hello),
    path('allProducts/', views.get_products),
    path('product/<int:id>',  views.get_product)

]