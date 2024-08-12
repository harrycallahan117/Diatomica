import os
import xml.etree.ElementTree as ET

# Define the base directory
base_dir = r'C:\\Users\\aryam\\Desktop\\github\\Diatomica\\data\\resized_and_augmented_images'

# Define the XML folder path
xml_folder_path = r'C:\Users\aryam\Desktop\github\Diatomica\data\xmls'

# Create a dictionary to store the species names and their corresponding image counts
species_image_counts = {}
# Create a set to store unique species names
species_names = set()

# Iterate over all XML files in the folder
for filename in os.listdir(xml_folder_path):
    if filename.endswith(".xml"):
        # Parse the XML file
        tree = ET.parse(os.path.join(xml_folder_path, filename))
        root = tree.getroot()

        # Iterate over all object elements
        for object_element in root.findall('.//object'):
            # Find the name element
            name_element = object_element.find('.//name')
            # Get the text of the name element
            species_name = name_element.text
            # Add the species name to the set
            species_names.add(species_name)

        # Find the corresponding image file
        image_filename = filename.replace('.xml', '.jpg')

        # Determine the split (train, val, or test) based on the image file path
        for dir_name in ['train', 'test', 'val']:
            dir_path = os.path.join(base_dir, dir_name)
            if os.path.exists(os.path.join(dir_path, image_filename)):
                # Initialize the image count for the species
                if species_name not in species_image_counts:
                    species_image_counts[species_name] = {}
                if dir_name not in species_image_counts[species_name]:
                    species_image_counts[species_name][dir_name] = 0

                # Generate the new filename
                new_filename = f"{species_name}_{species_image_counts[species_name][dir_name] + 1}.jpg"

                # Check if the new filename exists
                while os.path.exists(os.path.join(dir_path, species_name, new_filename)):
                    species_image_counts[species_name][dir_name] += 1
                    new_filename = f"{species_name}_{species_image_counts[species_name][dir_name] + 1}.jpg"

                # Rename the image file
                os.rename(os.path.join(dir_path, image_filename), os.path.join(dir_path, species_name, new_filename))

print("Renamed image files based on species names.")