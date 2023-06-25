from django.shortcuts import render
from django.http import HttpResponse
import math

# Create your views here.
def cal(request,at=100,dif=100,po=100):
    x = math.floor(22 * at * po / dif)
    y = math.floor(x / 50 + 2)
    damage = [math.floor(y * (0.85 + (i / 100))) for i in range(16)]
    context = {'damage': damage}
    return render(request, 'cal_simple/cal_simply.html', context)

def result(request):
    if request.POST["at"] == "":
        at = 100
    else:
        at = int(request.POST["at"])
    if request.POST["dif"] == "":
        dif = 100
    else:
        dif = int(request.POST["dif"])
    if request.POST["po"] == "":
        po = 100
    else:
        po = int(request.POST["po"])
    x = math.floor(22 * at * po / dif)
    y = math.floor(x / 50 + 2)
    damage = [math.floor(y * (0.85 + (i / 100))) for i in range(16)]
    context = {'damage': damage, 'at': at, 'dif': dif, 'po': po}
    return render(request, 'cal_simple/result.html', context)