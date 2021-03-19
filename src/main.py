import data_sourcing
from prefect import Flow, task


@task
def sourcing():

    return data_sourcing.get()


with Flow("greenhouse") as flow:

    sourcing()

flow.run()
