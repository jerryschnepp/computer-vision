import os
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

# Replace with your own API endpoint and key
endpoint = os.environ.get('AZURE_ENDPOINT')
subscription_key = os.environ.get('AZURE_KEY')

# Create an authenticated client
credentials = CognitiveServicesCredentials(subscription_key)
client = ComputerVisionClient(endpoint, credentials)

# Read and process the image
image_path = "static/burger.jpg"
with open(image_path, "rb") as image_file:
    result = client.analyze_image_in_stream(image_file, ["objects"])

# Check if the 'objects' attribute is present and not empty
if hasattr(result, 'objects'):
    print(f"Number of objects detected: {len(result.objects)}")
    if len(result.objects) > 0:
        print()
        print(f"Objects Detected:")
        print()
        for object in result.objects:
            print()
            print(f"Object: {object.object_property}")
            print(f"Confidence: {object.confidence}")
            print(f"Rectangle coordinates:")
            print(f"    Left: {object.rectangle.x}")
            print(f"    Top: {object.rectangle.y}")
            print(f"    Width: {object.rectangle.w}")
            print(f"    Height: {object.rectangle.h}")
            print()
    else:
        print("Objects attribute is empty.")
else:
    print("No objects attribute in the response.")
