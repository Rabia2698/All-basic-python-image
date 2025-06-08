import cv2
import numpy as np
import matplotlib.pyplot as plt

def blur_image(image):
    # Gaussian blur
    return cv2.GaussianBlur(image, (7, 7), 0)

def sharpen_image(image):
    # Sharpening kernel
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])
    return cv2.filter2D(image, -1, kernel)

def edge_image(image):
    # Canny edge detection
    return cv2.Canny(image, 100, 200)

if __name__ == "__main__":
    img_path = r'C:\Users\HP\Desktop\Learn\Python Image\All-basic-python-image\Input_image\Image_1.jpg' 
    image = cv2.imread(img_path)

    

    if image is None:
        print("Image not found.")
        exit()
    
    

    blurred = blur_image(image)
    sharpened = sharpen_image(image)
    edges = edge_image(image)


    #cv2.imwrite("blurred.jpg", blurred)
    #cv2.imwrite("sharpened.jpg", sharpened)
    #cv2.imwrite("edges.jpg", edges)

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for display
    # cv2 reads images in BGR format, convert to RGB for matplotlib
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.title('Blurred Image')
    plt.imshow(cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for display
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.title('Sharpened Image')
    plt.imshow(cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for display
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.title('Edges Detected Image')
    plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB), cmap='gray')  # Convert BGR to RGB for display
    plt.axis('off')

    plt.tight_layout()
    plt.show()