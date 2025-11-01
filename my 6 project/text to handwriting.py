from PIL import Image, ImageDraw, ImageFont
import textwrap, random, sys

def txt_to_handwriting(text, font_path, output="output.png"):
    img = Image.new("RGB", (1654, 2339), (250, 245, 235))  # A4 size background
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, 48)

    x, y = 120, 150
    for line in textwrap.wrap(text, width=45):
        jitter = random.randint(-2, 2)
        draw.text((x + jitter, y + jitter), line, font=font, fill=(20, 20, 20))
        y += 70
    img.save(output)
    print("✅ Saved:", output)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Use: python txt_to_handwriting.py input.txt font.ttf")
        sys.exit()

    txt_path, font_path = sys.argv[1], sys.argv[2]
    with open(txt_path, "r", encoding="utf-8") as f:
        content = f.read()
    txt_to_handwriting(content, font_path)
