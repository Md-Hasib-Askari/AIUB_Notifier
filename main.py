import threading
import time
from GetNotice import get_notice


def looping(refresh_period=300):
    start = time.time()
    get_notice()
    end = time.time()
    print(end - start)
    threading.Timer(refresh_period, looping).start()


if __name__ == '__main__':
    looping()
