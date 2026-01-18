from scipy.io import wavfile
from scipy.fft import rfft,fftfreq
import MorseCodePy as mp
import numpy as np

original_freqs = """
C	523.25
D	587.33
E	659.25
F	698.46
G	783.99
A	880.00
B	987.76
""".strip()

freqs = {}
for line in original_freqs.splitlines():
  note_name, freq = line.strip().split()
  freqs[note_name] = float(freq)

melody = """
C  C  G  G  A  A  G 
F  F  E  E  D  D  C 
G  G  F  F  E  E  D 
G  G  F  F  E  E  D 
C  C  G  G  A  A  G 
F  F  E  E  D  D  C 
""".strip().split()

def measure_frequencies(data, size):
  blocks = len(data) // size
  for i in range(blocks):
    magnitudes = rfft(data[size * i : size * i + size])
    frequency_bins = fftfreq(size, 1.0 / samplerate)
    normalized_magnitudes = 2.0 / size * np.abs(magnitudes[0 : size // 2])
    base_freq = frequency_bins[np.argmax(normalized_magnitudes)]
    yield base_freq

def filter_long_notes(freqs):
  for i, freq in enumerate(freqs):
    if (i % 50) % 8 == 7 or i % 50 >= 47:
      continue
    yield freq

samplerate, data = wavfile.read('melodia_secreta2.wav')
size = samplerate // 4
blocks = int(len(data) / size)
melody *= 5
measured = filter_long_notes(measure_frequencies(data, size))
ans = []

for measure, note in zip(measured, melody):
  variation = (measure - freqs[note]) / freqs[note]
  if variation > 0.04:
    ans.append(".")
  elif variation < -0.04:
    ans.append("-")
  else:
    ans.append(" ")

s = "".join(ans).split("  ")
print(" ".join(mp.decode(x, language="english").upper() for x in s))
