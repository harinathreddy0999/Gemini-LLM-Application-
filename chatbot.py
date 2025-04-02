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
        inputs.append(image_data)  # Properly add image

    if not inputs:
        return "No input provided."

    response = model.generate_content(inputs)
    
    # Safely extract response text
    return response.text if hasattr(response, "text") else "No response generated."

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="Gemini Vision Chatbot",
    page_icon="🤖",
    layout="centered"
)

# --- Initialize Chat History ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Streamlit UI ---
st.title("🤖 Gemini Vision Q&A Chatbot")

# Input text field
user_text = st.text_input("Enter your question:", key="input")

# Image upload field
uploaded_image = st.file_uploader("Upload an image (optional)", type=["jpg", "jpeg", "png"])

# Submit button
if st.button("Send"):
    if user_text.strip() or uploaded_image:  # Ensure at least one input
        response = get_gemini_response(user_text, uploaded_image)

        # Store chat history
        st.session_state.chat_history.append({"user": user_text, "image": uploaded_image, "response": response})

        # Clear input field
        st.session_state["input"] = ""

        st.rerun()  # Corrected from `st.rer`
