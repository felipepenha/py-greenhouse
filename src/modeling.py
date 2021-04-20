from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier


def fit_transform(train, valid, test, y_col, x_col, seed=1):

    x_train = train[x_col].values
    x_valid = valid[x_col].values
    x_test = test[x_col].values

    le = preprocessing.LabelEncoder()

    # Trin encoder over training set
    le.fit(train[y_col])

    y_train = le.transform(train[y_col])

    clf = RandomForestClassifier(max_depth=3, n_estimators=300, random_state=seed)

    # Trin model over training set
    clf.fit(x_train, y_train)

    # Predict
    pred_train = clf.predict(x_train)
    pred_valid = clf.predict(x_valid)
    pred_test = clf.predict(x_test)

    proba_train = clf.predict_proba(x_train)
    proba_valid = clf.predict_proba(x_valid)
    proba_test = clf.predict_proba(x_test)

    return (
        zip(proba_train, pred_train),
        zip(proba_valid, pred_valid),
        zip(proba_test, pred_test),
    )
