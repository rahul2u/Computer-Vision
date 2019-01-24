import cv2
coffeePic = cv2.imread('coffee.jpg')

#changing picture to grayscale 
gray = cv2.cvtColor(coffeePic, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayed Image",gray)

#writing the gray Image as newfile.jpg
cv2.imwrite("newfile.jpg",gray)
cv2.waitKey(0)