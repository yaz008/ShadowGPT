from handler import KeyHandler
from pynput.keyboard import Listener

with Listener(on_press=KeyHandler()) as listener:
    listener.join()
