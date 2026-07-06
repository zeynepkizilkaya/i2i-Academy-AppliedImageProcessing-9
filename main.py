import cv2

# Load image
image = cv2.imread("car.jpg")

if image is None:
    print("Image not found!")
    exit()

print("The picture is uploaded successfully.")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges
edges = cv2.Canny(blur, 75, 200)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

plate = None

for contour in contours:

    perimeter = cv2.arcLength(contour, True)

    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

    # Check if contour has 4 corners
    if len(approx) == 4:

        x, y, w, h = cv2.boundingRect(approx)

        aspect_ratio = w / float(h)

        # Typical license plate ratio
        if 2.5 < aspect_ratio < 6:

            plate = approx
            break

# Draw detected plate
if plate is not None:

    cv2.drawContours(image, [plate], -1, (0, 255, 0), 3)

    cv2.imshow("Detected License Plate", image)

else:

    print("License plate not found.")

    cv2.imshow("Detected License Plate", image)

cv2.waitKey(0)
cv2.destroyAllWindows()