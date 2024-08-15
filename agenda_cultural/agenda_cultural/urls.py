"""
URL configuration for agenda_cultural project.

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
from app_agenda_cultural import views
from app_agenda_cultural.views import criar_evento, editar_evento, excluir_evento

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('criar-evento/', views.criar_evento, name='criar_evento'),
    path('editar-evento/<int:id>/', views.editar_evento, name='editar_evento'),
    path('excluir-evento/<int:id>/', excluir_evento, name='excluir_evento'),
]
