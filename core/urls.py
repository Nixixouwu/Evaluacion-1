from django.urls import path
from .views import donaciones, home, quienessomos, herramientas, plantas, carrito, despacho_vendedor, login, pago, productoh1 , productoh2, productoh3, productoh4, productop1, productop2,productop3,productop4,root

urlpatterns = [
    path('',root),
    
    path('home',home,name="home"),

    path('quienessomos',quienessomos,name="quienessomos"),

    path('donaciones',donaciones,name="donaciones"),

    path('herramientas',herramientas,name="herramientas"),

    path('plantas',plantas,name="plantas"),

    path('carrito',carrito,name="carrito"),

    path('despacho_vendedor',despacho_vendedor,name="desp_vend"),

    path('login',login,name="login"),

    path('pago',pago,name="pago"),

    #path('producto/<str:producto>/',product_by_ZA,name='product-ZA'),

    path('producto herramienta 1',productoh1,name="prod_h1"),
    path('producto herramienta 2',productoh2,name="prod_h2"),
    path('producto herramienta 3',productoh3,name="prod_h3"),
    path('producto herramienta 4',productoh4,name="prod_h4"),

    path('producto planta 1',productop1,name="prod_p1"),
    path('producto planta 2',productop2,name="prod_p2"),
    path('producto planta 3',productop3,name="prod_p3"),
    path('producto planta 4',productop4,name="prod_p4"),
]