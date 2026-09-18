# ♻️ EcoVision – AI-Based Waste Classification System

## 📌 Overview

EcoVision is a Computer Vision-based waste classification system that uses **Deep Learning and Transfer Learning** to automatically classify waste images into six categories:

* Cardboard
* Glass
* Metal
* Paper
* Plastic
* Trash

The system uses **MobileNetV2 pretrained on ImageNet** and provides a simple **Streamlit web interface** for image classification.

---

## 🎯 Problem Statement

Improper waste segregation is a major environmental problem. Manually identifying different types of waste can be time-consuming and prone to human error.

EcoVision provides an automated image-based solution that identifies the category of a waste item and displays the prediction confidence.

---

## ✨ Features

* 📤 Upload waste images
* 🤖 AI-based waste classification
* ♻️ Six waste categories
* 📊 Prediction confidence score
* 📈 Classification probability distribution
* 📋 Prediction history
* 📊 Basic prediction analytics
* 🧪 Model evaluation
* ✅ Automated model testing
* ⚠️ Input and error handling

---

## 🧠 Machine Learning Model

### MobileNetV2 Transfer Learning

EcoVision uses **MobileNetV2**, a lightweight convolutional neural network pretrained on ImageNet.

The pretrained feature extraction layers are frozen and a custom classification head is added:

```text
Input Image
    ↓
Resize to 224 × 224
    ↓
Normalize Pixel Values
    ↓
MobileNetV2
    ↓
Global Average Pooling
    ↓
Dense Layer (128 neurons)
    ↓
Softmax Layer
    ↓
6 Waste Classes
```

### Why MobileNetV2?

MobileNetV2 was selected because it:

* Provides good image feature extraction
* Is relatively lightweight
* Requires fewer computational resources than many larger CNN architectures
* Is suitable for transfer learning
* Can be used for practical computer vision applications

---

## 📊 Dataset

The project uses the **TrashNet dataset**.

### Classes

| Class     | Description     |
| --------- | --------------- |
| Cardboard | Cardboard waste |
| Glass     | Glass waste     |
| Metal     | Metal waste     |
| Paper     | Paper waste     |
| Plastic   | Plastic waste   |
| Trash     | General trash   |

### Dataset Split

The training pipeline uses an **80/20 training-validation split**.

| Dataset    | Images |
| ---------- | -----: |
| Training   |   2024 |
| Validation |    503 |
| Total      |   2527 |

---

## 📈 Model Results

The model was trained for **5 epochs**.

| Metric                  | Result |
| ----------------------- | -----: |
| Final Training Accuracy | 97.73% |
| Validation Accuracy     | 77.73% |
| Validation Images       |    503 |

### Classification Report

| Class                | Precision |   Recall | F1-Score |
| -------------------- | --------: | -------: | -------: |
| Cardboard            |      0.89 |     0.74 |     0.81 |
| Glass                |      0.72 |     0.81 |     0.76 |
| Metal                |      0.74 |     0.85 |     0.79 |
| Paper                |      0.85 |     0.87 |     0.86 |
| Plastic              |      0.77 |     0.67 |     0.72 |
| Trash                |      0.56 |     0.52 |     0.54 |
| **Macro Average**    |  **0.75** | **0.74** | **0.75** |
| **Weighted Average** |  **0.78** | **0.78** | **0.78** |

The difference between training and validation accuracy indicates that the model has some **overfitting**, which can be addressed through additional data augmentation, fine-tuning, regularization, and more training data.

---

## 🏗️ Project Architecture

```text
                    ┌──────────────────┐
                    │    User Image    │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │  Streamlit App   │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Image Preprocess │
                    └────────┬─────────┘
                             ↓
                    ┌─────────────────
```
