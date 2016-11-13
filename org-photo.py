import os
import datetime
import shutil
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-p', '--path', required=True, help='path for photos')
parser.add_argument('-d', '--dry', action='store_true', help='dry run mode')
parser.add_argument('-s', '--sep', type = int, default = 0, help='separate day by X:00:00')
args = parser.parse_args()

root = args.path
files = [name for name in os.listdir(root) if not os.path.isdir(os.path.join(root, name)) ]

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
    new_dir = str(date.date())
    file2 = os.path.join(new_dir, file)
    print file, '->', file2, post_fix
    if not args.dry:
        new_dir = os.path.join(root, new_dir)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        shutil.move(os.path.join(root, file), os.path.join(new_dir, file))

if sum_day_shift:
    print 'day-shifted files:', sum_day_shift
