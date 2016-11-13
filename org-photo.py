import os
import sys
import re
import datetime
import shutil

dir1 = sys.argv[1]

files = [name for name in os.listdir(dir1) if not os.path.isdir(os.path.join(dir1, name)) ]

for file in files:
    try:
        a = datetime.datetime.strptime(file[:10], '%Y-%m-%d')
    except ValueError:
        print 'ignore', file
        continue
    dir2 = os.path.join(dir1, str(a.date()))
    if not os.path.exists(dir2):
        os.makedirs(dir2)
    name1 = os.path.join(dir1, file)
    name2 = os.path.join(dir2, file)
    print name1, '->', name2
    shutil.move(name1, name2)
