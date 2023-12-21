# STT-TTS-Demo
Quick GUI demo of STT->TTS voice replacement. Uses Vosk &amp; pyttsx3.

Note: to run this, you’ll need this Vosk model: [Vosk English Model (Small - 50 MB)](https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip) unzipped into the following directory: {PWD}/vosk-models

Common env issues:
if you get:
```
File "/opt/homebrew/lib/python3.11/site-packages/pyttsx3/drivers/nsss.py", line 13, in NSSpeechDriver
    @objc.python_method
     ^^^^
NameError: name 'objc' is not defined. Did you mean: 'object'?
```
run this:
`python -m pip install --upgrade py3-tts`
