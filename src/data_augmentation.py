import os
import cv2
import numpy as np
from imgaug import augmenters as iaa

# Define the annotations directory, images directory, and output directory
annotations_dir = r'C:\Users\aryam\Desktop\github\Diatomica\data\xmls'
images_dir = r'C:\Users\aryam\Desktop\github\Diatomica\data\images'
output_dir = r'C:\Users\aryam\Desktop\github\Diatomica\data\resized_and_augmented_images'

# Define the desired image size
image_size = (512, 512)  # resize images to 512x512

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through all XML files in the annotations directory
for filename in os.listdir(annotations_dir):
    if filename.endswith(".xml"):
        # Get the corresponding image file
        image_filename = filename.replace(".xml", "")
        image_path_png = os.path.join(images_dir, f"{image_filename}.png")
        image_path_jpg = os.path.join(images_dir, f"{image_filename}.jpg")

        # Check if the image file exists (either .png or .jpg)
        if os.path.exists(image_path_png):
            image_path = image_path_png
        elif os.path.exists(image_path_jpg):
            image_path = image_path_jpg
        else:
            print(f"Warning: Image file {image_filename} not found. Skipping.")
            continue

        # Load the image using OpenCV
        image = cv2.imread(image_path)

        # Check if the image was loaded successfully
        if image is None:
            print(f"Error: Unable to load image {image_filename}. Skipping.")
            continue

        # Normalize the image
        image = image / 255.0  # normalize pixel values to [0, 1]

        # Resize the image
        resized_image = cv2.resize(image, image_size)

        # Define the augmentation sequence (randomly generated for each image)
        aug_seq = iaa.Sequential([
            iaa.Fliplr(0.5),  # horizontal flip
            iaa.Affine(rotate=(-10, 10)),  # rotate by -10 to 10 degrees
            iaa.Add((-10, 10), per_channel=0.5),  # add random value to each pixel
            iaa.GaussianBlur(sigma=(0, 1.0))  # blur the image
        ])

        try:
            # Augment the image
            augmented_image = aug_seq.augment_image((resized_image * 255).astype(np.uint8))

            # Save the augmented image to the output directory
            output_path = os.path.join(output_dir, f"{image_filename}.jpg")  # save as .jpg
            cv2.imwrite(output_path, augmented_image)

            print(f"Resized, normalized, and augmented image {image_filename} and saved to {output_path}")
        except Exception as e:
            print(f"Error: Failed to augment image {image_filename}. Error: {e}")