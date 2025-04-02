from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini Vision Model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

def get_gemini_response(text, image):
    """Generate a response using text and/or image input."""
    inputs = []
    
    if text:
        inputs.append(text)  # Add text if provided

    if image:
        image_data = Image.open(image)  # Open image from uploaded file
        inputs.append(image_data)  # Add image if provided

    response = model.generate_content(inputs)
    return response.text

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="Gemini Vision App",
    page_icon="📊",
    layout="centered"
)

# --- Streamlit UI ---
st.header("Gemini Vision LLM Application")

# Input text field
user_text = st.text_input("Enter your question (optional):", key="input")

# Image upload field
uploaded_image = st.file_uploader("Upload an image (optional)", type=["jpg", "jpeg", "png"])

# Submit button
if st.button("Ask the Question"):
    if user_text.strip() or uploaded_image:  # Ensure at least one input
        response = get_gemini_response(user_text, uploaded_image)
        st.subheader("Response:")
        st.write(response)
    else:
        st.warning("Please enter text or upload an image before submitting.")
