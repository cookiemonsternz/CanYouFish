import tensorflow as tf
from tensorflow import keras as k
import numpy as np
import os
import matplotlib.pyplot as plt
# I'm creating a simple convolutional neural network to do live classification on whether a person is, or is not, a fish.
# Because this is intended to be more comedic, I am not too worried on training data diversity or accuracy, but rather the 
# speed and efficiency of the model. Hopefully this should be able to run at 10 fps on a smartphone. I'll be using a simple
# keras cnn for this and will be using an (unfortunately) hand labeled set of images of fish and people (maybe a few other, e.g cat idk)

# MAKE SURE TO FILTER FILES FIRST BY RUNNING PREPROCESS.PY

# Take the images and load them into dataset (also resizes)
image_size = (256, 256)
batch_size = 128

train_ds, val_ds = k.utils.image_dataset_from_directory(
    "images",
    validation_split=0.2,
    subset="both",
    seed=1337,
    image_size=image_size,
    batch_size=batch_size,
)

plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(int(labels[i]))
        plt.axis("off")
plt.show()

def make_model(input_shape, num_classes):
    inputs = k.Input(shape=input_shape)

    # Entry block
    x = k.layers.Rescaling(1.0 / 255)(inputs)
    x = k.layers.Conv2D(128, 3, strides=2, padding="same")(x)
    x = k.layers.BatchNormalization()(x)
    x = k.layers.Activation("relu")(x)

    previous_block_activation = x  # Set aside residual

    for size in [256, 512, 728]:
        x = k.layers.Activation("relu")(x)
        x = k.layers.SeparableConv2D(size, 3, padding="same")(x)
        x = k.layers.BatchNormalization()(x)

        x = k.layers.Activation("relu")(x)
        x = k.layers.SeparableConv2D(size, 3, padding="same")(x)
        x = k.layers.BatchNormalization()(x)

        x = k.layers.MaxPooling2D(3, strides=2, padding="same")(x)

        # Project residual
        residual = k.layers.Conv2D(size, 1, strides=2, padding="same")(
            previous_block_activation
        )
        x = k.layers.add([x, residual])
        previous_block_activation = x

    x = k.layers.SeparableConv2D(1024, 3, padding="same")(x)
    x = k.layers.BatchNormalization()(x)
    x = k.layers.Activation("relu")(x)

    x = k.layers.GlobalAveragePooling2D()(x)
    if num_classes == 2:
        units = 1
    else:
        units = num_classes

    x = k.layers.Dropout(0.25)(x)
    outputs = k.layers.Dense(units, activation=None)(x)
    return k.Model(inputs, outputs)

model = make_model(input_shape=image_size + (3,), num_classes=2)

epochs = 50

callbacks = [
    k.callbacks.ModelCheckpoint("save_at_{epoch}.keras"),
]

model.compile(
    optimizer=k.optimizers.Adam(1e-3),
    loss=k.losses.BinaryCrossentropy(from_logits=True),
    metrics=[k.metrics.BinaryAccuracy()],
)

model.fit(
    train_ds, 
    epochs=epochs, 
    callbacks=callbacks, 
    validation_data=val_ds,
)

# My model was trained on google colab. I uploaded the data set to my drive, mounted it, and ran the code there.
# this was significantly faster than running it on my local machine lol

model.evaluate(val_ds)