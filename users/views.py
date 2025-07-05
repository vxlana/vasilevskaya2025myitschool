from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from orders.models import Order

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('users:profile')

    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('users:profile')
            else:
                form.add_error(None, 'Неверное имя пользователя или пароль')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required(login_url='/users/login')
def user_logout(request):
    logout(request)
    return redirect('users:login')

@login_required(login_url='/users/login/')
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = UserProfileForm(instance=request.user)
    orders = Order.objects.filter(user=request.user)

    return render(request, 'users/profile.html', {'form': form, 'orders': orders})

def home(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/google/login/')
    return redirect('main:product_list')


