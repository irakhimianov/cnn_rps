from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from pathlib import Path


def add_text(
        image: Image,
        xy: tuple[int],
        text: str,
        font: ImageFont,
        spacing=0,
        fill=(0, 0, 0),
        stroke_width=0,
        stroke_fill=(0, 0, 0)
) -> Image:

    draw = ImageDraw.Draw(image, "RGB")
    draw.text(xy=xy,
              text=text,
              font=font,
              align='center',
              spacing=spacing,
              fill=fill,
              stroke_width=stroke_width,
              stroke_fill=stroke_fill)
    return image


def text_align(image: Image, font: ImageFont, text: str, pos: str, width: int = 0, height: int = 0) -> float | tuple[float]:
    width = width if width else image.size[0]
    height = height if height else image.size[1]

    if '\n' in text:
        text_width, text_height = font.getsize_multiline(text)
    else:
        text_width, text_height = font.getsize(text)
    if pos.lower() == 'h':
        return width // 2 - text_width // 2
    if pos.lower() == 'v':
        return height // 2 - text_height // 2
    if pos.lower() == 'hv':
        return (width // 2 - text_width // 2,
                height // 2 - text_height // 2)


def make_result_img(player_text: str, bot_text: str) -> BytesIO:
    font_path = Path('static', 'fonts', 'Symbola_hint.ttf')
    font = ImageFont.truetype(str(font_path), size=172)

    player_img_path = Path('static', 'temp.jpg')
    player_img = Image.open(player_img_path)
    s = player_img.size
    width = 300
    height = int(s[1] * (width / s[0]))
    player_img = player_img.resize(size=(width, height))

    res_img_path = Path('static', 'result_image.jpg')
    with Image.open(res_img_path) as image:
        image.paste(player_img, (256 - width // 2, 550 - height // 2))
        # player
        xy = text_align(image, font, player_text, 'h', width=512)
        image = add_text(image, (xy, 512), player_text, font)
        #bot
        xy = text_align(image, font, bot_text, 'h', width=1512)
        image = add_text(image, (xy, 512), bot_text, font)

    player_img.close()
    # image to bytes
    image_bio = BytesIO()
    image_bio.name = "image.jpeg"
    image.save(image_bio, 'JPEG')
    image_bio.seek(0)

    return image_bio
