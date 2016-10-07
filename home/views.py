from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    return render(request, 'home/home.html', {
        '15sof': ''
    })


def about(request):
    return render(request, 'home/about.html')
