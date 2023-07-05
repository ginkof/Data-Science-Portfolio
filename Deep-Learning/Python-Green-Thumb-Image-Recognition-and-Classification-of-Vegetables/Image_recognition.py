import tensorflow as tf
import tensorflow_hub as hub
from tensorflow.keras.models import load_model
# import cv2 as cv
import PIL.Image as Image
import numpy as np




# # Upload our DL model
# model = load_model("model_grayscale_10_8c.h5")

# Define the custom objects dictionary
custom_objects = {'KerasLayer': hub.KerasLayer}

#Load the model using the custom objects
model = tf.keras.models.load_model(
    'models/inception_16cl_40ep.h5', custom_objects=custom_objects)


class_names_4 = ['carrot', 'onion', 'potato', 'tomato']
class_names_16 = ['cabbage','capsicum','carrot','cauliflower','chilli pepper','cucumber','eggplant','garlic','ginger','lettuce','onion','peas','potato','spinach','sweetcorn','tomato']


# #Defining picture size 
# img_height = 244
# img_width = 244



def preprocess_image(image_path):
    image = Image.open(image_path).convert('RGB')  # Open image in RGB format
    # Resize the image to match the model's input size
    image = image.resize((224, 224))
    image_array = tf.keras.preprocessing.image.img_to_array(
        image)  # Convert image to numpy array
    image_array = image_array / 255.0  # Normalize image array
    return image_array


def predict_picture(image_path, model):
    preprocessed_image = preprocess_image(image_path)
    preprocessed_image = tf.expand_dims(
        preprocessed_image, axis=0)  # Add batch dimension
    predictions = model.predict(preprocessed_image)
    predicted_class = tf.argmax(predictions[0]).numpy()
    predicted_class_name = class_names_16[predicted_class]
    return predicted_class_name