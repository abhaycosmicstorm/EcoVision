# ♻️ EcoVision – AI-Based Waste Classification System

## Overview

EcoVision is a computer vision-based waste classification application that identifies the category of waste from an uploaded image.

The system uses MobileNetV2 transfer learning and provides predictions through an interactive Streamlit web application.

## Features

- Upload waste images
- Automatic image preprocessing
- AI-based waste classification
- Confidence score
- Classification probabilities
- Prediction history
- Basic analytics dashboard

## Waste Categories

The system supports six categories:

1. Cardboard
2. Glass
3. Metal
4. Paper
5. Plastic
6. Trash

## Technologies

- Python
- TensorFlow
- Keras
- MobileNetV2
- NumPy
- Pandas
- Pillow
- Streamlit

## Project Structure

```text
Ecovision/
│
├── dataset/
│   ├── cardboard/
│   ├── glass/
│   ├── metal/
│   ├── paper/
│   ├── plastic/
│   └── trash/
│
├── train.py
├── predict.py
├── app.py
├── statement.md
├── README.md
└── waste_classifier.keras