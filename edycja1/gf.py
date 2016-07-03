import os
import random
import sys
import tempfile
import time
import string


RANDOM_DATA_LEN = 10

def random_data():
    return "".join(random.SystemRandom().choice(
        string.ascii_lowercase + string.digits) for _ in range(RANDOM_DATA_LEN))

if __name__ == '__main__':
    assert len(sys.argv) > 1
    k = int(sys.argv[1])
    n = k // 3
    rds = [random_data() for _ in range(n)]
    for _ in range(k):
        f = tempfile.NamedTemporaryFile(dir='.', delete=False)
        with open(f.name, 'w') as tf:
            tf.write(rds[random.randint(0, n - 1)])
        os.utime(f.name, (random.randint(0, int(time.time())),
                            random.randint(0, int(time.time()))))
