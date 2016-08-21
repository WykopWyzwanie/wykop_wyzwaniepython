import os
import shutil
import time
from argparse import ArgumentParser


def get_year_and_month_of_modification(file):
    modtime = time.localtime(os.path.getmtime(file))
    return modtime.tm_year, '0{}'.format(modtime.tm_mon)[-2:]


def main(directory):
    os.chdir(directory)
    for file in os.listdir('.'):
        year, month = get_year_and_month_of_modification(file)
        destination_dir = '{}/{}'.format(year, month)
        os.makedirs(destination_dir, exist_ok=True)
        shutil.move(file, destination_dir)


if __name__ == '__main__':
    parser = ArgumentParser('Move files to directories based on modification date.')
    parser.add_argument('operating_dir', metavar='operating_dir', type=str)

    main(parser.parse_args().operating_dir)
