from os import listdir
from dataclasses import dataclass, field
from pynput.keyboard import Key, KeyCode
from j2pipeline import Prompt
from plyer import notification
from clipboard import Clipboard
from root import PROJECT_ROOT

AnyKey = Key | KeyCode

@dataclass(slots=True)
class KeyHandler:
    toggle: AnyKey
    status: AnyKey
    exit: AnyKey
    __is_activated: bool = field(default=False, init=False)
    __message: str = field(default=str(), init=False)
    __prompt: Prompt[str] = field(init=False)

    def __post_init__(self) -> None:
        self.__prompt = Prompt[str](path=f'{PROJECT_ROOT}\\prompts\\blank.j2')

    def __call__(self, pressed_key: AnyKey) -> None:
        match [pressed_key]:
            case [self.exit]: exit(code=0)
            case [self.status]: self.__on_status()
            case [self.toggle]: self.__on_toggle()
            case _:
                if self.__is_activated:
                    self.__extend_message(pressed_key)

    def __on_status(self) -> None:
        status: str = f'Activated: {self.__is_activated}\n'
        status += f'Message: {self.__message[:20]}'
        status += '...\n' if len(self.__message) > 20 else '\n'
        notification.notify(
            title='Status',
            message=status,
            app_name='ShadowGPT',
            timeout=5
        )

    def __on_toggle(self) -> None:
        if self.__is_activated and self.__message != str():
            match self.__message[0]:
                case '/': self.__execute_command(command=self.__message[1:])
                case _: self.__set_clipboard()
            self.__message = str()
        self.__is_activated = not self.__is_activated

    def __extend_message(self, pressed_key: AnyKey) -> None:
        if pressed_key == Key.backspace:
            self.__message = self.__message[:-1]
        if isinstance(pressed_key, KeyCode):
            self.__message += pressed_key.char
        self.__message += {
            Key.enter: '\n',
            Key.space: ' '
        }.get(pressed_key, str())

    def __execute_command(self, command: str) -> None:
        match command.split(sep=' '):
            case ['template' | 't', filename]:
                template_path: str = f'{PROJECT_ROOT}\\prompts\\{filename}.j2'
                if f'{filename}.j2' in listdir(f'{PROJECT_ROOT}\\prompts'):
                    self.__prompt = Prompt[str](path=template_path)
                 
    def __set_clipboard(self) -> None:
        with Clipboard() as clipboard:
            clipboard.data = self.__prompt(prompt=self.__message)
