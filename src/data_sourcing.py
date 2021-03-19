import palmerpenguins


def get():
    """
    This template function uses the Palmer Peguins dataset as a place holder.
    Replace it by your own code to import your project's data.
    """

    df = palmerpenguins.load_penguins()

    cols = [
        "bill_length_mm",
        "bill_depth_mm",
        "flipper_length_mm",
        "body_mass_g",
        "sex",
        "species",
    ]

    return df[cols]
