# from django.shortcuts import render
#
# # Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .models import Tapahtuma
from .forms import TapahtumaForm
import requests
from datetime import datetime
from django.http import JsonResponse
from django.db.models import Count

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# Seuraavana tapahtumien listaus -funktio

# if requests.get("https://visittampere.fi/api/search?type=event&tag=music&limit=10").status_code==200:
#     response = requests.get("https://visittampere.fi/api/search?type=event&tag=music&limit=10")
#     print(response.status_code)
#     json_data = response.json()
#     for obj in json_data:
#         tapahtuman_nimi = obj['title']

def json_example(request):
    return render(request, 'json_example.html')

def chart_data(request):
    dataset = Passenger.objects \
        .values('embarked') \
        .exclude(embarked='') \
        .annotate(total=Count('embarked')) \
        .order_by('embarked')

    port_display_name = dict()
    for port_tuple in Passenger.PORT_CHOICES:
        port_display_name[port_tuple[0]] = port_tuple[1]

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Titanic Survivors by Ticket Class'},
        'series': [{
            'name': 'Embarkation Port',
            'data': list(map(lambda row: {'name': port_display_name[row['embarked']], 'y': row['total']}, dataset))
        }]
    }

    return JsonResponse(chart)


def list_events_event(request):
    tapahtuma = Tapahtuma.objects.all()
    if requests.get('https://visittampere.fi/api/search?type=event&tag=music&start_datetime=1522684233000&limit=60').status_code==200:
        response = requests.get('https://visittampere.fi/api/search?type=event&tag=music&start_datetime=1522684233000&limit=60')
        print(response.status_code)
        eventdata = response.json()
        for event in eventdata:
            if event['start_datetime'] != None:
                event['pvm'] = datetime.fromtimestamp(event['start_datetime']/1000)
        return render(request, 'tapahtuma.html',{'event_list': eventdata, 'tapahtuma':tapahtuma})

def testi(request):
    tapahtuma = Tapahtuma.objects.all()
    kategoriat = {}

    if requests.get('https://visittampere.fi:443/api/v1/event?tag=music&limit=1000000').status_code==200:
        response = requests.get('https://visittampere.fi:443/api/v1/event?tag=music&limit=1000000')
        print(response.status_code)
        musicdata = response.json()
        i = 0

        for event in musicdata:
            #if event['start_datetime'] > 1522684233000:
            # for event['times'] in event:
            #    i += 1
            if event['start_datetime'] >= 1514764800000:
                if event['start_datetime'] < 1546128000000:
                    i += 1
                    print(i)
        kategoriat['musiikki'] = i
        i = 0
        print(kategoriat)

    if requests.get('https://visittampere.fi:443/api/v1/event?tag=culture&limit=1000000').status_code==200:
        response = requests.get('https://visittampere.fi:443/api/v1/event?tag=culture&limit=1000000')
        print(response.status_code)
        culturedata = response.json()
        j = 0

        for event in culturedata:
            if event['start_datetime'] >= 1514764800000:
                if event['start_datetime'] < 1546128000000:
                    j += 1
                    print(j)
        kategoriat['kulttuuri'] = j
        j = 0
        print(kategoriat)

    if requests.get('https://visittampere.fi:443/api/v1/event?tag=dance&limit=1000000').status_code==200:
        response = requests.get('https://visittampere.fi:443/api/v1/event?tag=dance&limit=1000000')
        print(response.status_code)
        dancedata = response.json()
        z = 0

        for event in dancedata:
            if event['start_datetime'] >= 1514764800000:
                if event['start_datetime'] < 1546128000000:
                    z += 1
                    print(z)
        kategoriat['tanssi'] = z
        z = 0
        print(kategoriat)




        # tammikuu 1514764800000 <= aika < 1517443200000
        # helmikuu 1517443200000 <= aika < 1519862400000
        # maaliskuu 1519862400000 <= aika < 1522540800000
        # huhtikuu 1522540800000 <= aika < 1525132800000
        # toukokuu 1525132800000 <= aika < 1527811200000
        # kesäkuu 1527811200000 <=
        # heinäkuu aika
        # elokuu aika
        # syyskuu aika
        # lokakuu aika
        # marraskuu aika
        # joulukuu aika

        return render(request, 'testi.html',{'kategoriat':kategoriat})
#     if requests.get('https://visittampere.fi/api/search?type=event&tag=music&start_datetime=1522684233000&limit=60').status_code==200:
#         response = requests.get('https://visittampere.fi/api/search?type=event&tag=music&start_datetime=1522684233000&limit=60')
#         print(response.status_code)
#         dataset = response.json()
#         # music = Tapahtuma.objects.annotate(music_count=Count('name'))
#         # music_list = list()
#         # for entry in music:
#         #     music_list.append(entry['music_count'])
#         return render(request, 'testi.html',{'music_list': music_count})


    # return render(request, 'event.html',{'event_name': event_name, 'event_list': event_list})
    # return render(request, 'event.html',{'event_list': event_list})
    # return render(request, 'event.html',{'event_list': eventdata})


# def list_events(request):
#     tapahtuma = Tapahtuma.objects.all()
#     return render(request, 'tapahtuma.html', {'tapahtuma':tapahtuma})

def create_event(request):
    form = TapahtumaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_events_event')
    return render(request, 'tapahtuma-form.html', {'form':form})

def update_event(request, id):
    tapahtuma = Tapahtuma.objects.get(id=id)
    form = TapahtumaForm(request.POST or None, instance = tapahtuma)

    if form.is_valid():
        form.save()
        return redirect('list_events_event')
    return render(request, 'tapahtuma-form.html', {'form':form, 'tapahtuma':tapahtuma})

def delete_event(request, id):
    tapahtuma = Tapahtuma.objects.get(id=id)

    if request.method == 'POST':
        tapahtuma.delete()
        return redirect('list_events_event')
    return render(request, 'tapahtuma-delete-confirm.html', {'tapahtuma':tapahtuma})
