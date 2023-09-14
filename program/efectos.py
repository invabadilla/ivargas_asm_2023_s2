import numpy as np
import soundfile as sf

def apply_phaser_effect(input_file, output_file, depth, rate, phase_shift):
    try:
        # Cargar la señal de audio
        audio_data, sample_rate = sf.read(input_file)

        # Crear un arreglo para almacenar la señal de audio procesada
        processed_audio = np.zeros_like(audio_data, dtype=np.float64)

        # Parámetros del efecto phaser
        max_phase = 2 * np.pi
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
        print("Efecto de phaser aplicado y archivo guardado con éxito.")

    except Exception as e:
        print("Ocurrió un error:", str(e))

if __name__ == "__main__":
    # Parámetros del efecto de phaser
    input_audio_file = "audio.wav"
    output_audio_file = "output_audio.wav"
    depth = 0.5  # Profundidad del efecto (ajustar según sea necesario)
    rate = 0.2   # Tasa de modulación (ajustar según sea necesario)
    phase_shift = 0.0  # Desplazamiento de fase inicial (ajustar según sea necesario)

    # Aplicar el efecto de phaser
    apply_phaser_effect(input_audio_file, output_audio_file, depth, rate, phase_shift)
