import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageEnhance
from src.detector import ObjectDetector
import cv2
import threading
import time

class DetectionApp:
    def __init__(self, root):
        self.detector = ObjectDetector()
        self.root = root
        self.root.title("YOLOv8 Object Detection")
        self.root.geometry("850x650")
        self.root.configure(bg="white")

        # Title
        self.title_label = tk.Label(
            root, text="📸 Object Detection",
            font=("Segoe UI", 20, "bold"),
            bg="white", fg="#333"
        )
        self.title_label.pack(pady=10)

        # Image display
        self.img_label = tk.Label(root, bg="white")
        self.img_label.pack(pady=20)

        # Status label (animated feedback)
        self.status_label = tk.Label(root, text="", font=("Segoe UI", 12), bg="white", fg="green")
        self.status_label.pack()

        # Select image button
        self.btn = tk.Button(root, text="🖼️ Select Image",
                             command=self.select_image,
                             font=("Segoe UI", 14), bg="#4CAF50", fg="white",
                             activebackground="#45a049", padx=15, pady=8, bd=0)
        self.btn.pack(pady=10)

        # Hover animation
        self.btn.bind("<Enter>", lambda e: self.btn.config(bg="#388E3C"))
        self.btn.bind("<Leave>", lambda e: self.btn.config(bg="#4CAF50"))

    def fade_in_image(self, img):
        for alpha in range(0, 11):
            enhancer = ImageEnhance.Brightness(img)
            faded = enhancer.enhance(alpha / 10)
            photo = ImageTk.PhotoImage(faded)
            self.img_label.config(image=photo)
            self.img_label.image = photo
            self.root.update()
            time.sleep(0.05)

    def detect_and_display(self, file_path):
        self.status_label.config(text="🔍 Detecting objects...", fg="#FF8800")

        # Run detection
        output_path = self.detector.detect(file_path)

        img = cv2.imread(output_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb).resize((600, 400))

        # Fade in effect
        self.fade_in_image(img_pil)

        self.status_label.config(text="✅ Detection complete!", fg="green")
        messagebox.showinfo("Done", f"Detection saved at:\n{output_path}")

    def select_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
        )
        if not file_path:
            return

        # Run detection in separate thread for responsiveness
        threading.Thread(target=self.detect_and_display, args=(file_path,)).start()
