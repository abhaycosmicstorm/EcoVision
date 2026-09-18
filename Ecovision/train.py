import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

# -----------------------------
# 1. Basic settings
# -----------------------------

IMG_SIZE = 224
BATCH_SIZE = 16
EPOCHS = 5

# -----------------------------
# 2. Load and preprocess data
# -----------------------------

datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    validation_split=0.2
)

train_data = datagen.flow_from_directory(
    "dataset",
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="training",
    shuffle=True
)

validation_data = datagen.flow_from_directory(
    "dataset",
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="validation",
    shuffle=False
)

# -----------------------------
# 3. Load MobileNetV2
# -----------------------------

base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(IMG_SIZE, IMG_SIZE, 3)
)

# Freeze the pretrained layers
base_model.trainable = False

# -----------------------------
# 4. Add our classification layers
# -----------------------------

x = base_model.output

x = GlobalAveragePooling2D()(x)

x = Dense(128, activation="relu")(x)

output = Dense(
    train_data.num_classes,
    activation="softmax"
)(x)

model = Model(
    inputs=base_model.input,
    outputs=output
)

# -----------------------------
# 5. Compile model
# -----------------------------

model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

# -----------------------------
# 6. Train model
# -----------------------------

history = model.fit(
    train_data,
    validation_data=validation_data,
    epochs=EPOCHS
)

# -----------------------------
# 7. Save model
# -----------------------------

model.save("waste_classifier.keras")

print("Model trained successfully!")

print("Class names:")
print(train_data.class_indices)