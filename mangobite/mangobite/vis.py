import io
import os

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/Rajan Sethi/Desktop/Online Courses/mangobite/mangobite/vision.json"
from google.cloud import vision
from google.cloud.vision import types
client=vision.ImageAnnotatorClient()

with io.open('C:/Users/Rajan Sethi/Desktop/crow.jpg','rb') as image_file:
    content=image_file.read()
image=types.Image(content=content)
response=client.label_detection(image=image)
labels=response.label_annotations

print("Labels:")

for label in labels:
    print(label.description)
