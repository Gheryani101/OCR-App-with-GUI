import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

# Set the path to the Tesseract executable (replace with your actual path)
pytesseract.pytesseract.tesseract_cmd = r'c:\users\hp\appdata\local\programs\python\python311\scripts\pytesseract.exe '

class OCRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OCR App")

        # Create a label to display the selected image
        self.image_label = tk.Label(root)
        self.image_label.pack()

        # Create a button to open an image file
        self.open_button = tk.Button(root, text="Open Image", command=self.open_image)
        self.open_button.pack()

        # Create a button to perform OCR on the image
        self.ocr_button = tk.Button(root, text="Perform OCR", command=self.perform_ocr)
        self.ocr_button.pack()

        # Create a text widget to display OCR result
        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack()

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image = Image.open(file_path)
            self.display_image()

    def display_image(self):
        # Resize the image to fit the label
        resized_image = self.image.resize((300, 300))
        tk_image = ImageTk.PhotoImage(resized_image)

        # Update the image label
        self.image_label.config(image=tk_image)
        self.image_label.image = tk_image

    def perform_ocr(self):
        try:
            text = pytesseract.image_to_string(self.image)
            self.result_text.delete(1.0, tk.END)  # Clear previous result
            self.result_text.insert(tk.END, text)
        except Exception as e:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = OCRApp(root)
    root.mainloop()
