from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def table(request):
    obj  =  Employes.objects.all()
    context =  {
        'obj' :obj,
    }
    return render(request,'table.html',context)


def save_data(request):
    if request.method =='POST':
        obj  =  MobileForm(request.POST)
        if obj.is_valid():
            obj.save()
        else:
            context = {'error':obj}
            return render(request,'save.html',context)
    return render(request,'save.html')


def update(request,id):
    if request.method =='POST':
        v=Employes.objects.get(id=id)
        obj  =  MobileForm(request.POST, instance=v)
        if obj.is_valid():
            obj.save()
        else:
            context = {'error':obj}
            return render(request,'edit.html',context)
    obj=Employes.objects.get(id=id)
    context={
        'obj':obj
    }
    return render(request, 'edit.html', context)


