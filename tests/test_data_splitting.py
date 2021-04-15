from src import data_splitting
import pandas as pd
import pytest


@pytest.fixture
def df_10_rows():

    return pd.DataFrame(
        {
            "col_1": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            "col_2": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
        }
    )


def test_data_splitting_train_ratio(df_10_rows):

    train, valid, test = data_splitting.split(
        df_10_rows, train_ratio=0.7, valid_ratio=0.2, test_ratio=0.1, seed=0
    )

    assert len(train) == 7


def test_data_splitting_valid_ratio(df_10_rows):

    train, valid, test = data_splitting.split(
        df_10_rows, train_ratio=0.7, valid_ratio=0.2, test_ratio=0.1, seed=0
    )

    assert len(valid) == 2


def test_data_splitting_test_ratio(df_10_rows):

    train, valid, test = data_splitting.split(
        df_10_rows, train_ratio=0.7, valid_ratio=0.2, test_ratio=0.1, seed=0
    )

    assert len(test) == 1


def test_data_splitting_train_vs_valid(df_10_rows):

    train, valid, test = data_splitting.split(
        df_10_rows, train_ratio=0.7, valid_ratio=0.2, test_ratio=0.1, seed=0
    )

    df_check = train.merge(
        valid,
        how="inner",
        right_on=["col_1", "col_2"],
        left_on=["col_1", "col_2"],
        sort=False,
    )

    assert df_check.empty


def test_data_splitting_train_vs_test(df_10_rows):

    train, valid, test = data_splitting.split(
        df_10_rows, train_ratio=0.7, valid_ratio=0.2, test_ratio=0.1, seed=0
    )

    df_check = train.merge(
        test,
        how="inner",
        right_on=["col_1", "col_2"],
        left_on=["col_1", "col_2"],
        sort=False,
    )

    assert df_check.empty


def test_data_splitting_valid_vs_test(df_10_rows):

    train, valid, test = data_splitting.split(
        df_10_rows, train_ratio=0.7, valid_ratio=0.2, test_ratio=0.1, seed=0
    )

    df_check = valid.merge(
        test,
        how="inner",
        right_on=["col_1", "col_2"],
        left_on=["col_1", "col_2"],
        sort=False,
    )

    assert df_check.empty
