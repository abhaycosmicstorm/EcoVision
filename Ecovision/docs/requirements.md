# EcoVision – Requirements

## 1. Functional Requirements

### FR1 – Image Upload

The system shall allow users to upload waste images in JPG, JPEG, and PNG formats.

### FR2 – Image Preprocessing

The system shall convert uploaded images to RGB format, resize them to 224 × 224 pixels, normalize pixel values, and prepare them for model prediction.

### FR3 – Waste Classification

The system shall classify an uploaded image into one of six waste categories:

* Cardboard
* Glass
* Metal
* Paper
* Plastic
* Trash

### FR4 – Confidence Score

The system shall display the confidence score associated with the predicted waste category.

### FR5 – Probability Display

The system shall display classification probabilities for all six waste categories.

### FR6 – Prediction History

The system shall maintain prediction history during the current application session.

### FR7 – Analytics

The system shall display the total number of predictions and average prediction confidence.

### FR8 – Model Evaluation

The system shall support evaluation of the trained model using validation data and generate classification metrics and a confusion matrix.

---

## 2. Non-Functional Requirements

### NFR1 – Performance

The system should provide predictions within a reasonable time on a standard computer.

### NFR2 – Usability

The Streamlit interface should be simple enough for a user to upload an image and understand the prediction easily.

### NFR3 – Reliability

The system should handle invalid image paths and prediction errors without crashing unexpectedly.

### NFR4 – Maintainability

The project should use separate modules for configuration, preprocessing, prediction, evaluation, and testing.

### NFR5 – Resource Efficiency

The system should use a lightweight transfer-learning architecture based on MobileNetV2.

### NFR6 – Error Handling

The application should provide meaningful error messages when an image cannot be loaded or processed.

### NFR7 – Scalability

The system architecture should allow additional waste categories and improved models to be added in future versions.

### NFR8 – Security

The system should process uploaded images locally during application use and should not require users to provide personal information.

### NFR9 – Portability

The project should be executable on systems with the required Python dependencies installed.

### NFR10 – Documentation

The project should contain source-code documentation, requirements, README documentation, testing information, and a final project report.
