import os

from os import path
from wordcloud import WordCloud


# Read the whole text.
text = open('voxforge_transc_preprocessed.txt').read()
text = text.decode("utf-8")

# Generate a word cloud image
wordcloud = WordCloud(width=1200,height=750).generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
