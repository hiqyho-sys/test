from django.shortcuts import render

def index(request):
	return render(request, 'core/index.html')

def certificates(request):
    return render(request, 'core/certificates.html')

# Create your views here.
