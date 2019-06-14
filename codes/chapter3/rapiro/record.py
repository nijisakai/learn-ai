#!coding:utf-8
import pyaudio
import logging
import ctypes
import audioop
import tempfile
import wave
import os

import mute_alsa

class Mic:

    def __init__(self):
        self._audio = pyaudio.PyAudio()
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(level = logging.INFO)
        self._threshold = None
        handler = logging.FileHandler("log.txt")
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)

        self._logger.addHandler(handler)
        self._logger.addHandler(console)
        try:
            asound = ctypes.cdll.LoadLibrary('libasound.so.2')
            asound.snd_lib_error_set_handler(mute_alsa.c_error_handler)
        except OSError:
            pass
        self._audio = pyaudio.PyAudio()
        self._logger.info("Initialization of PyAudio completed.")

    def getScore(self, data):
        rms = audioop.rms(data, 2)
        score = rms / 3
        return score

    def fetchThreshold(self):

        # TODO: Consolidate variables from the next three functions
        THRESHOLD_MULTIPLIER = 2.5
        RATE = 16000
        CHUNK = 1024

        # number of seconds to allow to establish threshold
        THRESHOLD_TIME = 1

        # prepare recording stream
        stream = self._audio.open(format=pyaudio.paInt16,
                                  channels=1,
                                  rate=RATE,
                                  input=True,
                                  frames_per_buffer=CHUNK)

        # stores the audio data
        frames = []

        # stores the lastN score values
        lastN = [i for i in range(20)]

        # calculate the long run average, and thereby the proper threshold
        for i in range(0, RATE / CHUNK * THRESHOLD_TIME):
            try:
                data = stream.read(CHUNK)
                frames.append(data)

                # save this data point as a score
                lastN.pop(0)
                lastN.append(self.getScore(data))
                average = sum(lastN) / len(lastN)

            except Exception as e:
                print(e)
                self._logger.debug(e)
                continue

        try:
            stream.stop_stream()
            stream.close()
        except Exception as e:
            self._logger.debug(e)
            pass

        # this will be the benchmark to cause a disturbance over!
        THRESHOLD = average * THRESHOLD_MULTIPLIER
        self._threshold = THRESHOLD
        return THRESHOLD

    def activeListenToAllOptions(self, THRESHOLD=None, LISTEN=True,
                                 MUSIC=False):
        """
            Records until a second of silence or times out after 12 seconds

            Returns a list of the matching options or None
        """
        # self.beforeListenEvent()

        RATE = 16000
        CHUNK = 1024
        LISTEN_TIME = 12

        # check if no threshold provided
        if self._threshold:
            THRESHOLD = self._threshold
        elif(THRESHOLD is None):
            THRESHOLD = self.fetchThreshold()
        # prepare recording stream
        stream = self._audio.open(format=pyaudio.paInt16,
                                  channels=1,
                                  rate=RATE,
                                  input=True,
                                  frames_per_buffer=CHUNK)

        frames = []
        # increasing the range # results in longer pause after command
        # generation
        lastN = [THRESHOLD * 1.2] * 40

        for i in range(0, int(RATE / CHUNK * LISTEN_TIME)):
            try:
                data = stream.read(CHUNK, exception_on_overflow=False)
                frames.append(data)
                score = self.getScore(data)

                lastN.pop(0)
                lastN.append(score)

                average = sum(lastN) / float(len(lastN))

                # TODO: 0.8 should not be a MAGIC NUMBER!
                if average < THRESHOLD * 0.8:
                    break
            except Exception as e:
                self._logger.error(e)
                continue

        # self.endListenEvent()

        # save the audio data
        try:
            stream.stop_stream()
            stream.close()
        except Exception as e:
            self._logger.debug(e)
            pass

        with open('record.wav',mode='w+b') as f:
            wav_fp = wave.open(f, 'wb')
            wav_fp.setnchannels(1)
            wav_fp.setsampwidth(pyaudio.get_sample_size(pyaudio.paInt16))
            wav_fp.setframerate(RATE)
            wav_fp.writeframes(''.join(frames))
            wav_fp.close()
            f.seek(0)
            # return self.active_stt_engine.transcribe(f)
            return

if __name__ == '__main__':
    mic = Mic()
    threshold = mic.fetchThreshold()
    while True:
        print('start listening')
        mic.activeListenToAllOptions(threshold)
        print('listen over')
        os.system('aplay record.wav')
