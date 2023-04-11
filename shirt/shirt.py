import sys
import os
from PIL import Image, ImageOps

def main():
    # check number of command-line arguments
    if len(sys.argv) != 3 and len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    # Get the input and output file names and extensions
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    # Define a set of supported file extensions
    supported_files = {".jpeg", ".jpg", ".png"}

    # Check if the input and output files have valid and matching extensions
    if input_ext not in supported_files:
        sys.exit("Invalid input")

    if output_ext not in supported_files:
        sys.exit("Invalid output")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    # Check if the file specified by the user exists
    image_file = sys.argv[1]
    if not os.path.isfile(image_file):
        sys.exit('Input does not exist')

    # Call the overlay_images function to perform the task
    overlay_images(input_file, output_file)

def overlay_images(input_image, output_image):

    try:
        # Open the shirt image with a context manager
        with Image.open("shirt.png") as shirt:
            # Open the input image with a context manager
            with Image.open(input_image) as base_image:
                # Resize and crop the input image to match the shirt image size
                base_image = ImageOps.fit(base_image, shirt.size)
                # Overlay the shirt image on the input image using alpha channel as mask
                base_image.paste(shirt, (0, 0), shirt)
                # Save the output image with the given name or path
                base_image.save(output_image)

    except FileNotFoundError:
        # Handle the case when the input file does not exist
        sys.exit(f"Input {input_image} does not exist")

    except OSError:
        # Handle the case when the input file cannot be converted
        sys.exit(f"Cannot convert {input_image}")

# Execute the main function only when this script is run directly
if __name__ == "__main__":
    main()