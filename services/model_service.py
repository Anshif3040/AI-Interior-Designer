from tensorflow.keras.models import load_model
from config import MODEL_PATH


def get_model():
    return load_model(MODEL_PATH)