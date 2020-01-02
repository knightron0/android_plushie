# Image Classifier Model with Tensorflow and Keras to detect Android Plush Toys

# Data Collection and Pre-processing
A conventional dataset for Android Plushies was not readily available, so I had to collect the data manually. I simply scraped the images from a simple Google search which contained an Android Plushie in them. But these images were just 54 in number, so I used a widely known technque to expand data known as *Data Augmentation* I carried out this process with the help of **OpenCV** and **Numpy**. I generated new images using the following techniques.

- Addition of Salt and Pepper Noise
- Addition of Gaussian Noise
- Inverting Colours
- Flipping the Image
- Addition of Speckle Noise
- Conversion to Grayscale

PS: Before augmenting the data, I also resized all of the images to 225x225 pixels, to provide the network with a fixed input.

After this process, I ended up with 1080 images that contained Android Plushies. 
Now, all I had to do was to collect images that did not contain Android Plushies. For this, I recorded a small video around my house and then run the footage through **ffmpeg** which extracted the frames at a certain frame rate and ended up with around ~1110 images.
I resized all of these images to 225x225 pixels as done before and my data was ready.

# Building the Network
I used Keras with Tensorflow to build my Neural Network. It consisted of 2 hidden layers of 500 nodes each with the *Relu* activation function. The output layer used the *Softmax* activation function with converted the output to a list of probabilities of each class, in this case 2. I first created a .h5 model (using Keras) and then used the *tf.lite.TFLiteConverter* to convert it to a .tflie model.

# Training the Network
Due to a small amount of data, I ran the network through very few epochs to prevent overfitting. Using hit and trial, I decided that 20 Epochs would be the most suitable number of epochs.


PS: Due to Github's file size restriction, the data and the model is [here](https://drive.google.com/open?id=1k3lto3AvX1WPVQIDQ6lxGr3CcJxL-12k).
  
