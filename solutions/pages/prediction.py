import streamlit as st

from predict import predict

st.title("⚡️ Is my Pokémon legendary??")
st.write("")

st.subheader("Enter Pokémon Stats")

# Three columns, one input style each, to compare how the widgets feel.
col1, col2, col3 = st.columns(3)

with col1:
    # number_input enforces the range itself, so no validation is needed.
    attack = st.number_input('Attack', min_value=1, max_value=255, value=80, step=5)
    sp_attack = st.number_input("Special Attack", min_value=1, max_value=255, value=75, step=5)

with col2:
    # slider also enforces the range and shows it at a glance.
    defense = st.slider('Defense', min_value=1, max_value=255, value=80)
    sp_defense = st.slider("Special Defense", min_value=20, max_value=255, value=75)

with col3:
    # text_input returns a string and enforces nothing, so every value has to be
    # parsed and clamped by hand. This is why a numeric widget is the better fit.
    hp_str = st.text_input('Hit points', '70')
    try:
        hit_points = int(hp_str)
        if hit_points > 255:
            st.warning("HP cannot exceed 255. Setting to 255.")
            hit_points = 255
        elif hit_points < 1:
            st.warning("HP must be at least 1. Setting to 1.")
            hit_points = 1
    except ValueError:
        st.warning("Please enter a valid integer for HP.")
        hit_points = 70

    speed_str = st.text_input("Speed", "10")
    try:
        speed = int(speed_str)
        if speed > 255:
            st.warning("Speed cannot exceed 255. Setting to 255.")
            speed = 255
        elif speed < 5:
            st.warning("Speed must be at least 5. Setting to 5.")
            speed = 5
    except ValueError:
        st.warning("Please enter a valid integer for the speed.")
        speed = 10

# Shown to demonstrate the widget. The uploaded file is not used for the prediction.
st.subheader("Or upload a CSV file")
uploaded_file = st.file_uploader("Upload a CSV with Pokémon stats", type="csv")

# Without the button the prediction would rerun on every keystroke.
if st.button('Predict!'):
    features = {
        "hit_points": hit_points,
        "attack": attack,
        "defense": defense,
        "sp_attack": sp_attack,
        "sp_defense": sp_defense,
        "speed": speed
    }

    # predict() returns the class and the probability of the positive class.
    y_pred, y_prob = predict(features)

    if y_pred == 1:
        st.success(f"✅ This Pokémon is **Legendary**! (prob = {y_prob:.2%})")
        st.balloons()
    else:
        st.error(f"❌ This Pokémon is **Not Legendary** (prob = {y_prob:.2%})")
        st.snow()

# Shown to demonstrate the widget. There is no real file to download.
st.sidebar.download_button("Download prediction", data="", file_name="prediction.csv")
