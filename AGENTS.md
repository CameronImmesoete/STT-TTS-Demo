# AGENTS.md

## Repository Overview

Speech-to-text and text-to-speech desktop demo. Uses Vosk for offline speech recognition, pyttsx3 for text-to-speech synthesis, and tkinter for the GUI. Single Python module with threaded audio capture and processing.

## Code Guidelines

- Python 3.10+
- Follow existing code style (threading, queue-based audio pipeline)
- Lint with `ruff check .` before committing
- No secrets or API keys in code

## PR Guidelines

- All changes via pull request
- Squash merge only
