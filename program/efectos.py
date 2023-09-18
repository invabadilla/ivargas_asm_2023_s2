import numpy as np
import soundfile as sf

def effect(input_file, output_file, depth, rate, phase_shift):
    try:
        # Cargar la señal de audio
        audio_data, sample_rate = sf.read(input_file)

        # Crear un arreglo para almacenar la señal de audio procesada
        processed_audio = np.zeros_like(audio_data, dtype=np.float64)

        phase = 0

        for i in range(len(audio_data)):
            # Calcular el desplazamiento de fase en función del tiempo
            phase_increment = depth * np.sin(2 * np.pi * rate * i / sample_rate + phase_shift)

            # Actualizar la fase
            phase += phase_increment

            # Aplicar el efecto de fase a la señal de audio
            processed_audio[i] = audio_data[i] * np.exp(1j * phase).real

        # Guardar la señal procesada en un archivo de audio
        sf.write(output_file, processed_audio, sample_rate)

    except Exception as e:
        print("Ocurrió un error:", str(e))

if __name__ == "__main__":
    # Parámetros del efecto
    input_audio_file = "audio.wav"
    # Solicitar el nombre del archivo de salida desde la consola
    output_audio_file = input("Nombre del audio final (con extensión wav): ")

    depth = 0.2  # Profundidad del efecto
    rate = 1.5   # Tasa de modulación
    phase_shift = 0.2  # Desplazamiento de fase inicial

    # Aplicar el efecto
    effect(input_audio_file, output_audio_file, depth, rate, phase_shift)

#Vibrato
# depth = 0.1
# rate = 6.0
# phase_shift = 0.0

#Phaser
# depth = 0.6
# rate = 3.0
# phase_shift = 0.0

#Flanger
# depth = 0.2
# rate = 1.5
# phase_shift = 0.2