import cv2
import pandas as pd
import pickle

# Initialize global variables for feature usage
b = g = r = xpos = ypos = 0
clicked = False

# Loading the image path
image_path = r"C:\Users\jayas\OneDrive\Desktop\New folder\Color_detector\1000_F_755046480_4mLPbM6kq2BMGiRYk9LLvIO2qkajGn9H.jpg"
image = cv2.imread(image_path)
if image is None:
    print("Error: Image not found at the specified path.")
    exit()

# Pickle save/load for the image
pickle_image_path = r"C:\Users\jayas\OneDrive\Desktop\New folder\Color_detector\image.pkl"
with open(pickle_image_path, 'wb') as image_file:
    pickle.dump(image, image_file)
print("Image serialized using pickle.")

with open(pickle_image_path, 'rb') as image_file:
    image = pickle.load(image_file)
print("Image deserialized using pickle.")

# Loading the Dataset
csv_path = r"C:\Users\jayas\OneDrive\Desktop\New folder\Color_detector\colors.csv"
columns = ["color", "color_name", "hex", "R", "G", "B"]

# Pickle save/load for the dataset
pickle_csv_path = r"C:\Users\jayas\OneDrive\Desktop\New folder\Color_detector\colors.pkl"
try:
    df = pd.read_csv(csv_path, names=columns, header=None)
    with open(pickle_csv_path, 'wb') as csv_file:
        pickle.dump(df, csv_file)
    print("Dataset serialized using pickle.")
except FileNotFoundError:
    print("Error: CSV file not found at the specified path.")
    exit()

with open(pickle_csv_path, 'rb') as csv_file:
    df = pickle.load(csv_file)
print("Dataset deserialized using pickle.")

# Getting the R, G, B values
def draw_function(event, x, y, flags, params):
    global b, g, r, xpos, ypos, clicked
    if event == cv2.EVENT_LBUTTONDBLCLK:
        clicked = True
        xpos = x
        ypos = y
        if 0 <= y < image.shape[0] and 0 <= x < image.shape[1]:
            b, g, r = image[y, x]
            b = int(b)
            g = int(g)
            r = int(r)
            print(f"Mouse double-clicked at: ({x}, {y}) - Color: B={b}, G={g}, R={r}")
        else:
            print("Click outside the image bounds.")

# Function to get the name of the color or label name
def get_color_name(R, G, B):
    minimum = 10000
    color_name = "Unknown"
    for i in range(len(df)):
        d = abs(R - int(df.loc[i, "R"])) + abs(G - int(df.loc[i, "G"])) + abs(B - int(df.loc[i, "B"]))
        if d < minimum:
            minimum = d
            color_name = df.loc[i, "color_name"]
    print(f"Closest color name: {color_name}")
    return color_name

# Set up the mouse functions
cv2.namedWindow('Color_Detector')
cv2.setMouseCallback('Color_Detector', draw_function)

while True:
    temp_image = image.copy()

    if clicked:
        # Draw rectangle and display color name and the R, G, B values
        cv2.rectangle(temp_image, (18, 18), (750, 60), (b, g, r), -1)
        text = get_color_name(r, g, b) + f" R={r} G={g} B={b}"
        cv2.putText(temp_image, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        if (r + g + b) >= 600:
            cv2.putText(temp_image, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

    # Display the image
    cv2.imshow("Color_Detector", temp_image)

    # Exit using the ESC key
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
