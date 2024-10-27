from handler import KeyHandler
from pynput.keyboard import Listener, Key

key_handler: KeyHandler = KeyHandler(toggle_key=Key.shift_r,
                                     status_key=Key.ctrl_r,
                                     exit_key=Key.down)
with Listener(on_press=key_handler) as listener:
    listener.join()
