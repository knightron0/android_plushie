import cv2 as cv
# just a test to verify the image sizes after augmentation
pth = "/home/sarthak/code/android_plushie/data/train/yes/"
arr = []
for i in range(1, 1081):
    pthend = str(i) + '.jpeg'
    finalpth = pth + pthend
    img = cv.imread(finalpth)
    arr.append(img.shape)
arr2 = set(arr)
print(len(arr2))