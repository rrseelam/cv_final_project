"""
Data Preprocessing Script

- enumerates data in the raw_datasets/ and places stardized ouput pickles in the processes_dataset folder
- converts to standard format (jpeg)
- drops unsupported characters
- converts to custom bool encoding format
"""

import numpy as np
import cv2 as cv

from data_preprocessing import *
from bounding_box_detector import *


def main():

    f = "raw_datasets/CROHME_test_2011-converted/TestData1_2_sub_29.png"

    img = chunk_image_path(f, show=True)
    og = cv.imread(f) 
    boxes = grab_bounding_boxes(img)
    print(boxes)
    for box in boxes:
        print(box)
       
        pt1 = (box[2] - 1, box[0] - 1)
        pt2 = (box[3] + 1, box[0] - 1)
        pt3 = (box[3] + 1, box[1] + 1)
        pt4 = (box[2] - 1, box[1] + 1)

        cv.rectangle(og, pt1, pt3, (256, 128, 0), 1)  # Green color, thickness 2
    
    cv.imshow("img", og)
    cv.waitKey(0)
    cv.destroyAllWindows()

    print("This is a ulitiy module")

def chunk_image_path(img_path, show=False):
    # returns an np array of a a image compressed with out compression format
    # expects an image in the form
    
    image = cv.imread(img_path) 

    return chunk_image(image, show)
  

def chunk_image(img, show=False):
    # returns an np array of a a image compressed with out compression format
    # expects an np array of size H,W,3

    # Load the image

    # Convert the image to grayscale

    if show:
        cv.imshow("img", img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    if show:
        cv.imshow("img", gray_image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    gray_image[gray_image < 200] = 0
    gray_image[gray_image >= 200] = 255


    if show:
        cv.imshow("img", gray_image)
        cv.waitKey(0)
        cv.destroyAllWindows()
   
    return gray_image


if __name__ == "__main__":
    main()