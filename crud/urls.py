from django.urls import path
from .views import *

urlpatterns = [
    path('',product_list,name='product-list'),
    path('<str:product_id>/delete',product_delete,name='product-delete'),
    path('<str:product_id>/edit',product_edit,name='product-edit'),
]