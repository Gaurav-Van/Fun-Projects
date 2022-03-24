from cv2 import cv2
import datetime as dt

cv = cv2

capture = cv.VideoCapture(0)

# Reading HaarCascade File
haar_Cascade = cv.CascadeClassifier("HaarCascade_Face.xml")

j = 0
color = ((0, 0, 255), (0, 255, 0), (255, 0, 0))

while True:
    isTrue, frame = capture.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect_vid = haar_Cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)
    for i in faces_rect_vid:
        if j > 2:
            j = 0
        f1 = i
        Result_vid = cv.rectangle(frame, (f1[0], f1[1]), (f1[0] + f1[2], f1[1] + f1[3]), color=color[j], thickness=2)
        date_time = dt.datetime.now()
        tod = date_time.strftime(" %A, %d-%B-%y  and Time is %H : %M : %S")
        cv.putText(Result_vid, f"{tod}", (f1[0] - 20, f1[1] - 10), color=(0, 255, 0), fontFace=cv.FONT_ITALIC,
                   fontScale=0.5, thickness=1)
        j = j + 1
        # print(f"No of Faces Found in video=  {len(faces_rect_vid)}")
        cv.imshow("Result-vid", Result_vid)

    if cv.waitKey(20) & 0xFF == ord('s'):  # if letter s is pressed, break out of the video
        break

capture.release()  # release the capture instance
cv.destroyAllWindows()
