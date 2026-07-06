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
image_height = image.shape[0]

for contour in contours:

    perimeter = cv2.arcLength(contour, True)

    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

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

# Draw detected plate
if plate is not None:

    x, y, w, h = cv2.boundingRect(plate)

    # Add a small padding around the plate
    padding = 10

    x1 = max(x - padding, 0)
    y1 = max(y - padding, 0)

    x2 = min(x + w + padding, image.shape[1])
    y2 = min(y + h + padding, image.shape[0])

    # Crop the license plate
    plate_image = image[y1:y2, x1:x2]

    # Draw rectangle on original image
    cv2.drawContours(image, [plate], -1, (0, 255, 0), 3)

    cv2.imshow("Detected License Plate", image)
    cv2.imshow("Cropped Plate", plate_image)

else:

    print("License plate not found.")

    cv2.imshow("Detected License Plate", image)

cv2.waitKey(0)
cv2.destroyAllWindows()