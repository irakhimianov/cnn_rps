import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from keras_preprocessing import image
from keras_preprocessing.image import ImageDataGenerator


model = tf.keras.models.load_model('model.h5')
print(model.summary())
name_classes = ['Бумага', 'Камень', 'Ножницы']

img_path = 'test.png'
img = image.load_img(img_path, target_size=(150, 150))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
images = np.vstack([x])
classes = model.predict(images, batch_size=10)
print(classes)
print(name_classes[np.argmax(classes)])
img = mpimg.imread(img_path)
plt.imshow(img)
plt.axis('Off')
plt.show()