from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroForms


def login(request):
    form = LoginForms()

    return render(request, 'usuarios/login.html', {"form": form})
    
def logout(request):


    return render(request, 'usuarios/logout.html')

def register(request):
    form = CadastroForms
    return render(request, 'usuarios/register.html', {"form": form})
