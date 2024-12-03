from django.urls import path

from miTienda import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar/', views.registrar_cliente, name='registrar_cliente'),
    path('login/', views.login_cliente, name='login_cliente'),
    path('logout/', views.logout_cliente, name='logout_cliente'),
    path('productos/', views.listar_productos, name='listar_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('producto/borrar/<int:producto_id>/', views.borrar_producto, name='borrar_producto'),
    path('exportar_excel/', views.exportarExcel, name='exportar_excel'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)