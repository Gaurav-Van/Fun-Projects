Using Tensorflow implementation of keras
Using concept of open cv and face detection and recognition

# Short - overview

This Projects - takes in images of 20 Simpsons characters, we only took top 10
which will be fed to model as training data and on new data , it will predict the name of the Character

# Some short important points
 - While building a Deep CV model - all the data [ here images] has to be of same size, so we have to resize
 - Image Data generator -> Synthesize (make) new images from existing images - to introduce some Randomness


2nd Project - [ A Mini Project ] -> Web_cam_Face_Detection
  - Here face and eye detection is achieved by Haar Cascade Classifier
  - Got the 4 coordinates of face and then applied haar cascade classifier of eye within the region of face
  - datetime is used to show the real time while detecting the face on webcam

3rd Project - [ A Mini Project ] -> Number Plate Detection_Recog
  - Here Number Plate detection is achieved by Haar Cascade Classifier
  - With those 4 coordinates, extracted the Region of interest image
  - and applied reader from easyocr on that ROI, to detect numbers of Number Plate
  - PS: With the help of cv.write - saved that ROI in a Separate folder [Saved_Number_Plate]