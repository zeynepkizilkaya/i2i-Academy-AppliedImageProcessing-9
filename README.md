# Automatic License Plate Recognition (ALPR)

This project was developed as part of the i2i Academy Applied Image Processing assignment.

## Features

- Load any vehicle image from the computer
- Convert image to grayscale
- Apply Gaussian Blur
- Detect edges using Canny Edge Detection
- Find license plate using contour analysis
- Crop the detected plate
- Improve OCR input using Otsu Thresholding and Morphological Opening
- Read license plate text with EasyOCR

## Technologies

- Python
- OpenCV
- EasyOCR
- Tkinter

## Notes

The application performs best on clear front-view vehicle images. During testing, standard Turkish license plates produced more accurate OCR results, while decorative symbols on some foreign license plates could affect text recognition.

## How to Run

```bash
pip install opencv-python easyocr

python main.py
