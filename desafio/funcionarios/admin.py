from django.contrib import admin
from funcionarios.models import Funcionario


# Register your models here.
@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'city']