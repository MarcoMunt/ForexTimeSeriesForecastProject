import pickle

class Prediction:
    def __init__(self):
        self.model = pickle.load(open('./model/model.pkl', 'rb'))

    def predict(self, data):
        return self.model.predict(data)