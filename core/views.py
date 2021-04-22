from django.shortcuts import render

# Create your views here.

def HomeView(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)





