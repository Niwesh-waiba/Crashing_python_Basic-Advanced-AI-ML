from fast_api import FastAPI, HTTPExeption
from pydantic import BaseModel,conlist
import joblib

#initialize FastAPI app
app = FastAPI()

#load the trained model 
model=joblib.load('iris_logistic_regression.pkl')

#Define request model
class Features(BaseModel):
    Features: conlist(float,min_length=4,max_length=4)   #ensure the features list has exactly 4 float values

#define a route for the prediction API
@app.post('/predict')
def predict(data:Features):
    try:
        #predict using the model
        prediction=model;.predict([data.Features])
        return {'prediction': int(prediction[0])}
    except Exception as e:
        #handle errors during prediction
        raise HTTPExeption(status_code=500,detail=str(e))
    