import PhotoSplitter
import google_annotate
import Prediction
import os
import time
 
estat_estanteries = [[],[],[],[],[]]

PhotoToAnalize = "resources/t485. 12.11.00.jpg" # escollim la foto a analitzar


PhotoSplitter.get_product_slots(PhotoToAnalize)

c = []
for file in os.listdir("product_slots"):
    c.append(file)
c.sort()

# m = google_annotate.analyze_image(PhotoToAnalize)

# print(m)

# c = []



# d = []
# for i in c:
#     state = Prediction.prediccio("product_slots/%s" % i)
#     d.append(state)

print(c)
# print(d)

time.sleep(4)

for file in os.listdir("product_slots"):
    os.remove("product_slots/%s" % file)