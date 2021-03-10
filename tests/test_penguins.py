import pandera as pa
from src.main import data_sourcing


def test_import_data():

    df = data_sourcing()

    print(df)

    cats_sex = ["male", "female"]
    cats_species = ["Adelie", "Gentoo", "Chinstrap"]

    schema = pa.DataFrameSchema(
        {
            "bill_length_mm": pa.Column(float, nullable=True),
            "bill_depth_mm": pa.Column(float, nullable=True),
            "flipper_length_mm": pa.Column(float, nullable=True),
            "body_mass_g": pa.Column(float, nullable=True),
            "sex": pa.Column(str, checks=pa.Check.isin(cats_sex), nullable=True),
            "species": pa.Column(
                str, checks=pa.Check.isin(cats_species), nullable=True
            ),
        }
    )

    validated_df = schema(df)
