import cv2
import easyocr
from tkinter import Tk
from tkinter.filedialog import askopenfilename

print("=" * 45)
print(" Automatic License Plate Recognition ")
print("=" * 45)
print("Please select a car image...\n")

# Open file dialog
Tk().withdraw()

file_path = askopenfilename(
    title="Select a car image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png")
    ]
)

if not file_path:
    print("No image selected.")
    exit()

# Load image
image = cv2.imread(file_path)

if image is None:
    print("Image not found!")
    exit()

print("Image loaded successfully.")

# Initialize OCR
reader = easyocr.Reader(['en'])

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges
edges = cv2.Canny(blur, 75, 200)

# Find contours
contours, _ = cv2.findContours(
    edges,
    cv2.RETR_LIST,
    cv2.CHAIN_APPROX_SIMPLE
)

plate = None
image_height = image.shape[0]

# Search for a license plate candidate
for contour in contours:

    perimeter = cv2.arcLength(contour, True)

    approx = cv2.approxPolyDP(
        contour,
        0.02 * perimeter,
        True
    )

    if len(approx) == 4:

        x, y, w, h = cv2.boundingRect(approx)

        aspect_ratio = w / float(h)
        area = cv2.contourArea(contour)

        if (
            2.5 < aspect_ratio < 6
            and area > 2000
            and y > image_height * 0.4
        ):

            plate = approx
            break

if plate is not None:

    x, y, w, h = cv2.boundingRect(plate)

    # Add padding around the detected plate
    padding = 10

    x1 = max(x - padding, 0)
    y1 = max(y - padding, 0)

    x2 = min(x + w + padding, image.shape[1])
    y2 = min(y + h + padding, image.shape[0])

    # Crop plate
    plate_image = image[y1:y2, x1:x2]

    # Preprocess for OCR
    gray_plate = cv2.cvtColor(
        plate_image,
        cv2.COLOR_BGR2GRAY
    )

    _, threshold_plate = cv2.threshold(
        gray_plate,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # Remove small noise
    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT,
        (3, 3)
    )

    clean_plate = cv2.morphologyEx(
        threshold_plate,
        cv2.MORPH_OPEN,
        kernel
    )

    # OCR
    result = reader.readtext(
        clean_plate,
        allowlist="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    )

    if result:

        print("\nDetected License Plate:")

        for detection in result:
            print(detection[1])

    else:

        print("\nNo text detected.")

    # Draw detected contour
    cv2.drawContours(
        image,
        [plate],
        -1,
        (0, 255, 0),
        3
    )

    # Show results
    cv2.imshow("Detected License Plate", image)
    cv2.imshow("Cropped Plate", plate_image)
    cv2.imshow("Clean Plate", clean_plate)

else:

    print("License plate not found.")
    cv2.imshow("Detected License Plate", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("\nProcess completed successfully.")