import os
import datetime
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', required=True, help='path for photos')
parser.add_argument('-d', '--dry', action='store_true', help='dry run mode')
args = parser.parse_args()

dir1 = args.path
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
    if not args.dry:
        shutil.move(name1, name2)
