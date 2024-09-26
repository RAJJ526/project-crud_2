from django.shortcuts import render, redirect
from .forms import CompanyForm
from .models import Company

# Create your views here.
def index(request):
    obj=Company.objects.all()
    context={
        'obj':obj
    }
    return render(request, 'index.html', context)

def add1(request):
    return render(request, 'add1.html')

def save1(request):
    Company=CompanyForm(request.GET)
    if Company.is_valid():
        Company.save()
        return redirect('/raj')
    else:
        context={'error':Company}
        return render(request, 'add1.html', context)
    
def delete1(request, id):
    Company.objects.get(id=id).delete()
    return redirect('/raj')

def edit1(request, id):
    obj=Company.objects.get(id=id)
    context={
        'obj':obj
    }
    return render(request, 'edit1.html', context)

def update1(request, id):
    obj=Company.objects.get(id=id)
    company=CompanyForm(request.GET, instance=obj)
    if company.is_valid():
        company.save()
        return redirect('/raj')
    else:
        context={'error':company, 'obj': obj}
        return render (request, 'edit1.html', context)