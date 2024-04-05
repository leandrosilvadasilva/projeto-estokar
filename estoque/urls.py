# ----------------------------------------------------------------
#                     URLS DO APP - ESTOQUE
# ----------------------------------------------------------------

# urls.py

from django.urls import path
from .views import AlimentoListView, AlimentoCreateView, AlimentoUpdateView, AlimentoDeleteView

urlpatterns = [
    path('', AlimentoListView.as_view(), name='alimento_list'),
    path('create/', AlimentoCreateView.as_view(), name='alimento_create'),
    path('update/<int:pk>/', AlimentoUpdateView.as_view(), name='alimento_update'),
    path('delete/<int:pk>/', AlimentoDeleteView.as_view(), name='alimento_delete'),
]
