"""INED URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import INED_app.views
from django.contrib.auth.decorators import login_required

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', INED_app.views.Login.as_view()),
    path('login/', INED_app.views.Login.as_view(), name = 'login'),
    path('logout/', login_required(INED_app.views.Logout.as_view()), name = 'logout'),
    path('users-admin/', login_required(INED_app.views.Administrador.as_view()), name = 'users-manager'),
    path('monitor/', login_required(INED_app.views.Monitor.as_view()), name = 'monitor'),
    path('supervisor/', login_required(INED_app.views.Supervisor.as_view()), name = 'supervisor'),
    path('personal/', login_required(INED_app.views.Personal.as_view()), name = 'personal'),
    path('editar_usuario/<int:id>', login_required(INED_app.views.editarAutor), name = 'editar_usuario'),
    path('visualizar_usuario/<int:id>', login_required(INED_app.views.verAutor), name = 'ver_usuario'),
    path('eliminar_usuario/<int:id>', login_required(INED_app.views.eliminarUsuario), name = 'eliminar_usuario'),
    path('reactivar_usuario/<int:id>', login_required(INED_app.views.reactivarUsuario), name = 'reactivar_usuario'),
    path('registrar_usuario/', login_required(INED_app.views.RegistrarUsuario.as_view()), name = 'registrar_usuario'),
    path('registrar_adulto/', INED_app.views.RegistrarAdulto.as_view(), name = 'registro_adulto')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
