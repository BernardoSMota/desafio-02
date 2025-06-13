from django.contrib import admin
from django.urls import path
from funcionarios.views import index, delete_funcionario, create, edit_funcionario

app_name = 'funcionarios'

urlpatterns = [
    path('', index, name='index'),
    path('funcionario/create/', create, name='create'),
    path('funcionario/edit/<int:funcionario_id>/', edit_funcionario, name='edit'),
    path('funcionario/delete/<int:funcionario_id>/', delete_funcionario, name='delete'),
]
