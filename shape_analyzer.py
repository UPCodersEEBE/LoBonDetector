
     
def check_if_object_over_square(matrix_square,object_square):
    #check horizontally
    if check_horizontally(matrix_square,object_square):
        if check_vertically(matrix_square,object_square):
            return True
    return False

def check_horizontally(matrix_square,object_square):
    if object_square[0]<matrix_square[0] and object_square[2]<matrix_square[2] and object_square[2]>matrix_square[0]:
        return True
    elif object_square[0]>matrix_square[0] and object_square[2]>matrix_square[2] and object_square[0]<matrix_square[2]:
            return True
    elif object_square[0]<matrix_square[0] and object_square[2]>matrix_square[2]:
        return True
    return False
    
def check_vertically(matrix_square,object_square):
    if object_square[1]<matrix_square[1] and object_square[3]<matrix_square[3] and object_square[3]>matrix_square[3]:
        return True
    elif object_square[1]>matrix_square[1] and object_square[3]>matrix_square[3] and object_square[1]<matrix_square[3]:
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
                        covered_fila.append(matrix_square)
                        uncovered_fila.remove(matrix_square)
        covered_matrix.append(covered_fila)
        uncovered_matrix.append(uncovered_fila)
    return covered_matrix, uncovered_matrix

def collision(matrix_square,object_square):
    return(((matrix_square[0] < object_square[2]) and (matrix_square[0] > object_square[0]) and (matrix_square[1] < object_square[3]) and (matrix_square[1] > object_square[1])) or 
           ((matrix_square[2] < object_square[2]) and (matrix_square[2] > object_square[0]) and (matrix_square[3] < object_square[3]) and (matrix_square[3] > object_square[1]))
           or ((matrix_square[0] < object_square[2]) and (matrix_square[0] > object_square[0]) and (matrix_square[3] < object_square[3]) and (matrix_square[3] > object_square[1]))
            or ((matrix_square[2] < object_square[2]) and (matrix_square[2] > object_square[0]) and (matrix_square[1] < object_square[3]) and (matrix_square[1] > object_square[1])))


def check_all_squares_collision(matrix,objects):
    covered_matrix=[]
    uncovered_matrix=[]
    for fila in matrix:
        uncovered_fila=fila.copy()
        covered_fila=[]
        for matrix_square in fila:
            for object in objects:
                object_coords=objects[object]
                object_square=(object_coords[0][0],object_coords[0][1],object_coords[2][0],object_coords[2][1])
                if collision(matrix_square,object_square):
                    if matrix_square not in covered_fila:
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


        