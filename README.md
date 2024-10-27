# ShadowGPT

## Installation

First, copy this repository

```sh
git clone https://github.com/yaz008/ShadowGPT.git
```

Create Python 3.12 virtual environment and run

```sh
pip install -r requirements.txt
```

Create `blank.j2` file inside `prompts` folder

```j2
{% PROMPT %}
```

### Note

ShadowGPT relies on [j2pipeline](https://pypi.org/project/j2pipeline/) library which requires a TCP server listening on port `50027` that provides the actual GPT responses

You might consider installing [TG-GPT-API](https://github.com/yaz008/TG-GPT-API) server that provides GPT from the [Telegram](https://telegram.org/)

_(For installation instuctions and documentation visit the GitHub repositories)_

## Usage

To start ShadowGPT, run `src/main.py` file

**Note:** If you run the app and absolutely nothing happens, don't be concerned - ShadowGPT is designed to operate with minimal side effects

### States

ShadowGPT could be in 5 states: `inactive`, `waiting`, `message`, `command` and `exit`

**Transitions:**

- (`DownKey`, `*` -> `exit`): stop the app

- (`RightShift`, `inactive` -> `waiting`)

- (`AnyKey`, `waiting` -> `message`): Write a message

- (`/`, `waiting` -> `command`): activate command mode

- (`RightShift`, `message` -> `inactive`): send a message to GPT

- (`RightShift`, `command` -> `inactive`): execute a command

Once a message is sent to GPT, the response will be copied to your clipboard, allowing you to access it using `Ctrl + V`

### Commands

If your message starts with a `/`, it will be interpreted as a command

- **template template-name**: switch a prompt template

### Customization

#### Prompts

You can create custom prompt templates inside the `prompts` folder

The templates should be in `.j2` format with a `{% PROMPT %}` substitution

#### Keys

To change default keys, adjust corresponding values in `config.json` file

## License

ShadowGPT is a free, open-source software distributed under the [MIT License](LICENSE.txt)
