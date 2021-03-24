def get(df, train_ratio=0.8, valid_ratio=0.1, test_ratio=0.1, seed=0):

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
