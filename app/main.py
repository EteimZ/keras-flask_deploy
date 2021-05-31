from flask import Flask, request, jsonify

from app.utils import transform_image, get_prediction

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    # check if file is an allowed extension
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({'error': 'no file'})
        if not allowed_file(file.filename):
            return jsonify({'error': 'format not supported'})
        
        try:
            img_bytes = file
            tensor = transform_image(img_bytes)
            prediction = get_prediction(tensor)
            data = {'prediction': int(prediction)}
            return jsonify(data)
        except:
            return jsonify({'error': 'error during prediction'})
