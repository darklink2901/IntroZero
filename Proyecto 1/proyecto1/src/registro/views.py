from django.shortcuts import render,redirect
from .forms import RegistradoForm,FormLogin
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from .models import Registrado,Libro,Resena
from django.db.models import Q
# Create your views here.


def inicio(request):
    if request.user.is_authenticated:
        todRes = Resena.objects.all();
        return render(request, "index.html",{'todRes':todRes})
    # En otro caso redireccionamos al login
    return redirect('login')

def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=usuario, password=password)
            if user is not None:
                request.session['usr'] = user.username
                do_login(request, user)
                return redirect('index')
    return render(request, "login.html", {'form': form})

def logout(request):
    do_logout(request)
    return redirect('login')

def registro(request):
        form = UserCreationForm()
        if request.method == "POST":
            form = UserCreationForm(data=request.POST)
            if form.is_valid():
                user = form.save()
                if user is not None:
                    request.session['usr'] = user.username
                    do_login(request, user)
                    return redirect('index')

        form.fields['username'].help_text = None
        form.fields['password1'].help_text = None
        form.fields['password2'].help_text = None
        return render(request, "registro.html", {'form': form})

def libros(request):
    if request.user.is_authenticated:
        libros = Libro.objects.all()
        queryset = request.GET.get("bus")
        if queryset:
            libros =Libro.objects.filter(
             Q(isbn__icontains = queryset) |
             Q(title__icontains = queryset)|
             Q(author__icontains = queryset)|
             Q(year__icontains = queryset)
            ).distinct()
        return render(request, "libros.html",{'libros': libros})
    return redirect('login')

def detalles_libro(request,isbn):
    if request.user.is_authenticated:
        libro = Libro.objects.get(isbn = isbn)
        titulo = libro.title
        usuario = request.session.get('usr')
        libroR = Resena.objects.filter(libro_titulo = titulo)
        contexto = {
            'libro': libro,
            'resenas':libroR
        }
        if request.POST.get('inf') and request.POST.get('inf2'):
            resena = request.POST.get("inf")
            calificacion = request.POST.get("inf2")
            post=Resena()
            post.usuario = usuario
            post.calificacion = calificacion
            post.resena = resena
            post.libro_titulo = titulo
            post.save()

            return render(request, "crear_resena.html",contexto)
        else:

            return render(request, "crear_resena.html",contexto)
