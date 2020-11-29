import os

import PhotoSplitter
import Prediction
from image_modifier import analyze_image
 
def compta_buits(final_state):
    buits=0
    for fila in final_state:
        for item in fila:
            if item==0:
                buits+=1
    return buits
    
def complete_function(PhotoToAnalize):
    estat_estanteries = [[],[],[],[],[]]
    PhotoSplitter.get_product_slots(PhotoToAnalize)

    c = []
    for file in os.listdir("product_slots"):
        c.append(file)
    c.sort()

    m = analyze_image(PhotoToAnalize)
    x = 0
    f = 0
    for i in m:
        for j in i:
            if j == 1:
                estat_estanteries[f].append("X")
            else:
                estat_estanteries[f].append(Prediction.prediccio("product_slots/%s" % c[x]))
            x += 1
        f +=1
    for file in os.listdir("product_slots"):
        os.remove("product_slots/%s" % file)
    return(estat_estanteries)
