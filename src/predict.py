import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model = load_model("models/room_classifier.keras")

classes = [
    "bathroom",
    "bedroom",
    "home-office",
    "kitchen",
    "living-room",
    "pool"
]

img = image.load_img(
    "uploads/test.jpeg",
    target_size=(224,224)
)

img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0

prediction = model.predict(img_array)

print("Prediction:", classes[np.argmax(prediction)])