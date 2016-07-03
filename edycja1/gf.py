import os
import random
import sys
import tempfile
import time

if __name__ == '__main__':
    assert len(sys.argv) > 1
    k = int(sys.argv[1])
    for _ in range(k):
        f = tempfile.NamedTemporaryFile(dir='.', delete=False)
        os.utime(f.name, (random.randint(0, int(time.time())),
                          random.randint(0, int(time.time()))))
