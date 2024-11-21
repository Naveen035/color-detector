# 🎨 Color Detector  

This project is a **Color Detection Application** built using Python and OpenCV, designed to identify colors from an image interactively. With a dataset of **30,000 color combinations**, the application accurately detects the closest color name based on RGB values.  

Whether you're a designer, developer, or just curious about colors, this tool can help identify colors by double-clicking on an image! 🌈  

---

## 🚀 Features  

### 🔍 Accurate Color Detection  
- Utilizes a dataset of **30,000 colors** to identify and display the closest color name.  
- Computes the **Manhattan distance** between the clicked RGB value and dataset entries for high accuracy.  

### 🖼️ Image Upload and Interaction  
- Upload any image in JPG, PNG, or JPEG format.  
- Interactive detection through double-clicking on any part of the image.  

### 📋 Key Functionalities  
- **Displays Color Name**: Shows the detected color name along with its RGB values.  
- **Visual Feedback**: Highlights the color area with a rectangle and updates dynamically.  
- **Responsive Text Color**: Automatically adjusts text visibility based on the detected color brightness.  

---

## 📊 Dataset Overview  

The **color dataset** used in this project contains:  
- **30,000 unique entries** of color names, RGB values, and HEX codes.  
- Comprehensive mapping of human-readable color names to RGB values.  

#### Example of Dataset Columns:  
| Color Name       | R   | G   | B   | HEX       |  
|------------------|-----|-----|-----|-----------|  
| Dark Jungle Green| 19  | 33  | 44  | #13212C   |  
| Bright Red       | 255 | 0   | 0   | #FF0000   |  
| Ocean Blue       | 28  | 107 | 160 | #1C6BA0   |  

---

## 🌟 Advantages  

### 🎨 Design-Friendly  
- Perfect for **graphic designers** and **UI/UX professionals** who need to identify colors from screenshots, logos, or photos.  

### 🛠️ Developer-Ready  
- Useful for **web developers** needing precise HEX or RGB values for front-end development.  

### 🔬 Educational Use  
- Learn about the RGB color model and its real-world applications.  

### 💡 Customizable  
- Expandable dataset: Add more colors or integrate with real-time APIs for dynamic results.  
- Adjustable detection logic to fine-tune accuracy for specific needs.  

---
## 🧑‍💻 How It Works  
1. **Upload an Image**: Drag and drop or browse an image into the app.  
2. **Double-Click**: On the image, double-click to pick a color.  
3. **Result**: The detected color name and RGB values appear below the image.  

---

## 💡 Future Enhancements  
- **Real-Time Color Detection**: Using live webcam feed for instant color detection.  
- **Color Palette Generation**: Automatically generate a color palette from uploaded images.  
- **Integration with Pantone Matching System (PMS)**: Ideal for design professionals seeking accurate color standards.  

---

## 🤝 Contributing  

Contributions are welcome! If you'd like to improve the application or add new features, feel free to fork this repository and submit a pull request.  

