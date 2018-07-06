from PIL import Image
import os, glob
import numpy as np 
from sklearn import model_selection

classes = ["altocumulus","stratus","nimbostratus","altostratus","cirrocumulus","cirrostratus","cirrus","cumulonimbus","cumulus","stratocumulus"]
num_classes = len(classes)
image_size = 50
num_testdata = 150

X_train =[]
X_test = []
Y_train = []
Y_test = []


for index, classlabel in enumerate(classes):
    photos_dir = "./" + classlabel 
    files = glob.glob(photos_dir + "/*.jpg")
    for i, file in enumerate(files):
        if i >= 250:break
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)

        if i < num_testdata:
            X_test.append(data)
            Y_test.append(index)
        
        else:
            X_train.append(data)
            Y_train.append(index)

            for angle in range(-20,20,4):
                img_r = image.rotate(angle)
                data = np.asarray(img_r)
                X_test.append(data)
                Y_test.append(index)

                img_trans = image.transpose(Image.FLIP_LEFT_RIGHT)
                X_train.append(data)
                Y_train.append(index)


        #X.append(data)
        #Y.append(index)

X_train = np.array(X_train)
Y_train = np.array(Y_train)
X_test = np.array(X_test)
Y_test = np.array(Y_test)

#X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X,Y)

xy = (X_train, X_test, Y_train, Y_test)

np.save("./cloud.npy",xy)
