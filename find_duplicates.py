import os
from PIL import Image
from collections import defaultdict

# Function to check for duplicates
def find_duplicates(folder_path):
    image_hashes = defaultdict(list)
    duplicates = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            with open(os.path.join(root, file), 'rb') as f:
                img_hash = hash(f.read())
                if img_hash in image_hashes:
                    duplicates.append((file, image_hashes[img_hash]))
                else:
                    image_hashes[img_hash].append(file)
    return duplicates

# Example usage:
duplicates = find_duplicates("C:\Users\856ma\Downloads\bkhlpbqirempjay8wdfsfb.zip")
print("Duplicates found:", duplicates)
