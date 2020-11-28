import cv2
import tensorflow as tf
import os
CATEGORIES = ['Empty','NotEmpty']
def prepare(filepath):
    IMG_SIZE = 70  # 50 in txt-based
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)
model = tf.keras.models.load_model("model.h5")
c=[]
directory = r'product_slots'
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        c.append(os.path.join(directory, filename))
    else:
        continue
    
def prediccio(path):
    stock=[]
    for path in c:
        prediction=model.predict([prepare(path)])
        stock.append(CATEGORIES[int(prediction[0][0])])
    return stock

print(prediccio('Test'))
