from django.shortcuts import render
from django.http import HttpResponse

def index1(request):
  eka_dict = {'sisalto': "Tämä on tekstiä views.py:stä!"}
  return render(request, 'app1/sivu.html', context=eka_dict)

def index2(request):
  eka_dict = {'sisalto': "Tämä on myös tekstiä views.py:stä!"}
  return render(request, 'app1/sivu.html', context=eka_dict)
