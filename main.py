import cv2

# reads the image
image = cv2.imread("car.jpg")

# if can not then error
if image is None:
    print("The picture is not found!")
else:
    print("The picture is uploaded succesfully.")

    # show the image at the screen
    cv2.imshow("Car Image", image)

    # wait till someone pushes a button
    cv2.waitKey(0)

    cv2.destroyAllWindows()