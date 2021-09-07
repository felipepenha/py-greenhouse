import numpy as np
import pandas as pd


def get():
    """Get the data.

    ** Vanilla definition. **
    Include your own code below to import your project's data.

    Parameters
    ----------
    None

    Returns
    -------
    df: pandas dataframe

    Examples
    --------

    Raises
    ------

    Notes
    -----

    """

    df = pd.DataFrame(
        {
            "id": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
            "x": [0.0, np.nan, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            "y": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        }
    )

    return df
