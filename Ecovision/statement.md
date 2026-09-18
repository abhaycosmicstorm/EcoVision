# EcoVision – AI-Based Waste Classification System

## 1. Problem Statement

Improper waste segregation is a major environmental problem. Manually identifying and separating different types of waste can be time-consuming and prone to human error.

EcoVision is a computer vision-based waste classification system that uses an image of a waste item and automatically classifies it into one of six categories: cardboard, glass, metal, paper, plastic, or trash.

The system uses a transfer learning approach with MobileNetV2 to perform image classification.

## 2. Scope

The project focuses on image-based classification of common household waste.

The system accepts JPG, JPEG, and PNG images and provides the predicted waste category along with a confidence score.

The current version supports six categories:

- Cardboard
- Glass
- Metal
- Paper
- Plastic
- Trash

## 3. Target Users

The system can be useful for:

- Students learning computer vision
- Educational institutions
- Waste management awareness programs
- Environmental projects
- Individuals interested in waste segregation
- Developers experimenting with image classification

## 4. High-Level Features

### Image Upload
Users can upload a waste image through the Streamlit interface.

### Image Preprocessing
The uploaded image is converted to RGB, resized to 224 × 224 pixels, and normalized.

### Waste Classification
MobileNetV2 with transfer learning classifies the image into one of six waste categories.

### Confidence Score
The application displays the predicted category and model confidence.

### Classification Probabilities
The application displays probability values for all six categories.

### Prediction History
The application maintains a session-based history of previous predictions.

### Analytics
The application displays total predictions and average prediction confidence.

## 5. Technologies Used

- Python
- TensorFlow
- Keras
- MobileNetV2
- OpenCV
- NumPy
- Pillow
- Pandas
- Streamlit
- Git/GitHub

## 6. Expected Input

An image containing a waste item.

Supported formats:

- JPG
- JPEG
- PNG

## 7. Expected Output

The system provides:

- Predicted waste category
- Confidence percentage
- Probability of each supported category
- Prediction history
- Basic prediction analytics