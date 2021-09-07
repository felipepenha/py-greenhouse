def split(df, train_ratio=0.8, valid_ratio=0.1, test_ratio=0.1, seed=0):
    """Data splitting into 3 sets: train, valid, test

    train: training set. Used for training the ML model.
    valid: validation set. Used for frequent validation.
    test: test set. Used for final test.

    Parameters
    ----------
    df: pandas dataframe
        Input data

    train_ratio: float
        Amount of data that goes into training, in percentage

    valid_ratio: float
        Amount of data that goes into validation, in percentage

    test_ratio: float
        Amount of data that goes into testing, in percentage

    seed: int
        Seed for the data shuffling.
        It is important to keep it fixed throughout the tuning of the model.

    Returns
    -------
    list
        (train, valid, test)
        (pandas dataframe, pandas dataframe, pandas dataframe)

    Examples
    --------

    >>> len(data)
    100
    >>> train, valid, test = split(data)
    >>> len(train)
    80
    >>> len(valid)
    10
    >>> len(test)
    10

    Raises
    ------

    Notes
    -----

    """

    # Train set extracted from a random sample from `df`
    train = df.sample(frac=train_ratio, random_state=seed)

    # Everything from `df` except `train`
    rest = df.copy().drop(train.index)

    # Valid set ratio within `rest`
    new_ratio = valid_ratio / (valid_ratio + test_ratio)

    # Train set extracted from a random sample from `rest`
    valid = rest.sample(frac=new_ratio, random_state=seed)

    # Test set is everything in rest `except` for `valid`
    test = rest.drop(valid.index)

    return train, valid, test
