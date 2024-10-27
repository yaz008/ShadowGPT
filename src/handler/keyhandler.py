from dataclasses import dataclass, field
from pynput.keyboard import Key, KeyCode, HotKey
from j2pipeline import Prompt
from clipboard import Clipboard

AnyKey = Key | KeyCode

@dataclass(slots=True)
class KeyHandler:
    toggle: AnyKey
    exit: AnyKey
    __is_activated: bool = field(default=False, init=False)
    __message: str = field(default=str(), init=False)
    __prompt: Prompt[str] = field(init=False)

    def __post_init__(self) -> None:
        self.__prompt = Prompt[str](path='prompts\\.j2')

    def __call__(self, pressed_key: AnyKey) -> None:
        match [pressed_key]:
            case [self.exit]: exit(code=0)
            case [self.toggle]: self.__on_toggle()
            case _:
                if self.__is_activated:
                    self.__on_pressed(pressed_key)

    def __on_toggle(self) -> None:
        if self.__is_activated and self.__message != str():
            with Clipboard() as clipboard:
                clipboard.data = self.__prompt(text=self.__message)
                self.__message = str()
        self.__is_activated = not self.__is_activated

    def __on_pressed(self, pressed_key: AnyKey) -> None:
        if self.__message[-2:] == '``': self.__message = str()
        if pressed_key == Key.backspace:
            self.__message = self.__message[:-1]
        if isinstance(pressed_key, KeyCode):
            self.__message += pressed_key.char
        self.__message += {
            Key.enter: '\n',
            Key.space: ' '
        }.get(pressed_key, str())
