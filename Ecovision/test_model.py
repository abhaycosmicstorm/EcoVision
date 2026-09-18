import os
import tensorflow as tf
from PIL import Image

from config import MODEL_PATH, CLASS_NAMES
from preprocess import preprocess_image
from utils import predict_waste


print("===== ECOVISION MODEL TESTING =====")


# Test 1: Check model file
print("\nTest 1: Checking model file...")

if os.path.exists(MODEL_PATH):
    print("PASS - Model file exists.")
else:
    print("FAIL - Model file not found.")


# Test 2: Load model
print("\nTest 2: Loading model...")

try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("PASS - Model loaded successfully.")
except Exception as e:
    print("FAIL - Model could not be loaded.")
    print(e)
    exit()


# Test 3: Check output classes
print("\nTest 3: Checking output classes...")

output_classes = model.output_shape[-1]

if output_classes == len(CLASS_NAMES):
    print("PASS - Model has 6 output classes.")
else:
    print("FAIL - Incorrect number of output classes.")


# Test 4: Test image preprocessing
print("\nTest 4: Testing image preprocessing...")

try:
    test_image = Image.new("RGB", (224, 224), "white")

    processed_image = preprocess_image(test_image)

    if processed_image.shape == (1, 224, 224, 3):
        print("PASS - Image preprocessing works.")
    else:
        print("FAIL - Incorrect processed image shape.")

except Exception as e:
    print("FAIL - Image preprocessing failed.")
    print(e)


# Test 5: Test prediction
print("\nTest 5: Testing prediction...")

try:
    predicted_class, confidence, probabilities = predict_waste(
        model,
        test_image
    )

    if predicted_class in CLASS_NAMES:
        print("PASS - Prediction returned a valid class.")
        print("Predicted class:", predicted_class)
        print("Confidence:", round(confidence, 2), "%")
    else:
        print("FAIL - Invalid predicted class.")

except Exception as e:
    print("FAIL - Prediction failed.")
    print(e)


print("\n===== TESTING COMPLETED =====")