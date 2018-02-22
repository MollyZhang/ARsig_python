import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score


def stratified_cv(X, y, clf, folds=10, random_state=0):
    skf = StratifiedKFold(n_splits=folds, 
                          shuffle=True, random_state=random_state)
    skf.get_n_splits(X, y)
    result_df = pd.DataFrame()
    fold_num = 0
    genes_used = []
    for train_idx, test_idx in skf.split(X, y):
        fold_num += 1
        print(fold_num, end=",")
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        test_auc = roc_auc_score(y_test, y_pred)
        train_auc = roc_auc_score(y_train, clf.predict(X_train))
        result_df.loc["train AUC", fold_num] = train_auc
        result_df.loc["test AUC", fold_num] = test_auc
    return result_df


def leave_pair_out_cv(X, y, classifier):
    """ Leave pair out cross validation as defined in this paper:
        http://www.jmlr.org/proceedings/papers/v8/airola10a/airola10a.pdf
    """
    folds = get_all_01_pairs(y)
    auc = []
    print("Total cross validation folds: ", len(folds))
    for fold in folds:
        print(".", end="")
        X_train = X[fold["train"]]
        y_train = y[fold["train"]]
        X_test = X[fold["test"]]
        y_test = y[fold["test"]]
        classifier.fit(X_train, y_train)
        y_pred = classifier.predict(X_test)
        auc.append(calc_auc_cv(y_pred, y_test))
    auc = float(sum(auc))/len(folds)
    return auc


def get_all_01_pairs(y):
    folds = []
    zeros = np.arange(y.shape[0])[y==0]
    ones = np.arange(y.shape[0])[y==1]
    y_idx = np.arange(y.shape[0])
    for zero in zeros:
        for one in ones:
            folds.append({"train": y_idx[[i for i in y_idx if i not in (zero, one)]], 
                          "test": np.array([zero, one])})
    return folds


def calc_auc_cv(y_pred, y_test):
    assert(y_test[1] == 1)
    assert(y_test[0] == 0)
    zero = y_pred[0]
    one = y_pred[1]
    if zero == one:
        return 0.5
    elif zero < one:
        return 1
    else:
        return 0
