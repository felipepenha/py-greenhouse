from feature_engine import encoding, imputation


def numerical_missing_imputation(train, valid, test, cols, imputation_method="median"):

    fe = imputation.MeanMedianImputer(
        imputation_method=imputation_method, variables=cols
    )

    # Fit over training set
    fe.fit(train[cols])

    # Apply to train, valid, test
    return (
        fe.transform(train[cols]),
        fe.transform(valid[cols]),
        fe.transform(test[cols]),
    )


def one_hot_encoding(train, valid, test, cols):

    fe = encoding.OneHotEncoder(variables=cols)

    for k in cols:
        train[k] = train[k].fillna("na")
        valid[k] = valid[k].fillna("na")
        test[k] = test[k].fillna("na")

    # Fit over training set
    fe.fit(train[cols])

    # Apply to train, valid, test
    return (
        fe.transform(train[cols]),
        fe.transform(valid[cols]),
        fe.transform(test[cols]),
    )
