import pandera as pa
from src.data_sourcing import get


def test_data_sourcing_get():

    df = get()

    print(df)

    cats_sex = [
        "male",
        "female",
    ]
    cats_species = [
        "Adelie",
        "Gentoo",
        "Chinstrap",
    ]

    schema = pa.DataFrameSchema(
        {
            "bill_length_mm": pa.Column(
                float,
                nullable=True,
            ),
            "bill_depth_mm": pa.Column(
                float,
                nullable=True,
            ),
            "flipper_length_mm": pa.Column(
                float,
                nullable=True,
            ),
            "body_mass_g": pa.Column(
                float,
                nullable=True,
            ),
            "sex": pa.Column(
                str,
                checks=pa.Check.isin(cats_sex),
                nullable=True,
            ),
            "species": pa.Column(
                str,
                checks=pa.Check.isin(cats_species),
                nullable=True,
            ),
        }
    )

    schema(df)
