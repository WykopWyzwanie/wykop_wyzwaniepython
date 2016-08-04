import os
import shutil
from datetime import datetime
from glob import glob
from os.path import abspath, getctime, getmtime, getsize, isdir, isfile


class CmdHandlers():
    def pwd():
        return os.getcwd()

    def cd(path):
        os.chdir(path)

    def mv(src, dst):
        shutil.move(src, dst)

    def ls():
        return '\n'.join(os.listdir(os.getcwd()))

    def touch(path):
        with open(path, 'w+'):
            pass

    def cp(src, dst):
        shutil.copy2(src, dst) if isfile(src) else shutil.copytree(src, dst)

    def rm(path):
        os.remove(path) if isfile(path) else shutil.rmtree(path)

    def info(path):
        filesizes = CmdHandlers._lst_file_sizes(path) if isdir(path) else [getsize(path)]
        return '\n'.join('{}: {}'.format(name, value) for (name, value) in [
            ('typ', 'plik' if isfile(path) else 'katalog' if isdir(path) else 'inny'),
            ('sciezka', abspath(path)),
            ('rozmiar', '{}B'.format(sum(filesizes))),
            ('liczba_plikow', sum(isfile(f) for f in os.listdir()) if isdir(path) else None),
            ('ctime', datetime.fromtimestamp(getctime(path)).date()),
            ('mtime', datetime.fromtimestamp(getmtime(path)).date()),
        ] if value is not None)

    def _lst_file_sizes(path):
        return list(getsize(f) for f in glob("{}/**".format(path), recursive=True) if isfile(f))


def parse(cmd, *args, **kwargs):
    return CmdHandlers.__dict__.get(cmd, lambda *a, **kw: None)(*args, **kwargs)


def main():
    command, args = '', []
    while command != 'exit':
        command, *args = input().split()
        print(parse(command, *args) or '')


if __name__ == '__main__':
    main()
