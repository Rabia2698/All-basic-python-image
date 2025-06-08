import cv2
import numpy as np

import matplotlib.pyplot as plt

# Load an image
image_path = r'C:\Users\HP\Desktop\Learn\Python Image\All-basic-python-image\Input_image\Image_1.jpg' 
img = cv2.imread(image_path)  # Replace with your image path
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert to different color spaces
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

print("Grayscale is a single channel image, while RGB, HSV, and LAB are three channel images.")
print("RGB: Red, Green, Blue")
print("Grayscale: Single channel representing intensity")
print("HSV: Hue, Saturation, Value")
print("LAB: Lightness, A channel, B channel")
print("Note: LAB is often visualized in grayscale, but it has three channels.")


# Display images
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.title('RGB')
plt.imshow(img_rgb)
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Grayscale')
plt.imshow(img_gray, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('HSV')
plt.imshow(img_hsv, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('LAB')
plt.imshow(img_lab, cmap='gray')  # LAB is often visualized in grayscale
plt.axis('off')

plt.tight_layout()
plt.show()