from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model
from keras.layers import Input,Flatten,Dense,Dropout,GlobalAveragePooling2D
from keras.applications.resnet50 import ResNet50
import keras
from keras.applications.imagenet_utils import preprocess_input,decode_predictions
from keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt


img_path = 'img_path/cat.jpeg'
img = image.load_img(img_path,target_size= (224,224))
plt.imshow(img)
plt.show()





