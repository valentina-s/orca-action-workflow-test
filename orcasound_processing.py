import glob
import logging

import matplotlib.pyplot as plt
from scipy.io import wavfile

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def create_spectrogram(filename):
    samplerate, data = wavfile.read(filename)

    plt.subplot(211)
    plt.title("Channel 0 above, Channel 1 below")
    plt.specgram(data[:, 0], Fs=samplerate)
    plt.ylabel("Frequency")

    plt.subplot(212)
    plt.specgram(data[:, 1], Fs=samplerate)
    plt.xlabel("Time")
    plt.ylabel("Frequency")

    outfile = filename.replace(".wav", "_spectrogram.png")
    plt.savefig(outfile)

    plt.cla()
    plt.close("all")
    logging.info("Finished " + filename)


for filename in sorted(glob.glob("bush_point/*.wav")):
    create_spectrogram(filename)
