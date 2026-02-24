#!/usr/bin/env python3
"""
Skillforge Photo → ASCII Art Converter
Converts a portrait photo into terminal-style ASCII art for use in README.md
Usage: python3 scripts/photo_to_ascii.py /path/to/photo.jpg
"""

import sys
from PIL import Image

# ASCII character ramp from dark to light
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=60):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)  # 0.55 corrects for font aspect ratio
    return image.resize((new_width, new_height))

def to_grayscale(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    chars = [ASCII_CHARS[pixel * len(ASCII_CHARS) // 256] for pixel in pixels]
    return chars

def convert(image_path, width=60):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        sys.exit(1)

    image = resize_image(image, width)
    image = to_grayscale(image)
    chars = pixels_to_ascii(image)
    w = image.width
    ascii_str = "\n".join(
        "".join(chars[i:i+w]) for i in range(0, len(chars), w)
    )
    return ascii_str

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/photo_to_ascii.py /path/to/photo.jpg [width=60]")
        sys.exit(1)

    path = sys.argv[1]
    width = int(sys.argv[2]) if len(sys.argv) > 2 else 60
    ascii_art = convert(path, width)

    print(ascii_art)

    # Save to file
    output_path = path.rsplit(".", 1)[0] + "_ascii.txt"
    with open(output_path, "w") as f:
        f.write(ascii_art)
    print(f"\n✅ ASCII art saved to: {output_path}")
    print("Wrap it in triple backticks in your README.md")
