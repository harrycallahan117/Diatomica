import tensorflow as tf
from tensorflow.keras.applications import MobileNet
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.metrics import CategoricalAccuracy
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import backend as K
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau

# Define the MobileNet model
base_model = MobileNet(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Freeze the base model layers
for layer in base_model.layers:
    layer.trainable = False

# Add a global average pooling layer
x = base_model.output
x = GlobalAveragePooling2D()(x)

# Add a dense layer for classification
x = Dense(5, activation='softmax')(x)  # Assuming 5 classes

# Define the model
model = Model(inputs=base_model.input, outputs=x)

# Define the loss function and metrics
loss_fn = CategoricalCrossentropy(from_logits=False)
metric_fn = CategoricalAccuracy()

# Compile the model
model.compile(optimizer=Adam(), loss=loss_fn, metrics=[metric_fn])

# Define the data generators
train_datagen = ImageDataGenerator(
    rescale=1./255,
    horizontal_flip=True,
    rotation_range=30,
    brightness_range=[0.5, 1.5]
)
validation_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    r'C:\Users\aryam\Desktop\github\Diatomica\data\resized_and_augmented_images\train',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

validation_generator = validation_datagen.flow_from_directory(
    r'C:\Users\aryam\Desktop\github\Diatomica\data\resized_and_augmented_images\val',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory(
    r'C:\Users\aryam\Desktop\github\Diatomica\data\resized_and_augmented_images\test',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

# Check data quality and preprocessing
print("Data quality and preprocessing checks:")
print("Train dataset shape:", train_generator.samples)
print("Validation dataset shape:", validation_generator.samples)
print("Test dataset shape:", test_generator.samples)

# Evaluate baseline performance (random predictions)
from sklearn.metrics import accuracy_score
from sklearn.dummy import DummyClassifier

dummy_clf = DummyClassifier(strategy='uniform')
dummy_clf.fit(test_generator.classes, test_generator.classes)  # Fit the dummy classifier
y_pred = dummy_clf.predict(test_generator.classes)
y_true = test_generator.classes

baseline_accuracy = accuracy_score(y_true, y_pred)
print(f'Baseline accuracy: {baseline_accuracy:.3f}')

# Train the model
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // 32,
    epochs=20,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // 32
)

# Save the model
model.save('mobilenet_model.keras')