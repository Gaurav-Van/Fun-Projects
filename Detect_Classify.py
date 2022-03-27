# Open-Cv
# Model to Detect and Classify between 10 Simpsons Characters

import os
import caer
import canaro
import numpy as np
from cv2 import cv2
import gc
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import LearningRateScheduler
import matplotlib.pyplot as plt

cv = cv2

# While building a Deep CV model - all the data [ here images] has to be of same size
# so we have to resize
IMG_SIZE = (80, 80)
channels = 1
char_path = r"C:\Users\Asus\PycharmProjects\Fun-Projects\Project - 2\simpsons_dataset"

# char ->  characters
char_dict = {}
for char in os.listdir(char_path):
    char_dict[char] = len(os.listdir(os.path.join(char_path, char)))
print(char_dict)
print("\n\n")

# ---- Sorting [ in order to get top 10] ---------

values = []
Characters_high_to_low = {}
values = sorted(char_dict.values(), reverse=True)
for i in values:
    for j in char_dict.keys():
        if char_dict[j] == i:
            Characters_high_to_low[j] = i
print(Characters_high_to_low)
print("\n\n")

Characters = []
count = 0
for i in Characters_high_to_low.keys():
    Characters.append(i)
    count = count + 1
    if count > 10:
        break
print(Characters)

# Creating the training data
train_data = caer.preprocess_from_dir(char_path, Characters, channels=channels, IMG_SIZE=IMG_SIZE,
                                      isShuffle=True)

print(len(train_data))

features, labels = caer.sep_train(train_data, IMG_SIZE=IMG_SIZE)

# Normalizing the features

features = caer.normalize(features)

# one - hot encoding of labels

labels = to_categorical(labels, len(Characters))

x_train_feat, x_val_feat, y_train_lab, y_val_lab = caer.train_val_split(features, labels, val_ratio=0.20)

del train_data
del features
del labels
gc.collect()

# Image Data generator -> Synthesize (make) new images from existing images - to introducr some Randomness

data_gen = canaro.generators.imageDataGenerator()
BATCH_SIZE = 32
EPOCHS = 10
train_gen = data_gen.flow(x_train_feat, y_train_lab, batch_size=BATCH_SIZE)

# Creating the Model

model = canaro.models.createSimpsonsModel(IMG_SIZE=IMG_SIZE, channels=channels, output_dim=
len(Characters), loss="binary_crossentropy", decay=1e-6,
                                          learning_rate=0.001, momentum=0.9, nesterov=True)

model.summary()

callbacks_list = [LearningRateScheduler(canaro.lr_schedule)]

training = model.fit(train_gen,
                     steps_per_epoch=len(x_train_feat) // BATCH_SIZE,
                     epochs=EPOCHS,
                     validation_data=(x_val_feat, y_val_lab),
                     validation_steps=len(y_val_lab) // BATCH_SIZE,
                     callbacks=callbacks_list)

test_path = r"C:\Users\Asus\PycharmProjects\Fun-Projects\Project - 2\kaggle_simpson_testset\lisa_simpson_46.jpg"
img = cv.imread(test_path)
img1 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img1)
plt.show()


def prepare(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.resize(img, IMG_SIZE)
    img = caer.reshape(img, IMG_SIZE, 1)
    return img


predictions = model.predict(prepare(img))

# Getting class with the highest probability
print(Characters[np.argmax(predictions[0])])
