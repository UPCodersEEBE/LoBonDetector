import io
import os
# Imports the Google Cloud client library
from google.cloud import vision

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "LoBonDetector-95406d06e11b.json"

def locate_objects_path(path):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()
    
    # The name of the image file to annotate
    file_name = os.path.abspath(path)
    
    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    
    response=client.object_localization(image=image)
    objects = response.localized_object_annotations
    
    return objects

    
        
        
        
        
        