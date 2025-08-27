import cv2 as cv

# This function use for open camera. If you have more than two cameras you can pass argument 1,2,... . O is for your default camera.
cap=cv.Videocapture(0) # you can also play any video passing file name in place of 0.

four=cv.VideoWriter_fourcc(*'XVID')
out=cv.VideoWriter("output.avi",four,20,(640,480))
# use if for checking camera is open or not.
if not cap.isOpened():
    print("Your camera is not working.")
    exit()

# for video start
while True:

    # read your video frame or rate
    ret,frame=cap.read()

    # checking from video getting frame or not
    if not ret:
        print("Can't receive frame.")
        break
    out.write(frame)
    # you have choice to convert your video stream in any color. Its convert your color
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    # start your video and taking your window name as argument
    cv.imshow("Window",gray)

    if cv.waitKey(1)==ord('q'):
        break
cap.release()
out.release()
cv.destroyAllwindows()

  