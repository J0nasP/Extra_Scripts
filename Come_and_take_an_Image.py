import cv2, tkinter
from tkinter import filedialog, messagebox 
import numpy as np
from matplotlib import pyplot as plt





def ShowAndSave():
    img = cv2.imread('butterfly.jpg', 0)
    cv2.imshow('image', img)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord('s'):
        cv2.imwrite('butterfly.png', img)
        cv2.destroyAllWindows()

def showAndPlot():
    img = cv2.imread('butterfly.jpg',0)
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()



img = filedialog.askopenfile(title = "Choose an image:")