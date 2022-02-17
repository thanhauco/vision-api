from src.inference import Predictor
model = Predictor()
@app.post('/predict')
def predict(): return model.predict(None)