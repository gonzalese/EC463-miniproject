import cv2
import numpy as np

cap = cv2.VideoCapture('cars2.mp4')
car_cascade = cv2.CascadeClassifier('cars.xml')
ncars=0
nframe=0

fb = open('/home/pi/car_detection/data.txt', 'a+')
while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	cv2.line(frame, (0,60),(439,60),(255,0,0),1)
	cv2.line(frame, (0,63),(439,65),(0,0,255),1) 

	cars=car_cascade.detectMultiScale(gray, 1.1,3)
	for (x,y,w,h) in cars:
		cv2.rectangle(frame,(x,y),(x+w, y+h), (0,255,0),1)
		if (y+h)<=75 and (y+h)>=70:
			ncars=ncars+1
	cv2.imshow('video',frame)

	nframe+=1
	print(ncars,nframe)
	fb.write(str(ncars))
	fb.write(" , ")
	fb.write(str(nframe))
	fb.write('\n')
	if cv2.waitKey(25) & 0xFF == ord('q'):
		break

fb.close()

cap.release()

cv2.destroyAllWindows()

