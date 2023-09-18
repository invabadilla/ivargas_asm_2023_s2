import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parámetros de la señal seno
amplitud = 1.0
frecuencia = 5.0  # Hz
duracion = 1.0  # segundos
tasa_muestreo = 1000  # Hz

# Generar la señal seno
t = np.linspace(0, duracion, int(duracion * tasa_muestreo), endpoint=False)
senal_seno = amplitud * np.sin(2 * np.pi * frecuencia * t)

# Agregar ruido gaussiano
ruido = np.random.normal(0, 0.5, len(t))
senal_con_ruido = senal_seno + ruido

# Muestreo de Nyquist-Shannon para eliminar ruido
frecuencia_corte = frecuencia * 1.5
nyquist_frecuencia = 0.5 * tasa_muestreo
normalizada_frecuencia_corte = frecuencia_corte / nyquist_frecuencia
b, a = signal.butter(4, normalizada_frecuencia_corte, btype='low', analog=False)
senal_filtrada = signal.filtfilt(b, a, senal_con_ruido)

# Visualizar las señales
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, senal_con_ruido, label='Señal con ruido')
plt.plot(t, senal_seno, label='Señal seno original', linestyle='--')
plt.legend()
plt.title('Señal Original y Señal con Ruido')

plt.subplot(2, 1, 2)
plt.plot(t, senal_filtrada, label='Señal Reconstruida')
plt.plot(t, senal_seno, label='Señal seno original', linestyle='--')
plt.legend()
plt.title('Señal Reconstruida y Señal Original')
plt.tight_layout()
plt.savefig('seno.png')
plt.show()


