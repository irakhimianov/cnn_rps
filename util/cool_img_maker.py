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
    # font_path = Path('static', 'fonts', 'Symbola_hint.ttf')
    font_path = (r'../static/fonts/Symbola_hint.ttf')
    font = ImageFont.truetype(str(font_path), size=72)

    # player_img_path = Path('static', 'temp.jpg')
    player_img_path = (r'../static/temp.jpg')
    player_img = Image.open(player_img_path)
    player_img = player_img.resize(size=(150, 150))

    # res_img_path = Path('static', 'result_image.jpg')
    res_img_path = (r'../static/result_image.jpg')
    with Image.open(res_img_path) as image:
        image.paste(player_img, (256 - 75, 512 - 75))
        # player
        xy = text_align(image, font, player_text, 'h', width=512)
        image = add_text(image, (xy, 512), player_text, font)
        #bot
        xy = text_align(image, font, bot_text, 'h', width=1512)
        image = add_text(image, (xy, 512), bot_text, font)

        image.save(Path('static', 'cool_img.jpg'))

    player_img.close()


make_result_img('✋', '✌')
