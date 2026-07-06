import cv2

# Load image
image = cv2.imread("car.jpg")

if image is None:
    print("Image not found!")
else:
    print("The picture is uploaded successfully.")

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Show blurred image
    cv2.imshow("Blurred Image", blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()