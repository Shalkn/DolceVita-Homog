"""
URL configuration for DolceVita project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from adm.views import adm, main, CadastroUsuario, logar, painelControle, logauts, alterarsenha, senha, inicio, produtos, usuarios, dashboard_produtos, dashboard_balanco, edit_user
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Páginas
    path('admin/', admin.site.urls),
    path('adm/', adm, name='adm'),
    path('', main),
    path('painelcontrole/', painelControle),
    path('senha/', senha),
    path('inicio/', inicio),
    path('produtos/', produtos),
    path('usuarios/', usuarios),
    path('dashboard/produtos/', dashboard_produtos),
    path('dashboard/balanco/', dashboard_balanco),
    path('usuarios/editar/<int:pk>/', edit_user, name='edit_user'),
    
    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name="reset_password.html"), 
         name="reset_password"),
    
    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
         name="password_reset_done"),
    
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
         name="password_reset_confirm"),
    
    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), 
         name="password_reset_complete"),
    
    # Funções
    path('CadastroUsuario/', CadastroUsuario),
    path('logar/', logar),
    path('logauts/', logauts),
    path('alterarsenha/', alterarsenha),
    
]