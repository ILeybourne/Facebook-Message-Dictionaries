#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 02:22:40 2020

@author: Izzy
"""
import operator
import codecs
import string
import nltk 
import json
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize


def dataFormat(str):
    f=codecs.open("/Users/Izzy/Documents/fbMsg/"+str+"/message_1.html", 'r')
    
    htmlText = f.read()
    
    msgArray=[]
    
    divOffset = 22
    
    index = 0
    html = 1
    while(html):
        if(htmlText[index] == '<'):
            s=''
            while(htmlText[index] != '>'):
                s += htmlText[index]
                index += 1
            s += '>'
            
            if(s == '<div class="_3-96 _2let">'):
                char = htmlText[index + divOffset]
                msg = ''
                i=0
                while(char != '<'):
                    msg += char
                    i += 1
                    char = htmlText[index + divOffset + i]
    #            print(msg) 
                msg = msg.translate(str.maketrans('', '', string.punctuation))
                msg = msg.lower()
                
                text_tokens = word_tokenize(msg)
                tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
                new_tokens = []
                for token in tokens_without_sw: 
#                    print(token)
                    token = token.replace("039", "'")
                    if token == "’":
                        token = ''
#                    print(token)
                    new_tokens.append(token)
                filtered_sentence = (" ").join(new_tokens)
                
#                filtered_sentence.replace("039", "'")
#                print(filtered_sentence)
                msgArray.append(filtered_sentence)
                
                        
            
            if(s == "</html>"):
                html = 0
                index -= 1
        index += 1        
    
    diction = dict()
    for msgs in msgArray:
        dic1 = word_count(msgs)
        diction = mergeDict(diction, dic1)
        diction = dict(sorted(diction.items(), key=operator.itemgetter(1),reverse=True))
#    print(diction)
    return diction
           
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


def mergeDict(dict1, dict2):
   ''' Merge dictionaries and keep values of common keys in list'''
   dict3 = {**dict1, **dict2}
   for key, value in dict3.items():
       if key in dict1 and key in dict2:
               dict3[key] = value + dict1[key]
 
   return dict3

#a = dataFormat("Athena")
a2 = dataFormat("A")
#j = dataFormat("Jude")
#o = dataFormat("Oli")
#f = dataFormat("Felix")
#l = dataFormat("Lauren")
#i = dataFormat("India")
#d = dataFormat("Daniel")
#p = dataFormat("Patrick")
#m = dataFormat("Molly")
#pa = dataFormat("Paula")


#z = mergeDict(a, j)
#y = mergeDict(o, f)
#x = mergeDict(l, i)
#z = mergeDict(z, y)
#z = mergeDict(z, x)

print(a2)

f = open("athena2FbDict.txt", "w")
f.write(json.dumps(a2))
f.close()
       
#print(msgArray)
#print(diction)
#print(htmlText)
#print(htmlText[index])