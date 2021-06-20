from django.shortcuts import render, get_object_or_404, redirect
from .models import Disciplina, Matricula, Despesa
from django.contrib.auth.decorators import login_required

@login_required
def listaDespesas(request):

    listadespesa = Despesa.objects.all
    #lista a disciplina que o estudante está matriculado de acordo com o usuário que está logado.
    #listadespesa = Despesa.objects.filter(usuario=request.user)

    return render(request, 'gestaoacademicaapp/index.html', {'despesas':listadespesa})




@login_required
def fazerPagamento(request, id):
    efetuarpagamento = get_object_or_404(Despesa, pk=id)

    if(efetuarpagamento.status == 'pendente'):
       efetuarpagamento.status = 'pago'

    efetuarpagamento.save()

    return redirect('/')

@login_required
def tornarPendente(request, id):
    tornarpendente = get_object_or_404(Despesa, pk=id)

    if(tornarpendente.status == 'pago'):
       tornarpendente.status = 'pendente'

    tornarpendente.save()

    return redirect('/')

@login_required
def listaMatriculas(request):

    #listadisciplina = Matricula.objects.all
    #lista a disciplina que o estudante está matriculado de acordo com o usuário que está logado.
    listadisciplina = Matricula.objects.filter(estudante=request.user)

    return render(request, 'gestaoacademicaapp/index.html', {'disciplinas':listadisciplina})

@login_required
def fazerMatricula(request, id):
    matriculardisciplina = get_object_or_404(Matricula, pk=id)

    if(matriculardisciplina.status == 'prevista'):
        matriculardisciplina.status = 'matriculado'

    matriculardisciplina.save()

    return redirect('/')
