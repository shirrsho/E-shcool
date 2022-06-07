
from django.conf import settings
from django.http import JsonResponse
import googlesearch
import nltk
#nltk.download('punkt')
import numpy
import tflearn
import tensorflow
import random
import pickle
import os
from bs4 import BeautifulSoup

from django.shortcuts import render
from googlesearch import search

# Create your views here.

from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
words=[]
labels=[]
docs_x=[]
docs_y=[]
model=[]
data = {
            "intents": [
                {
                "tag": "greeting",
                "patterns": [
                    "Hi",
                    "How are you",
                    "Is anyone there?",
                    "Hello",
                    "Good day",
                    "Whats up"
                ],
                "responses": [
                    "Hello!",
                    "Good to see you again!",
                    "Hi there, how can I help?"
                ],
                "context_set": ""
                },
                {
                "tag": "goodbye",
                "patterns": [
                    "cya",
                    "See you later",
                    "Goodbye",
                    "I am Leaving",
                    "Have a Good day"
                ],
                "responses": ["Sad to see you go :(", "Talk to you later", "Goodbye!"],
                "context_set": ""
                }

            ]
            }


def hello():

    #with open('C:\\Users\\Asus\\Desktop\\New folder\\myProject\\intents.json','r') as file:

    #data = json.dumps(file)

    global data
    global words
    global labels
    global training
    global output
    global docs_x
    global docs_y
    global model


    try:
        with open("data.pickle","rb") as f:
            words, labels, training, output = pickle.load(f)
    except:
        
        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                wrds = nltk.word_tokenize(pattern)
                words.extend(wrds)
                docs_x.append(wrds)
                docs_y.append(intent["tag"])

            if intent["tag"] not in labels:
                labels.append(intent["tag"])
        
        words = [stemmer.stem(w.lower()) for w in words if w not in "?"]
        words = sorted(list(set(words)))

        labels = sorted(labels)

        training = []
        output = []

        out_empty = [0 for _ in range(len(labels))]

        for x, doc in enumerate(docs_x):
            bag = []
            wrds = [stemmer.stem(w) for w in doc]

            for w in words:
                if w in wrds:
                    bag.append(1)
                else:
                    bag.append(0)
            
            output_row = out_empty[:]
            output_row[labels.index(docs_y[x])] = 1

            training.append(bag)
            output.append(output_row)

            with open("data.pickle","wb") as f:
                pickle.dump((words, labels, training, output),f)
    
    training = numpy.array(training)
    output = numpy.array(output)

    tensorflow.compat.v1.reset_default_graph()

    net = tflearn.input_data(shape=[None, len(training[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(output[0]),activation="softmax")
    net = tflearn.regression(net)

    model = tflearn.DNN(net)

    try:
        model.load("model.tflearn")

    except:
        model.fit(training,output,n_epoch=1000,batch_size=8,show_metric=True)
        model.save("model.tflearn")

def bag_of_words(s,words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w== se:
                bag[i] = 1
    return numpy.array(bag)

def initialize(input):
    global model
    global data
    hello()
    print("Start talking with the bot")
    
    inp = input
    results = model.predict([bag_of_words(inp, words)])
    print("pred: ",results)
    print("finpred: ",numpy.max(results))
    if(numpy.max(results)<0.99):
        return ""
    results_index = numpy.argmax(results)
    tag = labels[results_index]

    print(tag)
    
    for tg in data["intents"]:
        if tg['tag'] == tag:
            responses = tg['responses']
    return responses
    #print(random.choice(responses))

def chat(request):
    
    # if request.method=="POST":
    #     print(request.POST.get('message'))
    input = request.GET.get('input')
    print("input::",input)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        responses = initialize(input)
        # return JsonResponse({'seconds':random.choice(responses)},status=200)
        searchresult = search(input)
        if(responses):
            searchresult['result'] = random.choice(responses)
            searchresult['link'] = ""
        print()
        print(searchresult["result"])
        print()
        try:
            return JsonResponse({'paragraph':searchresult['result'], 'link':searchresult['link'],'url':searchresult['url']},status=200)
        except:
            return JsonResponse({'paragraph':"Sorry, Couldn't find any definitions", 'link':searchresult['link'],'url':searchresult['url']},status=200)
    return render(request, 'chatbot/chatbot.html')

import requests
def search(user_q):
    URL = "https://www.google.co.in/search?q="+user_q
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'Accept-Language': 'en-US,en'
    }
    link = ""#"https://www.google.com/"
    page = requests.get(URL, headers=headers)
    #page.content = page.content.decode('utf-8')
    soup = BeautifulSoup(page.content,'html.parser')
    result = soup.find("div",{"class": "Z0LcW"})
    print(result)
    if result is not None:
        result = result.get_text(strip=True, separator='<br/>')
    if result is None:
        result = soup.find("div",{"class":"LGOjhe"})
        #result.append("HELLO")
        print('asda:',result)
        if result is not None:
            result = result.get_text(strip=True, separator='<br/>')
    if result is None:
        result = "Sorry, couldn't find any definitions."
    for i in googlesearch.search(user_q,tld='com',num=1,stop=1,pause=1):
        link = i
        print('link: ',i)
    # if result is None:
    #     result = soup.find("h3",{"class":"H1u2de"}).get('href')#ULSxyf"})
    #     #result.append("HELLO")
    #     print('asda:',result)
    # if result is None:
    #     result = soup.find("div",{"class":"yuRUbf"})#ULSxyf"})
    #     #result.append("HELLO")
    #     print('asda:',result)

    #print(result.get_text(strip=True, separator='|'))
    #result = soup.find(class_='Z0LcW XcVN5d').get_text()
    
    return {"result":result,"link":link,"url":URL}