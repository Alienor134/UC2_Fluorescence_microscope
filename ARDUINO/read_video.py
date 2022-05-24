import cv2
import matplotlib.pyplot as plt
import numpy as np
from tkinter.filedialog import askopenfilename
file = askopenfilename()

vidcap = cv2.VideoCapture(file)
success,image = vidcap.read()
images = []
success = True
count = 0
while success:
  success,image = vidcap.read()
  images.append(image)   # save frame as JPEG file

  count += 1
  print(count)