from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import ListView
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    return  render(request, 'index.html')

def display_computers(request):
    items = Computer.objects.all()#graps all the models in models
    computer_paginator = Paginator(items, 10)

    page_num = request.GET.get('page')
    page = computer_paginator.get_page(page_num)
    context = {
        'items' : items,
        'header' :  "Computers",
        'page': page,



    }
    return render(request,'index.html', context )#accepts 3 arguments, template ex index.html

def add_computer(request):
    if request.method == "POST":
        form = ComputersForms(request.POST)
        if form.is_valid():
            form.save()

            return redirect('display_computers')
    else:
        form = ComputersForms()
        return render(request, 'add_new.html', {'form' : form})



class SearchResults(ListView):
    model = Computer
    template_name = 'computer_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Computer.objects.filter(Q(computer_name__icontains=query) |
                                       Q(serial_number__icontains=query) | Q(user_name__icontains=query) | Q(person_full_name__icontains=query))