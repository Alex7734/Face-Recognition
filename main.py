import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('test.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 6)

for (x, y, w, h) in faces:
	cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

scale_percent = 60 
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

cv2.imshow('img', resized)
cv2.waitKey()