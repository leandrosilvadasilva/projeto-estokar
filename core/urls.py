# ----------------------------------------------------------------
#                     URLS GERAIS DO PROJETO
# ----------------------------------------------------------------

from django.contrib import admin
from django.urls import path, include
from autenticacao.views import HomeView, SigupView
from django.shortcuts import redirect


urlpatterns = [
    path('estoque/', include('estoque.urls')),
    path('admin/', admin.site.urls),
    path('',include('autenticacao.urls')),
    
   
]
