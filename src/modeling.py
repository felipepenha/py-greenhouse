from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
import numpy as np


def fit_transform(train, valid, test, y_col, x_col, seed=1):

    x_train = train[x_col].values
    x_valid = valid[x_col].values
    x_test = test[x_col].values

    le = preprocessing.LabelEncoder()

    # Trin encoder over training set
    le.fit(train[y_col].values.ravel())

    y_train = le.transform(train[y_col].values.ravel())
    y_valid = le.transform(valid[y_col].values.ravel())
    y_test = le.transform(test[y_col].values.ravel())

    clf = RandomForestClassifier(max_depth=3, n_estimators=300, random_state=seed)

    # Trin model over training set
    clf.fit(x_train, y_train.ravel())

    train_out = train.copy(deep=True)[y_col]
    valid_out = valid.copy(deep=True)[y_col]
    test_out = test.copy(deep=True)[y_col]

    train_out["actual"] = y_train
    valid_out["actual"] = y_valid
    test_out["actual"] = y_test

    # Predict
    train_out["pred"] = clf.predict(x_train)
    valid_out["pred"] = clf.predict(x_valid)
    test_out["pred"] = clf.predict(x_test)

    train_out["prob_0"], train_out["prob_1"], train_out["prob_2"] = np.transpose(
        clf.predict_proba(x_train)
    )
    valid_out["prob_0"], valid_out["prob_1"], valid_out["prob_2"] = np.transpose(
        clf.predict_proba(x_valid)
    )
    test_out["prob_0"], test_out["prob_1"], test_out["prob_2"] = np.transpose(
        clf.predict_proba(x_test)
    )

    return train_out, valid_out, test_out
