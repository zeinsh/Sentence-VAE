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
    description='''Statistics for text corpora/Russian text/''',
    epilog="""------""")

parser.add_argument('--savedir', type=str, default='./output', help='directory to save output')
parser.add_argument('--lang', type=str, default='ru', help='language ru/en')
parser.add_argument('filepath', type=str, help='text file path to make statistics')

"""





    parser.add_argument('dir', type=str, help='path to the download directory')
    args=parser.parse_args()

    audiotype=args.audiotype
    transcriptType=args.transcripttype
    dirpath=args.dir

"""
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
def plotBarChart(transcripts,STOPWORDS, ngram=1):
    global FIGCOUNT
    freq_dict = defaultdict(int)

    for sent in transcripts:
        for word in generate_ngrams(sent,ngram):
            freq_dict[word] += 1

    fd_sorted = pd.DataFrame(sorted(freq_dict.items(), key=lambda x: x[1])[::-1])
    fd_sorted.columns = ["word", "wordcount"]
    fd_sorted.to_csv('{}/{}gram_ru.csv'.format(DIRECTORY,ngram),sep='|')
    trace0 = horizontal_bar_chart(fd_sorted.head(100), 'blue')

    plt.figure()
    plt.plot(fd_sorted['wordcount'])
    plt.ylabel('counts')
    plt.xlabel('{}-gram'.format(ngram))
    plt.grid()
    plt.title("Frequent {}-gram".format(ngram))
    FIGCOUNT=FIGCOUNT+1
    plt.savefig('{}/fig{}.png'.format(DIRECTORY,FIGCOUNT))

makeDir(DIRECTORY)
STOPWORDS=getStopWords(LANG)
transcripts=loadData(DATAPATH,LANG)



plotBarChart(transcripts,STOPWORDS,1)
plotBarChart(transcripts,STOPWORDS,2)
plotBarChart(transcripts,STOPWORDS,3)



#### Number of words in each Transcript ###########


counts=np.array([len(trans.split()) for trans in transcripts])
#f, axes = plt.subplots(3, 1, figsize=(10,20))
plt.figure(figsize=(5,10))
plt.boxplot( counts)
plt.grid()
print("Mean=",counts.mean())
print("std=",counts.std())
plt.title('number of words in each text')
plt.savefig('{}/numwords.png'.format(DIRECTORY))

#### Words Count Histogram ######

import numpy as np
import matplotlib.pyplot as plt

print("total number of words",sum(counts))

#counts[counts>40]=40


# the histogram of the data
plt.figure()
pins=max(counts)-min(counts)+1

plt.hist(counts, pins, facecolor='g')

plt.xlabel('Word Count/text')
plt.ylabel('Probability')
plt.title('Word Counts histogram')
plt.grid(True)
#plt.show()
plt.savefig('{}/histogram.png'.format(DIRECTORY))

#### number of unique words ####

words=set()
for trans in transcripts:
    words=words.union(trans.split())
print("number of unique words in Dataset",len(words))
