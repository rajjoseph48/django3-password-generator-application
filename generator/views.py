from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, 'generator\home.html')

def password(request):

    chars = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        chars.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        chars.extend('0123456789')
    if request.GET.get('special'):
        chars.extend('!@#$%&*_.')

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(chars)

    return render(request, 'generator\password.html', {'password':thepassword})

def about(request):
    return render(request, r'generator\about.html')
