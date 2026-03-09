import streamlit as st
import cv2
import numpy as np
import joblib
from PIL import Image

# --- Page Configuration ---
st.set_page_config(page_title="Vision Classifier | Skill Set Go", page_icon="🤖", layout="centered")

# --- Custom CSS ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .header-text { text-align: center; color: #2c3e50; font-family: 'Helvetica Neue', sans-serif; }
    .footer { text-align: center; margin-top: 50px; color: #7f8c8d; font-size: 14px; border-top: 1px solid #ddd; padding-top: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- Configuration ---
CATEGORIES = ['Cat 🐱', 'Dog 🐶'] 
IMG_SIZE = 100
CONFIDENCE_THRESHOLD = 60.0 # Adjusted for RBF probabilities

@st.cache_resource
def load_model():
    try:
        # Loading the new, highly accurate pipeline
        return joblib.load('svm_advanced_model.pkl') 
    except FileNotFoundError:
        return None

model = load_model()

# --- App Header ---
st.markdown("<h1 class='header-text'>Skill Set Go: Image Classifier 🚀</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Powered by PCA Feature Extraction & RBF Support Vector Machines.</p>", unsafe_allow_html=True)
st.divider()

if model is None:
    st.error("⚠️ Model file 'svm_advanced_model.pkl' not found. Run the Jupyter notebook to train the advanced model.")
else:
    uploaded_file = st.file_uploader("Drop your image file here...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Your Input Image")
            image = Image.open(uploaded_file)
            st.image(image, use_container_width=True, caption="Ready for analysis")

        with col2:
            st.subheader("Analysis Results")
            with st.spinner("Applying PCA and processing pixels..."):
                
                img_array = np.array(image.convert('L')) 
                resized_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                flattened_array = resized_array.flatten()
                scaled_array = flattened_array / 255.0
                features = scaled_array.reshape(1, -1) 

                probability = model.predict_proba(features)[0]
                max_prob = np.max(probability) * 100
                prediction_index = np.argmax(probability)

                if max_prob < CONFIDENCE_THRESHOLD:
                    st.warning(f"### Result: Other / Unsure 👽")
                    st.info(f"**Confidence:** {max_prob:.2f}%\n\n*(Confidence is too low to definitively classify as a cat or dog)*")
                else:
                    st.success(f"### Result: {CATEGORIES[prediction_index]}")
                    st.info(f"**Confidence:** {max_prob:.2f}%")
                    
                st.progress(int(max_prob) / 100)

# --- Footer Branding ---
st.markdown("<div class='footer'>Architected by Parth Jitendra Angare | Day 10 of 50 Days of Machine Learning</div>", unsafe_allow_html=True)