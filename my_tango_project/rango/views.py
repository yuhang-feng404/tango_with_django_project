from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rango.models import Category, Page
from rango.forms import CategoryForm, UserForm
from datetime import datetime

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))

    last_visit_time = datetime.strptime(last_visit_cookie[:-7], "%Y-%m-%d %H:%M:%S")

    if (datetime.now() - last_visit_time).days > 0:
        visits += 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits

def index(request):
    visitor_cookie_handler(request)
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {
        'categories': category_list,
        'visits': request.session['visits'],
    }
    return render(request, 'rango/index.html', context_dict)

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/rango/')
    else:
        form = CategoryForm()
    return render(request, 'rango/add_category.html', {'form': form})

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
    else:
        user_form = UserForm()
    return render(request, 'rango/register.html', {'user_form': user_form, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('/rango/')
            else:
                return render(request, 'rango/login.html', {'error': "Your account is disabled."})
        else:
            return render(request, 'rango/login.html', {'error': "Invalid login details."})
    return render(request, 'rango/login.html')

def user_logout(request):
    logout(request)
    return redirect('/rango/')

@login_required
def restricted(request):
    return render(request, 'rango/restricted.html')

