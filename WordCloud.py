# -*- encoding:utf-8 -*-
import jieba.analyse

from scipy.misc import imread
import matplotlib as mpl 
import matplotlib.pyplot as plt 
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import glob

def MergeTxt(filepath,outfile):
    txt_filenames = glob.glob(filepath + '/*.txt')
    for file in txt_filenames:
        txt_file = open(file, 'r')
        buf = txt_file.read()  # the context of txt file saved to buf
        with open(outfile,'a') as f:
            f.write(str(buf) + '\n')
        txt_file.close()

if __name__ == "__main__":

    filepath = "/Users/xunuo/Desktop/crawler/数据备份"
    outfile = "summary.txt"
    MergeTxt(filepath, outfile)


    mpl.rcParams['font.sans-serif'] = ['FangSong']


    content = open("summary.txt","rb").read()
    print(type(content))

    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=False)
    text =" ".join(tags)
    text = str(text)


    wc = WordCloud(font_path='simsun.ttc',
            background_color="white", max_words=100, mask = None,
            max_font_size=40, random_state=42)

    # generate word cloud 
    wc.generate(text)



    plt.imshow(wc)
    plt.axis("off")
    plt.savefig('test.png',dpi = 600)
    plt.show()

