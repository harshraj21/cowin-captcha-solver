from keras.models import load_model
from helpers import resize_to_fit
from imutils import paths
import numpy as np
import cv2
import pickle

MODEL = "captcha_trained.hdf5"
MODEL_LABELS = "captcha_label.dat"
CAPTCHA_FILE = "captcha.png"
# CAPTCHA_FOLDER = "png"

with open(MODEL_LABELS, "rb") as f:
    lb = pickle.load(f)

model = load_model(MODEL)

captcha_image_files = []
captcha_image_files.append((CAPTCHA_FILE))
# captcha_image_files = list(paths.list_images(CAPTCHA_FOLDER))
# captcha_image_files = np.random.choice(captcha_image_files, size=(10,), replace=False)

for image_file in captcha_image_files:
    image = cv2.imread(image_file,0)

    img_mod = []
    img_mod.append((image[8:,8:35]))
    img_mod.append((image[8:,35:59]))
    img_mod.append((image[8:,59:85]))
    img_mod.append((image[8:,85:110]))
    img_mod.append((image[8:,110:138]))

    output = cv2.merge([image] * 3)
    prediction = []

    for letter_image in img_mod:
        letter_image = resize_to_fit(letter_image, 20, 20)
        letter_image = np.expand_dims(letter_image, axis=2)
        letter_image = np.expand_dims(letter_image, axis=0)
        prediction = model.predict(letter_image)
        letter = lb.inverse_transform(prediction)[0]
        prediction.append(letter)

    captcha_text = "".join(prediction)
    print("Predicated Text: {}".format(captcha_text))
    cv2.imshow("Output", output)
    cv2.waitKey()
