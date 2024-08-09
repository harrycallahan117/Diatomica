import os
import random
from sklearn.model_selection import train_test_split

# Define the output directory where the augmented images are saved
output_dir = r'C:\Users\aryam\Desktop\github\Diatomica\data\resized_and_augmented_images'

# Get a list of all image files in the output directory
image_files = [f for f in os.listdir(output_dir) if f.endswith('.jpg')]

# Split the data into training, validation, and testing sets (80% for training, 10% for validation, 10% for testing)
train_files, val_test_files = train_test_split(image_files, test_size=0.2, random_state=42)
val_files, test_files = train_test_split(val_test_files, test_size=0.1/(0.2), random_state=42)

# Create directories for the training, validation, and testing sets
train_dir = os.path.join(output_dir, 'train')
val_dir = os.path.join(output_dir, 'val')
test_dir = os.path.join(output_dir, 'test')

for dir in [train_dir, val_dir, test_dir]:
    if not os.path.exists(dir):
        os.makedirs(dir)

# Move the images to their respective directories
for file in train_files:
    os.rename(os.path.join(output_dir, file), os.path.join(train_dir, file))
for file in val_files:
    os.rename(os.path.join(output_dir, file), os.path.join(val_dir, file))
for file in test_files:
    os.rename(os.path.join(output_dir, file), os.path.join(test_dir, file))

print("Data split into training, validation, and testing sets:")
print(f"Training set: {len(train_files)} images")
print(f"Validation set: {len(val_files)} images")
print(f"Testing set: {len(test_files)} images")