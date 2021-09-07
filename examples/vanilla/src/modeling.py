class VanillaModel:
    """Vanilla model where the predictions are always 0"""

    def __init__(self):

        pass

    def fit(self, x, y):

        self.fitted = [0]

        return self

    def predict(self, x):

        return self.fitted * len(x)


class model:
    """
    Replace below `VanillaModel` by an actual ML
    model such as the ones provided by sklearn.

    We are assuming supervised models (a and y are available),
    but you may also adapt it for unsupervised models
    (only x available). In that case, erase any reference to
    `y` below.

    References
    ----------
    https://scikit-learn.org/stable/
    """

    def __init__(self):

        pass

    def fit(self, train, y_col, x_col):

        self.x_col = x_col
        self.y_col = y_col

        self.m = VanillaModel().fit(x=train[x_col], y=train[y_col])

        # Save your model in /models

        # Note: for saving your model, we suggest using the
        #       `joblib` python package

        # Ex:   path "/usr/app/models/"
        #       joblib.dump(self.m, path)

        return self

    def transform_sets(self, train, valid, test):

        x_train = train[self.x_col].values
        x_valid = valid[self.x_col].values
        x_test = test[self.x_col].values

        y_train = train[self.y_col].values
        y_valid = valid[self.y_col].values
        y_test = test[self.y_col].values

        train_out = train.copy(deep=True)[self.y_col]
        valid_out = valid.copy(deep=True)[self.y_col]
        test_out = test.copy(deep=True)[self.y_col]

        train_out["actual"] = y_train
        valid_out["actual"] = y_valid
        test_out["actual"] = y_test

        # Predict
        train_out["pred"] = (self.m).predict(x_train)
        valid_out["pred"] = (self.m).predict(x_valid)
        test_out["pred"] = (self.m).predict(x_test)

        return train_out, valid_out, test_out
