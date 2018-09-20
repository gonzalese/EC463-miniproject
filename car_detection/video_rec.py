import cv2
from picamera import PiCamera
from time import sleep

camera=PiCamera()
camera.resolution = (640,480)
camera.framerate = 15

camera.start_preview()
camera.start_recording('/home/pi/car_detection/car_video.h264')
sleep(20)
camera.stop_recording()
camera.stop_preview()


