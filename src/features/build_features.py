import gc
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix, hstack
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import roc_curve
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk import word_tokenize
import nltk
nltk.download('punkt')

MAX_FEATURES_ITEM_DESCRIPTION = 40000

def to_categorical(dataset, label):
    dataset[label] = dataset[label].astype('category')
    X_dummies = csr_matrix(pd.get_dummies(dataset[label],
                                          sparse=True).values)
    return X_dummies


def replace_na(dataset, labels):
    for label in labels:
        dataset[label].fillna(value='na', inplace=True)
    return dataset


def to_tfidf(dataset, label, stopwords):
    tv = TfidfVectorizer(max_features=MAX_FEATURES_ITEM_DESCRIPTION,
                         ngram_range=(1, 3),
                         stop_words=stopwords)
    X = tv.fit_transform(dataset[label])
    return X


def to_sparse_int(dataset, label):
    return csr_matrix(dataset[label].apply(lambda x:
                                           len(x.split())).values.reshape(-1,
                                                                          1))


def stack_sparse(components):
    return hstack([i for i in components]).tocsr()


def sent2vec(s, model, stopwords):
    words = str(s).lower()  #.decode('utf-8')
    words = word_tokenize(words)
    words = [w for w in words if not w in stopwords]
    words = [w for w in words if w.isalpha()]
    M = []
    for w in words:
        try:
            M.append(model[w])
        except:
            continue
    M = np.array(M)
    v = M.sum(axis=0)
    if type(v) != np.ndarray:
        return np.zeros(300)
    return v / np.sqrt((v ** 2).sum())

def get_vec(text, model, stopwords):
    array_fasttext = np.array([sent2vec(x, model, stopwords) for x in text])
    return array_fasttext
