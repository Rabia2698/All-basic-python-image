from PIL import Image, ImageFilter
import matplotlib.pyplot as plt


# Load an image
image_path = r'C:\Users\HP\Desktop\Learn\Python Image\All-basic-python-image\Input_image\Image_1.jpg' 
image = Image.open(image_path)  # Replace with your image path

# Apply BLUR filter
blurred = image.filter(ImageFilter.BLUR)

# Apply SHARPEN filter
sharpened = image.filter(ImageFilter.SHARPEN)

# Apply EDGE DETECTION filter
edges = image.filter(ImageFilter.FIND_EDGES)

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(image)
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Blurred Image')
plt.imshow(blurred)
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Sharpened Image')
plt.imshow(sharpened)
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('Edges Detected Image')
plt.imshow(edges)
plt.axis('off')

plt.tight_layout()
plt.show()