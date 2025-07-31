import os
from PIL import Image

def convert_to_webp(input_path, output_path):
    try:
        if os.path.exists(output_path):
            print(f"Skipping {input_path} as it's already converted.")
            return

        with Image.open(input_path) as img:
            img.save(output_path, 'WEBP')
            print(f"Image successfully converted to {output_path}")
    except Exception as e:
        print(f"Error occurred with {input_path}: {e}")

def batch_convert(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_folder, filename)
            output_filename = f"{os.path.splitext(filename)[0]}.webp"
            output_path = os.path.join(output_folder, output_filename)

            convert_to_webp(input_path, output_path)

def main():
    input_folder = r'C:/Users/se/works/webp-input'  # Replace with your folder path
    output_folder = r'C:/Users/se/works/webp-output'  # Replace with the folder where you want to save WebP images

    batch_convert(input_folder, output_folder)

    input("Press Enter to exit the program...")

if __name__ == "__main__":
    main()
