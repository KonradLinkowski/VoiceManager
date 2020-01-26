# VoiceManager
Voice assistant - running basic commands with speech recognition.

## Running
1. Download [chromedriver] that matches yoor chrome version.
2. Unzip driver and save it is `chromedriver` in project's root directory.
3. Follow this [answer][pyaudio].
4. Use [pipenv] to protect your sanity.
```sh
pipenv install
pipenv run python my_project.py
```
5. To improve your life satisfaction don't ever use python again.
## Customization
Use [config.json][config_file] to create a command that you need using regex.

[chromedriver]: https://chromedriver.chromium.org/downloads
[pyaudio]: https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error#answer-35593426
[pipenv]: https://github.com/pypa/pipenv
[config_file]: ./config.json
