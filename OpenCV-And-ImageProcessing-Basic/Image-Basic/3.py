#THINGS WE WILL BE LEARNING 
'''
1. Finding the Shape of Color Image
2. Understanding Channels
3. Splitting and Merging Channels 
4. Correlating with a Greyscale Image
'''

import cv2

pic = cv2.imread('messi2.png')


(b,g,r) = cv2.split(pic)

cv2.imshow("BLUE",b)
cv2.waitKey(0)

cv2.imshow("green",g)
cv2.waitKey(0)

cv2.imshow("RED",r)
cv2.waitKey(0)

merged_image = cv2.merge((b,g,r))
cv2.imshow("Merged Image",merged_image)
cv2.waitKey(0)

gray = cv2.cvtColor(merged_image, cv2.COLOR_BGR2GRAY)
x = gray.shape
print(x)

# RGB image - 3 channels 
# Grayscale image - 1 channel 

