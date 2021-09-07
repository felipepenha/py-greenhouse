from fastapi import FastAPI
from pydantic import BaseModel

from src.modeling import VanillaModel

app = FastAPI()


class ModelIn(BaseModel):
    x: str


class ModelOut(BaseModel):
    pred: float


class ModelOutHealth(BaseModel):
    id: str


app = FastAPI()


@app.post("/health")
async def health():

    return {"id": "Healthy"}


@app.post(
    "/predict/",
    response_model=ModelOut,
)
async def root(input: ModelIn):

    X = [
        float(input.x),
    ]

    # Load your model from /models

    # Note: for saving your model, we suggest using the
    #       `joblib` python package

    # Ex:   path "/usr/app/models/"
    #       joblib.dump(self.m, path)
    #       model = joblib.load(path)

    # Vanila model always predict 0, so that
    # inputs in the training phase are arbitrary
    model = VanillaModel().fit(x=[0], y=[0])

    out_dict = {}

    out_dict["pred"] = model.predict(X)[0]

    return out_dict
