from argparse import ArgumentParser
from collections import namedtuple
from glob import glob
import hashlib
from os.path import getsize, isfile
import os
import os.path
import sys


from sqlalchemy import Table, Column, Integer, String, create_engine, MetaData, ext, or_
from sqlalchemy.sql import select


AccumulatedSize = namedtuple('AccumulatedSize', 'extension size files')


def get_files(directory):
    yield from (f for f in glob("{}/**".format(directory), recursive=True) if isfile(f))


def get_files_info(directory):
    yield from ((extract_extension(f), getsize(f)) for f in get_files(directory))


def extract_extension(filename):
    return filename.split('.')[-1]


def accumulate_size_by_extension(files):
    d = {}
    for (ext, size) in files:
        acc = d.get(ext, AccumulatedSize(ext, 0, 0))
        d[ext] = AccumulatedSize(acc.extension, acc.size + size, acc.files + 1)
    yield from d.values()


def render_row(extension, size, histogram):
    return '{extension:>5}{size:>14}B{histogram:>60}\n'.format(**locals())


def get_his(value, total):
    return '#' * round(50 * value / total)


def main(directory):
    total_files, extensions = 0, set()
    for accumulated in accumulate_size_by_extension(get_files_info(directory)):
        total_files += accumulated.files
        extensions |= {accumulated}

    for (ext, size, files) in sorted(extensions, key=lambda acc: acc.files, reverse=True):
        yield render_row(ext, size, get_his(files, total_files))


def test_answer(operating_dir, output_file):
    rows = [r.strip() for r in main(operating_dir)]
    with open(output_file, 'r') as inp:
        to_be_tested = [r.strip() for r in inp.readlines()]

    if len(rows) != len(to_be_tested):
        print('Row count doesn\'t match.\n'
              'Expected: {}, got: {}.'.format(len(rows), len(to_be_tested)))
        return False

    rows, to_be_tested = sorted(rows), sorted(to_be_tested)

    for (expected, got) in zip(rows, to_be_tested):
        if expected != got:
            print('Invalid extension data.\n'
                  '<"{}"\n'
                  '>"{}"'.format(expected, got))
            return False

    return True


def load_tables(meta, engine, *names):
    tables = []
    for name in names:
        table = None
        try:
            table = Table(name, meta, autoload=True, autoload_with=engine)
        except:
            print('Cannot read {} table from db.'.format(name))
            raise
        tables.append(table)
    return tables

def md5(filepath):
    hash_md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def check_files(query_result):
    good = True
    for fid, filepath, ftype, md5sum_str in query_result:
        good = ftype == 'f'\
            and os.path.exists(filepath)\
            and md5(filepath) == md5sum_str\
            and good
    return good


def calculate_cardinality(dirpath):
    cardinality = 0
    for path in os.listdir(dirpath):
        object_path = os.path.join(dirpath, path)
        cardinality += calculate_cardinality(object_path) + 1\
                if os.path.isdir(object_path) else 1
    return cardinality


def check_dirs(query_result):
    good = True
    cardinality_dict = {}
    for did, dirpath, dtype, cardinality in query_result:
        if dirpath not in cardinality_dict:
            cardinality_dict[dirpath] = calculate_cardinality(dirpath)
        good = cardinality == cardinality_dict[dirpath]\
            and dtype == 'd'\
            and good
    return good


def test_db(operating_dir, db_path):
    engine = create_engine('sqlite:///{}'.format(db_path))
    meta = MetaData()
    objects, cardinality, checksums = load_tables(
        meta, engine, 'objects', 'cardinality', 'checksums')
    conn = engine.connect()
    files_stmt = select([objects.c.id, objects.c.path, objects.c.type,
        checksums.c.checksum]).where(objects.c.id == checksums.c.id)
    dirs_stmt = select([objects.c.id, objects.c.path, objects.c.type,
        cardinality.c.nbr_of_elements]).where(objects.c.id == cardinality.c.id)
    return check_files(engine.execute(files_stmt))\
        and check_dirs(engine.execute(dirs_stmt))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('operating_dir', metavar='operating_dir', type=str)
    parser.add_argument('output_file', metavar='output_file', type=str)
    parser.add_argument('version', default='easy', type=str)
    args = parser.parse_args()

    if args.version == 'easy':
        result = test_answer(args.operating_dir, args.output_file)
    elif args.version == 'hard':
        result = test_db(args.operating_dir, args.output_file)
    else:
        print('Invalid option value: only "easy" (default)/"hard" '
              'version allowed.''', file=sys.stderr)
        sys.exit(1)

    if result:
        print('All checks OK.')
    else:
        print('Errors found.')
