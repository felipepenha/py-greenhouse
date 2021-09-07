import pandera as pa
from src import data_sourcing


def test_data_sourcing_get():

    df = data_sourcing.get()

    print(df)

    schema = pa.DataFrameSchema(
        {
            "id": pa.Column(
                str,
                nullable=True,
            ),
            "x": pa.Column(
                float,
                nullable=True,
            ),
            "y": pa.Column(
                float,
                nullable=True,
            ),
        }
    )

    schema(df)
