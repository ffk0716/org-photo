import os
import glob
from PIL import Image
from PIL.ExifTags import TAGS
import time  
import re

def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret

#os.chdir("/path/to/images")

ext = 'jpg'
files = glob.glob("*." + ext)

for file in files:
    time = get_exif(file)["DateTimeOriginal"]
    f = re.sub(r'\d*-\d*-\d* \d*.\d*.\d*(.*).*\.' + ext,
            r'\1',
            file)
    new_name = re.sub(r'(\d*):(\d*):(\d*) (\d*):(\d*):(\d*)',
            r'\1-\2-\3 \4.\5.\6',
            time)
    new_name = new_name.encode("utf-8")
    new_name += f
    new_name += '.' + ext 
    if new_name != file:
        print('{} -> {}'.format(file, new_name))
        #os.rename(file, new_name)
