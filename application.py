import uvicorn

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from source.entities.prediction_request import PredictionRequest

from source.handlers.sklearn import SKLearnHandler as sklearnHandler


app = FastAPI(title="Generic Python API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/predict/sklearn/")
def sklearn_model(req: PredictionRequest):
    try:
        resp = sklearnHandler(req['dataset'], req['rawModel'], req['additionalInfo'], req['additionalInfo'])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    else:
        return resp


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8002)