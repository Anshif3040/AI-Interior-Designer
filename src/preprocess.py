import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator 

# Image size for the model
IMG_SIZE = (224, 224)

# Create image generator
datagen = ImageDataGenerator(
    rescale=1./255,      # Normalize pixels
    validation_split=0.2 # 80% train, 20% validation
)

# Training dataset
train_generator = datagen.flow_from_directory(
    "images",
    target_size=IMG_SIZE,
    batch_size=32,
    class_mode="categorical",
    subset="training"
)

# Validation dataset
validation_generator = datagen.flow_from_directory(
    "images",
    target_size=IMG_SIZE,
    batch_size=32,
    class_mode="categorical",
    subset="validation"
)

print("\nClasses Found:")
print(train_generator.class_indices)

print("\nTraining Samples:")
print(train_generator.samples)

print("\nValidation Samples:")
print(validation_generator.samples)