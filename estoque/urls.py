# ----------------------------------------------------------------
#                     URLS DO APP - ESTOQUE
# ----------------------------------------------------------------

# urls.py


from django.contrib import admin
from django.urls import path, include

from autenticacao.views import HomeView, SigupView
from django.shortcuts import redirect

from .views import AlimentoListView, AlimentoCreateView, AlimentoUpdateView, AlimentoDeleteView
from . import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',include('autenticacao.urls')),
    path('estoque/', include('estoque.urls')),
    
    path('', AlimentoListView.as_view(), name='alimento_list'),
    path('home/', views.home, name='home'),
    path('create/', AlimentoCreateView.as_view(), name='alimento_create'),
    path('update/<int:pk>/', AlimentoUpdateView.as_view(), name='alimento_update'),
    path('delete/<int:pk>/', AlimentoDeleteView.as_view(), name='alimento_delete'),
]





