import os
import shutil

# Define the directories
root_dir = r'C:\Users\aryam\Desktop\github\Diatomica\data\resized_and_augmented_images'
train_dir = os.path.join(root_dir, 'train')
test_dir = os.path.join(root_dir, 'test')
val_dir = os.path.join(root_dir, 'val')

# Define the class folders
class_folders = [f'class{i}' for i in range(1, 6)]

# Create the class folders
for dir in [train_dir, test_dir, val_dir]:
    for class_folder in class_folders:
        os.makedirs(os.path.join(dir, class_folder), exist_ok=True)

# Define the labels.csv files
train_labels_file = os.path.join(train_dir, 'labels.csv')
test_labels_file = os.path.join(test_dir, 'labels.csv')
val_labels_file = os.path.join(val_dir, 'labels.csv')

# Move images to their corresponding class folders
for dir, labels_file in [(train_dir, train_labels_file), (test_dir, test_labels_file), (val_dir, val_labels_file)]:
    if not os.path.exists(labels_file):
        print(f"Error: {labels_file} does not exist. Skipping...")
        continue

    with open(labels_file, 'r') as f:
        for line in f.readlines():
            filename, label = line.strip().split(',')
            label = int(label)  # Ensure label is an integer
            if label < 1 or label > 5:
                print(f"Error: Invalid label value {label} for file {filename}. Skipping...")
                continue

            class_folder = f'class{label}'
            src_file = os.path.join(dir, filename)
            if not os.path.exists(src_file):
                print(f"Error: File {src_file} does not exist. Skipping...")
                continue

            dst_file = os.path.join(dir, class_folder, filename)
            try:
                shutil.move(src_file, dst_file)
            except PermissionError:
                print(f"Error: Permission denied to move file {src_file} to {dst_file}. Skipping...")
                continue