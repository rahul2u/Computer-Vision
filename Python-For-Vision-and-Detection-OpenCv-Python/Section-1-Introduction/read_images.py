import cv2

img = cv2.imread('canvas.png',1)
# 0 flag means - color images
# 1 flag means is - graw images
# -1 flag means is - alpha channel images
print(img)

# show the image in window
cv2.imshow('lena',img)
key =cv2.waitKey(0)  # 0 means permanet or 5000 milisecond or 5 second
cv2.destroyAllWindows()

if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('lena.jpg',img)
    cv2.destroyAllWindows()





