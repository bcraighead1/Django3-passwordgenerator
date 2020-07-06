from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html', {'password': '1234'})

def password(request):
    the_password = ''
    length = int(request.GET.get('length', 12))
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNSPQRSTUVWXYS')

    if request.GET.get('numbers'):
        characters.extend('0123456789')

    if request.GET.get('special'):
        characters.extend('!@#$%^&*()_+=-<>?/')

    for x in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})

def about(request):
    return render(request, 'generator/about.html')
