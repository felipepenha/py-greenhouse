from fastapi import FastAPI
import joblib

from pydantic import BaseModel

app = FastAPI()


class ModelIn(BaseModel):
    id: int
    x: float
    y: float


class ModelOut(BaseModel):
    id: int
    x: float
    y: float
    pred: float


app = FastAPI()


@app.post(
    "/predict/",
    response_model=ModelOut,
)
async def root(input: ModelIn):

    X = [
        [
            float(input.x),
        ],
    ]

    model = joblib.load("/usr/app/models/model.joblib")

    out_dict = {}

    out_dict["pred"] = model.predict(X)[0]

    return out_dict
