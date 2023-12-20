from django.shortcuts import render

from new_app.models import ModelA


def index(request):
    context = {
        'object_list': ModelA.objects.all(),
        'title': 'Первая модель',
    }
    print(context)
    return render(request, 'new_app/modelF.html', context)

