from flask import Flask, request, jsonify
from src.detection import Detector

app = Flask(__name__)

# Define the inference fn() for your models
def model_inference(image):
    image, json_out = Detector('PP-YOLOE+')(image)
    return image, json_out

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image from the request
    image = request.files['image'].read()

    # Run the inference
    image, json_out = model_inference(image)

    # Return the results as JSON
    return jsonify(json_out)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=10086)