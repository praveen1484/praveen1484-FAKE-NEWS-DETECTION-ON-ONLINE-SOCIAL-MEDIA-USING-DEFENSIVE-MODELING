from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

class defensive_modeling_model(models.Model):

    names = models.CharField(max_length=300)
    uname= models.CharField(max_length=300)
    gender= models.CharField(max_length=300)
    address= models.CharField(max_length=300)
    news_subject= models.CharField(max_length=300)
    news_desc= models.CharField(max_length=300)
    news_date= models.CharField(max_length=300)
    posted_country= models.CharField(max_length=300)
    posted_media= models.CharField(max_length=300)
    news_Score= models.IntegerField()
    news_group= models.CharField(max_length=300)


class review_Model(models.Model):
    uname = models.CharField(max_length=100)
    ureview = models.CharField(max_length=100)
    sanalysis = models.CharField(max_length=100)
    dt= models.CharField(max_length=300)
    tname= models.CharField(max_length=300)
    feedback = models.CharField(max_length=300)

class recommend_Model(models.Model):
    uname1 = models.CharField(max_length=100)
    pname = models.CharField(max_length=100)
    loc = models.CharField(max_length=100)
    dt= models.CharField(max_length=300)
    usefull= models.CharField(max_length=300)

class news_accuracy_model(models.Model):
      names = models.CharField(max_length=300)
      accuracy = models.CharField(max_length=300)




