from django.contrib import admin
from .models import Producto, Categoria, Cliente

admin.site.register(Producto)
admin.site.register(Categoria) 
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('email', 'nombre', 'apellido', 'is_staff', 'is_active')
    search_fields = ('email', 'nombre', 'apellido')
    list_filter = ('is_staff', 'is_active') 
admin.site.register(Cliente, ClienteAdmin)