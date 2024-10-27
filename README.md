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

## License

ShadowGPT is a free, open-source software distributed under the [MIT License](LICENSE.txt)
