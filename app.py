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
def get_gemini_response(text_prompt, image, prompt):
  model = genai.GenerativeModel('gemini-1.5-pro')
  response = model.generate_content([text_prompt, image[0], prompt])
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

input_prompt = """You are a pharmaceutical expert analyzing the tablets in the image. Provide information in the format described below:
1. Identify the Tablets:
- Examine the image to identify each tablet by shape, color, and visible markings.
2. Detailed Description:
- For each tablet, provide:
- Name: Official and common brand names.
- Active Ingredients: Key substances and their concentrations.
- Uses: Common uses and conditions treated.
- Dosage: Typical dosages, frequency, and how it's taken.
- Side Effects: Common and serious side effects, and any warnings.
- Interactions: Possible interactions with other medications.
3. Additional Details:
- Visual Features: Any distinguishing marks.
- Regulatory Status: Approval status or relevant info.
4. Clarity and Accuracy:
- Ensure descriptions are clear and accurate.
Present the information in a structured and easy-to-understand format.
"""

# Initialize our Streamlit app
st.set_page_config(page_title="IntelliChem AI", page_icon="💊")

# Apply custom styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Raleway:wght@400;700&display=swap');
    
    body {
        font-family: 'Roboto', sans-serif;
        color: #e81010;
    }
    
    .header {
        font-family: 'Raleway', sans-serif;
        color: #e81010;
        text-align: center;
        font-size: 2.5em;
        margin-bottom: 0.5em;
        font-weight: bold;
    }
    
    .tagline {
        font-family: 'Raleway', sans-serif;
        color: #e81010;
        text-align: center;
        font-size: 1.5em;
        margin-bottom: 2em;
    }
    
    .upload-button, .submit-button {
        background-color: #178582;
        color: #e81010;
        font-size: 1em;
        padding: 0.8em 1.5em;
        border-radius: 5px;
        border: none;
        cursor: pointer;
    }
    
    .upload-button:hover, .submit-button:hover {
        background-color: #146a6d;
    }
    
    .result {
        background-color: #178582;
        color: #e81010;
        padding: 1em;
        border-radius: 5px;
        margin-top: 1em;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="header">IntelliChem AI</div>', unsafe_allow_html=True)
st.markdown('<div class="tagline">Your Personalized AI Chemist : Tailored to your convenience.</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

text_prompt = st.text_input("Input Prompt:", placeholder="Describe your requirements here...")

if st.button("Submit"):
    with st.spinner("Processing your image..."):
        try:
            image_data = input_image_setup(uploaded_file)
            response = get_gemini_response(text_prompt, image_data, input_prompt)
            st.markdown('<div class="result"><h3>Result:</h3></div>', unsafe_allow_html=True)
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")