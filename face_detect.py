
import cv2

img = cv2.imread("boy.jpg")

#The OpenCV reads images in BGR format, so we need to convert BGR to GRAY.
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#The XML file contains Haar Cascade data for face detection.Load the classifier for the frontal face into a face-cascade 
#variable using cv2.CascadeClassifier() method.

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Haar cascade runs on grayscale images, so we need to convert our image to grayscale first

#We shall be using the detectMultiscale() module of the classifier.
#The detectMultiScale() requires an image name, which is gray in our case, to be used for face detection. This function will return a rectangle with coordinates(x,y,w,h)
#around the detected face.

faces = face_cascade.detectMultiScale(gray,1.1, 5)

print(len(faces))
#The result shows a 2D array with four values, the first two values as x,y (343, 84) coordinates to start the rectangle and
#the last two values for the width & height of 242 x242.

for (x,y,w,h) in faces:
       
       #The next step is to loop over all the coordinates it returned and draw rectangles around them using OpenCV. We will
       #be drawing a blue rectangle. To draw a rectangular shape over an image we can use the rectangle() method.
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  
       #cv2.rectangle(image, start_point, end_point, color,thickness)
  


       # Crop the image to save the face image.
       roi_color = img[y:y+h, x:x+w]
       cv2.imwrite("face.jpg",roi_color)
              
cv2.imshow('img',img)
cv2.waitKey(0)



