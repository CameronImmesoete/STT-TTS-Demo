# Copilot Instructions

> Base instructions: [CameronImmesoete/.github/.github/copilot-instructions.md@1f79bfb](https://github.com/CameronImmesoete/.github/blob/1f79bfb3e9eee277d05ecdd3332220204cb0f38b/.github/copilot-instructions.md)

## Repository-Specific Guidelines

This is a speech-to-text and text-to-speech desktop demo using Vosk for offline speech recognition and pyttsx3 for synthesis, with a tkinter GUI.

- Audio pipeline uses sounddevice with 16kHz sample rate and int16 dtype
- Threading model: recording and recognition run on separate threads, coordinated via queue and threading.Event
- Vosk model directory is expected at `./vosk-models` relative to working directory
- GUI updates must happen on the main thread (tkinter is not thread-safe)
- No network calls at runtime (fully offline after model download)
