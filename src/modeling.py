from sklearn import preprocessing
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV


def fit_transform(train, valid, test, y_col, x_col, n_jobs=1, seed=1):
    """"""

    x_train = train[x_col].values
    x_valid = valid[x_col].values
    x_test = test[x_col].values

    le = preprocessing.LabelEncoder()

    # Trin encoder over training set
    le.fit(train[y_col].values.ravel())

    y_train = le.transform(train[y_col].values.ravel())
    y_valid = le.transform(valid[y_col].values.ravel())
    y_test = le.transform(test[y_col].values.ravel())

    # Store the grid in a dictionary
    grid = {}

    grid["max_features"] = [2, 3, 4]
    grid["max_depth"] = [2, 3, 4]
    grid["n_estimators"] = [100, 500, 1000]

    clf = RandomForestClassifier(random_state=seed)

    clf_random = RandomizedSearchCV(
        estimator=clf,
        param_distributions=grid,
        n_iter=10,
        cv=None,
        verbose=2,
        random_state=seed,
        n_jobs=n_jobs,
    )

    # Trin model over training set
    clf_random.fit(x_train, y_train.ravel())

    train_out = train.copy(deep=True)[y_col]
    valid_out = valid.copy(deep=True)[y_col]
    test_out = test.copy(deep=True)[y_col]

    train_out["actual"] = y_train
    valid_out["actual"] = y_valid
    test_out["actual"] = y_test

    # Predict
    train_out["pred"] = clf_random.predict(x_train)
    valid_out["pred"] = clf_random.predict(x_valid)
    test_out["pred"] = clf_random.predict(x_test)

    train_out["prob_0"], train_out["prob_1"], train_out["prob_2"] = np.transpose(
        clf_random.predict_proba(x_train)
    )
    valid_out["prob_0"], valid_out["prob_1"], valid_out["prob_2"] = np.transpose(
        clf_random.predict_proba(x_valid)
    )
    test_out["prob_0"], test_out["prob_1"], test_out["prob_2"] = np.transpose(
        clf_random.predict_proba(x_test)
    )

    return train_out, valid_out, test_out, clf_random.best_params_
