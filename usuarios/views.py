from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form["nome_login"].value()
            senha = form["senha"].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None:
            auth.login(request,usuario)
            messages.success(request,f"{nome} logado com sucesso!")

            return redirect('lista')

        else:
            messages.error(request,"Erro ao efetuar login.")

            return redirect('login')


    return render(request, 'usuarios/login.html', {"form": form})
    
def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    
    return redirect('login')

def register(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            
            nome = form["nome_cadastro"].value()
            email = form["email"].value()
            senha = form["senha1"].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request,'Usuário já existe.')

                return redirect('register')
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request,"Cadastro realizado com sucesso!")
            return redirect('login')
        
    return render(request, 'usuarios/register.html', {"form": form})