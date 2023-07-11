from django.shortcuts import render, redirect
from django.contrib import messages
from myapp.forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Save the user in the database or perform other necessary actions
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Perform authentication check
        # Redirect to the hello world page on successful login
        if authenticated:
            return redirect('hello')
        else:
            messages.error(request, 'Invalid username or password!')
    return render(request, 'login.html')

def hello(request):
    return render(request, 'hello.html')
