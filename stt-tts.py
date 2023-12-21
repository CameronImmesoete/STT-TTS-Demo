import queue
import sounddevice as sd
import vosk
import json
import pyttsx3
import threading
import tkinter as tk
import os
import numpy as np

model_path = os.getcwd() + "/vosk-models"

# Initialize the Vosk model
print(model_path)
model = vosk.Model(model_path)

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()

# Global variables
IS_RECORDING = False
AUDIO_QUEUE = queue.Queue()
STOP_THREAD = threading.Event()
RECOGNIZED_TEXT = ""

def recognize_audio(q, recognizer, text_display, stop_button):
    global RECOGNIZED_TEXT
    while not STOP_THREAD.is_set():
        data = q.get()
        if data is None:
            break
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            if result:
                text = json.loads(result)['text']
                RECOGNIZED_TEXT += text + " "
                text_display.delete(1.0, tk.END)
                text_display.insert(tk.END, RECOGNIZED_TEXT)
                stop_button.config(state=tk.NORMAL)  # Enable the stop button once text appears

def record_audio(q, text_display, stop_button):
    global STOP_THREAD
    STOP_THREAD.clear()
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1) as stream:
        print("Recording started. Speak into the microphone...")
        recognizer = vosk.KaldiRecognizer(model, 16000)

        audio_thread = threading.Thread(target=recognize_audio, args=(q, recognizer, text_display, stop_button))
        audio_thread.start()

        while not STOP_THREAD.is_set():
            data, overflowed = stream.read(8000)
            if data:
                # Convert the data to bytes and put it in the queue
                q.put(bytes(data))

        q.put(None)  # End of recording
        audio_thread.join()

def update_recording_status(text_display, status_label, recording):
    status_label.config(text=f"Recording Status: {'Recording' if recording else 'Stopped'}")
    if not recording:
        text_display.config(state=tk.NORMAL)
    else:
        text_display.delete(1.0, tk.END)
        RECOGNIZED_TEXT = ""

def start_recording(text_display, status_label, stop_button):
    global IS_RECORDING
    if not IS_RECORDING:
        IS_RECORDING = True
        update_recording_status(text_display, status_label, True)
        stop_button.config(state=tk.DISABLED)
        threading.Thread(target=record_audio, args=(AUDIO_QUEUE, text_display, stop_button)).start()

def stop_recording(status_label, stop_button):
    global IS_RECORDING
    IS_RECORDING = False
    STOP_THREAD.set()
    stop_button.config(state=tk.NORMAL)
    update_recording_status(text_display, status_label, False)

def play_output():
    tts_engine.say(RECOGNIZED_TEXT)
    tts_engine.runAndWait()

# GUI
root = tk.Tk()
root.title("Speech-to-Text App")

text_display = tk.Text(root, height=10, width=50)
text_display.pack(pady=10)

status_label = tk.Label(root, text="Recording Status: Stopped")
status_label.pack()

record_button = tk.Button(root, text="Record", command=lambda: start_recording(text_display, status_label, stop_button))
record_button.pack()

stop_button = tk.Button(root, text="Stop recording", command=lambda: stop_recording(status_label, stop_button), state=tk.DISABLED)
stop_button.pack()

play_button = tk.Button(root, text="Play output", command=play_output)
play_button.pack()

root.mainloop()
