from django.shortcuts import render, get_list_or_404
from django.http import Http404

from period.models import Period


def index(request):
    periods = Period.objects.all()
    context = {'periods': periods}
    return render(request, "period/index.html", context)

def detail(request, period_name):
    try:
        period = Period.objects.get(name=period_name)
    except Period.DoesNotExist:
        raise Http404("Does not found.")
    context = {'period': period}
    return render(request, "period/detail.html", context)