import tensorflow as tf
import numpy as np

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report, confusion_matrix

from config import IMG_SIZE, BATCH_SIZE, CLASS_NAMES, MODEL_PATH


# Load trained model
model = tf.keras.models.load_model(MODEL_PATH)


# Same preprocessing and validation split used during training
datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    validation_split=0.2
)


# Load validation images
validation_data = datagen.flow_from_directory(
    "dataset",
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="validation",
    shuffle=False
)


# Get predictions
predictions = model.predict(validation_data, verbose=1)

predicted_labels = np.argmax(predictions, axis=1)
actual_labels = validation_data.classes


# Calculate accuracy
accuracy = np.mean(
    predicted_labels == actual_labels
)


print("\n===== MODEL EVALUATION =====")

print(
    "Validation Images:",
    len(actual_labels)
)

print(
    "Validation Accuracy:",
    round(accuracy * 100, 2),
    "%"
)


# Classification report
print("\n===== CLASSIFICATION REPORT =====")

print(
    classification_report(
        actual_labels,
        predicted_labels,
        target_names=CLASS_NAMES
    )
)


# Confusion matrix
print("\n===== CONFUSION MATRIX =====")

matrix = confusion_matrix(
    actual_labels,
    predicted_labels
)

print(matrix)