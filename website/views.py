from django.shortcuts import redirect,render
from . import views
from django.http import HttpResponse
from website.models import crudst
from django.contrib import messages

def index_redirect(request):
    return redirect('/web/')

    
def stdisplay(request):
    results = crudst.objects.all()
    return render(request,'record.html',{"crudst":results})

def stinsert(request):
    if request.method == "POST":
        if request.POST.get('stname') and request.POST.get('stemail') and request.POST.get('staddress') and request.POST.get('stmobile') and request.POST.get('stgender'):
            savest=crudst()
            savest.stname=request.POST.get('stname')
            savest.stemail=request.POST.get('stemail')
            savest.staddress=request.POST.get('staddress')
            savest.stmobile=request.POST.get('stmobile')
            savest.stgender=request.POST.get('stgender')
            savest.save()
            messages.success(request,"The Record " +savest.stname +" IS Saved Succesfully .....!")
            return render(request,"create.html")

    else:
        return render(request,"create.html")
    return render(request,"create.html")   

def isPage(request):
    return render(request,'isdept.html')

def ecPage(request):
    return render(request,'ecdept.html')

def cstable(request):
    return render(request,'cstable.html')


def main(request):
    return render(request,'main.html')