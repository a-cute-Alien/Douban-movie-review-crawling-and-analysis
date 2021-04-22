import matplotlib.pyplot as plt
import jieba.analyse
from imageio import imread
from wordcloud import WordCloud


def showWordCloud(filename):
    with open(filename, encoding='utf-8') as f:
        mytext = f.read()
    jpg = imread(r'.\show\bird.png')
    jieba.analyse.set_stop_words(r'.\show\停用词.txt')
    result = jieba.analyse.extract_tags(mytext, topK=100, withWeight=True)
    frequencies = {}
    for each in result:
        frequencies[each[0]] = float(each[1])
    font = r'.\show\SourceHanSans-Normal.ttc'
    wordcloud = WordCloud(
        font_path=font,
        background_color='white',
        width=500,
        height=350,
        max_font_size=50,
        min_font_size=10,
        mode='RGBA',
        mask=jpg
    )
    wordcloud.generate_from_frequencies(frequencies)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
