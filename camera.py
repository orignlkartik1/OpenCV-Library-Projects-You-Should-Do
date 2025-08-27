import cv2 as cv

cam=cv.VideoCapture(0)

count=0

while True:

    ret,frame=cam.read()

    if not ret:
        print("Can't recieve frame.")
        break

    frame=cv.imshow("Camera",frame)

    k=cv.waitkey(1)


    # if you click "esc" then it stop running.
    if k==27:
        print("Closed.")
        break

    if k==32:
        # if you click "space" button . It click your image and save on your cwd.
        img="Image_{}.png".format(count)
        cv.imwrite(img,frame)
        print(img,"save !")
        count+=1
cam.release()
cam.destroyAllwindows()

#please read all old files first for this. after reading those file .You can undrstand this

