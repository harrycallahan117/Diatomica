import os
import cv2

# Define the annotations directory, images directory, and output directory
annotations_dir = r'C:\Users\aryam\Desktop\github\Diatomica\data\xmls'
images_dir = r'C:\Users\aryam\Desktop\github\Diatomica\data\images'
output_dir = r'C:\Users\aryam\Desktop\github\Diatomica\data\resized_images'

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

        # Resize the image
        resized_image = cv2.resize(image, image_size)

        # Save the resized image to the output directory
        output_path = os.path.join(output_dir, f"{image_filename}.jpg")  # save as .jpg
        cv2.imwrite(output_path, resized_image)

        print(f"Resized image {image_filename} and saved to {output_path}")