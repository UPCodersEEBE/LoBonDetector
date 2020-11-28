import PhotoSplitter
import google_annotate
import os
import time
 

PhotoToAnalize = "resources/1.jpg" # escollim la foto a analitzar



PhotoSplitter.get_product_slots(PhotoToAnalize)

print(google_annotate.analyze_image("1.jpg"))

time.sleep(4)

for file in os.listdir("product_slots"):
    os.remove("product_slots/%s" % file)
