from django.shortcuts import redirect, render
from item.models import Item, Category
from django.contrib.auth.models import auth

from . forms import SignUpForm
from django.contrib import messages

def frontpage(request):
    items=Item.objects.filter(is_sold=False)[0:4]
    categories=Category.objects.all()
    context={
        'items': items,
        'categories': categories
    }
    return render(request, 'core/frontpage.html', context)

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('/login/')
    else:
        form=SignUpForm()
    context={
        'form': form
    }
    return render(request, 'core/signup.html', context)

def logout(request):
    auth.logout(request)
    messages.success(request, 'Вы успешно вышли из системы')
    return redirect('core:login')
