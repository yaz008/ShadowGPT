import win32clipboard
from typing import Any

class Clipboard:
    @property
    def data(self) -> str:
        return win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)

    @data.setter
    def data(self, __data: str, /) -> None:
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(__data)

    def __enter__(self) -> 'Clipboard':
        win32clipboard.OpenClipboard()
        return self

    def __exit__(self, *_: Any | None) -> None:
        win32clipboard.CloseClipboard()
