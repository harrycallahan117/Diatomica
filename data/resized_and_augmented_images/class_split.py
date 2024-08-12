import xml.etree.ElementTree as ET
import os

# Define the base directory
base_dir = r'C:\\Users\\aryam\\Desktop\\github\\Diatomica\\data\\resized_and_augmented_images'

# Define the XML folder path
xml_folder_path = r'C:\Users\aryam\Desktop\github\Diatomica\data\xmls'

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

# Create folders for each species in train, test, and val directories
for dir_name in ['train', 'test', 'val']:
    dir_path = os.path.join(base_dir, dir_name)
    for species_name in species_names:
        folder_path = os.path.join(dir_path, species_name)
        os.makedirs(folder_path, exist_ok=True)

print(f"Created {len(species_names)} folders for each species in train, test, and val directories.")