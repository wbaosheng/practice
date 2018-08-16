"""
    Detect blur images.
"""

from imutils import paths
import argparse
import cv2


def variance_of_laplacian(image):
    return  cv2.Laplacian(image, cv2.CV_64F).var()
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--images", required=True, help="path to input directory of images")
    parser.add_argument("-t", "--threshold", type=float, default=100.0,
                        help="focus measure that fall below this value will be considered 'blurry'")
    args = vars(parser.parse_args())

    # loop over the input images
    for imagePath in paths.list_images(args["images"]):
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fm = variance_of_laplacian(gray)

        print imagePath, fm

        text = "Not Blurry"
        if (fm < args["threshold"]):
            text = "blurry"

        print imagePath + " is " + text
