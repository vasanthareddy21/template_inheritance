from django.shortcuts import render

# Create your views here.

def parent(request):
    return render(request,'parent.html')

def child(request):
    return render(request,'child.html')

def mdb4(request):
    return render(request,'mdb4.html')
