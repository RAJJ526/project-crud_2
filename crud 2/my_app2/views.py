from django.shortcuts import render, redirect
from .forms import MobileForm
from .models import Mobile
# Create your views here.
def delta(request):
    obj=Mobile.objects.all()
    context={
        'obj':obj
    }
    return render(request, 'delta.html', context)

def add2(request):
    return render(request, 'add2.html')

def save2(request):
    x=MobileForm(request.GET)
    if x.is_valid():
        x.save()
        return redirect('/delta')
    else:
        context={'error':x}
        return render(request, 'add2.html', context)
    
def delete2(request, id):
    Mobile.objects.get(id=id).delete()
    return redirect('/delta')

def edit2(request, id):
    obj=Mobile.objects.get(id=id)
    context={
        'obj':obj
    }
    return render(request, 'edit2.html', context)

def update2(request, id):
    obj=Mobile.objects.get(id=id)
    x=MobileForm(request.GET, instance=obj)
    if x.is_valid():
        x.save()
        return redirect('/delta')
    else:
        context={'error':x, 'obj':obj}
        return render(request, 'edit2.html', context)
    
    