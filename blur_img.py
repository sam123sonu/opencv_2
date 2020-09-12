import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("saltpepper.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(20,20));
gblur = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,15)
bilateral = cv2.bilateralFilter(img,9,75,75)
titles = ['images','2D convolution','blur','gblur','median','bilateral']
images = [img,dst,blur,gblur,median,bilateral]
for i in range(6):
    plt.subplot(1,6,i+1),plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
k=cv2.waitKey()
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s') or ord('S'):
    cv2.imwrite('filter&blur.jpg',blur)
    cv2.destroyAllWindows()

