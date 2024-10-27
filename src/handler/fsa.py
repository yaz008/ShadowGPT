from dataclasses import dataclass
from enum import IntEnum
from typing import NamedTuple
from pynput.keyboard import Key, KeyCode
from handler._types import AnyKey

class State(IntEnum):
    INACTIVE: int = 0
    WAITING: int = 1
    MESSAGE: int = 2
    COMMAND: int = 3
    EXIT: int = 4

class Transition(NamedTuple):
    old: State
    new: State

@dataclass(slots=True)
class FSA:
    toggle: AnyKey
    exit: AnyKey
    state: State = State.INACTIVE

    def __update_state(self, key: AnyKey) -> State:
        if key == self.exit: return State.EXIT
        match self.state:
            case State.INACTIVE:
                if key == self.toggle: return State.WAITING
            case State.WAITING:
                if key == KeyCode(char='/'): return State.COMMAND
                return State.MESSAGE
        if key == self.toggle: return State.INACTIVE
        return self.state
        
    def update(self, key: AnyKey) -> Transition:
        transition: Transition = Transition(self.state, self.__update_state(key))
        self.state = transition.new
        return transition
    
    @property
    def is_active(self) -> bool:
        return not (self.state == State.INACTIVE)
