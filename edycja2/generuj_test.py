import os, os.path
import random
import sys
import tempfile


EXTENSIONS = (
        '.7z', '.BDMV', '.DX', '.M8M',
        '.PNCL', '.JPEG', '.jpg', '.doc',
        '.P', '.zip', '.cpp', '.docx',
        '.hpp', '.PCM', '.png', '.W3N',
        '.wp', '.Ynn', '.py', '.tar'
        )


def cumsum(l):
    total = 0
    for x in l:
        total += x
        yield total


DEVIATION = 50
DISTRIBUTION = tuple(cumsum([
    random.randint(1, DEVIATION) for _ in range(len(EXTENSIONS))]))
MAX_INDEX = max(DISTRIBUTION)


def random_ext():
    roulette = random.randint(0, MAX_INDEX)
    i = 0
    while DISTRIBUTION[i] < roulette:
        i += 1
    return EXTENSIONS[i]


def random_data(max_length=50):
    return os.urandom(random.randint(1, max_length))


def fill_directory(path, mind=2, maxd=10, minf=8, maxf=16, level=0):
    nbr_of_dirs = random.randint(max(0, mind - level), max(0, maxd - 2 * level))
    nbr_of_files = random.randint(max(0, minf - level), max(0, maxf - 2 * level))
    for _ in range(nbr_of_files):
        with tempfile.NamedTemporaryFile(dir=path, suffix=random_ext(), delete=False) as f:
            f.write(random_data())
    dirnames = [tempfile.mkdtemp(dir=path) for _ in range(nbr_of_dirs)]
    for dirname in dirnames:
        fill_directory(os.path.join(path, dirname), level=level+1)


def generate_test(main_dir_name):
    try:
        os.mkdir(main_dir_name)
    except OSError:
        sys.stderr.write('WARN: Katalog {} juz istnieje'.format(main_dir_name), file=sys.stderr)
    fill_directory(os.path.abspath(main_dir_name))


if __name__ == '__main__':
    generate_test('tst')
