"""
Remove Background Application

A Python application for removing background from pictures containing persons and/or animals.
Loads images from pics_input folder and saves processed images to pics_output folder.
"""

import os
from pathlib import Path
from rembg import remove
from PIL import Image
import sys


def get_input_files(input_dir):
    """Get all JPG and PNG files from the input directory."""
    input_path = Path(input_dir)
    if not input_path.exists():
        print(f"Error: Input directory '{input_dir}' does not exist.")
        return []
    
    supported_extensions = {'.jpg', '.jpeg', '.png'}
    files = []
    
    for ext in supported_extensions:
        files.extend(input_path.glob(f'*{ext}'))
        files.extend(input_path.glob(f'*{ext.upper()}'))
    
    return sorted(files)


def remove_background_from_image(input_path, output_dir):
    """Remove background from a single image and save it as PNG."""
    try:
        # Read the input image
        with open(input_path, 'rb') as input_file:
            input_data = input_file.read()
        
        # Remove background
        output_data = remove(input_data)
        
        # Create output filename (same name but with .png extension)
        output_filename = input_path.stem + '.png'
        output_path = Path(output_dir) / output_filename
        
        # Save the output image
        with open(output_path, 'wb') as output_file:
            output_file.write(output_data)
        
        print(f"✓ Processed: {input_path.name} -> {output_filename}")
        return True
    
    except Exception as e:
        print(f"✗ Error processing {input_path.name}: {str(e)}")
        return False


def main():
    """Main function to process all images."""
    # Define directories
    input_dir = Path('pics_input')
    output_dir = Path('pics_output')
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)
    
    # Get all input files
    input_files = get_input_files(input_dir)
    
    if not input_files:
        print(f"No JPG or PNG files found in '{input_dir}' directory.")
        return
    
    print(f"Found {len(input_files)} image(s) to process...")
    print("-" * 50)
    
    # Process each image
    success_count = 0
    for input_file in input_files:
        if remove_background_from_image(input_file, output_dir):
            success_count += 1
    
    print("-" * 50)
    print(f"Processing complete: {success_count}/{len(input_files)} image(s) processed successfully.")


if __name__ == '__main__':
    main()

