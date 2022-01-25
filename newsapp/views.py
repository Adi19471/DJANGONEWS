from multiprocessing import context
from django.shortcuts import render

# Create your views here.

from newsapi import NewsApiClient



def home_view(request):
    # Init
    newsapi = NewsApiClient(api_key='1b2ddf7bd71a4bbaadde54aef30aae80')
    headlines = newsapi.get_top_headlines(sources='bbc-news')
    articles  = headlines['articles']
    desc = []
    news = []
    img = []
    
    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    mylist = zip(news,desc,img)

    return render(request,"N/home.html",context = {"mylist":mylist})

    