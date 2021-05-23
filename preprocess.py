import os
import os.path
import glob
import cv2

CAPTCHA_FOLDER = "png"
OUTPUT_FOLDER = "classified"

# CAPTCHA_IMAGE_FOLDER = "idk"
# OUTPUT_FOLDER = "idk/classified"

captcha_images = glob.glob(os.path.join(CAPTCHA_FOLDER, "*"))
counts = {}

for (i, captcha_image_file) in enumerate(captcha_images):
    print("[INFO] processing image {}/{}".format(i + 1, len(captcha_images)))
    filename = os.path.basename(captcha_image_file)
    captcha_correct_text = os.path.splitext(filename)[0]
    img = cv2.imread(captcha_image_file,0)

    img_mod = []
    img_mod.append((img[8:,8:35]))
    img_mod.append((img[8:,35:59]))
    img_mod.append((img[8:,59:85]))
    img_mod.append((img[8:,85:110]))
    img_mod.append((img[8:,110:138]))

    for letter_image, letter_text in zip(img_mod, captcha_correct_text):
        save_path = os.path.join(OUTPUT_FOLDER, letter_text)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        count = counts.get(letter_text, 1)
        p = os.path.join(save_path, "{}.png".format(str(count).zfill(6)))
        cv2.imwrite(p, letter_image)
        counts[letter_text] = count + 1