import numpy as np
import pandas as pd
import librosa
import pickle


class Model():
    def preprocessing_modelling(self , audioname):
        self.y, self.sr = librosa.load(audioname, sr=44100, mono=True, duration=None)
        self.rmse = librosa.feature.rms(y=self.y)
        self.chroma_stft = librosa.feature.chroma_stft(y=self.y, sr=self.sr)
        self.spec_cent = librosa.feature.spectral_centroid(y=self.y, sr=self.sr)
        self.spec_bw = librosa.feature.spectral_bandwidth(y=self.y, sr=self.sr)
        self.rolloff = librosa.feature.spectral_rolloff(y=self.y, sr=self.sr)
        self.zcr = librosa.feature.zero_crossing_rate(self.y)
        self.mfcc = librosa.feature.mfcc(y=self.y, sr=self.sr)

        self.data = pd.DataFrame({"chroma_stft" : [np.mean(self.chroma_stft)],
                                  "rmse" : [np.mean(self.rmse)],
                                  "spec_cent" : [np.mean(self.spec_cent)],
                                  "spec_bw" : [np.mean(self.spec_bw)],
                                  "rolloff" : [np.mean(self.rolloff)],
                                  "zcr" : [np.mean(self.zcr)]})

        for index, value in enumerate(self.mfcc):
            self.data[f"mfcc_{index+1}"]  = np.mean(value)

        with open("preprocessor-and-model/scaler.pkl", "rb") as new_file:
            self.std_scaler = pickle.load(new_file)
        self.test_data = self.std_scaler.transform(np.array(self.data,  dtype = float))

        with open("preprocessor-and-model/xgb_model.pkl", "rb") as new_file2:
            self.xgb_model = pickle.load(new_file2)

        self.result = self.xgb_model.predict(self.test_data)

        result_map = {}
        result_map["aveh"] = 0
        result_map["bveh"] = 1
        result_map["gman"] = 2
        result_map["sman"] = 3

        for class_name, value in result_map.items():
            if (self.result[0] == value):
                self.final_result = class_name

        return self.final_result


