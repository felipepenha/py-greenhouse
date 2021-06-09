import pandas as pd


class VanillaModel:
    def __init__(self):

        pass

    def fit(self, x, y):

        self.fitted = [0]

        return self

    def predict(self, x):

        return self.fitted * len(x)


class model:
    def __init__(self):

        pass

    def fit(self, train, y_col, x_col):

        self.m = VanillaModel.fit(x=train[x_col], y=train[y_col])

        # Save your model in /models

        # Note: for saving your model, we suggest using the
        #       `joblib` python package

        # joblib.dump(self.m, path)

        pass

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

    def transform_new(self, obs):
        """
        obs: pandas dataframe
        """

        x_obs = obs[self.x_col].values

        # Predict
        obs_out = pd.DataFrame({"pred": (self.m).predict(x_obs)})

        return obs_out
