import base64
import os
import shutil

import cv2
import qrcode as qc


def videoDecoder():
    print("Decoding Video")
    capture = cv2.VideoCapture("C:/Users/surya/Desktop/new/project.avi")
    frame_no = 0
    while True:
        success, frame = capture.read()
        if success:
            cv2.imwrite(f'C:/Users/surya/Desktop/new/imgcache/VideoReads/frame_{frame_no}.jpg', frame)
            if frame_no + 1 % 26 == 0:
                print(f'f{frame_no}')
            else:
                print(f'f{frame_no}', end=' ')
            frame_no += 1
        else:
            break
    capture.release()


def videoEncoder():
    print("\n Encoding video")
    img_array = []
    for filename in os.listdir('C:/Users/surya/Desktop/new/imgcache/temp'):
        if filename.endswith(".png"):
            img = cv2.imread('C:/Users/surya/Desktop/new/imgcache/temp/' + filename)
            height, width, layers = img.shape
            size = (width, height)
            img_array.append(img)
    out = cv2.VideoWriter('C:/Users/surya/Desktop/new/project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

    # shutil.rmdir('C:/Users/91909/Desktop/new/imgcache/temp')


def fileread(file_location="./imgcache/Bike 1_0.jpg"):
    data = []
    chars = 600
    with open(file_location, "rb") as file:
        print('reading file')
        string = str(base64.b64encode(file.read()))[2:-1]
        size = len(string)
        print('splitting data')
        for i in range(0, size, chars):
            if i + chars < size:
                data.append(string[i:i + chars])
        if i < size:
            data.append(string[i:size] + '&' * (chars - (size - i)))
        qrgenerator(data)


def qrgenerator(data):
    if data:
        if os.path.isdir("./imgcache/temp"):
            shutil.rmtree('C:/Users/surya/Desktop/new/imgcache/temp')
        os.mkdir("./imgcache/temp")
        for i in range(len(data)):
            img = qc.make(data[i])
            print(f'{i}.png ', len(data[i]), end=" ")
            if i % 12 == 0 and i != 0:
                print()
            img.save(f'./imgcache/temp/{i}.png')
        videoEncoder()
    else:
        img = qc.make("hello world")
        img.save('./imgcache/temp/hello.png')


def qrRead(location):
    img = cv2.imread(location)
    det = cv2.QRCodeDetector()
    val, pts, st_code = det.detectAndDecode(img)
    # print(len(val))
    return val


def imageReader():
    frame_no = 0
    data = []
    print("reading images")
    while os.path.isfile(f"./imgcache/VideoReads/frame_{frame_no}.jpg"):
        print(frame_no, end=" ")
        data.append(qrRead(f"./imgcache/VideoReads/frame_{frame_no}.jpg"))
        frame_no += 1
    if data:
        for i, dat in enumerate(data):
            print(i, " len ", len(dat), end=", ")


# fileread()
# videoEncoder()
# videoDecoder()
imageReader()
