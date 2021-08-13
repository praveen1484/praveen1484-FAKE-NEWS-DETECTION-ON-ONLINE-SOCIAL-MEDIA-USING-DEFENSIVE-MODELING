
from django.db.models import  Count, Avg
from django.shortcuts import render, redirect
from django.db.models import Count
from django.db.models import Q
import datetime


# Create your views here.
from Remote_User.models import defensive_modeling_model,ClientRegister_Model,review_Model,recommend_Model,news_accuracy_model


def serviceproviderlogin(request):
    if request.method  == "POST":
        admin = request.POST.get('username')
        password = request.POST.get('password')
        if admin == "SProvider" and password =="SProvider":
            news_accuracy_model.objects.all().delete()
            return redirect('View_Remote_Users')

    return render(request,'SProvider/serviceproviderlogin.html')


def viewtreandingquestions(request,chart_type):
    dd = {}
    pos,neu,neg =0,0,0
    poss=None
    topic = defensive_modeling_model.objects.values('ratings').annotate(dcount=Count('ratings')).order_by('-dcount')
    for t in topic:
        topics=t['ratings']
        pos_count=defensive_modeling_model.objects.filter(topics=topics).values('names').annotate(topiccount=Count('ratings'))
        poss=pos_count
        for pp in pos_count:
            senti= pp['names']
            if senti == 'positive':
                pos= pp['topiccount']
            elif senti == 'negative':
                neg = pp['topiccount']
            elif senti == 'nutral':
                neu = pp['topiccount']
        dd[topics]=[pos,neg,neu]
    return render(request,'SProvider/viewtreandingquestions.html',{'object':topic,'dd':dd,'chart_type':chart_type})

def Search_News(request): # Search
   if request.method == "POST":
        kword = request.POST.get('keyword')
        print(kword)
        obj = defensive_modeling_model.objects.all().filter(Q(news_desc__contains=kword) | Q(names__contains=kword))
        return render(request, 'SProvider/Search_News.html', {'objs': obj})
   return render(request, 'SProvider/Search_News.html')

def Fake_News(request): # Search
    sentiment='Fake News'
    f1 = 'wrongly'
    f2 = 'misinformation'
    f3 = 'misleading'
    f4 = 'falsely'
    f5 = 'fake'
    f6 = 'misguide'
    f11 = 'wrong'
    f22 = 'worst'
    f33 = 'forgery'
    f44 = 'reproduction'
    f55 = 'likeness'
    f66 = 'replicate'
    f77 = 'warning'
    f88 = 'denied'

    obj = defensive_modeling_model.objects.all().filter(
        Q(news_desc__contains=f1)| Q(news_desc__contains=f2)|Q(news_desc__contains=f3)|Q(news_desc__contains=f4)|
        Q(news_desc__contains=f5)|Q(news_desc__contains=f6)|Q(news_desc__contains=f11)|Q(news_desc__contains=f22)|
        Q(news_desc__contains=f33)|Q(news_desc__contains=f44)|Q(news_desc__contains=f55)|Q(news_desc__contains=f66)|Q(news_desc__contains=f77)|Q(news_desc__contains=f88))
    obj1 = defensive_modeling_model.objects.all()
    count = obj.count()
    count1 = obj1.count()
    accuracy = count / count1

    if accuracy != 0:
        news_accuracy_model.objects.create(names=sentiment, accuracy=accuracy)

    return render(request, 'SProvider/Fake_News.html', {'objs': obj,'count':accuracy})


def View_Positive_News(request): # Positive
     sentiment='Postive'
     f1='good'
     f2='beautiful'
     f3='fantastic'
     f4='extraordinary'
     f5='best'
     f6='healthy'
     f7 ='happy'
     f8 = 'help'
     f9='original'
     obj = defensive_modeling_model.objects.all().filter(Q(news_desc__contains=f1) | Q(news_desc__contains=f2)|Q(news_desc__contains=f3) | Q(news_desc__contains=f4)|Q(news_desc__contains=f5) | Q(news_desc__contains=f6)| Q(news_desc__contains=f7)| Q(news_desc__contains=f8)| Q(news_desc__contains=f9))

     obj1 = defensive_modeling_model.objects.all()
     count = obj.count()
     count1 = obj1.count()
     accuracy = count / count1

     if accuracy != 0:
         news_accuracy_model.objects.create(names=sentiment, accuracy=accuracy)

     return render(request, 'SProvider/View_Positive_News.html', {'objs': obj,'count':accuracy})

def Negative_News(request):
    sentiment='Negative'
    f1 = 'bad'
    f2 = 'worst'
    f3 = 'heavy'
    f4 = 'ridicules'
    f5 = 'sad'
    f6 = 'burst'
    f7 = 'unwilling'
    obj = defensive_modeling_model.objects.all().filter(Q(news_desc__contains=f1) | Q(news_desc__contains=f2) | Q(news_desc__contains=f3) | Q(news_desc__contains=f4) | Q(news_desc__contains=f5) | Q(news_desc__contains=f6)| Q(news_desc__contains=f7))

    obj1 = defensive_modeling_model.objects.all()
    count = obj.count()
    count1 = obj1.count()
    accuracy = count / count1

    if accuracy != 0:
        news_accuracy_model.objects.create(names=sentiment, accuracy=accuracy)

    return render(request, 'SProvider/Negative_News.html', {'objs': obj,'count':accuracy})


def View_Remote_Users(request):
    obj=ClientRegister_Model.objects.all()
    return render(request,'SProvider/View_Remote_Users.html',{'objects':obj})

def ViewTrendings(request):
    topic = defensive_modeling_model.objects.values('topics').annotate(dcount=Count('topics')).order_by('-dcount')
    return  render(request,'SProvider/ViewTrendings.html',{'objects':topic})

def negativechart(request,chart_type):
    dd = {}
    pos, neu, neg = 0, 0, 0
    poss = None
    topic = defensive_modeling_model.objects.values('ratings').annotate(dcount=Count('ratings')).order_by('-dcount')
    for t in topic:
        topics = t['ratings']
        pos_count = defensive_modeling_model.objects.filter(topics=topics).values('names').annotate(topiccount=Count('ratings'))
        poss = pos_count
        for pp in pos_count:
            senti = pp['names']
            if senti == 'positive':
                pos = pp['topiccount']
            elif senti == 'negative':
                neg = pp['topiccount']
            elif senti == 'nutral':
                neu = pp['topiccount']
        dd[topics] = [pos, neg, neu]
    return render(request,'SProvider/negativechart.html',{'object':topic,'dd':dd,'chart_type':chart_type})


def charts(request,chart_type):
    chart1 = news_accuracy_model.objects.values('names').annotate(dcount=Avg('accuracy'))
    return render(request,"SProvider/charts.html", {'form':chart1, 'chart_type':chart_type})

def View_News_Details(request):
    obj = defensive_modeling_model.objects.all()
    return render(request, 'SProvider/View_News_Details.html', {'list_objects': obj})

def likeschart(request,like_chart):
    charts = defensive_modeling_model.objects.values('names').annotate(dcount=Avg('news_Score'))
    return render(request,"SProvider/likeschart.html", {'form':charts, 'like_chart':like_chart})

def View_News_Accuracy(request):
    obj = news_accuracy_model.objects.all()
    return render(request, 'SProvider/View_News_Accuracy.html', {'list_objects': obj})




