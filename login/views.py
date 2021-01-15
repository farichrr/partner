from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def Test(request):
        return render(request, 'login.html')