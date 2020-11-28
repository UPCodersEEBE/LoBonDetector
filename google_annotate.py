import io
import os
from PIL import Image
# Imports the Google Cloud client library
from google.cloud import vision

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

    
def get_dims(filepath):
    width, height = Image.open(f'resources/{filepath}').size
    dims=(width,height)
    print(dims)
    return dims
    
def map_object_to_pixels(objects, dims):
    ob={}
    i=0
    for object_ in objects:
        if filter_objects(object_.name):
            vertices=[]
            for vertex in object_.bounding_poly.normalized_vertices:
                vertices.append((vertex.x*dims[0],vertex.y*dims[1]))
            ob[object_.name+str(i)]=vertices
            i+=1
    return ob

def filter_objects(object_name):
    embotits=['Packaged goods']
    for item in embotits:
        if item in object_name:
            return False
        else:
            return True

def analyze_image(path):
    
    objects=locate_objects_path(path)
    dims=get_dims(path)
    object_dict=map_object_to_pixels(objects,dims)
    
    return object_dict

def check_if_object_over_square(matrix_square,object_square):
    #check horizontally
    if check_horizontally(matrix_square,object_square):
        if check_vertically(matrix_square,object_square):
            return True
    return False

def check_horizontally(matrix_square,object_square):
    if object_square[0]>matrix_square[0] and object_square[2]<matrix_square[2]:
        return True
    elif object_square[2]>matrix_square[0] and object_square[0]<matrix_square[2]:
        if object_square[0]>matrix_square[0] or object_square[2]<matrix_square[2]:
            #check vertically
            return True
    elif object_square[0]<matrix_square[0] and object_square[2]>matrix_square[2]:
        return True
    return False
    
def check_vertically(matrix_square,object_square):
    if object_square[1]>matrix_square[1] and object_square[3]<matrix_square[3]:
        return True
    elif object_square[3]>matrix_square[1] and object_square[1]<matrix_square[3]:
        if object_square[1]>matrix_square[1] or object_square[3]<matrix_square[3]:
            #check vertically
            return True
    elif object_square[1]<matrix_square[1] and object_square[3]>matrix_square[3]:
        return True
    return False
    
def check_all_squares(matrix,objects):
    covered_matrix=[]
    uncovered_matrix=[]
    for fila in matrix:
        uncovered_fila=fila.copy()
        covered_fila=[]
        for matrix_square in fila:
            for object in objects:
                object_coords=objects[object]
                object_square=(object_coords[0][0],object_coords[0][1],object_coords[2][0],object_coords[2][1])
                if check_if_object_over_square(matrix_square,object_square):
                    if matrix_square not in covered_fila:
                        print(object)
                        covered_fila.append(matrix_square)
                        uncovered_fila.remove(matrix_square)
        covered_matrix.append(covered_fila)
        uncovered_matrix.append(uncovered_fila)
    return covered_matrix, uncovered_matrix


def estanteries(matrix,a):
    estanteria=[]
    for fila in range(len(matrix)):
        fils=[]
        for cela in matrix[fila]:
            if cela in a[fila]:
                fils.append(1)
            else:
                fils.append(0)
        estanteria.append(fils)
    return estanteria
        
        
        
        
        
        
        
        
        
        