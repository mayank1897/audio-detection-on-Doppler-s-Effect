import numpy as np
import pandas as pd
import librosa
import pickle


class Model:
    def __init__(self):
        self.y = None
        self.sr = None
        self.rmse = None
        self.chroma_stft = None
        self.spec_cent = None
        self.spec_bw = None
        self.rolloff = None
        self.zcr = None
        self.mfcc = None
        self.data = None
        self.std_scaler = None
        self.test_data = None
        self.knn_model = None
        self.result = None
        self.final_result = None

    def preprocessing_modelling(self, audioname):
        self.y, self.sr = librosa.load(audioname, sr=44100, mono=True)
        self.rmse = librosa.feature.rms(y=self.y)
        self.chroma_stft = librosa.feature.chroma_stft(y=self.y, sr=self.sr)
        self.spec_cent = librosa.feature.spectral_centroid(y=self.y, sr=self.sr)
        self.spec_bw = librosa.feature.spectral_bandwidth(y=self.y, sr=self.sr)
        self.rolloff = librosa.feature.spectral_rolloff(y=self.y, sr=self.sr)
        self.zcr = librosa.feature.zero_crossing_rate(self.y)
        self.mfcc = librosa.feature.mfcc(y=self.y, sr=self.sr)
        # self.distance = distance
        # self.speed = speed
        # self.angle = angle
        # self.actual = actual_label

        self.data = pd.DataFrame({"chroma_stft": [np.mean(self.chroma_stft)],
                                  "rmse": [np.mean(self.rmse)],
                                  "spec_cent": [np.mean(self.spec_cent)],
                                  "spec_bw": [np.mean(self.spec_bw)],
                                  "rolloff": [np.mean(self.rolloff)],
                                  "zcr": [np.mean(self.zcr)]})

        for index, value in enumerate(self.mfcc):
            self.data[f"mfcc_{index+1}"] = np.mean(value)

        with open("preprocessor-and-model/scaler.pkl", "rb") as new_file:
            self.std_scaler = pickle.load(new_file)
        self.test_data = self.std_scaler.transform(np.array(self.data,  dtype=float))

        with open("preprocessor-and-model/xgb_model.pkl", "rb") as new_file2:
            self.knn_model = pickle.load(new_file2)

        self.result = self.knn_model.predict(self.test_data)

        result_map = {"aveh": 0, "bveh": 1, "gman": 2, "sman": 3}

        for class_name, value in result_map.items():
            if self.result[0] == value:
                self.final_result = class_name

        return self.final_result
