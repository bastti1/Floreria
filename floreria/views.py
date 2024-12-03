from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForm, ClienteForm, LoginForm, CategoriaForm
from .models import Producto, Categoria
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()

    return render(request, 'agregar_producto.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_cliente')
    else:
        form = ClienteForm()
    return render(request, 'registrar_cliente.html', {'form': form})

def login_cliente(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    form.add_error(None, 'Cuenta inactiva. Contacta al administrador.')
            else:
                form.add_error(None, 'Credenciales incorrectas.')
    else:
        form = LoginForm()
    return render(request, 'login_cliente.html', {'form': form})

def logout_cliente(request):
    logout(request)
    return redirect('index')

@login_required
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_producto')
    else:
        form = CategoriaForm()
    return render(request, 'crear_categoria.html', {'form': form})
@login_required
def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'borrar_producto.html', {'producto': producto})

import xlwt
from django.http import HttpResponse
from .models import Producto  # Asegúrate de importar tu modelo Producto

def exportarExcel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=productos.xls'
    archivo = xlwt.Workbook(encoding='utf-8')
    hoja = archivo.add_sheet('Productos')
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columnas = ['ID', 'Nombre', 'Descripción', 'Precio', 'Categoría']
    for i in range(len(columnas)):
        hoja.write(0, i, columnas[i], font_style)

    productos = Producto.objects.all().values_list('id', 'nombre', 'descripcion', 'precio', 'categoria__nombre')
    
    row_num = 1
    for producto in productos:
        for i in range(len(producto)):
            hoja.write(row_num, i, producto[i], font_style)
        row_num += 1

    archivo.save(response)
    return response
