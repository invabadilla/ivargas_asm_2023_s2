import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# Solicitar el nombre del archivo
audio_file = input("Nombre del audio: ")

# Cargar la señal de audio
y, sr = librosa.load(audio_file, sr=None)

# Calcular el espectrograma complejo
D = librosa.stft(y, n_fft=1024, hop_length=512)

# Obtener la magnitud y la fase del espectrograma complejo
magnitude = np.abs(D)
phase = np.angle(D)


# Solicitar el nombre del archivo de salida desde la consola
magnitud_nombre = input("Nombre del gráfico magnitud (sin extensión): ")


# Visualizar el espectrograma de magnitud
plt.figure(figsize=(12, 6))
librosa.display.specshow(librosa.amplitude_to_db(magnitude, ref=np.max), y_axis='log', x_axis='time')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de Magnitud')
plt.savefig(f'{magnitud_nombre}.png')
plt.show()

# Solicitar el nombre del archivo de salida desde la consola
fase_nombre = input("Nombre del gráfico magnitud (sin extensión): ")

# Visualizar el espectrograma de fase
plt.figure(figsize=(12, 6))
librosa.display.specshow(phase, y_axis='log', x_axis='time', cmap='twilight')
plt.colorbar()
plt.title('Espectrograma de Fase')
plt.savefig(f'{fase_nombre}.png')
plt.show()

plt.savefig(format("png"))
