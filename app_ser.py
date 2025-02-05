# -*- coding: utf-8 -*-
"""app_ser.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NQDns_INeCRidK3pnpMAFcF3GizcEjx4
"""

import streamlit as st
import numpy as np
import librosa
import joblib
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

# Load the trained model
#model_path = '/content/saved_models/Emotion_Model_no_gender.h5'
#model = tf.keras.models.load_model(model_path)

# Load the scaler used during training
#scaler = joblib.load('scaler.pkl')

# Function to extract features from audio
def extract_features(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    return np.mean(mfcc.T, axis=0)

# Streamlit app
st.title('Speech Emotion Recognition')
st.write('Upload an audio file to predict the emotion')

# File uploader
uploaded_file = st.file_uploader("Choose an audio file...", type=["wav", "mp3"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    with open("temp_audio_file.wav", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract features
    features = extract_features("temp_audio_file.wav")

    # Scale features
    features_scaled = scaler.transform([features])

    # Expand dimensions to match model input
    features_scaled = np.expand_dims(features_scaled, axis=2)

    # Predict emotion
    prediction = model.predict(features_scaled)
    predicted_emotion = np.argmax(prediction, axis=1)

    # Mapping emotions
    emotion_map = {0: 'angry', 1: 'happy', 2: 'neutral', 3: 'sad', 4: 'surprise'}
    st.write('Predicted Emotion:', emotion_map[predicted_emotion[0]])