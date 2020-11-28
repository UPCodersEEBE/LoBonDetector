import io
import os
import json
# Imports the Google Cloud client library
from google.cloud import vision
from google.protobuf.json_format import MessageToJson

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "LoBonDetector-95406d06e11b.json"

def locate_objects_path(path):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()
    
    # The name of the image file to annotate
    file_name = os.path.abspath(f'resources/{path}')
    
    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    
    response=client.object_localization(image=image)
    objects = response.localized_object_annotations
    
    print('Number of objects found: {}'.format(len(objects)))
    for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))
            
    
    return objects

from PIL import Image
    
def get_num_pixels(filepath):
    width, height = Image.open(filepath).size
    return width,height
    
print (get_num_pixels("source/485. 11.55.15.jpg"))