from PIL import Image

# Read the image
input_path = r'C:\Users\HP\Desktop\Learn\Python Image\All-basic-python-image\Input_image\Image_1.jpg'  # Replace with your image file path
image = Image.open(input_path)

# Optionally, you can perform operations on the image here

# Write (save) the image
image_name = input_path.split('\\')[-1]  # Extract the image name from the path
print(f"Image name: {image_name}")
output_path = r'C:\Users\HP\Desktop\Learn\Python Image\All-basic-python-image\Output _image'  
output_path = output_path + '\\' + 'Output_' + image_name  # Combine output path with image name
outputimage_name = output_path.split('\\')[-1]
print(f"Output image name: {outputimage_name}")
# Ensure the output directory exists
image.save(output_path)

print(f"Image read from {input_path} and saved to {output_path}")