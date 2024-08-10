import os
import csv

# Define constants
NUM_CLASSES = 5

# Define the directories for train, val, and test images
train_dir = r'C:\Users\aryam\Desktop\github\Diatomica\data\resized_and_augmented_images\train'
val_dir = r'C:\Users\aryam\Desktop\github\Diatomica\data\resized_and_augmented_images\val'
test_dir = r'C:\Users\aryam\Desktop\github\Diatomica\data\resized_and_augmented_images\test'

# Generate the labels.csv file for train images
labels = [1, 2, 3, 4, 5]

# Generate the labels.csv file
with open(os.path.join(train_dir, 'labels.csv'), 'w', newline='') as f:
    for i, filename in enumerate(os.listdir(train_dir)):
        if filename.endswith('.jpg'):
            label = labels[i % len(labels)]
            f.write(f'{filename},{label}\n')

# Generate labels.csv for val images
val_image_files = [f for f in os.listdir(val_dir) if f.endswith('.jpg')]
with open(os.path.join(val_dir, 'labels.csv'), 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i, image_file in enumerate(val_image_files):
        label = (i % NUM_CLASSES) + 1  # Calculate label for val and test
        writer.writerow([image_file, label])

# Generate labels.csv for test images
test_image_files = [f for f in os.listdir(test_dir) if f.endswith('.jpg')]
with open(os.path.join(test_dir, 'labels.csv'), 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i, image_file in enumerate(test_image_files):
        label = (i % NUM_CLASSES) + 1  # Calculate label for val and test
        writer.writerow([image_file, label])