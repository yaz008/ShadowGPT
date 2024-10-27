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

**When you run the app and absolutely nothing happens, do not worry - ShadowGPT is designed to operate with minimal side effects**

### How it works

ShadowGPT could be in 2 modes: `active` and `inactive`

When it is in `active` mode, it stores everything you type

When turned to `inactive` mode, it sends the stored message to GPT and saves the responce into Clipboard: you can access it with `Ctrl + V`

### Commands

If your message starts with a `/`, it will be interpreted as a command

- **template template-name**: switch a prompt template

- **process funcion-name \*function-args**: switch a prompt process funnction _(see [j2pipeline](https://github.com/yaz008/j2pipeline))_

### Control

- **Right Shift**: toggle between `active` and `inactive` modes

- **Right Ctrl**: display the status

- **Down**: exit the application

### Customization

You can create custom prompt templates inside the `prompts` folder

The templates must be in `.j2` format with a `{% PROMPT %}` substitution

## License

ShadowGPT is a free, open-source software distributed under the [MIT License](LICENSE.txt)
