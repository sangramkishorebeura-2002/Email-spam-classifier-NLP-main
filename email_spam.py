import streamlit as st
import pickle
import numpy as np

# Load your trained model and vectorizer



import os
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
model = pickle.load(open(model_path, 'rb'))


## model = pickle.load(open('model.pkl', 'rb'))
vectorizer_path = os.path.join(os.path.dirname(__file__), 'vectorizer.pkl')
vectorizer = pickle.load(open(vectorizer_path, 'rb'))

# Streamlit UI
st.title("📩 SMS Spam Classifier")
st.write("Enter a message below to check if it's spam or not:")

# Input box
user_input = st.text_area("Message", height=150)

# Predict button
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message to classify.")
    else:
        # Transform and predict
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)[0]
        prob = model.predict_proba(input_vector)[0][prediction]

        # Display result
        if prediction == 1:
            st.error("🚫 This message is classified as **Spam**.")
            st.markdown(f"Confidence: **{prob:.2f}** 🧠")

        else:
            st.success("✅ This message is classified as **Not Spam**.")
            st.markdown(f"Confidence: **{prob:.2f}** 🧠")
