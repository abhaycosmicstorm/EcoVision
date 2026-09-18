import numpy as np
from PIL import Image
from config import IMG_SIZE


def preprocess_image(image):
    """
    Convert an image into the format required by the model.
    """

    # Convert image to RGB
    image = image.convert("RGB")

    # Resize image
    image = image.resize((IMG_SIZE, IMG_SIZE))

    # Convert image to NumPy array
    image = np.array(image)

    # Normalize pixel values
    image = image / 255.0

    # Add batch dimension
    image = np.expand_dims(image, axis=0)

    return image