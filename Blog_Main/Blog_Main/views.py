from django.shortcuts import render, redirect
from blogs.models import Category, Blogs
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import auth

def home(request):
    categories = Category.objects.all()
    featured_blogs = Blogs.objects.filter(is_featured = True, status = 'published')
    non_featured_blogs = Blogs.objects.filter(is_featured = False, status = 'published')
    context = {
        'categories' : categories,
        'featured_blogs' : featured_blogs,
        'non_featured_blogs' : non_featured_blogs
    }
    return render(request, "home.html", context)

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, "auth/register.html", context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, "auth/login.html", context)

def logout_view(request):
    auth.logout(request)
    return redirect("home")