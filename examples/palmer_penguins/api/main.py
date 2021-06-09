from fastapi import FastAPI
import joblib
import numpy as np

from pydantic import BaseModel

app = FastAPI()


class ModelIn(BaseModel):
    sex: str
    bill_length_mm: str
    bill_depth_mm: str
    flipper_length_mm: str
    body_mass_g: str


class ModelOut(BaseModel):
    prob_0: float
    prob_1: float
    prob_2: float
    species_code: int
    species_name: str


app = FastAPI()


@app.post(
    "/predict/",
    response_model=ModelOut,
)
async def root(input: ModelIn):

    sex_male = {"male": 1, "female": 0, "na": 0}[input.sex]

    sex_female = {"male": 0, "female": 1, "na": 0}[input.sex]

    sex_na = {"male": 0, "female": 0, "na": 1}[input.sex]

    X = [
        [
            int(sex_male),
            int(sex_female),
            int(sex_na),
            float(input.bill_length_mm),
            float(input.bill_depth_mm),
            float(input.flipper_length_mm),
            float(input.body_mass_g),
        ],
    ]

    model = joblib.load("/usr/app/models/clf_random.joblib")

    out_dict = {}

    out_dict["prob_0"], out_dict["prob_1"], out_dict["prob_2"] = np.transpose(
        model.predict_proba(X)
    )

    out_dict["prob_0"] = out_dict["prob_0"][0]

    out_dict["prob_1"] = out_dict["prob_1"][0]
    out_dict["prob_2"] = out_dict["prob_2"][0]

    encoder = joblib.load("/usr/app/models/label_encoder.joblib")

    # Recover classes
    classes = encoder.classes_

    # Enumerate classes to recover codes (integers)
    # Convert enumerate to dictionary
    map_classes = dict(enumerate(classes))

    code = model.predict(X)[0]

    out_dict["species_code"] = int(code)
    out_dict["species_name"] = map_classes[code]

    return out_dict
