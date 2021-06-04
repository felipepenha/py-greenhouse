from sklearn import preprocessing
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
import joblib


class model:
    def __init__(self):

        pass

    def fit(self, train, y_col, x_col, n_jobs=1, seed=1):

        self.x_col = x_col
        self.y_col = y_col

        x_train = train[self.x_col].values

        self.le = preprocessing.LabelEncoder()

        # Trin encoder over training set
        (self.le).fit(train[self.y_col].values.ravel())

        path = "/usr/app/models/label_encoder.joblib"

        joblib.dump(self.le, path)

        y_train = (self.le).transform(train[self.y_col].values.ravel())

        # Store the grid in a dictionary
        grid = {}

        grid["max_features"] = [4, 5]
        grid["max_depth"] = [4, 5]
        grid["n_estimators"] = [50, 75, 200]

        clf = RandomForestClassifier(random_state=seed)

        self.clf_random = RandomizedSearchCV(
            estimator=clf,
            param_distributions=grid,
            n_iter=10,
            cv=None,
            verbose=2,
            random_state=seed,
            n_jobs=n_jobs,
        )

        # Train model over training set
        (self.clf_random).fit(x_train, y_train.ravel())

        path = "/usr/app/models/clf_random.joblib"

        joblib.dump(self.clf_random, path)

    def transform_sets(self, train, valid, test):

        x_train = train[self.x_col].values
        x_valid = valid[self.x_col].values
        x_test = test[self.x_col].values

        y_train = (self.le).transform(train[self.y_col].values.ravel())
        y_valid = (self.le).transform(valid[self.y_col].values.ravel())
        y_test = (self.le).transform(test[self.y_col].values.ravel())

        train_out = train.copy(deep=True)[self.y_col]
        valid_out = valid.copy(deep=True)[self.y_col]
        test_out = test.copy(deep=True)[self.y_col]

        train_out["actual"] = y_train
        valid_out["actual"] = y_valid
        test_out["actual"] = y_test

        # Predict
        train_out["pred"] = (self.clf_random).predict(x_train)
        valid_out["pred"] = (self.clf_random).predict(x_valid)
        test_out["pred"] = (self.clf_random).predict(x_test)

        train_out["prob_0"], train_out["prob_1"], train_out["prob_2"] = np.transpose(
            (self.clf_random).predict_proba(x_train)
        )
        valid_out["prob_0"], valid_out["prob_1"], valid_out["prob_2"] = np.transpose(
            (self.clf_random).predict_proba(x_valid)
        )
        test_out["prob_0"], test_out["prob_1"], test_out["prob_2"] = np.transpose(
            (self.clf_random).predict_proba(x_test)
        )

        return train_out, valid_out, test_out, (self.clf_random).best_params_

    def transform_new(self, obs):
        """
        obs: pandas dataframe
        """

        x_obs = obs[self.x_col].values

        # Predict
        obs_out = pd.DataFrame({"pred": (self.clf_random).predict(x_obs)})

        obs_out["prob_0"], obs_out["prob_1"], obs_out["prob_2"] = np.transpose(
            (self.clf_random).predict_proba(x_obs)
        )

        return obs_out
