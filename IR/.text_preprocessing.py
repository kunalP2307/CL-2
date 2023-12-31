# -*- coding: utf-8 -*-
"""text_preprocessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xlx0IbaI_5ZQfBjOMkVnPSRE_k65MAIs
"""

import nltk
nltk.download('punkt')

"""### **Tokenization**"""

text = "Hello Everyone, I am learning NLP Basics from Udemy Course"

"""**Sentence Tokenization**"""

sents = (sent_tokenize(text))

sents

word_tokenize(text)

words = [word_tokenize(text) for sent in sents]

words

"""### **Stop Word Removal**"""

!pip install nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

punctuation

custom_list = set(stopwords.words('english') + list(punctuation))

custom_list

word_list = [word for word in word_tokenize(text) if word not in custom_list]

word_list

"""### **N-Grams** (Bi-Grams)"""

from nltk.collocations import BigramCollocationFinder

finde = BigramCollocationFinder.from_words(word_list)

finde.ngram_fd.items()

"""### **Stemming**"""

from nltk.stem.lancaster import LancasterStemmer

new_text = "After Playing Cricket\
            She eats bananas"

l_s = LancasterStemmer()
stem_lan = [l_s.stem(word) for word in word_tokenize(new_text)]

stem_lan

"""### **Word Sense Disambiguation**"""

from nltk.corpus import wordnet

nltk.download('wordnet')
nltk.download('omw-1.4')

for ss in wordnet.synsets('mouse'):
    print(ss, ss.definition())

from nltk.wsd import lesk

context_1 = lesk(word_tokenize("Sing in a lower tone, along with the bass"), "bass")
print(conext_1, context_1.definition())

context_2 = lesk(word_tokenize("The sea bass really very hard to catch"), "bass")
print(context_2, context_2.definition())

context_3 = lesk(word_tokenize("My mouse is not working, need to change it"), "mouse")
print(context_3, context_3.definition())

"""### **Count Vectorizer**"""

import pandas as pd

sentences =  ["One of the most basic ways we can numerically represent words "
               "is through the one-hot encoding method (also sometimes called "
               "count vectorizing)."]

df = pd.DataFrame({'Text' : sentences})

df

from sklearn.feature_extraction.text import CountVectorizer

count_v = CountVectorizer()
X = count_v.fit_transform(df.Text).toarray()

count_v.get_feature_names()

X

count_v.vocabulary_

count_v = CountVectorizer(stop_words = ['of', 'the','is'])
X = count_v.fit_transform(df.Text).toarray()

X

count_v.vocabulary_

"""### **TF-IDF**"""

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
vectorizer.fit(sentences)

vectorizer.vocabulary_

vectorizer.idf_

"""### **Hashing Vectorizer**"""

from sklearn.feature_extraction.text import HashingVectorizer

df = pd.DataFrame({'Text' : sentences})

hash_v = HashingVectorizer(n_features = 9, norm = None, alternate_sign =True)

hash_v.fit_transform(df.Text).toarray()