from PIL import Image

from utils import load_model, predict_waste


# Load trained model
model = load_model()


# Ask user for image path
image_path = input("Enter image path: ")


try:
    # Open image
    image = Image.open(image_path)

    # Make prediction
    result, confidence, probabilities = predict_waste(
        model,
        image
    )

    # Display result
    print()
    print("Predicted Waste:", result)
    print("Confidence:", round(confidence, 2), "%")

except FileNotFoundError:
    print("Error: Image file not found.")

except Exception as e:
    print("Error:", e)