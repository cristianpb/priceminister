import pandas as pd
from os.path import join as op

PATH_RAW = '../data/raw'
PATH_EXTERNAL = '../data/external'


def read_data(test=False):
    """ Read train and test data
    """
    df_train = pd.read_csv(op(PATH_RAW, 'train.csv'), sep=';')
    df_test = pd.read_csv(op(PATH_RAW, 'test.csv'), sep=';')
    if test:
        return df_train, df_test
    else:
        return df_train


def get_stopwords():
    """ Get french stopwords
    """
    with open(op(PATH_EXTERNAL, 'fr-stopwords.txt')) as fp:
        stopwords = fp.read().splitlines()
    return stopwords
