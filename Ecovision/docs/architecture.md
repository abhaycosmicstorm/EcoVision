# EcoVision – System Architecture and Workflow

## 1. System Architecture

EcoVision follows a modular machine-learning application architecture.

```text
                    USER
                     |
                     v
              +--------------+
              |  Streamlit   |
              |  Web Interface|
              +------+-------+
                     |
                     v
              +--------------+
              | Image Upload |
              +------+-------+
                     |
                     v
              +--------------+
              | Preprocessing|
              | RGB / Resize |
              | Normalization|
              +------+-------+
                     |
                     v
              +--------------+
              | MobileNetV2  |
              | ML Classifier |
              +------+-------+
                     |
                     v
              +--------------+
              | Prediction & |
              | Confidence   |
              +------+-------+
                     |
          +----------+----------+
          |                     |
          v                     v
   +-------------+       +-------------+
   | Probability |       | Prediction  |
   | Results     |       | History     |
   +-------------+       +-------------+
                              |
                              v
                       +-------------+
                       | Analytics   |
                       +-------------+
```

## 2. Main Components

### User Interface

Streamlit provides the web interface for uploading images and displaying results.

### Image Preprocessing Module

The uploaded image is converted to RGB, resized to 224 × 224 pixels, normalized, and converted into a model-compatible array.

### Classification Module

MobileNetV2 with transfer learning is used to classify the image into six waste categories.

### Prediction Module

The system selects the class with the highest predicted probability and calculates its confidence score.

### Analytics Module

The application stores prediction history during the current session and calculates total predictions and average confidence.

### Evaluation Module

The validation dataset is used to calculate accuracy, precision, recall, F1-score, and the confusion matrix.

## 3. Process Workflow

```text
Start
  |
  v
Upload Waste Image
  |
  v
Validate Image
  |
  v
Convert to RGB
  |
  v
Resize to 224 × 224
  |
  v
Normalize Pixel Values
  |
  v
MobileNetV2 Model
  |
  v
Generate Class Probabilities
  |
  v
Select Highest Probability
  |
  v
Display Waste Category
  |
  v
Display Confidence
  |
  v
Store Prediction
  |
  v
Update Analytics
  |
  v
End
```

## 4. Training Workflow

```text
TrashNet Dataset
       |
       v
Image Preprocessing
       |
       v
Training / Validation Split
       |
       v
MobileNetV2 Transfer Learning
       |
       v
Train Classification Layers
       |
       v
Validate Model
       |
       v
Save waste_classifier.keras
```

## 5. Module Structure

| Module        | Responsibility                 |
| ------------- | ------------------------------ |
| train.py      | Train the classification model |
| predict.py    | Command-line prediction        |
| app.py        | Streamlit user interface       |
| config.py     | Store project configuration    |
| preprocess.py | Image preprocessing            |
| utils.py      | Model loading and prediction   |
| evaluate.py   | Model evaluation               |
| test_model.py | Software testing               |

## 6. Data Flow

```text
Input Image
     |
     v
Preprocessing
     |
     v
224 × 224 × 3 Image
     |
     v
MobileNetV2
     |
     v
6 Class Probabilities
     |
     v
Predicted Category
     |
     v
Confidence + Analytics
```
