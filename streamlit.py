import streamlit as st
import cv2
import pandas as pd
import numpy as np
import pickle
from PIL import Image

# Set up the title and emojis
st.title("🎨 Color Detector")
st.write("👋 Upload an image and double-click anywhere to detect the color!")

# Load the dataset and image from pickle files
pickle_csv_path = r"C:\Users\jayas\OneDrive\Desktop\New folder\Color_detector\colors.pkl"
pickle_image_path = r"C:\Users\jayas\OneDrive\Desktop\New folder\Color_detector\image.pkl"

# Load the CSV dataset (color data)
with open(pickle_csv_path, 'rb') as f:
    df = pickle.load(f)

# Load the image from pickle
with open(pickle_image_path, 'rb') as f:
    image = pickle.load(f)

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

# Upload an image
uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    # Read the uploaded image
    file_bytes = np.asarray(bytearray(uploaded_image.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Convert BGR to RGB for Streamlit display
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display the uploaded image
    st.image(image_rgb, caption="Uploaded Image", use_column_width=True)

    # Create an OpenCV window to select colors
    st.write("💡 **Double-click anywhere on the image to detect the color!**")

    if st.button("Detect Colors"):
        # Variables to store the detected color
        global clicked, xpos, ypos, b, g, r
        clicked = False
        b = g = r = xpos = ypos = 0

        # Mouse callback function
        def draw_function(event, x, y, flags, param):
            global clicked, xpos, ypos, b, g, r
            if event == cv2.EVENT_LBUTTONDBLCLK:
                clicked = True
                xpos, ypos = x, y
                b, g, r = image[y, x]
                b, g, r = int(b), int(g), int(r)

        # Set up OpenCV mouse callback
        cv2.namedWindow("Color Detector")
        cv2.setMouseCallback("Color Detector", draw_function)

        while True:
            temp_image = image.copy()
            if clicked:
                # Draw rectangle and display color name
                cv2.rectangle(temp_image, (18, 18), (750, 60), (b, g, r), -1)
                color_name = get_color_name(r, g, b)
                text = f"{color_name} | R={r}, G={g}, B={b}"
                cv2.putText(temp_image, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
                if (r + g + b) >= 600:  # Adjust text color for bright backgrounds
                    cv2.putText(temp_image, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
                st.write(f"🎉 **Detected Color:** {color_name}")

            # Display the updated image
            cv2.imshow("Color Detector", temp_image)

            # Exit on pressing ESC
            if cv2.waitKey(20) & 0xFF == 27:
                break

        cv2.destroyAllWindows()
