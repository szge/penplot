"""
convert images in the input directory to svg
"""

import os
from wand.image import Image
from pathlib import Path

INPUT_DIR = "input"
OUTPUT_DIR = "output"

def convert_images_to_svg():
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(INPUT_DIR, filename)
            output_path = os.path.join(OUTPUT_DIR, f"{os.path.splitext(filename)[0]}.svg")
            
            try:
                with Image(filename=input_path) as img:
                    img.format = 'svg'
                    img.save(filename=output_path)
                print(f"Successfully converted {filename} to SVG")
            except Exception as e:
                print(f"Error converting {filename}: {str(e)}")

if __name__ == "__main__":
    convert_images_to_svg()
