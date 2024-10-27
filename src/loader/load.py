from json import load
from root import PROJECT_ROOT

def load_config() -> dict[str, str]:
    with open(file=f'{PROJECT_ROOT}\\config.json',
            mode='r',
            encoding='UTF-8') as config_file:
        return load(config_file)
