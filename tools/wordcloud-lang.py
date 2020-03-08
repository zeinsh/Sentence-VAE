# -*- coding: utf-8 -*-

import os

from os import path
from wordcloud import WordCloud

import argparse
parser=argparse.ArgumentParser(
    description='''WORDCLOUD for text corpora/Russian text/''',
    epilog="""------""")

parser.add_argument('--savedir', type=str, default='./output', help='directory to save output')
parser.add_argument('--lang', type=str, default='ru', help='language ru/en')
parser.add_argument('filepath', type=str, help='text file path to make statistics')

args=parser.parse_args()
DIRECTORY=args.savedir
DATAPATH=args.filepath
LANG=args.lang

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
text = removeStopWords(text, STOPWORDS)

try:
    text = text.decode("utf-8")
except:
    text = text
# Generate a word cloud image
wordcloud = WordCloud(width=1200,height=750).generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('{}/wordcloud.png'.format(DIRECTORY))
