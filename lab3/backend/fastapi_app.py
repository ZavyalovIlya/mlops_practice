from fastapi import FastAPI
from make_prediction import main as make_prediction

app = FastAPI(title="California housing")

@app.get("/")
async def app_running():
    return {"Status": "200 OK"}

@app.post("/predict/")
async def predict(X: dict):
    pred = make_prediction(X['X'])
    return {"prediction": pred}