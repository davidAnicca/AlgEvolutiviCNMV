import numpy as np
import pyaudio


def play_chord(notes):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=44100,
                    output=True)

    duration = 3
    volume = 0.1
    sample_rate = 44100
    t = np.linspace(0, duration, int(duration * sample_rate), False)

    final_waveform = 0

    for freq in notes:
        waveform = volume * np.sin(2 * np.pi * freq * t)
        timbre_waveform = np.sin(waveform * np.pi)
        final_waveform += timbre_waveform

    stream.write((final_waveform / len(notes)).astype(np.float32).tobytes())
    stream.stop_stream()
    stream.close()
    p.terminate()
