import os
import pytesseract
import cv2 as cv

def main():
    path = os.getcwd()
    file = path + "/images/1.jpeg"
    image = cv.imread(file)
    decoded_text = pytesseract.image_to_string(image)
    print(decoded_text)

main()
