import numpy as np
import pandas as pd
import gc

from data.read_data import read_data, get_stopwords
from models.train_model import split_train, score_function, model_ridge, model_xgb, model_ensembler
from models.predict_model import predict_test
from features.build_features import feature_extraction
from visualization.visualize import plot_roc, plot_scatter

def main():
    train, test = read_data(test=True)
    nrow_train = train.shape[0]
    y = train['Target']
    merge: pd.DataFrame = pd.concat([train, test])
    submission: pd.DataFrame = test['ID']

    del train
    del test
    gc.collect()

    stopwords = get_stopwords()

    merge_sparse, merge_ft = feature_extraction(merge, stopwords)

    X_sparse = merge_sparse[:nrow_train]
    X_ft = merge_ft[:nrow_train]
    X_test_sparse = merge_sparse[nrow_train:]
    X_test_ft = merge_ft[nrow_train:]

    ens = model_ensembler(X_sparse, X_ft, y)

    test_data_dict = {0: [X_test_sparse, X_test_sparse], 1: [X_test_ft]}
    preds = ens.predict(test_data_dict, lentest=X_test_ft.shape[0])
    preds1 = np.mean((preds[0][:,1], preds[1][:,1]),axis=0)

    predict_test(submission,preds1)

if __name__ == '__main__':
    main()
