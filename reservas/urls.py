from django.urls import path
from .views import ver_reservas, agregar_reserva, modificar_reserva, eliminar_reserva

urlpatterns = [
    path('', ver_reservas, name='ver_reservas'),
    path('agregar/', agregar_reserva, name='agregar_reserva'),
    path('modificar/<int:pk>/', modificar_reserva, name='modificar_reserva'),
    path('eliminar/<int:pk>/', eliminar_reserva, name='eliminar_reserva'),
]
