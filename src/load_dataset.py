import os
import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level=logging.ERROR)

annotations_dir = r'C:\Users\aryam\Desktop\github\Diatomica\data\xmls'  # replace with your annotations directory

def parse_xml_file(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        logging.error(f"Error parsing {file_path}: {e}")
        return None

def extract_image_info(root):
    filename_elem = root.find('filename')
    filename = filename_elem.text if filename_elem is not None else ""

    size_elem = root.find('size')
    if size_elem is not None:
        width_elem = size_elem.find('width')
        height_elem = size_elem.find('height')
        if width_elem is not None and height_elem is not None:
            width = int(width_elem.text)
            height = int(height_elem.text)
        else:
            width = 0
            height = 0
    else:
        width = 0
        height = 0

    return filename, width, height

def extract_object_info(root):
    objects_elem = root.find('objects')
    if objects_elem is not None:
        for object_elem in objects_elem.findall('object'):
            id_elem = object_elem.find('id')
            name_elem = object_elem.find('name')
            bbox_elem = object_elem.find('bbox')
            if id_elem is not None and name_elem is not None and bbox_elem is not None:
                object_id = int(id_elem.text)
                object_name = name_elem.text
                xmin_elem = bbox_elem.find('xmin')
                xmax_elem = bbox_elem.find('xmax')
                ymin_elem = bbox_elem.find('ymin')
                ymax_elem = bbox_elem.find('ymax')
                if xmin_elem is not None and xmax_elem is not None and ymin_elem is not None and ymax_elem is not None:
                    xmin = int(xmin_elem.text)
                    xmax = int(xmax_elem.text)
                    ymin = int(ymin_elem.text)
                    ymax = int(ymax_elem.text)
                    print(f"Object {object_id} ({object_name}): x={xmin}:{xmax}, y={ymin}:{ymax}")
                else:
                    logging.error(f"Invalid bounding box for object {object_id} ({object_name})")
            else:
                logging.error(f"Invalid object {object_id} ({object_name})")
    else:
        logging.error("No objects found")

for file in os.listdir(annotations_dir):
    file_path = os.path.join(annotations_dir, file)
    root = parse_xml_file(file_path)
    if root is not None:
        filename, width, height = extract_image_info(root)
        print(f"Image {filename}: width={width}, height={height}")
        extract_object_info(root)