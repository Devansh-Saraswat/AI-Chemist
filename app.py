# AI Chemist App
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Load all environment variables
load_dotenv()

# Configure the Generative AI API with your API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Pro Vision API and get a response
def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    """
    Checks if a file has been uploaded and processes it.
    Args:
        uploaded_file: The uploaded file object.
    Returns:
        A list of image parts, or an empty list if no file is uploaded.
    """
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
    else:
        raise FileNotFoundError("No file uploaded")

    return image_parts

input_prompt = """You are an expert pharmaceutical/chemist where you need to see the tablets from the image
and also provide the details of every drug/tablet item with the below format:
  1. Examine the image carefully and identify the tablets depicted.
  2. Describe the uses and functionalities of each tablet shown in the image.
  3. Provide information on the intended purposes, features, and typical applications of the tablets.
  4. If possible, include any notable specifications or distinguishing characteristics of each tablet.
  5. Ensure clarity, conciseness, and accuracy in your descriptions, focusing on key details and distinguishing features.
"""

# Initialize our Streamlit app
st.set_page_config(page_title="AI Chemist App")

st.header("AI Chemist App")
input_prompt = st.text_input("Input Prompt:", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me")

# If submit button is clicked
if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input_prompt)
    st.subheader("The Response is")
    st.write(response)
