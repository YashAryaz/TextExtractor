import gradio as gr
import cv2
import pytesseract
import numpy as np
from PyPDF2 import PdfReader
import os
import tempfile

# Path to the Tesseract executable (change this path to your installation path)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Function to extract text from either an image or a PDF
def extract_text(input_file):
    temp_dir = "/content/"
    input_path = os.path.join(temp_dir, input_file.name)
    with open(input_path, "wb") as f:
        f.write(input_file.read())

    _, file_extension = os.path.splitext(input_path)
    file_extension = file_extension.lower()

    if file_extension in (".jpg", ".jpeg", ".png", ".gif", ".bmp"):
        # For images
        image = cv2.imread(input_path)

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply dilation and erosion to improve text visibility
        kernel = np.ones((1, 1), np.uint8)
        dilated = cv2.dilate(gray, kernel, iterations=1)
        eroded = cv2.erode(dilated, kernel, iterations=1)

        # Apply adaptive thresholding
        binary_image = cv2.adaptiveThreshold(
            eroded, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
        )

        # Perform OCR using Pytesseract on the preprocessed image
        text = pytesseract.image_to_string(binary_image)
    elif file_extension == ".pdf":
        # For PDFs
        reader = PdfReader(input_path)

        # Initialize a variable to store the entire text
        text = ""

        # Loop through each page and extract the text
        for page in reader.pages:
            page_text = page.extract_text()
            text += page_text
    else:
        text = "Unsupported file format. Please upload an image or PDF."

    return text

iface = gr.Interface(
    fn=extract_text,
    inputs="file",
    outputs="text",
    title="Text Extraction",
    description="Upload an image or PDF file to extract text. The file will be temporarily stored.",
)

if __name__ == "__main__":
    iface.launch(debug=True)
