import cv2

def empty(a):
    pass
fish_cascade = cv2.CascadeClassifier('fish_cascade.xml')
cv2.namedWindow("trackbars")
cv2.createTrackbar("scale","trackbars",450,1000,empty)
cv2.createTrackbar("neig","trackbars",12,40,empty)
#cv2.createTrackbar("brightness","trackbars",100,255,empty)
video =cv2.VideoCapture('C:/Users/ASUS/Desktop/videos rov.mp4')


while True:
    #camerabrightness = cv2.getTrackbarPos("brightness", "trackbars")
    #video.set(10, camerabrightness)
    ret, img = video.read()
    #blur = cv2.GaussianBlur(img, (5, 5), 0)
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    scaleval = 1 + (cv2.getTrackbarPos("scale", "trackbars") / 1000)
    neig = cv2.getTrackbarPos("neig", "trackbars")
    fishs = fish_cascade.detectMultiScale(img, scaleval, neig)

    for (x, y, w, h) in fishs:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        #roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]


    cv2.imshow('img', img)
    #k = cv2.waitKey(1) & 0xff
    key = cv2.waitKey(1)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()