from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import *
from .forms import *
from .models import Usuario
from django.urls import reverse_lazy
from django.http import Http404

# Create your views here.
def prueba(request, tipo_usuario):
    if request.user.tipo_usuario == tipo_usuario:
        return True
    else:
        raise Http404(f"No tienes permisos de {tipo_usuario}")
        
class Administrador(ListView):
    model = Usuario
    template_name = 'administrador.html'
    queryset = Usuario.objects.filter()
    
    def dispatch(self, request, *args, **kwargs):
        if prueba(request, 'Administrador'):
            return self.get(request, *args, **kwargs)


class Monitor(ListView):
    
    def get(self, request, *args, **kwargs):
        if request.user.tipo_usuario == 'Monitor':

            return render(request, 'monitor.html')
        else:
            messages.warning(request, 'Su cuenta no tiene accesos de monitor')
            return redirect('logout')
    

class Supervisor(View):
    def get(self, request, *args, **kwargs):
        if request.user.tipo_usuario == 'Supervisor de módulo':
            return render(request, 'supervisor.html')
        else:
            messages.warning(request, 'Su cuenta no tiene accesos de supervisor')
            return redirect('logout')

class Personal(View):
    def get(self, request, *args, **kwargs):
        if request.user.tipo_usuario == 'Personal de módulo':
            return render(request, 'personal.html')
        else:
            messages.warning(request, 'Su cuenta no tiene accesos de personal')
            return redirect('logout')

class Logout(View):
        def get(self, request, *args, **kwargs):
            logout(request)
            return redirect('login')

class Login(View):
    def defineUserURL(self, request):
        if request.user.tipo_usuario == 'Administrador':
            return redirect('administrador')
        if request.user.tipo_usuario == 'Monitor':
            return redirect('monitor')
        if request.user.tipo_usuario == 'Supervisor de módulo':
            return redirect('supervisor')
        if request.user.tipo_usuario == 'Personal de módulo':
            return redirect('personal')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.defineUserURL(request)
        else:
            return render(request, 'users/login.html')
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return self.defineUserURL(request)
        else:
            messages.warning(request, 'Nombre de usuario o contraseña inválido(s)')
            return self.get(request)
    
# class EditarUsuario(UpdateView):
#     model = Usuario
#     template_name = 'users/crear_usuario.html'
#     form_class = FormaRegistro
#     success_url = reverse_lazy('administrador')

#     def dispatch(self, request, *args, **kwargs):
#         if prueba(request, 'Administrador'):
#             return self.get(request, request, *args, **kwargs)

def editarAutor(request, id):
    usuario = Usuario.objects.get(id = id)
    if request.method == 'GET':
        user_form = FormaRegistro(instance = usuario)
    else:
        user_form = FormaRegistro(request.POST, request.FILES, instance=usuario)
        if user_form.is_valid():
            user_form.save()
        return redirect('administrador')
    return render(request, 'users/editar_usuario.html', {'form':user_form})

def eliminarUsuario(request, id):
    usuario = Usuario.objects.get(id = id)
    if request.method == 'GET':
        user_form = FormaVisualizar(instance = usuario)
    else:
        usuario.delete()
        return redirect('administrador')
    return render(request, 'users/eliminar_usuario.html', {'form':user_form})

def reactivarUsuario(request, id):
    usuario = Usuario.objects.get(id = id)
    if request.method == 'GET':
        user_form = FormaVisualizar(instance = usuario)
    else:
        usuario.reactive()
        return redirect('administrador')
    return render(request, 'users/reactivar_usuario.html', {'form':user_form})

def verAutor(request, id):
    usuario = Usuario.objects.get(id = id)
    if request.method == 'GET':
        user_form = FormaVisualizar(instance = usuario)
    return render(request, 'users/ver_usuario.html', {'form':user_form, 'user':usuario})
    

class RegistrarUsuario(CreateView):
    def get(self, request, *args, **kwargs):
        form = FormaRegistro()
        if request.user.tipo_usuario == 'Administrador':
            return render(request, 'users/crear_usuario.html', {'form': form})
        else:
            return redirect('administrador')

    def post(self, request, *args, **kwargs):
        form = FormaRegistro(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.save()
            return redirect('administrador')
        return render(request, 'users/crear_usuario.html', {'form': form})

