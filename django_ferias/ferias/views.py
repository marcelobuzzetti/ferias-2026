from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Ferias
from .forms import FeriasForm

def listar_ferias(request):
    ferias = Ferias.objects.all()
    
    # Filtros
    nome = request.GET.get('nome', '')
    secao = request.GET.get('secao', '')
    periodo = request.GET.get('periodo', '')
    tipo_carreira = request.GET.get('tipo_carreira', '')
    
    if nome:
        ferias = ferias.filter(nome_guerra__icontains=nome)
    if secao:
        ferias = ferias.filter(secao__icontains=secao)
    if periodo:
        ferias = ferias.filter(periodo_aquisitivo=periodo)
    if tipo_carreira:
        ferias = ferias.filter(tipo_carreira=tipo_carreira)
    
    context = {
        'ferias': ferias,
        'total_registros': Ferias.objects.count(),
        'total_carreira': Ferias.objects.filter(tipo_carreira='CARREIRA').count(),
        'total_temporario': Ferias.objects.filter(tipo_carreira='TEMPORÁRIO').count(),
    }
    return render(request, 'ferias/listar.html', context)

def criar_ferias(request):
    if request.method == 'POST':
        form = FeriasForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Férias cadastradas com sucesso!')
            return redirect('listar_ferias')
    else:
        form = FeriasForm()
    
    return render(request, 'ferias/form.html', {'form': form, 'titulo': 'Cadastrar Férias'})

def editar_ferias(request, pk):
    ferias = get_object_or_404(Ferias, pk=pk)
    
    if request.method == 'POST':
        form = FeriasForm(request.POST, instance=ferias)
        if form.is_valid():
            form.save()
            messages.success(request, 'Férias atualizadas com sucesso!')
            return redirect('listar_ferias')
    else:
        form = FeriasForm(instance=ferias)
    
    return render(request, 'ferias/form.html', {'form': form, 'titulo': 'Editar Férias'})

def deletar_ferias(request, pk):
    ferias = get_object_or_404(Ferias, pk=pk)
    
    if request.method == 'POST':
        ferias.delete()
        messages.success(request, 'Férias excluídas com sucesso!')
        return redirect('listar_ferias')
    
    return render(request, 'ferias/confirmar_delete.html', {'ferias': ferias})

def visualizar_ferias(request, pk):
    ferias = get_object_or_404(Ferias, pk=pk)
    return render(request, 'ferias/visualizar.html', {'ferias': ferias})
