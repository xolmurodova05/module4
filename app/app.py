from flask import Flask, request, jsonify
from model import load_model, make_prediction
from logging_config import setup_logger

app = Flask(__name__)
logger = setup_logger()
model = load_model()

@app.route('/predict', methods=['GET'])
def predict():
    country = request.args.get('country', default='ALL')
    try:
        prediction = make_prediction(model, country)
        logger.info(f"Prediction made for {country}: {prediction}")
        return jsonify({"country": country, "prediction": prediction})
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
