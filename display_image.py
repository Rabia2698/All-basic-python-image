import cv2

# Path to your image file
image_path = r'C:\Users\HP\Desktop\Learn\Python Image\All-basic-python-image\Input_image\Image_1.jpg'  
# Replace with your image file name

# Read the image
image = cv2.imread(image_path)

# Check if image was loaded
if image is None:
    print("Error: Image not found.")
else:
    # Display the image
    cv2.imshow('Displayed Image', image)
    # Show the image in a window
    cv2.waitKey(5000)
    # Wait for 5000 milliseconds (5 seconds) before closing the window
    # if you want to close the window manually, you can use 0
    cv2.destroyAllWindows()
    # Close the image window
    print("Image displayed successfully.")
