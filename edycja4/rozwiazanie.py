import sys
from threading import Thread
from argparse import ArgumentParser
from contextlib import redirect_stdout
from queue import Queue

import markdown


def convert_to_html(queue):
    md = markdown.Markdown()
    while True:
        print(md.convert(queue.get()))


def read_text(queue):
    while True:
        queue.put(sys.stdin.readline())


def main():
    q = Queue()
    Thread(target=read_text, args=(q,)).start()
    conv = Thread(target=convert_to_html, args=(q,))
    conv.start()
    conv.join()


if __name__ == "__main__":
    parser = ArgumentParser('Convert markdown to html.')
    parser.add_argument('output_file', metavar='output_file', type=str)
    with open(parser.parse_args().output_file, 'w+') as f:
        with redirect_stdout(f):
            main()
