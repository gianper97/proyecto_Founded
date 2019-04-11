from django.shortcuts import render, HttpResponse

def home(request):
    return render(request,"core/index.html")

def politicas(request):
    return render(request, "core/politicas.html")
