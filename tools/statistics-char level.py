from collections import defaultdict
import seaborn as sns
import pandas as pd
import plotly.graph_objs as go
from plotly import tools
import plotly.offline as py
import os,sys, errno

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

import argparse
parser=argparse.ArgumentParser(
    description='''Statistics - char level for text corpora/Russian text/''',
    epilog="""------""")

parser.add_argument('--savedir', type=str, default='./output', help='directory to save output')
parser.add_argument('--lang', type=str, default='ru', help='language ru/en')
parser.add_argument('filepath', type=str, help='text file path to make statistics')

 
args=parser.parse_args()
FIGCOUNT=0
DIRECTORY=args.savedir
DATAPATH=args.filepath
LANG=args.lang


def plotHistogram(data):
    # the histogram of the data
    plt.figure()
    n, bins, patches = plt.hist(data, 50, density=True, facecolor='g', alpha=0.75)

    plt.xlabel('record length')
    plt.ylabel('Probability')
    plt.title('Record lengths histogram')
    plt.grid(True)
    #plt.show()
def removeStopWords(text,STOPWORDS):
    return ' '.join([w for w in text.split() if w.lower() not in STOPWORDS])    
def getStopWords(lang):
    if lang=='en':
      f=open('data/stopwords.en')
      return f.read().split()
    else:
      f=open('data/stopwords.ru')
      return f.read().split()

## custom function for ngram generation ##
def generate_ngrams(text, n_gram=1):
    token = [token for token in text.lower().split(" ") if token != "" if token not in STOPWORDS]
    ngrams = zip(*[token[i:] for i in range(n_gram)])
    return [" ".join(ngram) for ngram in ngrams]

## custom function for horizontal bar chart ##
def horizontal_bar_chart(df, color):
    trace = go.Bar(
        y=df["word"].values[::-1],
        x=df["wordcount"].values[::-1],
        showlegend=False,
        orientation = 'h',
        marker=dict(
            color=color,
        ),
    )
    return trace
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
def loadData(filepath,lang='ru'):
    f=open(filepath,'r')
    transcriptsFile=f.readlines()
    transcripts=[clean(line,lang) for line in transcriptsFile]
    return transcripts

def makeDir(directory):
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
## Get the bar chart from transcipts##
def plotBarChart(transcripts,STOPWORDS,name='' , ngram=1):
    global FIGCOUNT
    freq_dict = defaultdict(int)

    for sent in transcripts:
        for word in generate_ngrams(sent,ngram):
            freq_dict[word] += 1

    fd_sorted = pd.DataFrame(sorted(freq_dict.items(), key=lambda x: x[1])[::-1])
    fd_sorted.columns = ["word", "wordcount"]
    fd_sorted.to_csv('{}/char-{}gram_ru.csv'.format(DIRECTORY,name),sep='|')
    trace0 = horizontal_bar_chart(fd_sorted.head(100), 'blue')

    plt.figure()
    plt.plot(fd_sorted['wordcount'])
    plt.ylabel('counts')
    plt.xlabel('{}-gram'.format(name))
    plt.grid()
    plt.title("Frequent {}-gram".format(name))
    FIGCOUNT=FIGCOUNT+1
    plt.savefig('{}/char-fig{}.png'.format(DIRECTORY,FIGCOUNT))
    
makeDir(DIRECTORY)
STOPWORDS=getStopWords(LANG)
transcripts=loadData(DATAPATH,LANG)

words=(' '.join(transcripts)).lower().split()
unichar=[]
bichar=[]
trichar=[]
forchar=[]
for w in words:
    for i in range(len(w)): unichar.append(w[i])
    for i in range(1,len(w)): bichar.append(w[i-1:i+1])
    for i in range(2,len(w)): trichar.append(w[i-2:i+1])
    for i in range(3,len(w)): forchar.append(w[i-3:i+1])

plotBarChart(' '.join(unichar),STOPWORDS,name=1)
plotBarChart(' '.join(bichar),STOPWORDS,name=2)
plotBarChart(' '.join(trichar),STOPWORDS,name=3)
plotBarChart(' '.join(forchar),STOPWORDS,name=4)
