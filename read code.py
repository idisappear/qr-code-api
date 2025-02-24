import cv2
from pyzbar.pyzbar import decode

# Load the QR code image
image = cv2.imread("image.png")  # Make sure to use the correct file path
print('file loaded')
# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Decode the QR code
decoded_objects = decode(gray)

# Print extracted data
for obj in decoded_objects:
    print("QR Code Data:", obj.data.decode("utf-8"))
