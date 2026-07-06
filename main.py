import cv2

# Load image
image = cv2.imread("car.jpg")

if image is None:
    print("Image not found!")
else:
    print("The picture is uploaded successfully.")

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Show grayscale image
    cv2.imshow("Grayscale Image", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()