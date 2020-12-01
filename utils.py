import tensorflow as tf
import numpy as np
import PIL

mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.load_model('saved_model')

probability_model = tf.keras.Sequential([model, 
                                         tf.keras.layers.Softmax()])

def transform_image(path):
    img = PIL.Image.open(path)
    img = img.convert('RGB')
    img = np.array(img)
    img = tf.image.rgb_to_grayscale(img, name=None)
    img = tf.convert_to_tensor(img)
    img = tf.image.resize(img, (28,28))

    return img

def get_prediction(img):
    img = (np.expand_dims(img,0))
    predictions = probability_model(img)
    
    return np.argmax(predictions)
