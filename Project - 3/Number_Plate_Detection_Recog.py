import cv2
from easyocr import Reader
cv = cv2

Num_Plate = cv.CascadeClassifier(r"Haar_Cascade/HaarCascade_Number-Plate.xml")

url = r"Photos [Number_plate_Detection]/NP-6.jpg"
list_np = url.split("/")

img = cv.imread(url)

imgRoi = img.copy()

color = (255, 0, 0)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

n_plate = Num_Plate.detectMultiScale(gray, 1.1, 5)

for (x, y, w, h) in n_plate:
    imgRoi = img[y:y + h, x:x + w]
    cv.imwrite("Saved_Number_Plate/Number_Plate_Scanned_" + list_np[1], imgRoi)

reader = Reader(['en'])
detection = reader.readtext(imgRoi)
print(detection)


for (x, y, w, h) in n_plate:
    cv.rectangle(img, (x, y), (x + w, y + h), color=(255, 0, 0), thickness=2)
    cv.putText(img, f"{detection[0][1]}", (x - 8, y - 8), fontFace=cv.FONT_ITALIC, fontScale=1, color=color, thickness=1)
    cv.imshow("ROI", imgRoi)

cv.imshow("Result", img)

while True:
    if cv.waitKey(1) & 0xFF == ord('s'):
        cv.rectangle(img, (0, 0), (300, 100), color=(255, 0, 0), thickness=cv.FILLED)
        cv.putText(img, "SCANNED_SAVED", (20, 50), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 255, 0),
                   thickness=2)
        cv.imshow("Result", img)
        cv.waitKey(3000)
        break
