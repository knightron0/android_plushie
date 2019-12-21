import cv2 as cv
import random
import numpy as np
curr = 55
pth = "/home/sarthak/code/android_plushie/data/train/yes/"
for i in range(1, 55):
    pthend = str(i) + '.jpeg'
    finalpth = pth + pthend
    img = cv.imread(finalpth)
    arr = []
    flip1 = cv.flip(img, 1)
    flip2 = cv.flip(img, -1)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    rot1 = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
    rot2 = cv.rotate(img, cv.ROTATE_180)
    rot3 = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)
    row, col, channels = img.shape
    for l in range(7):
        rnd = cv.imread(finalpth)
        p = 0.05
        for i in range(row):
            for j in range(col):
                r = random.random()
                if r < p/2:
                    rnd[i][j] = [0, 0, 0]
                elif r < p:
                    rnd[i][j] = [255, 255, 255]
                else:
                    rnd[i][j] = img[i][j]
        arr.append(rnd)
    arr.append(flip1)
    arr.append(flip2)
    arr.append(rot1)
    arr.append(rot2)
    arr.append(rot3)
    arr.append(gray)
    gauss = np.random.normal(0,0.5,img.size)
    gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')
    img_gauss = cv.add(img,gauss)
    arr.append(img_gauss)
    gauss = np.random.normal(0,1,img.size)
    gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')
    img_gauss = cv.add(img,gauss)
    arr.append(img_gauss)
    gauss = np.random.normal(0,0.25,img.size)
    gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')
    img_gauss = cv.add(img,gauss)
    arr.append(img_gauss)
    gauss = np.random.normal(0,1,img.size)
    gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')
    noise = img + img * gauss
    arr.append(noise)
    invert = cv.bitwise_not(img)
    arr.append(invert)
    gauss = np.random.normal(0,2,img.size)
    gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')
    img_gauss = cv.add(img,gauss)
    arr.append(img_gauss)
    print(len(arr))

    for j in range(len(arr)):
        end = str(curr) + '.jpeg'
        final = pth + end
        cv.imwrite(final, arr[j])
        curr+=1