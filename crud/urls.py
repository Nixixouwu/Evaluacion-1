from django.urls import path
from login_app.views import login
from login_app.views import homel, success
from .views import *

urlpatterns = [
    path('',login,name='product-list'),
    path('new/',product_new,name='product-new'),
    path('marca/<str:marca>/',product_by_marca,name='product-marca'),
    path('<str:product_id>/',product_detail,name='product-detail'),
    path('<str:product_id>/edit',product_edit,name='product-edit'),
    path('<str:product_id>/delete',product_delete,name='product-delete'),
]