import os
from PIL import Image

def convert_to_webp(input_path, output_path):
    try:
        # Check if the output file already exists
        if os.path.exists(output_path):
            print(f"Skipping {input_path} as it's already converted.")
            return

        # Open the image file
        with Image.open(input_path) as img:
            # Convert the image to WebP and save it
            img.save(output_path, 'WEBP')
            print(f"Image successfully converted to {output_path}")
    except Exception as e:
        print(f"Error occurred with {input_path}: {e}")

def batch_convert(input_folder, output_folder):
    # Check if the output folder exists, create if not
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        # Check if the file is a JPG, JPEG, or PNG image
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_folder, filename)
            # Construct the output filename with .webp extension
            output_filename = f"{os.path.splitext(filename)[0]}.webp"
            output_path = os.path.join(output_folder, output_filename)

            # Call the function to convert the image to WebP
            convert_to_webp(input_path, output_path)

def main():
    # Example usage:
    input_folder = r'C:/Users/se/works/webp-input'  # Replace with your folder path
    output_folder = r'C:/Users/se/works/webp-output'  # Replace with the folder where you want to save WebP images

    batch_convert(input_folder, output_folder)

    # Wait for the user to press Enter before closing
    input("Press Enter to exit the program...")

if __name__ == "__main__":
    main()
