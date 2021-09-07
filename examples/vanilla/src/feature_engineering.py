from feature_engine import encoding, imputation

# Note: we suggest using the below helper functions
#       for missing imputation (for numerical) and
#       one-hot-encoding (for categorical).
#       You will find most of other popular Feature
#       Engineering methods in the `feature_engine`
#       python package.


def numerical_missing_imputation(train, valid, test, cols, imputation_method="median"):
    """Missing imputation for numerical variables.

    The algorithm learns from the train set and applies transformations
    to all three input datasets: train, valid, test.

    Parameters
    ----------
    train: pandas dataframe
        Training set

    valid: pandas dataframe
        Validation set

    test: pandas dataframe
        Test set

    cols: list
        List of numerical columns

    imputation_method: string
        Desired method of imputation. Options are 'mean' and 'median'.
        Default value: 'median'.

    Returns
    -------
    list
        (train, valid, test)
        (pandas dataframe, pandas dataframe, pandas dataframe)

    Examples
    --------

    Raises
    ------

    Notes
    -----

    """

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
    """One-hot-encoding of all categories found in `cols`.

    The algorithm learns from the train set and applies transformations
    to all three input datasets: train, valid, test.

    Missing values in col lead to col_na=1

    Parameters
    ----------
    train: pandas dataframe
        Training set

    valid: pandas dataframe
        Validation set

    test: pandas dataframe
        Test set

    cols: list
        List of numerical columns

    Returns
    -------
    list
        (train, valid, test)
        (pandas dataframe, pandas dataframe, pandas dataframe)

    Examples
    --------

    Raises
    ------

    Notes
    -----

    """

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
