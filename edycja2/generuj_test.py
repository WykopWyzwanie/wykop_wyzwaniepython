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


def random_ext():
    return random.choice(EXTENSIONS)


def random_data(max_length=50):
    return os.urandom(random.randint(1, max_length))


def random_dir():
    pass


def fill_directory(path, mind=3, maxd=12, minf=5, maxf=10, level=0):
    nbr_of_dirs = random.randint(max(0, mind - level), max(0, maxd - 2 * level))
    nbr_of_files = random.randint(max(0, minf - level), max(0, maxf - 2 * level))
    print('{}/{}'.format(nbr_of_dirs, nbr_of_files))
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
        print('WARN: Katalog {} juz istnieje'.format(main_dir_name), file=sys.stderr)
    fill_directory(os.path.abspath(main_dir_name))


if __name__ == '__main__':
    generate_test('tst')
