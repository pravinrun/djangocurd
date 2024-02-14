from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import dhote

def create(request):
    data=dhote.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        gmail=request.POST['gmail']
        mobile=request.POST['mobile']
        date=request.POST['date']
        dhote(name=name,gmail=gmail,mobile=mobile,date=date).save()
        data=dhote.objects.all()
        return render(request,'rahul/create.html',{'key':data})
    return render(request,'rahul/create.html',{'key':data})


def update(request):
    data=dhote.objects.get(pk=request.GET['q'])
    if request.method=='POST':
        data.name=request.POST['name']
        data.gmail=request.POST['gmail']
        data.mobile=request.POST['mobile']
        data.date=request.POST['date'] 
        data.save()
        return redirect('/')
    return render(request,'rahul/update.html',{'key':data})
def delete(request):
    data=dhote.objects.get(pk=request.GET['q']).delete()
    return redirect('/')
# Create your views here.
