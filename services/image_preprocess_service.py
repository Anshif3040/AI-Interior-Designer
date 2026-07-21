import os
import numpy as np
from tensorflow.keras.preprocessing import image


def save_and_preprocess_image(file):

    os.makedirs("static/uploads", exist_ok=True)

    filepath = os.path.join("static", "uploads", file.filename)

    file.save(filepath)

    uploaded_image = file.filename

    img = image.load_img(filepath, target_size=(224, 224))

    img_array = image.img_to_array(img)

    img_array = np.expand_dims(img_array, axis=0)

    img_array = img_array / 255.0

    return filepath, uploaded_image, img_array