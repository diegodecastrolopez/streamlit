import pandas as pd
import pickle
import os
import streamlit as st


FEATURE_ORDER = ['hit_points', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']


@st.cache_resource
def load_model():
    filepath = os.path.join("models", "random_forest.pkl")   # Set path
    with open(filepath, "rb") as f:
        return pickle.load(f)   # Load model with pickle


def predict(features):
    """
    Function to predict whether a Pokémon is Legendary or not.
    Input: dictionary with the different features and their values.
    """

    model = load_model()

    X = pd.DataFrame([features])[FEATURE_ORDER]

    y_pred = model.predict(X)[0]   # Prediction
    y_prob = model.predict_proba(X)[0][1]   # Probability of being Legendary

    return int(y_pred), float(y_prob)
