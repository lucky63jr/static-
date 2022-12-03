from django.shortcuts import render

# Create your views here.
def small(request):
    return render(request,'small.html')
