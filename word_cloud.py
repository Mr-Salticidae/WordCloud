from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
import numpy as np

def read_file(csv_file='texts.json'):
    print('Please enter the name of the file you want to build a word cloud.\n')
    csv_file_name = input()
    if len(csv_file_name) > 0:
        csv_file = csv_file_name
    try:
        df = pd.read_json(csv_file)
        return df
    except:
        print('There is no file called ' + csv_file + ' in this folder, try again.')
        read_file()

def get_mask(mask='china_map.jpg'):
    mask_name = input('Please enter the name of the mask. The default is a China map.\n')
    if len(mask_name) > 0:
        mask = mask_name
    try:
        mask = np.array(Image.open(mask))
        return mask
    except:
        print('There is no picture called ' + mask_name + ', try again.')
        get_mask()
        

def get_font(font='LoveIsEasy.otf'):
    font_name = input('Please enter the name of the font. The default font is Love is Easy.\n')
    if len(font_name) > 0:
        font = font_name
    try:
        return font
    except:
        print('There is no font called ' + font + ', try again.')
        get_font()

def get_file_name(name='word cloud'):
    file_name = input('Please enter the name of the World Cloud Image.\n')
    if len(file_name) > 0:
        name = file_name
    return name


df = read_file()
# mask = get_mask()
# font = get_font()
name = get_file_name()

comment_words = ''
stopwords = set(STOPWORDS)

for val in df.iloc[:, 0]:
    val = str(val)
    tokens = val.split()
    
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
    
    comment_words += ' '.join(tokens) + ' '

wordcloud = WordCloud(width=1000, height=500, stopwords=stopwords, background_color='white').generate(comment_words)

plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)

plt.savefig(fname=name)