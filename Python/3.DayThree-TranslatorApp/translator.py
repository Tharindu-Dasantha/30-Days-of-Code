import tkinter as tk
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import pyaudio


audioData = ""
recording = False

def record_audio(filename):
    # Recording logic using sounddevice
    fs = 44100
    seconds = 10
    Recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    global recording
    recording = True
    sd.wait()
    save_audio(Recording, fs, filename=filename)


def stop_recording():
    # Stop recording logic
    global recording
    recording = False
    sd.stop()


def play_audio(filename):
    # Playing logic using pyaudio
    audio_data, fs = wav.read(filename=filename)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=2, rate=fs, output=True)
    stream.write(audio_data.astype(np.float32).tobytes())
    stream.stop_stream()
    steam.close()
    p.terminate()


def save_audio(audio_data, Samplerate, filename):
    # Saving audio data to a WAV file
    wav.write(filename, Samplerate, audio_data)


def create_gui():
    # Create Tkinter GUI with buttons for record, stop, play, and save
    root = tk.Tk()
    root.title("Audio recorder")
    root.geometry("600x400")
    root.config(background="#eaeaea")

    # Creating the GUI
    Record_Button = tk.Button(root, text="Record", command=record_audio("audio.wav"))
    Record_Button.pack(pady=(20, 0))
    Stop_Button = tk.Button(root, text="Stop", command=stop_recording)
    Stop_Button.pack(pady=(0, 20))
    Play_Button = tk.Button(root, text="Play", command=lambda: play_audio("audio.wav"))
    Play_Button.pack(pady=(0, 20))
    Save_Button = tk.Button(root, text="Save", command=lambda: save_audio(audioData, 44100, "audio.wav"))
    Save_Button.pack(pady=(0, 20))    

    # Start the GUI
    root.mainloop()


if __name__ == "__main__":
    create_gui()