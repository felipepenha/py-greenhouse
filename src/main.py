import data_sourcing
import data_splitting
import data_cleansing
from prefect import Flow, task


@task
def sourcing():

    return data_sourcing.get()


@task(nout=3)
def splitting(df):

    return data_splitting.split(df)


@task
def cleansing(df):

    return data_cleansing.clean(df)


with Flow("greenhouse") as flow:

    df = sourcing()
    s = splitting(df)

    train = s["train"]
    valid = s["valid"]
    test = s["test"]

    train = cleansing(train)
    valid = cleansing(valid)
    test = cleansing(test)

flow.run()

flow.visualize(filename="../flow/prefect_flow")
