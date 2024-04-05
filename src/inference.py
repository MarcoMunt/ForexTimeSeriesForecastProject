from prediction import Prediction
from flask import Flask, request, jsonify

app = Flask(__name__)

model = Prediction()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    data = data['data']
    prediction = model.predict([data]).tolist()
    return jsonify(prediction=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)