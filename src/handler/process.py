from typing import Callable

class Process:
    @staticmethod
    def split(sep: str, element: str) -> Callable[[str], str]:
        return lambda x: x.split(sep=sep)[int(element)].strip()
