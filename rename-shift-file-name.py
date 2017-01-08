import datetime


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

ext = 'mts'
files = glob.glob("*." + ext)

for file in files:
    suff = re.search(r'(\d*-\d*-\d* \d*.\d*.\d*)(.*).*\.' + ext,
            file).groups()
    a = datetime.datetime.strptime(suff[0], "%Y-%m-%d %H.%M.%S")
    a = a + datetime.timedelta(hours=1)
    new_name = a.strftime('%Y-%m-%d %H.%M.%S') + suff[1] + '.mts'
    if new_name != file:
        print('{} -> {}'.format(file, new_name))
        #os.rename(file, new_name)
