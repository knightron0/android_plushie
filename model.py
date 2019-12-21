import tensorflow as tf
from tensorflow import keras
import cv2 as cv
import numpy as np
from tensorflow.keras.models import model_from_json
from tensorflow.contrib import lite

traindir = '/home/sarthak/code/android_plushie/data/train/'
testdir = '/home/sarthak/code/android_plushie/data/test/'

trainimg = []
trainlabel = []

def createdata():
    for i in range(1, 1081):
        pthend = 'yes_' + str(i) + '.jpeg'
        fullpth = traindir + pthend
        img = cv.imread(fullpth)
        trainimg.append(img)
        trainlabel.append(1)
        # np.append(trainimg, img)
        # np.append(trainlabel, [1])
        # print(img.shape)
    for i in range(1081, 2191):
        pthend = 'no_' + str(i) + '.jpeg'
        fullpth = traindir + pthend
        img = cv.imread(fullpth)
        trainimg.append(img)
        trainlabel.append(0)
        # np.append(trainimg, img)
        # np.append(trainlabel, [0])
        
createdata()
trainimg = np.array(trainimg)
trainlabel = np.array(trainlabel)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(225, 225, 3)),
    keras.layers.Dense(500, activation='relu'), 
    keras.layers.Dense(500, activation='relu'),
    keras.layers.Dense(2, activation='softmax')
])

model.compile(optimizer='adam', loss ='sparse_categorical_crossentropy',metrics= ['accuracy'])

model.fit(trainimg, trainlabel, epochs=20)

model_file = "model.h5"
keras.models.save_model(model, model_file)

converter = tf.lite.TFLiteConverter.from_keras_model_file(model_file)
tflite_model = converter.convert()
open("finalmodel.tflite", "wb").write(tflite_model)