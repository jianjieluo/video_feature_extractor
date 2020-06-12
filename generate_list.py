import argparse
import glob
import os
import csv
import re

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default=None)
    parser.add_argument('--dst', type=str, default='input.csv')
    parser.add_argument('--suffix', type=str, default='mp4')
    
    args = parser.parse_args()
    return args

def path2vid(path):
    basename = os.path.basename(path).split('.')[0]
    gid = int(re.findall(r'\d+', basename)[0])
    return gid

if __name__ == "__main__":
    args = parse_args()
    
    video_list = sorted(glob.glob(os.path.join(args.dir, '*.%s' % args.suffix)))

    fieldnames = ['video_path', 'video_id']
    writer = csv.DictWriter(open(os.path.join(args.dst), 'w', encoding='utf-8'), fieldnames=fieldnames, delimiter=',')
    writer.writeheader()

    for video_path in video_list:
        vid = path2vid(video_path)
        writer.writerow({'video_path': video_path, 'video_id': str(vid)})
