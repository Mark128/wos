from django.shortcuts import render


def index(request):
    output = {}
    return render(request, 'wos_tracker/index.html', output)

def clients(request):
    output = {}
    return render(request, 'wos_tracker/clients.html', output)
