import os
from PIL import Image

# === Resize Configuration ===
resize_target_width = 800    # Change as needed
resize_target_height = 600   # Change as needed

# === Conversion Function ===
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

# === Resize Function ===
def resize_webp_images(input_folder, output_folder, width, height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.webp'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                with Image.open(input_path) as img:
                    resized_img = img.resize((width, height), Image.LANCZOS)
                    resized_img.save(output_path, 'WEBP')
                    print(f"Resized and saved: {output_path}")
            except Exception as e:
                print(f"Error resizing {input_path}: {e}")

# === Main Menu ===
def main():
    print("Image Processor Menu:")
    print("1. Convert images to WebP")
    print("2. Resize WebP images")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == '1':
        input_folder = r'D:\webp_converter\webp-input'
        output_folder = r'D:\webp_converter\webp-output'
        batch_convert(input_folder, output_folder)

    elif choice == '2':
        input_folder = r'D:\webp_converter\webp-output'  # You can change this
        output_folder = r'D:\webp_converter\webp-resized'
        resize_webp_images(input_folder, output_folder, resize_target_width, resize_target_height)

    else:
        print("Invalid choice. Please enter 1 or 2.")

    input("Press Enter to exit the program...")

if __name__ == "__main__":
    main()

