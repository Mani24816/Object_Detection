# Object_Detection

# 🧠 YOLOv8 Object Detection GUI (Tkinter + Ultralytics)

A simple and intuitive desktop application for object detection using the **YOLOv8** model with a stylish GUI built using **Tkinter** and enhanced with animations. Easily select an image and get annotated object predictions in one click.

![Detection Screenshot](results.jpg)

---

## 🚀 Features

- 🖼️ Select any local image for detection
- ⚡ Fast inference using YOLOv8n
- 💡 Fade-in animation for enhanced UI
- 🧵 Non-blocking UI using threading
- ✅ Results saved automatically

---

## 🛠️ Tech Stack

- Python 3.12+
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- OpenCV
- Tkinter (GUI)
- Pillow (image handling)

---

## 📂 Project Structure

├── assets/
│ └── yolov8n.pt # Pre-trained YOLOv8 model
├── output/
│ └── results.jpg # Output image with detections
├── src/
│ ├── detector.py # Object detection logic
│ └── ui.py # GUI application code
├── main.py # Entry point
├── requirements.txt # Dependencies
└── README.md # Project overview

## 🧪 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/yolov8-object-detector-gui.git
cd yolov8-object-detector-gui

# Install required packages
pip install -r requirements.txt
🏁 Run the App
bash
Copy
Edit
python main.py
This will launch the object detection GUI. Select an image to get started!

📸 Example Output

📌 Notes
The default YOLOv8 model used is yolov8n.pt placed in the assets/ folder.

Detected images are saved in the output/ directory.

🙌 Acknowledgements
Ultralytics YOLOv8

Tkinter Docs

Pillow

## ✒️ Author
K Manish Kumar - [https://github.com/Mani24816]
Feel free to reach out for feedback or collaboration!
