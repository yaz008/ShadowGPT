from os import listdir
from re import findall
from dataclasses import dataclass, field

from j2pipeline import Prompt
from clipboard import Clipboard
from handler.process import Process
from handler.fsa import FSA, State, Transition
from notifier import notify

from pynput.keyboard import Key, KeyCode
from root import PROJECT_ROOT

from handler._types import AnyKey

@dataclass(slots=True)
class KeyHandler:
    toggle_key: AnyKey
    status_key: AnyKey
    exit_key: AnyKey
    __state: FSA = field(init=False)
    __buffer: str = field(default=str(), init=False)
    __prompt: Prompt[str] = field(init=False)

    def __post_init__(self) -> None:
        self.__state = FSA(toggle=self.toggle_key, exit=self.exit_key)
        self.__prompt = Prompt[str](path=f'{PROJECT_ROOT}\\prompts\\blank.j2')

    def __call__(self, pressed_key: AnyKey) -> None:
        if pressed_key == self.status_key:
            notify(title='Status', message=self.status)
        match self.__state.update(key=pressed_key):
            case Transition(_, State.EXIT):
                exit(code=0)
            case Transition(State.WAITING | State.MESSAGE, State.MESSAGE):
                self.__extend_buffer(key=pressed_key)
            case Transition(State.COMMAND, State.COMMAND):
                self.__extend_buffer(key=pressed_key)
            case Transition(State.MESSAGE, State.INACTIVE):
                with Clipboard() as clipboard:
                    try:
                        clipboard.data = self.__prompt(prompt=self.__buffer)
                    except UnicodeEncodeError:
                        clipboard.data = 'UnicodeEncodeError'
                self.__buffer = str()
            case Transition(State.COMMAND, State.INACTIVE):
                self.__execute_command()
                self.__buffer = str()

    @property
    def status(self) -> str:
        result: str = f'State: {self.__state.state.name.capitalize()}\n'
        result += f'Buffer: \"{self.__buffer}\"'
        return result

    def __extend_buffer(self, key: AnyKey) -> None:
        if key == Key.backspace:
            self.__buffer = self.__buffer[:-1]
        if isinstance(key, KeyCode):
            self.__buffer += key.char
        if key == Key.space:
            self.__buffer += ' '
        if key == Key.enter:
            self.__buffer += '\n'

    def __execute_command(self) -> None:
        pattern: str = r'[a-z]+|[0-9]+|(?<=\").*(?=\")|(?<=\').*(?=\')'
        match findall(pattern=pattern, string=self.__buffer):
            case ['template' | 't', filename]:
                template_path: str = f'{PROJECT_ROOT}\\prompts\\{filename}.j2'
                if f'{filename}.j2' in listdir(f'{PROJECT_ROOT}\\prompts'):
                    self.__prompt = Prompt[str](path=template_path)
            case ['process' | 'p', funcname, *args]:
                self.__prompt.process = getattr(Process, funcname)(*args)
