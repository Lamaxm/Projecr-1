from django.shortcuts import render
from ..user_app.models import User

def consolt(request):
    context = {'consoler': User.objects.all() }
    return render(request, 'counsolting.html', context)
