from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def propertygrid(request):
    return render(request, 'property-grid.html')

def propertysingle(request):
    return render(request, 'property-single.html')


def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def agentsgrid(request):
    return render(request, 'agents-grid.html')

def agentsingle(request):
    return render(request, 'agent-single.html')

def about(request):
    return render(request, 'about.html')
