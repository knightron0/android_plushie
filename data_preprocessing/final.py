import cv2 as cv

yesdir = "/home/sarthak/code/android_plushie/data/train/yes/"
nodir = "/home/sarthak/code/android_plushie/data/train/no/"
pth = "/home/sarthak/code/android_plushie/data/train/"

for i in range(1, 1081):
    strpath = 'yes_' + str(i) + '.jpeg'
    strpath2 = str(i) + '.jpeg' 
    finpath = yesdir + strpath2
    img = cv.imread(finpath)
    finpath2 = pth + strpath
    cv.imwrite(finpath2, img)

for i in range(1, 1111):
    strpath = 'no_' + str(i + 1080) + '.jpeg'
    strpath2 = str(i) + '.jpeg'
    finpath = nodir + strpath2
    img = cv.imread(finpath)
    finpath2 = pth + strpath
    cv.imwrite(finpath2, img)


