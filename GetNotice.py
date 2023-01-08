import requests
from bs4 import BeautifulSoup
import time
from collections import deque
import notifier


def get_notice():
    url = 'https://www.aiub.edu/category/notices/'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    notices = soup.select('ul.event-list li')

    notice_queue = deque([])
    try:
        with open('unseen.txt', 'r') as f:
            unseen = f.read().splitlines()
            for item in unseen:
                notice_queue.appendleft(item)
        f.close()
    except FileNotFoundError:
        print('File not found')
    print(notice_queue)
    ID = 0
    for child in notices:
        if child.select_one('div') is not None:
            title = child.select_one('div>h2').text
            date = [
                child.select_one('time span.day').text,
                child.select_one('time span.month').text,
                child.select_one('time span.year').text
            ]
            date_str = date[0] + ' ' + date[1] + ' ' + date[2]
            link = child.select_one('a').get('href')
            main_link = 'https://www.aiub.edu' + link
            encode = link
            ID += 1
            if encode not in notice_queue:
                notice_queue.appendleft(encode)
                notifier.notify(title=title, msg=date_str, link=main_link)
            if len(notice_queue) > 20:
                notice_queue.pop()

    unseen_data = ""
    n = len(notice_queue) - 1
    for i in range(n + 1):
        # unseen_data += item + '\n'
        x = notice_queue.pop() + '\n'
        unseen_data += x
        # print(x, end='')
    try:
        with open('unseen.txt', 'w') as fw:
            fw.write(unseen_data)
        fw.close()
    except FileNotFoundError:
        print('File not found')


if __name__ == '__main__':
    start = time.time()
    get_notice()
    end = time.time()
    print(end - start)
