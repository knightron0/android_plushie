import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import model_from_json
import cv2 as cv
import numpy as np

# json_file = open('model.json', 'r')
# loaded_model_json = json_file.read()
# json_file.close()
# loaded_model = model_from_json(loaded_model_json)
# loaded_model.load_weights("model.h5")
# print("Loaded model from disk")
 
# loaded_model.compile(optimizer='adam', loss ='sparse_categorical_crossentropy',metrics= ['accuracy'])

# dirpath = '/home/sarthak/code/android_plushie/data/test/'
# tests = []
# for i in range(1, 9):
#     end = str(i) + '.jpeg'
#     fullpth = dirpath + end
#     img = cv.imread(fullpth)
#     tests.append(img)
# tests = np.array(tests)

# prediction = loaded_model.predict(tests)
# for i in range(0, len(prediction)):
#     print(np.argmax(prediction[i]))

# converter = tf.lite.TFLiteConverter.from_keras_model(loaded_model)
# tflite_model = converter.convert()

# open("finalmodel.tflite", "w").write(tflite_model)

converter = tf.lite.TFLiteConverter.from_keras_model_file('model.h5')
tflite_model = converter.convert()

open("finalmodel.tflite", "wb").write(tflite_model)