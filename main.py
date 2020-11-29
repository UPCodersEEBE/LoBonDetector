import PhotoSplitter
import google_annotate
import Prediction
import os
import time
 
estat_estanteries = [[],[],[],[],[]]

PhotoToAnalize = "resources/t485. 09.44.27.jpg" # escollim la foto a analitzar


PhotoSplitter.get_product_slots(PhotoToAnalize)

c = []
for file in os.listdir("product_slots"):
    c.append(file)
c.sort()

m = google_annotate.analyze_image(PhotoToAnalize)


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


for i in estat_estanteries:
    print(i)

for file in os.listdir("product_slots"):
    os.remove("product_slots/%s" % file)