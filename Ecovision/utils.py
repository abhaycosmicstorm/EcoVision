import tensorflow as tf
import numpy as np

from config import MODEL_PATH, CLASS_NAMES
from preprocess import preprocess_image


def load_model():
    """
    Load the trained waste classification model.
    """
    return tf.keras.models.load_model(MODEL_PATH)


def predict_waste(model, image):
    """
    Predict the waste category from an image.
    """

    # Preprocess image
    image_array = preprocess_image(image)

    # Get model predictions
    predictions = model.predict(image_array, verbose=0)

    # Find class with highest probability
    predicted_index = np.argmax(predictions[0])

    # Get predicted class
    predicted_class = CLASS_NAMES[predicted_index]

    # Calculate confidence
    confidence = predictions[0][predicted_index] * 100

    return predicted_class, confidence, predictions[0]