import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, fftfreq
from pydub import AudioSegment
from scipy.io import wavfile
from notes import get_note_from_freq, Notes

def main():
    # Read MP3 file
    mp3_file = AudioSegment.from_mp3("Musics/frantic.mp3")

    # Convert do Wav
    wav_file = mp3_file.export("output.wav", format="wav")

    # Load the WAV file
    sample_rate, audio_data = wavfile.read("output.wav")

    print(type(audio_data))
    print(audio_data.shape)

    audio_mono = audio_data[:,0]

    # TODO filter out voice, bass, piano to keep only guitar

    samples = int(round(sample_rate/10)) # One Slice each 100ms
    print("Samples " + str(samples))

    act_sample = 0
    while(act_sample < audio_mono.nbytes/audio_mono.itemsize):

        audio_slice = audio_mono[act_sample:(act_sample+samples)]

        # Number of samples in normalized_tone
        N = int(round(audio_slice.nbytes / audio_slice.itemsize))
        yf = fft(audio_slice)
        xf = fftfreq(N, 1 / sample_rate)

        #plt.plot(xf, np.abs(yf))
        #plt.show()

        max_freq_component = 0
        max_freq_value = 0

        for idx, x in enumerate(xf):
            if yf[idx] > max_freq_component:
                max_freq_component = yf[idx]
                max_freq_value = x

        note = get_note_from_freq(np.abs(max_freq_value))
        if(note != Notes.ERR):
            print("Note: " + str(note))
            print("Freq: " + str(np.abs(max_freq_value)))
            print("Time: " + str(act_sample/sample_rate))

        act_sample += samples

if __name__ == '__main__':
   main()

