# converting to a single video files

import os

import cv2


def videoEncoder():
    img_array = []
    for filename in os.listdir('C:/Users/91909/Desktop/bikes'):
        if filename.endswith(".jpg"):
            print(filename, "hello")
            img = cv2.imread('C:/Users/91909/Desktop/bikes/' + filename)
            height, width, layers = img.shape
            size = (width, height)
            img_array.append(img)
    out = cv2.VideoWriter('C:/Users/91909/Desktop/project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
