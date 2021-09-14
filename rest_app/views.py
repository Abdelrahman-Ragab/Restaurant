from django.shortcuts import render

from .models import *
from .forms import *

from django.core.paginator import Paginator

# Create your views here.

def index(request):

    if request.method == 'POST':
        table_book = TableForm(request.POST)
        if table_book.is_valid():
            table_book.save()

        mail = EmailForm(request.POST)
        if mail.is_valid():
            mail.save()
       


    context = {
        'table_form' : TableForm(),
        'email_form' : EmailForm(),
        'foods' : Food.objects.all(),
        'posts' : Post.objects.all(),
        'services' : Service.objects.all(),
    }
    return render(request , 'pages/index.html' , context)


def contact(request):


    if request.method == 'POST':
        message = ContactForm(request.POST)
        if message.is_valid():
            message.save()

    
    context = {
        'contact_form' : ContactForm(),
    }
    return render(request , 'pages/contact.html' , context)


def blog(request):


    if request.method == 'POST':
        mail = EmailForm(request.POST)
        if mail.is_valid():
            mail.save()


    bloging = Blog.objects.all()

    paginator = Paginator(bloging,1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'email_form' : EmailForm(),
        'blogs' : page_obj,
    }
    return render(request , 'pages/blog.html' , context)


def menu(request):

    if request.method == 'POST':
        table_book = TableForm(request.POST)
        if table_book.is_valid():
            table_book.save()
    
    
    breaking = Break.objects.all()
    lunching = Lunch.objects.all()
    dinnering = Dinner.objects.all()
    desserting = Dessert.objects.all()


    paginator1 = Paginator(breaking,1)
    page_number1 = request.GET.get('page1')
    page_obj1 = paginator1.get_page(page_number1)



    paginator2 = Paginator(lunching,1)
    page_number2 = request.GET.get('page2')
    page_obj2 = paginator2.get_page(page_number2)



    paginator3 = Paginator(dinnering,1)
    page_number3 = request.GET.get('page3')
    page_obj3 = paginator3.get_page(page_number3)



    paginator4 = Paginator(desserting,1)
    page_number4 = request.GET.get('page4')
    page_obj4 = paginator4.get_page(page_number4)


    context = {
        'table_form' : TableForm(),
        'breaks' : page_obj1,
        'lunchs' : page_obj2,
        'dinners' : page_obj3,
        'desserts' : page_obj4,
    }
    return render(request , 'pages/menu.html' , context)
