import pyaudio
import wave
import audioop
import os
import subprocess

# Parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
THRESHOLD = 5000  # Adjust based on testing, this value detects loud noises

def open_file():
    file_path = "Jarvis.py"
    subprocess.call(['/usr/local/bin/python3', file_path])  # Specify the file you want to open

def listen_for_claps():
    audio = pyaudio.PyAudio()

    # Start streaming
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("Listening for claps...")

    try:
        while True:
            data = stream.read(CHUNK)
            rms = audioop.rms(data, 2)  # Gets the RMS of the audio chunk

            if rms > THRESHOLD:
                print("Clap detected")
                open_file()
                break  # Exit after opening the file once, remove this if continuous detection is needed
    finally:
        # Stop and close the stream
        stream.stop_stream()
        stream.close()
        audio.terminate()
        print("Terminated")

listen_for_claps()