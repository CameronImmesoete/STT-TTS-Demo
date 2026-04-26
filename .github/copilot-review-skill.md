# Code Review Standards

> Base review standards: [CameronImmesoete/.github/.github/copilot-review-skill.md@1f79bfb](https://github.com/CameronImmesoete/.github/blob/1f79bfb3e9eee277d05ecdd3332220204cb0f38b/.github/copilot-review-skill.md)

## Repository-Specific Review Criteria

### Audio Pipeline
- Sample rate must stay at 16kHz (Vosk model requirement)
- Queue-based producer/consumer pattern between recording and recognition
- RawInputStream blocksize should match recognizer expectations
- No audio data should leak after STOP_THREAD is set

### Threading Safety
- tkinter widgets must only be updated from the main thread or via thread-safe mechanisms
- Global mutable state (IS_RECORDING, RECOGNIZED_TEXT) must be protected against races
- Threading.Event used for stop signaling, not bare booleans
- Queue.get() must have a timeout or sentinel to avoid deadlocks

### Resource Management
- Vosk model loaded once at startup (large memory footprint)
- pyttsx3 engine lifecycle managed correctly (init/say/runAndWait)
- sounddevice stream closed cleanly on stop
