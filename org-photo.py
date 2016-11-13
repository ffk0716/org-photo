import os
import datetime
import shutil
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-p', '--path', required=True, help='path for photos')
parser.add_argument('-d', '--dry', action='store_true', help='dry run mode')
parser.add_argument('-s', '--sep', type = int, default = 0, help='separate day by X:00:00')
args = parser.parse_args()

dir1 = args.path
files = [name for name in os.listdir(dir1) if not os.path.isdir(os.path.join(dir1, name)) ]

sum_day_shift = 0
for file in files:
    try:
        raw_date = datetime.datetime.strptime(file[:19], '%Y-%m-%d %H.%M.%S')
    except ValueError:
        print 'ignore', file
        continue
    date = raw_date - datetime.timedelta(hours = args.sep)
    post_fix = ''
    if raw_date.date() != date.date():
        post_fix = '*'
        sum_day_shift += 1
    dir2 = os.path.join(dir1, str(date.date()))
    if not os.path.exists(dir2):
        os.makedirs(dir2)
    name1 = os.path.join(dir1, file)
    name2 = os.path.join(dir2, file)
    print name1, '->', name2, post_fix
    if not args.dry:
        shutil.move(name1, name2)

if sum_day_shift:
    print 'day-shifted files:', sum_day_shift
