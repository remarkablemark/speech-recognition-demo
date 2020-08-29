# Speech Recognition Demo

## Prerequisites

[Python 3](https://www.python.org/):

```sh
python3 --version
```

[pip](https://pypi.org/project/pip/):

```sh
pip3 --version
```

[virtualenv](https://docs.python-guide.org/dev/virtualenvs/):

```sh
pip3 install virtualenv
virtualenv --version
```

## Install

Create and activate project virtual environment:

```sh
virtualenv venv
source venv/bin/activate
```

If `requirements.txt` exists, install dependencies:

```sh
pip3 install -r requirements.txt
```

Otherwise, install dependencies and create `requirements.txt`:

```sh
pip3 install SpeechRecognition
pip3 freeze > requirements.txt
```

## Run

Create an audio file named `audio.wav` in the current working directory.

Run script to convert `audio.wav` to text:

```sh
python3 transcribe.py
```

## License

[MIT](LICENSE)
