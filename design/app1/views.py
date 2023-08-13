from django.shortcuts import render
from app1.models import Place,Team

def home(request):
    p = Place.objects.all()
    t=Team.objects.all()

    return render(request,'base.html', {'p': p,'t':t})



def contact(request):
    return render(request,'contact.html')


def news(request):
    return render(request,'news.html')
