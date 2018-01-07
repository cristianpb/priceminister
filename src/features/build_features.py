from os.path import join as op
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix, hstack
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk import word_tokenize
from gensim.models import KeyedVectors
nltk.download('punkt')

PATH_RAW = '../data/raw'
PATH_EXTERNAL = '../data/external'
PATH_MODELS = '../models/'
MAX_FEATURES_ITEM_DESCRIPTION = 40000


def to_categorical(dataset, label):
    """ Transform variable to categorical using one hot encoding
    """
    dataset[label] = dataset[label].astype('category')
    X_dummies = csr_matrix(pd.get_dummies(dataset[label],
                                          sparse=True).values)
    return X_dummies


def replace_na(dataset, labels):
    """ Fill NaN with 'na'
    """
    for label in labels:
        dataset[label].fillna(value='na', inplace=True)
    return dataset


def to_tfidf(dataset, label, stopwords):
    """ Term frequency–inverse document frequency reflect how important a word
    is to a document in a collection or corpus

    :param ngram_range: tuple containing the range of ngram sizes to use.
    """
    tv = TfidfVectorizer(max_features=MAX_FEATURES_ITEM_DESCRIPTION,
                         ngram_range=(1, 3),
                         stop_words=stopwords)
    X = tv.fit_transform(dataset[label])
    return X


def to_sparse_int(dataset, label):
    """ Transform to intiger encoding and in sparse from
    """
    return csr_matrix(dataset[label].apply(lambda x:
                                           len(x.split())).values.reshape(-1,
                                                                          1))


def stack_sparse(components):
    """ Stack sparse vectors horizontally [X_1, X_2, ..]
    """
    return hstack([i for i in components]).tocsr()


def sent2vec(s, model, stopwords):
    """ Transform a sentence into a vector using fasttext representation
    """
    words = str(s).lower()  # .decode('utf-8')
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
    """
    Transform text pandas series in array with the vector representation of the
    sentence using fasttext model
    """
    array_fasttext = np.array([sent2vec(x, model, stopwords) for x in text])
    return array_fasttext


def get_fasttext():
    """ Load fasttext french pretrained model

    https://fasttext.cc/docs/en/pretrained-vectors.html
    """
    filename = op(PATH_EXTERNAL, 'wiki.fr.bin')
    model = KeyedVectors.load_word2vec_format(filename, binary=True)
    return model


def feature_extraction(dataset, stopwords):
    """ Main function to do all feature engineering
    """
    dataset = replace_na(dataset, ['review_content', 'review_title'])
    X_dummies = to_categorical(dataset, 'review_stars')
    X_content = to_tfidf(dataset, 'review_content', stopwords)
    X_title = to_tfidf(dataset, 'review_title', stopwords)
    X_length = to_sparse_int(dataset, 'review_content')
    sparse_merge = stack_sparse([X_dummies, X_content, X_title, X_length])

    model_fasttext = get_fasttext()
    dataset_ft = get_vec(dataset['review_content'].values, model_fasttext,
                         stopwords)
    return sparse_merge, dataset_ft
