from django.shortcuts import render
# from django.shortcuts import get_object_or_404, render
# Create your views here.

def index(request):
    context={}
    return render(request, 'portal/index.html', context)   