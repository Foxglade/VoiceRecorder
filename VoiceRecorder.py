# import required libraries
import os
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# Get the current working directory
current_directory = os.getcwd()

# Sampling frequency
freq = 44100

# Recording duration
duration = 5

# Start recorder with the given values 
# of duration and sample frequency
print("Recording started...")
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

# Record audio for the given number of seconds
print("Recording completed. Waiting for the recording to finish...")
sd.wait()

# This will convert the NumPy array to an audio
# file with the given sampling frequency
print("Recording finished. Writing to files...")
file_path_0 = os.path.join(current_directory, "recording0.wav")
write(file_path_0, freq, recording)
print(f"File 0 written to: {file_path_0}")

# Convert the NumPy array to audio file
file_path_1 = os.path.join(current_directory, "recording1.wav")
wv.write(file_path_1, recording, freq, sampwidth=2)
print(f"File 1 written to: {file_path_1}")
print("Files written successfully.")
