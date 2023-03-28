from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
sw = stopwords.words('russian')

from wordcloud import WordCloud
import matplotlib.pyplot as plt

from pymorphy2 import MorphAnalyzer
morph = MorphAnalyzer()

def get_cloud(sentence):
    # удаляем знаки пунктуации и токенизуем
    for sign in punctuation:
        sentence = sentence.replace(sign,'')
        sentence_token = word_tokenize(sentence)
    # удаляем стоп-слова и не-последовательности-букв
    for token in sentence_token:
        if token in sw:
            sentence_token.remove(token)
    for token in sentence_token:
        if token.isalpha() != True:
            sentence_token.remove(token)
    # лемматизируем, соединяем в строку
    sentence_lemmas = ''
    for token in sentence_token:
        lemma = morph.parse(token)[0].normal_form
        if lemma not in sw:
            sentence_lemmas += lemma + ' '
    sentence_lemmas = sentence_lemmas[:-1]
    cloud = WordCloud(background_color='white').generate(sentence_lemmas)
    cloud.to_file("wordcloud.png")
    
    

