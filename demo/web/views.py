from django.shortcuts import render
from django.http import response

# Create your views here.

def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")
