import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score


def stratified_cv(X, y, clf, folds=10, random_state=0):
    skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=1)
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


def leave_pair_out_cv(X, Y, classifier):
    """ Leave pair out cross validation as defined in this paper:
        http://www.jmlr.org/proceedings/papers/v8/airola10a/airola10a.pdf
    """
    label = Y.columns[0]
    pairs = get_all_01_pairs(Y)
    auc = []
    print("Total cross validation folds: ", len(pairs))
    for pair in pairs:
        print(".", end="")
        X_train = X[~X.index.isin(pair)]
        Y_train = Y[~Y.index.isin(pair)]
        X_test = X[X.index.isin(pair)]
        Y_test = Y[Y.index.isin(pair)]
        assert(list(X_train.index)==list(Y_train.index))
        assert(list(X_test.index)==list(Y_test.index))        
        classifier.fit(X_train, np.array(list(Y_train[label])))
        coef = classifier.coef_[0]
        Y_pred = np.matmul(X_test, coef)        
        auc.append(calc_auc_cv(Y_pred, Y_test))
    auc = float(sum(auc))/len(pairs)
    return auc


def get_all_01_pairs(Y):
    pairs = []
    label = Y.columns[0]
    zeros = Y[Y[label]==0].index
    ones = Y[Y[label]==1].index    
    for zero in zeros:
        for one in ones:
            pairs.append((zero, one))
    return pairs


def calc_auc_cv(Y_pred, Y_test):
    Y_test = list(Y_test[Y_test.columns[0]])
    assert(Y_test[1] != Y_test[0])
    if Y_test[1] > Y_test[0]:
        zero = Y_pred[0]
        one = Y_pred[1]
    else:
        zero = Y_pred[1]
        one = Y_pred[0]
    if zero == one:
        return 0.5
    elif zero < one:
        return 1
    else:
        return 0
