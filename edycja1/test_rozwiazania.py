import datetime
import os
import os.path as path
import sys
import time

def check_file(out_dir, in_dir, filepath):
    mdate = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
    ystr = str(mdate.year)
    mstr = ("{:0>2}").format(mdate.month)
    if out_dir == ystr and in_dir == mstr:
        return True
    else:
        print("zle: {}, {}, {}".format(filepath, ystr, mstr))
        return False


def get_dirs_filter(path):
    return filter(lambda x: os.path.isdir(os.path.join(path, x)), os.listdir(path))

def check_solution(working_dir):
    all_files = 0
    good_moves = 0
    lambda x, filepath: os.path.isdir()
    for out_dir in get_dirs_filter(working_dir):
        for in_dir in get_dirs_filter(os.path.join(working_dir, out_dir)):
            for f in os.listdir(os.path.join(working_dir, out_dir, in_dir)):
                if check_file(out_dir, in_dir,
                        os.path.join(working_dir, out_dir, in_dir, f)):
                    good_moves += 1
                all_files += 1
    print("{}/{} plikow dobrze skatalogowanych".format(good_moves, all_files))


if __name__ == '__main__':
    working_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    check_solution(os.path.abspath(working_dir))
