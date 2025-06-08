import cv2

# Load the pre-trained DNN face detector model
modelFile = "deploy.prototxt"
weightsFile = "res10_300x300_ssd_iter_140000_fp16.caffemodel"
net = cv2.dnn.readNetFromCaffe(modelFile, weightsFile)

# Read the image
image = cv2.imread(r'C:\Users\HP\Desktop\Learn\Python Image\All-basic-python-image\Input_image\Image_1.jpg' )
(h, w) = image.shape[:2]

# Prepare the image for the neural network
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
                             (300, 300), (104.0, 177.0, 123.0))

net.setInput(blob)
detections = net.forward()

# Draw rectangles around detected faces
for i in range(0, detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > 0.5:
        box = detections[0, 0, i, 3:7] * [w, h, w, h]
        (startX, startY, endX, endY) = box.astype("int")
        cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)

# Show the result
cv2.imshow('Detected Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()