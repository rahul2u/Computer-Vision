# Obtaining an image from a url 
#REMEMBER -> skimage reads in RGB format
#OPENCV - used BGR convention
import cv2
from skimage import io

rabbit = io.imread('http://www.verypdf.com/wordpress/wp-content/uploads/2011/11/clip_image00455.jpg')
converted_image = cv2.cvtColor(rabbit,cv2.COLOR_RGB2BGR)
cv2.imshow('URL image',converted_image)
cv2.waitKey(0)
