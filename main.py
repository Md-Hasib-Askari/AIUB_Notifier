import threading
import time
from GetNotice import get_notice


def looping():
    start = time.time()
    get_notice()
    end = time.time()
    print(end - start)
    threading.Timer(10, looping).start()


if __name__ == '__main__':
    looping()
