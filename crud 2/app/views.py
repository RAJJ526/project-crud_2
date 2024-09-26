from django.shortcuts import render,redirect
from .forms import CarForm
from .models import Car
# Create your views here.
def tables(request):
    obj  =  Car.objects.all()
    context  ={
        'obj':obj
    }
    return render(request, 'tables.html', context)

def add(request):
    return render(request, 'add.html')


def save(request):
    car  = CarForm(request.GET)
    if car.is_valid():
        car.save()
        return redirect('/')
    else:
        context = {'error':car}
        return render(request, 'add.html', context)


def delete(request,id):
    Car.objects.get(id = id).delete()
    return redirect('/')

def edit(request,id):
    obj  =Car.objects.get(id = id)
    context  =  {
        'obj':obj
    }
    return render(request, 'edit.html', context)


def update(request,id):
    obj  =Car.objects.get(id = id)
    car  = CarForm(request.GET, instance =  obj)
    if car.is_valid():
        car.save()
        return redirect('/')
    else:
        context = {'error':car, 'obj': obj}
        return render(request, 'edit.html', context)