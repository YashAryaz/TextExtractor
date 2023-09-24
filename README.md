# TextExtractor
This Python script uses the [Gradio](https://gradio.app/) library to create a simple web-based interface for extracting text from images or PDFs using OpenCV and PyTesseract. It also supports running as a standalone script. Here's how it works:

## Dependencies

Before running the script, make sure you have the following dependencies installed:

- [Gradio](https://gradio.app/)
- [OpenCV](https://opencv.org/)
- [PyTesseract](https://github.com/madmaze/pytesseract)
- [NumPy](https://numpy.org/)
- [PyPDF2](https://pythonhosted.org/PyPDF2/)

You can install them using pip:

``` bash
pip install gradio opencv-python-headless pytesseract numpy PyPDF2
```

# Tesseract Configuration
You need to specify the path to the Tesseract executable on your system. Modify the pytesseract.pytesseract.tesseract_cmd variable to point to the correct path. Example:
```bash
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
```
# Usage
Run the script using Python:

```bash
python main.py
```

The Gradio interface will launch, allowing you to upload an image or PDF file.

Once you upload a file, the script will process it and extract text.

The extracted text will be displayed on the web interface.

