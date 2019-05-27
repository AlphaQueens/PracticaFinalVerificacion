from django.shortcuts import render, HttpResponse
from django.template import Template
from . import forms
#from forms import FormUserName

import argparse, sys, logging, operator, nltk, re, twitter, tweepy, numpy, datetime
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

consumer_key='n6CfA1nQ059XAMU3cJJVYEJAn'
consumer_secret='KgkiceQ2pne1kcwLguOtxhxtJpkSg0ZJ30JKBw0yMlLAjQWydx'
access_token_key='749191207-vG9JLL2whW8mlvx9HafKZzZWvi9epGiEWKWJlcox'
access_token_secret='LRt73w3ukWM9SU0jOHbxrBPcl8vVqHjIAbmljQZzxWLWA'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)


def index(request):
    form = forms.FormUserName()


    if request.method == 'POST':
        form = forms.FormUserName(request.POST)

        if form.is_valid():
            userName = form.cleaned_data['name']

            try:
                wordsCounted = run(userName)
                context = {'form':form, 'wordsCounted': wordsCounted}
                return render(request, 'page.html', context)
            except Exception as e:
                return render(request, 'error.html')

    return render(request, 'page.html', {'form':form})

def conection():
    api = tweepy.API(auth)
    if(api.user_timeline()):
        return True

def delete_bad_chars(str1):
    str1=''.join(re.sub(r'[^\w]', ' ',str1))
    return str1

def delete_numbers_from_string(str1):
    str1 = ''.join([i for i in str1 if not i.isdigit()])
    return str1

def remove_links(str1):
    return re.sub(r"http\S+", "", str1)

def delete_stop_words(str1):
    stop_words = set(stopwords.words('spanish'))
    word_tokens = word_tokenize(str1)
    str1 = ' '.join(w for w in word_tokens if not w in stop_words)
    return str1

# Calcula la frecuencia de las 10 palabras más usadas
def getFrecuency(counts, totalWords):
    individualFrecuency = []

    for x in counts:
        individualFrecuency.append((x[1]/totalWords) * 100)

    return individualFrecuency

# Devuelve las 10 palabras más usadas
def word_count(str1):
        counts = dict()
        words = str1.split()
        totalWords = 0

        for word in words:
            totalWords += 1


        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        counts=sorted(counts.items(),key=operator.itemgetter(1))
        counts.reverse()

        individualFrecuency = getFrecuency(counts[0:10],totalWords)

        counts = [(word[0], frecuency) for word, frecuency in zip(counts, individualFrecuency)]

        return counts[0:10]

# Devuelve los tweets de los últimos 7 días
def get_tweets(userName):
    api = tweepy.API(auth)
    statuses = api.user_timeline(screen_name=userName, tweet_mode='extended')
    now = datetime.datetime.now()
    tweets = []
    for s in statuses:
        if (not s.retweeted) and ('RT @' not in s.full_text):
            if(now-s.created_at).days<7:
                tweets.append(s.full_text)

    return tweets

# Busca los tweets en los que aparezcan las palabras más usadas
def findTweets(words, userName):
    dictionary=dict()
    t=[]
    tweets=get_tweets(userName)
    for i in tweets:
        t.append(i)

    for word in words:
        dictionary[word] = []
        for tweet in t:
            if word[0] in tweet:
                dictionary[word].append(tweet)

    return dictionary

# Limpia los tweets
def clean_tweets(str1):

    str1 = ''.join(str1)
    str1 = remove_links(str1)
    result = delete_bad_chars(str1)
    result = delete_numbers_from_string(result)
    result = delete_stop_words(result)
    result = word_count(result)
    return result

def run(userName):
    result = get_tweets(userName)
    result = clean_tweets(result)
    result = findTweets(result,userName)
    return result;
