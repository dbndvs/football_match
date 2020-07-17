from django.db import models

# Create your models here.
class REG(models.Model):
    team=models.CharField(max_length=30)
    manager=models.CharField(max_length=20)
    coach=models.CharField(max_length=20)
    player1=models.CharField(max_length=20)
    player2=models.CharField(max_length=20)
    player3=models.CharField(max_length=20)
    player4=models.CharField(max_length=20)
    player5=models.CharField(max_length=20)
    player6=models.CharField(max_length=20)
    player7=models.CharField(max_length=20)
    player8=models.CharField(max_length=20)
    player9=models.CharField(max_length=20)
    player10=models.CharField(max_length=20)
    player11=models.CharField(max_length=20)
    sub1=models.CharField(max_length=20)
    sub2=models.CharField(max_length=20)
    sub3=models.CharField(max_length=20)

class fixture(models.Model):
    team1=models.CharField(max_length=30,default='a')
    team2=models.CharField(max_length=30,default='b')
    date=models.DateTimeField()
    venue=models.CharField(max_length=20,default='c')


