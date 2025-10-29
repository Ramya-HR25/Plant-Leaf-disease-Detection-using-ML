import os
from PIL import Image, UnidentifiedImageError

DATASET_DIR = 'PlantVillage'

def is_image_file(filepath):
    try:
        with Image.open(filepath) as img:
            img.verify()  # Will raise an exception if not an image
        return True
    except (UnidentifiedImageError, OSError):
        return False

for class_folder in os.listdir(DATASET_DIR):
    class_path = os.path.join(DATASET_DIR, class_folder)
    if not os.path.isdir(class_path):
        continue
    for fname in os.listdir(class_path):
        fpath = os.path.join(class_path, fname)
        if not os.path.isfile(fpath):
            continue
        if not is_image_file(fpath):
            print(f"Deleting corrupted or non-image file: {fpath}")
            os.remove(fpath) 