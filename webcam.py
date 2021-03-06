import cv2

# get the camera as a variable
webcam = cv2.VideoCapture(0)

while True:
    state,img = webcam.read()
    if state:
        cv2.imshow('webcam', img)
        if cv2.waitKey(1) == ord('q'):
            print('camera stopped')
            break
    else:
        print('camera not working')
        break
webcam.release()
cv2.destroyAllWindows()
 
 
# before running install module 
#pip install opencv-contrib-python
        