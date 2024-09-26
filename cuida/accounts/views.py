from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST['nome']
        email = request.POST['email']
        password = request.POST['senha']

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, 'Conta criada com sucesso! Faça login.')
        return redirect('login')

    return render(request, 'accounts/login.html') 

def login_view(request):
    if request.method == 'POST':
        username = request.POST['nome']
        password = request.POST['senha']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos.')

    return render(request, 'accounts/login.html')
