import os
from PIL import Image
from pathlib import Path
from time import time


def uniq_fname(prefix: str, suffix: str) -> str:
    return f"{prefix} - {str(int(time() * 100))}.{suffix}"


mypath = Path(r'D:\Projects\cnn_diploma\cnn\dataset')
only_images = [f for f in Path.iterdir(mypath) if Path.is_file(Path(mypath, f))]

if not Path.exists(Path(mypath, 'edited')):
    Path.mkdir(Path(mypath, 'edited'))

for image in only_images:
    with Image.open(Path(mypath, image)) as img:
        img_width, img_height = img.size
        img = img.crop((430, 0, img_width - 578, img_height))
        img = img.resize(size=(150, 150))
        img.save(fp=Path(mypath,
                         'edited',
                         uniq_fname('test', Path(image).name.split('.')[-1])))
