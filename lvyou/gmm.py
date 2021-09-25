from sklearn.mixture import GaussianMixture
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
import jieba
import pandas as pd
import json
import jieba.analyse as analyse
from sklearn.decomposition import PCA
stopwords = [line.strip() for line in open('stop.txt', encoding='UTF-8').readlines()]
class Gmm_News:
    def __init__(self,data):
        self.data=data
    def read_data(self):
        self.datas = [" ".join([i for i in jieba.cut(item) if i not in stopwords]) for item in self.data]
    def transform(self):
        tfidf=TfidfVectorizer()
        self.x=tfidf.fit_transform(self.datas).todense()
        self.x=PCA(n_components=20).fit_transform(self.x)
        print(self.x)
        gmm=GaussianMixture(n_components=40)
        gmm.fit(self.x)
        print("训练完成")
        result=gmm.predict(self.x)
        self.data=pd.DataFrame({'content':self.data})
        self.data['result']=result
        self.data['clean_text']=self.datas
        self.data.to_excel('result.xlsx')
    def count_word(self):
        self.word=[]
        for i in range(40):
            data=self.data[self.data['result']==i]
            text=''
            for i in data['clean_text'].values.tolist():
                text=text+i

            keywords = analyse.extract_tags(text, topK=20, withWeight=True)
            d=[]
            for item in keywords:
                print(item[0], item[1])
                d.append(item[0])
            self.word.append(d)

        print(self.word)