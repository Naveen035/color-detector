#IMporting Necessary Libraries
import cv2
import pandas as pd

# Initialize global variables for feature usage
b = g = r = xpos = ypos = 0
clicked = False

# Loading the image path
image_path = r"C:\Users\jayas\OneDrive\Desktop\New folder\Color_detector\1000_F_755046480_4mLPbM6kq2BMGiRYk9LLvIO2qkajGn9H.jpg"
image = cv2.imread(image_path)
if image is None:
    print("Error: Image not found at the specified path.")
    exit()

# Loading the Dataset
csv_path = r"C:\Users\jayas\OneDrive\Desktop\New folder\Color_detector\colors.csv"
#Indexing the column names of the Dataset
columns = ["color", "color_name", "hex", "R", "G", "B"]
try:
    df = pd.read_csv(csv_path, names=columns, header=None)
except FileNotFoundError:
    print("Error: CSV file not found at the specified path.") #If the path does not exist
    exit()

#Getting the R,G,B values
def draw_function(event, x, y, flags, params):
    global b, g, r, xpos, ypos, clicked
    if event == cv2.EVENT_LBUTTONDBLCLK:
        clicked = True
        xpos = x
        ypos = y
        # Ensure the click is within the images only if we click on the outside the image its will doesn't excute
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
        #Manehatten Distance calculation
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
        # Draw rectangle and display color name and the R,G,B values
        cv2.rectangle(temp_image, (18, 18), (750, 60), (b, g, r), -1)
        text = get_color_name(r, g, b) + f" R={r} G={g} B={b}"
        cv2.putText(temp_image, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        if (r + g + b) >= 600: # Reducing this we can find bright colors only while increasing this we can we can find bright colors also
            cv2.putText(temp_image, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

    # Display the image
    cv2.imshow("Color_Detector", temp_image)

    # Exit using the ESC key
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
