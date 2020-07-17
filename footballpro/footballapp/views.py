from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def home(request):
    return render(request,'index.html')
def reg(request):
    return render(request,'reg.html')
def register(request):
    if request.method == "POST":
        fm = Myform(request.POST)
        if fm.is_valid():
            team = fm.cleaned_data['team']
            manager = fm.cleaned_data['manager']
            coach = fm.cleaned_data['coach']
            player1 = fm.cleaned_data['player1']
            player2 = fm.cleaned_data['player2']
            player3 = fm.cleaned_data['player3']
            player4 = fm.cleaned_data['player4']
            player5 = fm.cleaned_data['player5']
            player6 = fm.cleaned_data['player6']
            player7 = fm.cleaned_data['player7']
            player8 = fm.cleaned_data['player8']
            player9 = fm.cleaned_data['player9']
            player10 = fm.cleaned_data['player10']
            player11 = fm.cleaned_data['player11']
            sub1= fm.cleaned_data['sub1']
            sub2= fm.cleaned_data['sub2']
            sub3= fm.cleaned_data['sub3']
            a = REG(team=team, manager=manager, coach=coach, player1=player1, player2=player2, player3=player3, player4=player4, player5=player5, player6=player6, player7=player7, player8=player8, player9=player9, player10=player10, player11=player11, sub1=sub1,sub2=sub2,sub3=sub3)
            a.save()
            return HttpResponse('success')
        else:
            return HttpResponse('something went wrong')
    else:
        return render(request, 'reg.html', {})
def admin_use(request):
    if request.method == "POST":
        b = fixt(request.POST)
        if b.is_valid():
            team1 = b.cleaned_data['team1']
            team2 = b.cleaned_data['team2']
            date = b.cleaned_data['date']
            venue = b.cleaned_data['venue']
            a = fixture(team1=team1, team2=team2, date=date, venue=venue)
            a.save()
            return HttpResponse('fixture set')
        else:
            return HttpResponse('something went wrong')
    else:
        return render(request, 'fix.html', {})


def op(request):
    x=fixture.objects.all()
    return render(request,'op.html',{'y':x})