@app.post('/batch_predict')
def batch(imgs: list):
    return [model.predict(i) for i in imgs]