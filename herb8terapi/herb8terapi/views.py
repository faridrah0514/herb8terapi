from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello, saya farid software engineer andalan anda")
    return render(request, 'medicio/index.html')