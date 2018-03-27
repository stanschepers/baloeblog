from django.shortcuts import render

# Create your views here.


def register_vote(request):
    schacht_name = request.GET.get('schacht', None)
    por_name = request.GET.get('por', None)
    time = request.GET.get('time', '12h00')
    name = request.GET.name

    vote = Vote.make
