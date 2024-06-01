import cv2
import os

# Read the image
img = cv2.imread("img6.png")
if img is None:
    raise ValueError("Image not found")

# Get the message and passcode from the user
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Create dictionaries for character-to-ASCII and ASCII-to-character conversion
d = {}
c = {}
for i in range(256):
    d[chr(i)] = i
    c[i] = chr(i)

# Initialize variables for pixel indexing
n = 0
m = 0
z = 0

# Encrypt the message in the image
for char in msg:
    img[n, m, z] = d[char]
    z = (z + 1) % 3
    if z == 0:
        m += 1
        if m >= img.shape[1]:
            m = 0
            n += 1
            if n >= img.shape[0]:
                raise ValueError("Message is too long to encode in the image")

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)

# Open the encrypted image file
os.startfile("encryptedImage.jpg")

# Decryption
message = ""
n = 0
m = 0
z = 0
pas = input("Enter passcode for decryption: ")

if password == pas:
    for i in range(len(msg)):
        message += c[img[n, m, z]]
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= img.shape[1]:
                m = 0
                n += 1
                if n >= img.shape[0]:
                    break
    print("Decrypted message =", message)
else:
    print("You are not authenticated")
