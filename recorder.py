import threading
import pyaudio
import wave
import datetime
import csv
import os
import model

class Recorder():
    def __init__(self):
        super().__init__()
        self.isrecording = False
        self.chunk = 1024
        self.sample_format = pyaudio.paInt16
        self.channels = 2
        self.fs = 44100

    def startrecording(self):
        self.frames = []
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.sample_format, channels=self.channels, rate=self.fs,
                                  frames_per_buffer=self.chunk, input=True)

        self.isrecording = True

        print('Recording')
        t = threading.Thread(target=self.record)
        t.start()

    def stoprecording(self):
        self.isrecording = False
        print('recording stopped')
        self.filename = f"recorded-audios/REC{datetime.datetime.now().strftime('%H-%M-%S')}"
        self.filename = self.filename + ".wav"
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def record(self):
        while self.isrecording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)


    def submitrecording(self):
        self.model = model.Model()
        try:
            self.result = self.model.preprocessing_modelling(self.filename)
            with open("audio-records.csv", "a", newline="") as csvfile:
                self.d = csv.DictWriter(csvfile, fieldnames=["DateTime", "Audio Name", "Label"])
                if (os.stat("audio-records.csv").st_size==0):
                    self.d.writeheader()
                self.d.writerow({"DateTime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"Audio Name": self.filename.replace("recorded-audios/",""),"Label":self.result})
            return self.result
        except:
            return "Other audio captured"




