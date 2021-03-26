import data_sourcing
import data_splitting
import data_preprocessing
from prefect import Flow, task

import pathlib

path = pathlib.Path(__file__).parents[1].absolute()


@task
def sourcing():

    return data_sourcing.get()


@task
def cleansing(df):

    return data_preprocessing.clean(df)


@task
def normalizing(df):

    return data_preprocessing.normalize(df)


@task(nout=3)
def splitting(df):

    return data_splitting.split(df)


# Define prefect flow
with Flow("greenhouse") as flow:

    df = sourcing()
    df = cleansing(df)
    df = normalizing(df)
    s = splitting(df)

    train = s["train"]
    valid = s["valid"]
    test = s["test"]

if __name__ == "__main__":

    # Run prefect flow
    flow.run()

    print(path)

    # Export flow as a PDF
    flow.visualize(filename="flow/prefect_flow")
