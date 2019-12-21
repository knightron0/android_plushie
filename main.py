import tensorflow as tf
from tensorflow import keras

# 0 is no
# 1 is yes


def labelimg(img):
    arr = img.split('_')
    if(arr[0] == 'yes'):
        return 1
    else:
        return 0

traindir = '/home/sarthak/code/android_plushie/data/train'
testdir = '/home/sarthak/code/android_plushie/data/test'

# def create_data(x):, create data... (on the pc)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(225, 225)),
    keras.layers.Dense(500, activation='relu'), 
    keras.layers.Dense(500, activation='relu'),
    keras.layers.Dense(2, activation='softmax')
])

model.compile(optimizer='adam', loss ='sparse_categorical_crossentropy',metrics= ['accuracy'])
