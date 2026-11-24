from django.shortcuts import redirect, render
from .form import *
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def agendamento(request):
    return render(request, 'agendamento.html')

def login(request):
    return render(request, 'login.html')



# Cadastro

def cadastrar_medico(request):
    if request.method == "POST":
        form = medicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_medicos")
        else:
            return render(request, 'templates/login_medico.html', {'form': form})

def listar_medico(request):
    medicos = Medico.objects.all()
    return render(request,'')