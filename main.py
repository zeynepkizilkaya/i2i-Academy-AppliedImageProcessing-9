import cv2

# upload the image
image = cv2.imread("car.jpg")

if image is None:
    print("Image not found!")
else:
    print("The picture is uploaded successfully.")

    # convert image to the grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # apply gaussian blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # detect edges using canny
    edges = cv2.Canny(blur, 75, 200)

    # show edge image
    cv2.imshow("Canny Edge Detection", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()