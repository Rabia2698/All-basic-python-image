from PIL import Image

import matplotlib.pyplot as plt

# Load the image
input_image = r'C:\Users\HP\Desktop\Learn\Python Image\All-basic-python-image\Input_image\Image_1.jpg'  # Replace with your image file path=
image_name = input_image.split('\\')[-1]
output_pathmain = r'C:\Users\HP\Desktop\Learn\Python Image\All-basic-python-image\Output _image'
output_path = output_pathmain + '\\' + 'resized_' + image_name
image = Image.open(input_image)

# 1. Resize the image
resized_image = image.resize((400, 300))  # width=400, height=300
output_path = output_pathmain + '\\' + 'resized_' + image_name
resized_image.save(output_path)

# 2. Crop the image (left, upper, right, lower)
cropped_image = image.crop((100, 100, 400, 400))
output_path = output_pathmain + '\\' + 'crop_' + image_name
cropped_image.save(output_path)

# 3. Rotate the image (angle in degrees)
rotated_image = image.rotate(45)  # Rotate 45 degrees counter-clockwise
output_path = output_pathmain + '\\' + 'rotate_' + image_name
rotated_image.save(output_path)

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(image)
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Resized Image')
plt.imshow(resized_image)
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Cropped Image')
plt.imshow(cropped_image)
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('Rotated Image')
plt.imshow(rotated_image)
plt.axis('off')

plt.tight_layout()
plt.show()