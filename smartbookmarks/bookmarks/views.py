from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import UserForm
# Create your views here.

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'bookmarks/login.html')
    else:
        return render(request, 'bookmarks/index.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'bookmarks/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'bookmarks/index.html')
            else:
                return render(request, 'bookmarks/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'bookmarks/login.html', {'error_message': 'Invalid login'})
    return render(request, 'bookmarks/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(email=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'bookmarks/index.html')
    context = {
        "form": form,
    }
    return render(request, 'bookmarks/register.html', context)
