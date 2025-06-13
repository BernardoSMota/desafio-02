from django.shortcuts import render, redirect, get_object_or_404
from funcionarios.models import Funcionario
from funcionarios.forms import FuncionariosForm

# Create your views here.
def index(request):
    funcionarios = Funcionario.objects.all()
    context = {
        'funcionarios_list': funcionarios,
        'page_title': 'Página Inicial'
    }
    return render(request, 'funcionarios/pages/index.html', context=context)


def create(request):
    if request.method == 'POST':
        form = FuncionariosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('funcionarios:index')
    else:
        form = FuncionariosForm()
    
    context = {
        'form': form,
        'page_title': 'Cadastrar novo funcionário'
    }
    return render(request, 'funcionarios/pages/form.html', context=context)


def edit_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)

    if request.method == 'POST':
        form = FuncionariosForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('funcionarios:index')
    
    else:
        form = FuncionariosForm(instance=funcionario)
        
    context = {
        'form': form,
        'page_title': f'Editando {funcionario.name}'
    }
    return render(request, 'funcionarios/pages/form.html', context=context)


def delete_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    funcionario.delete()
    
    return redirect('funcionarios:index')