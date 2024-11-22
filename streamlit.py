import streamlit as st
import cv2
import pandas as pd
import numpy as np
from PIL import Image
import requests
from io import BytesIO

# Set up the title and emojis
st.title("🎨 Color Detector")
st.write("👋 Upload an image or use the default image to detect colors!")

# Load the dataset (color data)
colors_csv_path = "colors.csv"
df = pd.read_csv(colors_csv_path)

# Function to get the closest color name
def get_color_name(R, G, B):
    minimum = 10000
    color_name = "Unknown"
    for i in range(len(df)):
        d = abs(R - int(df.loc[i, "R"])) + abs(G - int(df.loc[i, "G"])) + abs(B - int(df.loc[i, "B"]))
        if d < minimum:
            minimum = d
            color_name = df.loc[i, "color_name"]
    return color_name

# Load a default image from URL
default_image_url = "https://as1.ftcdn.net/v2/jpg/1000_F_755046480_4mLPbM6kq2BMGiRYk9LLvIO2qkajGn9H.jpg"
response = requests.get(default_image_url)
default_image = Image.open(BytesIO(response.content))
default_image_array = np.array(default_image)

# Upload an image
uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

# Use the uploaded image or fallback to the default image
if uploaded_image is not None:
    file_bytes = np.asarray(bytearray(uploaded_image.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
else:
    st.write("Using default image.")
    image = cv2.cvtColor(default_image_array, cv2.COLOR_RGB2BGR)

# Convert the image to RGB for display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the image
st.image(image_rgb, caption="Click anywhere on the image to detect colors", use_column_width=True)

# Use Streamlit's `st.session_state` to store click coordinates
if 'coords' not in st.session_state:
    st.session_state['coords'] = None

# Detect colors upon click
click = st.image(image_rgb, use_column_width=True, key="color_image")

if click:
    st.session_state['coords'] = click['x'], click['y']

if st.session_state['coords']:
    x, y = st.session_state['coords']
    b, g, r = image[y, x]
    color_name = get_color_name(r, g, b)

    # Display the detected color details
    st.write(f"🎉 **Detected Color:** {color_name}")
    st.write(f"RGB Values: R={r}, G={g}, B={b}")
    st.markdown(f"<div style='background-color:rgb({r},{g},{b});width:100px;height:50px;border:1px solid black'></div>", unsafe_allow_html=True)
