from django import forms
from .models import REG
class Myform(forms.Form):
    team=forms.CharField(max_length=30)
    manager=forms.CharField(max_length=20)
    coach=forms.CharField(max_length=20)
    player1=forms.CharField(max_length=20)
    player2=forms.CharField(max_length=20)
    player3=forms.CharField(max_length=20)
    player4=forms.CharField(max_length=20)
    player5=forms.CharField(max_length=20)
    player6=forms.CharField(max_length=20)
    player7=forms.CharField(max_length=20)
    player8=forms.CharField(max_length=20)
    player9=forms.CharField(max_length=20)
    player10=forms.CharField(max_length=20)
    player11=forms.CharField(max_length=20)
    sub1=forms.CharField(max_length=20)
    sub2=forms.CharField(max_length=20)
    sub3=forms.CharField(max_length=20)
    def clean(self):
        super(Myform,self).clean()
        if REG.objects.filter(team=self.cleaned_data['team']).count()>=10:
            raise forms.ValidationError("Registration closed")

class fixt(forms.Form):
    team1=forms.CharField(max_length=30)
    team2=forms.CharField(max_length=30)
    date=forms.DateTimeField()
    venue=forms.CharField(max_length=20)