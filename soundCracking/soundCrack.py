import wave as wave
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp
import sounddevice as sd

file = wave.open('../sample_sound/sounds_a.wav')

data = file.readframes(file.getnframes())
data = np.frombuffer(data, dtype=np.int16)
data = data[::2]

duration = file.getnframes()/file.getframerate()

f, t, stft_i = sp.stft(data, fs=file.getframerate(),window='hann', nperseg=512, noverlap=256)
#stft_i[round(2*len(stft_i)/8):,:]=0
#stft_i[:round(len(stft_i)/50),:]=0

t, istft_i = sp.istft(stft_i, fs=file.getframerate(),window='hann', nperseg=512, noverlap=256)

plt.title('Subtracted Voice Wave')
plt.xlabel('time(s)')
plt.ylabel('intensity(Pa)')
plt.plot(t, istft_i, color='navy')
plt.show()

x_list = []
for i in range(len(data)):
    x_list.append(duration*i/len(data))
x = np.array(x_list)

plt.title('Voice Wave')
plt.xlabel('time(s)')
plt.ylabel('intensity(Pa)')
plt.plot(x, data, color='lightseagreen')
plt.show()

sd.play(istft_i, file.getframerate())
print('NOW PLAYING...')
sd.wait()
