import os
from PIL import Image
import pillow_avif

def convert_png_to_avif(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(
                output_folder, os.path.splitext(filename)[0] + ".avif"
            )

            image = Image.open(input_path)
            image.save(output_path, format="AVIF")
            print(f"Converted {input_path} to {output_path}")

        if filename.endswith(".PNG"):
            print(
                f"Please rename {filename} file extension to lowercase before converting. (png, jpg, etc.)"
            )
            for file in os.listdir(output_folder):
                os.remove(os.path.join(output_folder, file))
            break


input_folder = "png_input"
output_folder = "avif_output"

for file in os.listdir(output_folder):
    os.remove(os.path.join(output_folder, file))

convert_png_to_avif(input_folder, output_folder)
