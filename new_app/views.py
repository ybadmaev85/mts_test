from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from new_app.models import ModelA, ModelB, ModelC


def index(request):
    context = {
        'object_list': ModelA.objects.all(),
        'title': 'Первая модель',
    }
    return render(request, 'new_app/modelF.html', context)


def index2(request):
    context = {
        'object_list': ModelB.objects.all(),
        'title': 'Вторая модель',
    }
    return render(request, 'new_app/modelS.html', context)


def index3(request):
    context = {
        'object_list': ModelC.objects.all(),
        'title': 'Третья модель',
    }
    return render(request, 'new_app/modelT.html', context)


def my_view(request):
    if request.method == 'POST':
        a_one = request.POST.get('a_one')
        a_two = request.POST.get('a_two')
        a_three = request.POST.get('a_three')
        return render(request, 'new_app/base.html')
