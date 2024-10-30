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
from django.urls import path, include
from adm.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from adm import views
# from django.conf.urls import url



urlpatterns = [
    # Páginas
    path('admin/', admin.site.urls),
    path('home/', ReactView.as_view(), name="home"),
    path('prod/', ReactViewProd.as_view(), name="produtos"),
    path('adm/', adm, name='adm'),
    path('', views.main, name='main'),
    path('painelcontrole/', painelControle),
    path('senha/', senha),
    path('inicio/', inicio),
    path('produtos/', produtos, name='produtos'),
    path('usuarios/', usuarios),
    path('createprodutos/', createprodutos, name='Criar Produto'),
    path('dashboard/produtos/', dashboard_produtos),
    path('dashboard/balanco/', dashboard_balanco),
    path('usuarios/editar/<int:pk>/', edit_user, name='edit_user'),
    path('produtos/editar/<int:pk>/', edit_produtos, name='edit_produtos'),
    
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
    path('AdicionarProduto/', AdicionarProduto, name='AdicionarProduto'),
    path('logar/', logar),
    path('logauts/', logauts),
    path('alterarsenha/', alterarsenha),
    path('produtos/update/<int:pk>/', update_produtos, name='update_produtos'),
    path('produtos/delete/<int:pk>/', delete_produtos, name='delete_produtos'),
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = "adm.views.error404"


   
