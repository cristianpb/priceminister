import datetime
import pandas as pd

PATH_MODELS = '../models/'

def predict_test(submission, preds1):
    """ Create submission file from predictions
    """
    submission = pd.concat([submission,pd.Series(preds1, name='Target')],
                           axis=1)
    Date = datetime.datetime.now().strftime("%y-%m-%d")
    submission.to_csv(PATH_MODELS + 'submission_' + Date + '.csv',
                      index=False, sep=';')
