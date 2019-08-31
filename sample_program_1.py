from __future__ import print_function
import librosa
from matplotlib import pyplot as plt
import numpy as np

# 音楽のインポート
filename = librosa.util.example_audio_file()
y, sr = librosa.load(filename)

# numpyの波形をwavにエクスポート
output_data = np.sin(2 * np.pi * np.arange(0, 100000) / 200)
output_data = output_data.astype("float32")
librosa.output.write_wav("./test.wav", output_data, sr)
