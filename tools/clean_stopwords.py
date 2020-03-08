# -*- coding: utf-8 -*-

import os

from os import path
from wordcloud import WordCloud

import argparse
parser=argparse.ArgumentParser(
    description='''remove stopwords from text (output text file) to use in wordcloud-lang generator ''',
    epilog="""------""")

parser.add_argument('--savedir', type=str, default='./tmp', help='directory to save output')
parser.add_argument('--lang', type=str, default='ru', help='language ru/en')
parser.add_argument('filepath', type=str, help='text file path to make statistics')

args=parser.parse_args()
DIRECTORY=args.savedir
DATAPATH=args.filepath
LANG=args.lang

def clean(text,lang='ru'):
    if lang=='en':
        alphabet='abcdefghijklmnopqrstuvwxyz \'ABCDEFGHIJKLMNOPQRSTUVWXYZ'        
    else:
        alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЫЭЮЯ'
    replacepuncs=''
    for c in text:
        if c not in alphabet:
            replacepuncs+=' ' 
        else:
            replacepuncs+=c
    return replacepuncs
def removeStopWords(text,STOPWORDS):
    return ' '.join([w for w in text.split() if w.lower() not in STOPWORDS])    
def getStopWords(lang):
    if lang=='en':
      f=open('data/stopwords.en')
      return f.read() 
    else:
      f=open('data/stopwords.ru')
      return f.read()

STOPWORDS=getStopWords(LANG)
 
# Read the whole text.
text = open(DATAPATH).read()
text = removeStopWords(clean(text,LANG), STOPWORDS)

with open('{}/{}'.format(DIRECTORY,'clean_output.txt'),'w') as f:
    f.write(text)
