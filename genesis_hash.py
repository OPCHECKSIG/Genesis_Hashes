from hashlib import sha256
from PIL import Image

def hash_to_pixels(hash_str, width=16, height=16):
    hash_digest = sha256(hash_str.encode()).hexdigest()
    pixel_data = []
    for char in hash_digest:
        pixel_data.append(int(char, 16))

    # Create an image from the pixel data
    image = Image.new('RGB', (width, height))
    pixels = image.load()

    # Define a wider range of colors
    colors = [
        (255, 0, 0),     # Red
        (0, 255, 0),     # Green
        (0, 0, 255),     # Blue
        (255, 255, 0),   # Yellow
        (255, 0, 255),   # Magenta
        (0, 255, 255),   # Cyan
        (255, 128, 0),   # Orange
        (128, 0, 255),   # Purple
        (0, 255, 128),   # Lime
        (128, 128, 128), # Gray
    ]

    # Set pixel colors based on the hash data
    for y in range(height):
        for x in range(width):
            index = y * width + x
            color_index = pixel_data[index % len(pixel_data)] % len(colors)
            pixels[x, y] = colors[color_index]

    return image


def main():
    hash_str = input("Enter hash: ")
    pixel_art = hash_to_pixels(hash_str)

    # Save the pixel art as a WebP file
    output_filename = "pixel_art.webp"
    pixel_art.save(output_filename, "WEBP")

    print(f"Pixel art saved as {output_filename}")

if __name__ == "__main__":
    main()
