import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "models", "room_classifier.keras")

UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")

OUTPUT_FOLDER = os.path.join(BASE_DIR, "outputs")

DATABASE = os.path.join(BASE_DIR, "interior.db")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")