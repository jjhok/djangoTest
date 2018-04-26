from django.shortcuts import render
from .models import Note
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
#from django.http import HttpResponse

import random

class Write(CreateView):
    model = Note
    fields = ['name', 'text']
    success_url = reverse_lazy('note')
    # success_url = 'simple/hello....' url 바뀌면 다 바꿔줘야하므로 이렇게 하지말 것.

def hello(request):
    data = {'lotto': getLottoNum()}
    return render(request, 'simple/hello.html', {'data': data})

def getLottoNum():
    lotto = [random.randint(1,45) for i in range(6)]
    lotto.sort()
    return lotto

def note(reqeust):
    notes = Note.objects.all().order_by('-published_date')
    return render(reqeust, 'simple/note.html', {'notes': notes})