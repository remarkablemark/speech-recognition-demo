# Speech Recognition Demo

Demo that transcribes audio to text using [SpeechRecognition](https://pypi.org/project/SpeechRecognition/).

See [blog post](https://remarkablemark.org/blog/2020/08/24/python-speech-recognition/) for more information.

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

Clone repository:

```sh
git clone https://github.com/remarkablemark/speech-recognition-demo.git
cd speech-recognition-demo
```

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

Run script to convert file `audio.wav` to text:

```sh
python3 transcribe.py audio.wav
```

Optional: save transcription to file `transcript.txt`:

```sh
python3 transcribe.py audio.wav transcript.txt
```

## License

[MIT](LICENSE)
