from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)
model = load_model(r'C:\Users\Divyanshu Dubey\OneDrive\Desktop\medicinal_plant.h5')

# Define function for preprocessing images
def preprocess_image(image_file):
    img = image.load_img(image_file, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalize pixel values to [0, 1]
    return img_array

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image file from the request
    image_file = request.files['file']
    # Preprocess the image
    image_array = preprocess_image(image_file)
    # Make prediction using the loaded model
    prediction = model.predict(image_array)
    # Get the predicted class label
    predicted_class = np.argmax(prediction)
    # Return the prediction
    return jsonify({'prediction': str(predicted_class)})

if __name__ == '__main__':
    app.run(debug=True)
