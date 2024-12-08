from wordcloud import WordCloud, STOPWORDS , ImageColorGenerator
import pandas as pd
import matplotlib.pylab as plt
from PIL import Image
import numpy as np

stopwords = set(STOPWORDS)
mask = np.array(Image.open('sar.png'))
data_file = pd.read_csv('text.csv')
wordcloud = WordCloud(stopwords = stopwords , width=1200 , height=1000,mask=mask,background_color="black",colormap="Set3").generate(''.join(data_file['text']))

background_image = Image.open('back6.jpg')
background_array = np.array(background_image)


plt.figure(figsize=(10, 9))
plt.imshow(background_array, interpolation='bilinear')
plt.imshow(wordcloud, interpolation='bilinear', alpha=0.7)
plt.axis('off')
plt.show()
