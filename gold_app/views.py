from django.shortcuts import render, redirect
import random
# from datetime import datetime


def index(request):
    # condition for session variable if key in object condition, if it doesn't exist set initial values
    if "gold" not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
        request.session['end'] = False
    context = {
        'places': {
            'farm': 'earns 10-20 gold',
            'cave': 'earns 5-10 gold',
            'house': 'earns 2-5 gold',
            'casino': 'earns/loses 0-50 gold',
        }
    }
    return render(request, "index.html", context)


def process_money(request, place):
    # if request.method == 'POST':print(place)
    # farm
    # if the name request being submitted is a post, then increment random integer
    if place == 'farm':
        print('You visited the Farm!!!')
        randy = round(random.random()*10+10)
        request.session['gold'] += randy
        request.session['activities'].append(f'You went to visit the Farm for Gold, and earned {randy} gold')

        # cave
    elif place == 'cave':
        print('You are looking for Gold in the Cave!!!')
        randy = round(random.random()*5+5)
        request.session['gold'] +=randy
        request.session['activities'].append(f'You went looking for gold at the Cave, and earned {randy} gold')

        # house
    elif place == 'house':
        print('You searched for Gold in House!!!')
        randy = round(random.random()*2+3)
        request.session['gold'] += randy
        request.session['activities'].append(f'You went searching for gold at the House, and earned {randy} gold')

        # casino
    else:
        print('You took a gamble mining at the casino!!!')
        randy = round(random.random()*100+-50)
        request.session['gold'] += randy
        if randy > 0:
            request.session['activities'].append(f"You took a gamble mining at the Casino and earned {randy} Gold")
        else:
            request.session['activities'].append(f"You took a gamble mining at the Casino and lost {randy} Gold")

    if request.session['gold'] >= request.session['win']:
        request.session['end']= True

    return redirect('/')


def win(request):
    if request.method == 'POST':
        request.session['win']=int(request.POST['win'])
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
