import os
import json
from shutil import copyfile

from .config import OUTPUT_DIR, VIDEO_LIST, FILE_EXTENSION


def copy_master_files():
    if not os.path.exists(VIDEO_LIST):
        print("Video list file '%s' doesn't exists" % VIDEO_LIST)
        raise Exception

    with open(VIDEO_LIST, 'r') as video_list_file:
        video_list = json.load(video_list_file)

    for barcode, path in video_list.items():
        barcode_dir = os.path.join(OUTPUT_DIR, 'OSA-AIP_%s' % barcode)
        master_dir = os.path.join(barcode_dir, 'Content', 'Preservation')
        master_file = os.path.join(master_dir, '%s.%s' % (barcode, FILE_EXTENSION))

        print("Start copying '%s'" % path)
        copyfile(path, master_file)
        print("Finished copying file to '%s'" % master_file)

if __name__ == '__main__':
    copy_master_files()