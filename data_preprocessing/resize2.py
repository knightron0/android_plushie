import cv2 as cv

pth = "/home/sarthak/code/android_plushie/data/train/no/"

for i in range(1, 1111):
    pthend = str(i) + '.jpeg'
    finalpth = pth + pthend
    img = cv.imread(finalpth)
    resized = cv.resize(img, (225, 225), interpolation = cv.INTER_AREA)
    newend = 'f' + str(i) + '.jpeg'
    finalpth2 = pth + newend
    cv.imwrite(finalpth2, resized)
