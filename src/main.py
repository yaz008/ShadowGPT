from handler import KeyHandler
from pynput.keyboard import Listener, Key

key_handler: KeyHandler = KeyHandler(toggle=Key.shift_r,
                                     status=Key.ctrl_r,
                                     exit=Key.down)
with Listener(on_press=key_handler) as listener:
    listener.join()
