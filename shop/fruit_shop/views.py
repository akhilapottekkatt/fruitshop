from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request,'about.html')




def order(request):
    return render(request, 'order.html')


def condact(request):
    return render(request, 'condact.html') 