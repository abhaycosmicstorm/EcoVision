# EcoVision – UML Diagrams

## 1. Use Case Diagram

```text
                    +----------------------+
                    |       EcoVision      |
                    |                      |
User -------------->| Upload Waste Image   |
                    |         |            |
                    |         v            |
                    | Preprocess Image     |
                    |         |            |
                    |         v            |
                    | Classify Waste       |
                    |         |            |
                    |         v            |
                    | View Prediction      |
                    |         |            |
                    |         v            |
                    | View Confidence      |
                    |         |            |
                    |         v            |
                    | View Analytics       |
                    +----------------------+
```

## 2. Class Diagram

```text
+----------------------+
|       Config         |
+----------------------+
| IMG_SIZE             |
| BATCH_SIZE           |
| MODEL_PATH           |
| CLASS_NAMES          |
+----------------------+

           |
           v

+----------------------+
|     Preprocessor     |
+----------------------+
| preprocess_image()   |
+----------------------+

           |
           v

+----------------------+
|   PredictionUtils    |
+----------------------+
| load_model()         |
| predict_waste()      |
+----------------------+

           |
           v

+----------------------+
|    StreamlitApp      |
+----------------------+
| upload_image()       |
| display_result()     |
| show_analytics()     |
+----------------------+

+----------------------+
|     Evaluator        |
+----------------------+
| evaluate_model()     |
| classification_report|
| confusion_matrix     |
+----------------------+
```

## 3. Sequence Diagram

```text
User          Streamlit       Preprocessor       Model       Analytics
 |                |                |               |             |
 | Upload Image   |                |               |             |
 |--------------->|                |               |             |
 |                | Preprocess     |               |             |
 |                |--------------->|               |             |
 |                |<---------------|               |             |
 |                |                |               |             |
 |                | Send Image                     |             |
 |                |------------------------------->|             |
 |                |<-------------------------------|             |
 |                | Prediction                     |             |
 |                |---------------------------------------------->|
 |                |                                |             |
 |<---------------| Display Result                 |             |
 |                |                                |             |
```

## 4. Component Diagram

```text
+------------------+
| Streamlit UI     |
|     app.py       |
+--------+---------+
         |
         v
+------------------+
| Prediction Layer |
|    utils.py      |
+--------+---------+
         |
    +----+----+
    |         |
    v         v
+--------+ +---------+
|Preprocess| | Config |
|  .py    | |  .py   |
+--------+ +---------+
    |
    v
+------------------+
| TensorFlow/Keras |
|  MobileNetV2     |
+------------------+
         |
         v
+------------------+
| Waste Prediction |
+------------------+
```

## 5. System Interaction

The user interacts with the Streamlit interface. The application sends the uploaded image to the preprocessing module. The processed image is passed to the trained MobileNetV2 model. The prediction module returns the predicted waste category and confidence score. The result is displayed to the user and stored in the session history for analytics.
