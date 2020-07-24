from django.shortcuts import render
import requests
from newsapi import NewsApiClient

url = 'http://newsapi.org/v2/top-headlines?'
headers = {'X-Api-Key':'bffe69c126b248aca96d06d968b0488f'}
params = {'sources':['abc-news,bbc-news,business-insider,google-news,hacker-news,natinal-geographic,techcrunch,the-hindu,the-times-of-india,the-wall-street-journal']}
response = requests.get(url,headers=headers,params=params).json()
article = response['articles']


def new(request):
    return render(request,'news/index.html',{'article':article})