# Create your views here.
from django.shortcuts import redirect, HttpResponse

from vote.models import Vote


def register_vote(request):
    schacht_id = request.GET.get('schacht', None)
    por_id = request.GET.get('por', None)
    time = request.GET.get('time', '12:00')
    name = request.GET.get('name')
    Vote.objects.create(schacht_id=schacht_id, por_id=por_id, time=time, name=name)
    return redirect('/baloe/gkr/')

def update_votes(request):
    output = """
    <div class="tile is-antecestor">
        <div class="tile is-parent">
            <div class="tile is-child box">
                <nav class="level">
                    <div class="level-item has-text-centered">
                        <div>
                            <p class="heading"> Meeste stemmen Schacht </p>
                            <p class="title has-text-info">%s</p>
                            <p class="title ">%s</p>
                        </div>
                    </div>
                    <div class="level-item has-text-centered">
                        <div>
                            <p class="heading"> Meeste stemmen Por </p>
                            <p class="title has-text-danger">%s</p>
                            <p class="title">%s</p>
                        </div>
                    </div>
                </nav>

            </div>
        </div>
    </div>
    <div class="tile is-antecestor">
        <div class="tile is-parent">
            <div class="tile is-child box">
                    %s
            </div>
        </div>
    """ % ()
    return HttpResponse()
