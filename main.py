import PhotoSplitter
import google_annotate
import Prediction
import os
import time
 
estat_estanteries = [[],[],[],[],[]]

PhotoToAnalize = "resources/t485. 09.44.27.jpg" # escollim la foto a analitzar


PhotoSplitter.get_product_slots(PhotoToAnalize)

m = google_annotate.analyze_image(PhotoToAnalize[10:])

c = []
for filename in os.listdir("product_slots"):
    state = Prediction.prediccio("product_slots/%s" % filename)
    c.append(state)

print(c)

# time.sleep(4)

# for file in os.listdir("product_slots"):
#     os.remove("product_slots/%s" % file)