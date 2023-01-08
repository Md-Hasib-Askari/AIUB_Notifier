import os
import time

from winotify import Notification, audio, Notifier


def print_hello(link):
    os.system("start " + link)
    print("Hello, World!")


def notify(title="TITLE", msg="DUMMY MESSAGE", link="https://www.aiub.edu/"):
    cwd = os.getcwd()
    toaster = Notification(
        app_id='AIUB Notifier',
        title=title,
        msg=msg,
        duration="long",
        icon=cwd + "\\static\\aiub-logo.png"
    )
    toaster.set_audio(audio.Default, loop=False)
    # Notifier.register_callback(print_hello)
    toaster.add_actions(label="Open", launch=link)
    toaster.show()


if __name__ == '__main__':
    notify()
