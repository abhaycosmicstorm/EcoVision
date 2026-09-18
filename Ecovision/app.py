import streamlit as st
import pandas as pd
from PIL import Image

from utils import load_model, predict_waste
from config import CLASS_NAMES


st.set_page_config(
    page_title="EcoVision",
    page_icon="♻️",
    layout="centered"
)


# Load model
model = load_model()


# Initialize prediction history
if "history" not in st.session_state:
    st.session_state.history = []


# Title
st.title("♻️ EcoVision")
st.subheader("AI-Based Waste Classification System")

st.write(
    "Upload an image of waste and EcoVision will "
    "classify it into one of six waste categories."
)

st.divider()


# Image upload
uploaded_file = st.file_uploader(
    "📤 Upload a waste image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )


    # Make prediction
    predicted_class, confidence, probabilities = predict_waste(
        model,
        image
    )


    # Display result
    st.success(
        f"♻️ Predicted Waste: {predicted_class.upper()}"
    )

    st.metric(
        "Confidence",
        f"{confidence:.2f}%"
    )


    # Store prediction
    prediction_record = {
        "Image": uploaded_file.name,
        "Prediction": predicted_class,
        "Confidence": round(confidence, 2)
    }


    # Avoid duplicate history entries
    already_exists = False

    for record in st.session_state.history:

        if record["Image"] == uploaded_file.name:
            already_exists = True


    if not already_exists:
        st.session_state.history.append(
            prediction_record
        )


    # Classification probabilities
    st.subheader("📊 Classification Probabilities")


    for i in range(len(CLASS_NAMES)):

        probability = probabilities[i] * 100

        st.write(
            f"{CLASS_NAMES[i].capitalize()}: "
            f"{probability:.2f}%"
        )

        st.progress(
            float(probabilities[i])
        )


# Prediction history
if len(st.session_state.history) > 0:

    st.divider()

    st.subheader("📋 Prediction History")


    history_df = pd.DataFrame(
        st.session_state.history
    )

    st.dataframe(
        history_df,
        use_container_width=True
    )


    # Analytics
    st.subheader("📈 Analytics")


    total_predictions = len(
        st.session_state.history
    )

    average_confidence = history_df[
        "Confidence"
    ].mean()


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Total Predictions",
            total_predictions
        )


    with col2:

        st.metric(
            "Average Confidence",
            f"{average_confidence:.2f}%"
        )


    # Clear history
    if st.button("🗑️ Clear Prediction History"):

        st.session_state.history = []

        st.rerun()