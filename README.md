# class-106-v2

face detection using Haar feature-based Cascade Classifiers
------------------------------------------------------------------
1. Detect face in an image
2.detect faces on each frame of videos from the webcam.
------------------------------------------------------------------

Object Detection using Haar feature-based cascade classifiers is an effective method proposed by Paul
Viola and Michael Jones in the 2001 paper, "Rapid Object Detection using a Boosted Cascade of Simple Features

----------------------------------------------------------------
Face Detection detects the presence of a face in an image. 


if you want to identify the face with pre-stored images then we would write a code that compares the detected image of a face. 
This process is known as face recognition
------------------------------------------------------------------
For computers to detect the face of humans, we need to  create an algorithm that will classify the image into two
parts, face and rest of image

OpenCV has face detection classifiers data stored in the form XML file format, which can be readily used in a
program. This classifier is known as the Haar Cascade Classifier

There are multiple Haar Cascade Classifiers available in the OpenCV library. These classifiers XML files get
downloaded along with opencv-python installation using pip to download the cv2 package.
All the Haar Cascade files are located in the “data” folder where cv2 is installed in your system.

ex:
Full Path to cv2/data folder:
C:/Users/preet/AppData/Local/Programs/Python/Python39/Lib/site-packages/cv2/data

----------------------------------------------------------------
Alternatively, the classifier files can be accessed from

https://github.com/opencv/opencv/tree/4.x/data/haarcascades

-----------------------------------------------------------------

Haar Cascade is an Object Detection Algorithm used to identify object in an image or a real-time video
As far as the human face is considered, the nose, lips, eyebrows, forehead, and eyes are considered as the
most relevant features of a face.


The haar cascade algorithm is looking for these features in an image to identify a face.
It does this by creating patterns with pixels next to each other, these patterns are either edge detection or line detection:

Edge Detection pattern is a series of white pixels above a series of black pixels or reverse, this pattern can be horizontal or vertical

Line Detection pattern is series of black pixels sandwiched between series of white pixels or reserve i.e white pixels sandwiched between black,
this pattern can also be vertical or horizontal
-------------------------------------------------------------------------
The Haar Cascade algorithm creates hundreds of such patterns and will then go through each of them to identify the closest feature of the face like eyebrow (edge pattern), lips (line pattern), nose (line pattern), eyes (edge pattern).

 In order to identify all the features, the Haar Cascade Edge/Lines Feature runs over the image portion(the rectangle box), known as the detection window
 
 
 The detection process is repeated multiple times, again and again till all the features are captured. The whole image traversed using the detection window and Haar Cascade features
 
 Gradually, it will cover more features of the face, using edge and line patterns, like eyebrow (edge pattern), lips (line pattern), nose (line pattern), eyes (edge pattern).
 
 The classifier will keep running till it is able to identify the features and at the end it combines all the features and returns a rectangle output in the form of x, y the starting point from where face is detected, along with width & height.
 
 
