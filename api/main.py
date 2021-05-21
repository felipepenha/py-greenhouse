from fastapi import FastAPI
import joblib
import numpy as np

from pydantic import BaseModel

app = FastAPI()


class ModelIn(BaseModel):
    sex: str
    bill_length_mm: float
    bill_depth_mm: float
    flipper_length_mm: float
    body_mass_g: float


class ModelOut(BaseModel):
    prob_0: float
    prob_1: float
    prob_2: float
    species: int


app = FastAPI()


@app.post(
    "/predict"
    "/{sex}"
    "/{bill_length_mm}"
    "/{bill_depth_mm}"
    "/{flipper_length_mm}"
    "/{body_mass_g}",
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

    print(out_dict["prob_0"])

    out_dict["prob_0"] = out_dict["prob_0"][0]

    print(out_dict["prob_0"])

    out_dict["prob_1"] = out_dict["prob_1"][0]
    out_dict["prob_2"] = out_dict["prob_2"][0]

    print(model.predict(X))

    out_dict["species"] = model.predict(X)[0]

    print(out_dict["species"])

    return out_dict
