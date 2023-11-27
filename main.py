import cv2
import matplotlib.pyplot as plt

def imgtogray(img):
    r,g,b = img[...,0], img[...,1], img[...,2]
    gray = 0.299*r + 0.587*g + 0.144*b
    return gray

image = cv2.imread(r"C:\Users\Arkan\Downloads\Lenna.png")

ret,thresh = cv2.threshold(imgtogray(image), 70,255,0)

imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.subplot(131),plt.imshow(imgRGB, cmap='gray'), plt.title('Original')
plt.subplot(132),plt.imshow(imgtogray(image), cmap='gray'), plt.title('Tons de Cinza')
plt.subplot(133), plt.imshow(thresh, cmap='gray'), plt.title('Binarizada')
plt.show()