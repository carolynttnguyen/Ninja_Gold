from django.shortcuts import render, redirect

import random


def index(request):
    if "gold" not in request.session:
        request.session['gold'] = 0
    context = {
        'places': {
            'farm': 'earns 10-20 gold',
            'cave': 'earns 5-10 gold',
            'house': 'earns 2-5 gold',
            'casino':'earns/takes 0-50 gold',
        }
    }
    return render(request, 'index.html', context)


def process(request, place):
    # farm
    if place == 'farm':
        request.session['gold'] += round(random.random()*10+10)
    # cave
    elif place == 'cave':
        request.session['gold'] += round(random.random()*5+5)
    # house
    elif place == 'house':
        request.session['gold'] += round(random.random()*3+2)
    # casino
    else:
        request.session['gold'] += round(random.random()*100+-50)
    return redirect('/')
