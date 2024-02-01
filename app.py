from flask import Flask, request, jsonify, render_template
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import os

app = Flask(__name__)

# Replace with your own API endpoint and key
endpoint = "https://csc490computervision.cognitiveservices.azure.com/"
subscription_key = "a771ed310c1b4033b523b1cba351f1d4"

# Create an authenticated client
credentials = CognitiveServicesCredentials(subscription_key)
client = ComputerVisionClient(endpoint, credentials)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET'])
def analyze_image():
    image_name = request.args.get('image')
    
    if image_name:
        image_path = os.path.join('static', image_name)  # Adjust path as necessary
        with open(image_path, "rb") as image_file:
            results = client.analyze_image_in_stream(image_file, ["objects"])
            objects_detected = [{'confidence': obj.confidence, 'Object Name': obj.object_property} for obj in results.objects]
            
            return jsonify({'results': objects_detected})
    else:
        return jsonify({'error': 'No image specified'}), 400

if __name__ == '__main__':
    app.run(debug=True)
