from PyQt5 import QtCore, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QWidget, QPushButton, QTextBrowser, QFileDialog, QLabel, QLineEdit, QVBoxLayout,\
    QApplication, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt, QUrl

import model
import recorder


class Recording(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 300)
        self.setWindowTitle("Recorder")
        self.setWindowIcon(QIcon("resources/microphone.png"))
        self.setStyleSheet("background-color:#e6ffff")
        self.start = QPushButton(self)
        self.stop = QPushButton(self)
        self.submit = QPushButton(self)
        self.distanceLabel = QLabel(self)
        self.distance = QLineEdit(self)
        self.speedLabel = QLabel(self)
        self.speed = QLineEdit(self)
        self.angleLabel = QLabel(self)
        self.angle = QLineEdit(self)
        self.actualLabel = QLabel(self)
        self.actual = QLineEdit(self)
        self.create_buttons()

    def create_buttons(self):
        # Start Button
        self.start.setText("Start")
        self.start.setGeometry(130, 40, 121, 35)
        # self.start.setEnabled(False)
        self.start.setIcon(QIcon("resources/start-button.png"))
        self.start.setStyleSheet("background-color:rgb(81, 165, 88);\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "border-style: outset;\n"
                                 "border-width:2px;\n"
                                 "border-radius:10px;\n"
                                 "border-color:black;\n"
                                 "font:bold 14px;\n"
                                 "padding :6px;\n"
                                 "min-width:10px;")

        # Stop Button
        self.stop.setText("Stop")
        self.stop.setGeometry(550, 40, 121, 35)
        # self.submit.setEnabled(False)
        self.stop.setIcon(QIcon("resources/stop-button.png"))
        self.stop.setStyleSheet("background-color:rgb(214, 71, 0);\n"
                                "color: rgb(0, 0, 0);\n"
                                "border-style: outset;\n"
                                "border-width:2px;\n"
                                "border-radius:10px;\n"
                                "border-color:black;\n"
                                "font:bold 14px;\n"
                                "padding :6px;\n"
                                "min-width:10px;")

        # Submit Button
        self.submit.setText("SUBMIT")
        self.submit.setGeometry(342, 220, 121, 35)
        # self.submit.setEnabled(False)
        self.submit.setStyleSheet("background-color:rgb(166, 166, 166);\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "border-style: outset;\n"
                                  "border-width:2px;\n"
                                  "border-radius:10px;\n"
                                  "border-color:black;\n"
                                  "font:bold 14px;\n"
                                  "padding :6px;\n"
                                  "min-width:10px;")

        # Distance Input dialog
        self.distanceLabel.setText('Distance of Object (mtrs):')
        self.distanceLabel.setStyleSheet("color:rgb(57, 98, 140);\n"
                                         "font-size:12px;\n"
                                         "font:bold 13px;\n"
                                         "text-decoration: underline;\n")
        self.distanceLabel.move(40, 115)

        font = self.distance.font()
        font.setPointSize(14)
        self.distance.setFont(font)
        self.distance.setGeometry(80, 137, 85, 35)

        # Speed Input dialog
        self.speedLabel.setText('Speed of Object (km/hr):')
        self.speedLabel.setStyleSheet("color:rgb(57, 98, 140);\n"
                                      "font-size:12px;\n"
                                      "font:bold 13px;\n"
                                      "text-decoration: underline;\n")
        self.speedLabel.move(240, 115)

        font = self.speed.font()
        font.setPointSize(14)
        self.speed.setFont(font)
        self.speed.setGeometry(275, 137, 85, 35)

        # Angle Input dialog
        self.angleLabel.setText('Angle of Object (deg):')
        self.angleLabel.setStyleSheet("color:rgb(57, 98, 140);\n"
                                      "font-size:12px;\n"
                                      "font:bold 13px;\n"
                                      "text-decoration: underline;\n")
        self.angleLabel.move(440, 115)

        font = self.angle.font()
        font.setPointSize(14)
        self.angle.setFont(font)
        self.angle.setGeometry(465, 137, 85, 35)

        # Actual Label Input dialog
        self.actualLabel.setText('Actual Label Of Object:')
        self.actualLabel.setStyleSheet("color:rgb(57, 98, 140);\n"
                                       "font-size:12px;\n"
                                       "font:bold 13px;\n"
                                       "text-decoration: underline;\n")
        self.actualLabel.move(620, 115)

        font = self.actual.font()
        font.setPointSize(14)
        self.actual.setFont(font)
        self.actual.setGeometry(645, 137, 85, 35)


# class Uploading(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.resize(800,300)
#         self.setWindowTitle("Uploader")
#         self.setWindowIcon(QIcon("resources/upload.png"))
#         self.setStyleSheet("background-color:#e6ffff")
#         self.input_buttons()
#
#
#     def input_buttons(self):
#
#         # Distance Input dialog
#         self.distanceLabel = QLabel(self)
#         self.distanceLabel.setText('Distance of Object (mtrs):')
#         self.distanceLabel.setStyleSheet("color:rgb(57, 98, 140);\n"
#                                          "font-size:12px;\n"
#                                          "font:bold 13px;\n"
#                                          "text-decoration: underline;\n")
#         self.distanceLabel.move(40, 95)
#
#         self.distance = QLineEdit(self)
#         self.distance.setObjectName("objDistance")
#         font = self.distance.font()
#         font.setPointSize(14)
#         self.distance.setFont(font)
#         self.distance.setGeometry(80, 117, 85, 35)
#
#         # Speed Input dialog
#         self.speedLabel = QLabel(self)
#         self.speedLabel.setText('Speed of Object (km/hr):')
#         self.speedLabel.setStyleSheet("color:rgb(57, 98, 140);\n"
#                                       "font-size:12px;\n"
#                                       "font:bold 13px;\n"
#                                       "text-decoration: underline;\n")
#         self.speedLabel.move(240, 95)
#
#         self.speed = QLineEdit(self)
#         self.speed.setObjectName("objSpeed")
#         font = self.speed.font()
#         font.setPointSize(14)
#         self.speed.setFont(font)
#         self.speed.setGeometry(275, 117, 85, 35)
#
#         # Angle Input dialog
#         self.angleLabel = QLabel(self)
#         self.angleLabel.setText('Angle of Object (deg):')
#         self.angleLabel.setStyleSheet("color:rgb(57, 98, 140);\n"
#                                       "font-size:12px;\n"
#                                       "font:bold 13px;\n"
#                                       "text-decoration: underline;\n")
#         self.angleLabel.move(440, 95)
#
#         self.angle = QLineEdit(self)
#         self.angle.setObjectName("objAngle")
#         font = self.angle.font()
#         font.setPointSize(14)
#         self.angle.setFont(font)
#         self.angle.setGeometry(465, 117, 85, 35)
#
#         # Actual Label Input dialog
#         self.actualLabel = QLabel(self)
#         self.actualLabel.setText('Actual Label Of Object:')
#         self.actualLabel.setStyleSheet("color:rgb(57, 98, 140);\n"
#                                        "font-size:12px;\n"
#                                        "font:bold 13px;\n"
#                                        "text-decoration: underline;\n")
#         self.actualLabel.move(620, 95)
#
#         self.actual = QLineEdit(self)
#         self.actual.setObjectName("objActual")
#         font = self.actual.font()
#         font.setPointSize(14)
#         self.actual.setFont(font)
#         self.actual.setGeometry(645, 117, 85, 35)
#
#         # Submit Button
#         self.submit = QPushButton(self)
#         self.submit.setText("SUBMIT")
#         self.submit.setGeometry(342, 220, 121, 35)
#         # self.submit.setEnabled(False)
#         self.submit.setStyleSheet("background-color:rgb(166, 166, 166);\n"
#                                   "color: rgb(0, 0, 0);\n"
#                                   "border-style: outset;\n"
#                                   "border-width:2px;\n"
#                                   "border-radius:10px;\n"
#                                   "border-color:black;\n"
#                                   "font:bold 14px;\n"
#                                   "padding :6px;\n"
#                                   "min-width:10px;")

class PlayAudio(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 800, 120
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowTitle("Audio Player")
        self.setWindowIcon(QIcon("resources/audio-player.png"))

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.playbackControl = QHBoxLayout(self)
        self.layout.addLayout(self.playbackControl)

        # play button
        self.playbtn = QPushButton(self)
        self.playbtn.setText("Play")
        self.playbtn.clicked.connect(self.play_audio_file)
        self.playbackControl.addWidget(self.playbtn)

        # pause button
        self.pausebtn = QPushButton(self)
        self.pausebtn.setText("Pause")
        self.pausebtn.clicked.connect(self.pause_audio_file)
        self.playbackControl.addWidget(self.pausebtn)

        # resume button
        self.resumebtn = QPushButton(self)
        self.resumebtn.setText("Resume")
        self.resumebtn.clicked.connect(self.resume_audio_file)
        self.playbackControl.addWidget(self.resumebtn)

        self.volumeControl = QHBoxLayout(self)
        self.layout.addLayout(self.volumeControl)

        # increase volume button
        self.btnVolumeUp = QPushButton(self)
        self.btnVolumeUp.setText("+")
        self.btnVolumeUp.clicked.connect(self.volumeup)

        # decrease volume button
        self.btnVolumeDown = QPushButton(self)
        self.btnVolumeDown.setText("-")
        self.btnVolumeDown.clicked.connect(self.volumedown)

        # mute volume button
        self.butVolumeMute = QPushButton(self)
        self.butVolumeMute.setText("Mute")
        self.butVolumeMute.clicked.connect(self.volumemute)

        self.volumeControl.addWidget(self.btnVolumeUp)
        self.volumeControl.addWidget(self.btnVolumeDown)
        self.volumeControl.addWidget(self.butVolumeMute)

        self.currentVolume = None
        self.file_name = None
        self.player = QMediaPlayer()

    def volumeup(self):
        self.currentVolume = self.player.volume()
        print(self.currentVolume)
        self.player.setVolume(self.currentVolume + 5)

    def volumedown(self):
        self.currentVolume = self.player.volume()
        print(self.currentVolume)
        self.player.setVolume(self.currentVolume - 5)

    def volumemute(self):
        self.player.setMuted(not self.player.isMuted())

    def play_audio_file(self):
        self.file_name, _ = QFileDialog.getOpenFileName()
        if self.file_name == "":
            pass
        else:
            try:
                url = QUrl.fromLocalFile(self.file_name)
                content = QMediaContent(url)
                self.player.setMedia(content)
                self.player.play()

            except:
                self.text.setText("Error occured during audio playback")

    def pause_audio_file(self):
        self.player.pause()

    def resume_audio_file(self):
        self.player.play()


class AudioPlayerDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 600, 60
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowTitle("Upload/Play Audio")

        self.filename = None
        self.result = None

        # Model class object
        self.model = model.Model()

        # Play Audio Window
        self.play_audio_window = PlayAudio()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.process_playControl = QHBoxLayout(self)
        self.layout.addLayout(self.process_playControl)

        # Process Button
        self.processbtn = QPushButton(self)
        self.processbtn.setText("Process")
        self.processbtn.setStyleSheet("background-color:rgb(72, 141, 231);\n"
                                      "color: whrgb(0, 0, 0)irgb(0, 0, 0)te;\n"
                                      "border-style: outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:10px;\n"
                                      "border-color:black;\n"
                                      "font:bold 20px;\n"
                                      "padding :6px;\n"
                                      "min-width:10px;")
        self.processbtn.setObjectName("processBtn")
        self.processbtn.clicked.connect(self.open_file_dialog)
        self.process_playControl.addWidget(self.processbtn)

        # Play Button
        self.playbtn = QPushButton(self)
        self.playbtn.setText("Play")
        self.playbtn.setIcon(QIcon("resources/play-button.png"))
        self.playbtn.setIconSize(QSize(20, 20))
        self.playbtn.setStyleSheet("background-color:rgb(35, 170, 11);\n"
                                   "color: whrgb(0, 0, 0)irgb(0, 0, 0)te;\n"
                                   "border-style: outset;\n"
                                   "border-width:2px;\n"
                                   "border-radius:10px;\n"
                                   "border-color:black;\n"
                                   "font:bold 20px;\n"
                                   "padding :6px;\n"
                                   "min-width:10px;")
        self.playbtn.setObjectName("playBtn")
        self.playbtn.clicked.connect(self.play_audio_window.show)
        self.process_playControl.addWidget(self.playbtn)

        self.outputControl1 = QHBoxLayout(self)
        self.layout.addLayout(self.outputControl1)

        # Display Output results of model prediction
        self.labelOutput = QLabel(self)
        self.labelOutput.setText("Output")
        self.labelOutput.setStyleSheet("color:rgb(57, 98, 140);\n"
                                       "font-size:20px;\n"
                                       "font:bold 15px;\n"
                                       "text-decoration: underline;\n")
        self.outputControl1.addWidget(self.labelOutput)

        self.outputControl2 = QHBoxLayout(self)
        self.layout.addLayout(self.outputControl2)

        # Text Browser
        self.text = QTextBrowser(self)
        self.text.setGeometry(QtCore.QRect(10, 50, 80, 20))
        self.text.setAlignment(Qt.AlignCenter)
        self.text.setStyleSheet("font-size:40px;\n"
                                "font:bold 40px;\n")
        self.outputControl2.addWidget(self.text)

        self.clearControl = QHBoxLayout(self)
        self.layout.addLayout(self.clearControl)

        # Clear Button
        self.clearBtn = QPushButton(self)
        self.clearBtn.setText("Clear")
        self.clearBtn.setStyleSheet("background-color:rgb(243, 93, 26);\n"
                                    "color: whrgb(0, 0, 0)irgb(0, 0, 0)te;\n"
                                    "border-style: outset;\n"
                                    "border-width:2px;\n"
                                    "border-radius:10px;\n"
                                    "border-color:black;\n"
                                    "font:bold 20px;\n"
                                    "padding :6px;\n"
                                    "min-width:10px;")
        self.clearBtn.setObjectName("clearBtn")
        self.clearBtn.clicked.connect(self.clear_display)
        self.clearControl.addWidget(self.clearBtn)

    def open_file_dialog(self):
        self.filename, _ = QFileDialog.getOpenFileName()
        if self.filename == "":
            pass

        else:
            # Upload Recording for audio prediction
            # Upload Window
            # self.upload_window.show()
            # if (self.upload_window.distance.text() and self.upload_window.speed.text()
            # and self.upload_window.angle.text() and self.upload_window.actual.text()):

            # self.upload_window.submit.clicked.connect(self.submit_upload_display)
            try:
                # self.result = self.model.preprocessing_modelling(self.filename,
                #                                                  float(self.upload_window.distance.text()),
                #                                                  float(self.upload_window.speed.text()),
                #                                                  float(self.upload_window.angle.text()),
                #                                                  self.upload_window.actual.text())

                # Play Audio Event
                # self.play_audio_window.setup_playui()
                # self.play_audio_window.setup_playui.clicked.connect(self.play_audio_file)
                # self.play_audio_file(self.filename)

                self.result = self.model.preprocessing_modelling(self.filename)
                self.text.setText(self.result)
                # self.upload_window.close()
            except:
                self.text.setText("Error occured during model prediction")

    def clear_display(self):
        self.text.clear()


class UiMainWindow(object):
    def __init__(self, mainwindow):
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.recordBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn = QtWidgets.QPushButton(self.centralwidget)

        # Model class object
        self.model = model.Model()

        # Recorder class object
        self.recorder = recorder.Recorder()

        # Recording Window
        self.record_window = Recording()

        # Uploading/Playing audio Window
        self.upload_play_window = AudioPlayerDisplay()

        self.uploadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.labelRecord = QLabel(self.centralwidget)
        self.labelUpload = QLabel(self.centralwidget)
        self.labelOutput = QLabel(self.centralwidget)
        self.labelRecordedAudios = QLabel(self.centralwidget)
        self.labelAudioDetails = QLabel(self.centralwidget)
        self.text = QTextBrowser(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainwindow)

        self.final_result = None

        self.play_app = QApplication(sys.argv)
        self.setupui(mainwindow)

    def setupui(self, mainwindow):
        mainwindow.setObjectName("MainWindow")
        mainwindow.resize(1000, 800)
        self.centralwidget.setObjectName("centralwidget")

        # Record Button
        self.recordBtn.setGeometry(QtCore.QRect(180, 180, 181, 51))
        self.recordBtn.setIcon(QIcon("resources/microphone.png"))
        self.recordBtn.setIconSize(QSize(20, 20))
        self.recordBtn.setStyleSheet("background-color:rgb(72, 141, 231);\n"
                                     "color: whrgb(0, 0, 0)irgb(0, 0, 0)te;\n"
                                     "border-style: outset;\n"
                                     "border-width:2px;\n"
                                     "border-radius:10px;\n"
                                     "border-color:black;\n"
                                     "font:bold 20px;\n"
                                     "padding :6px;\n"
                                     "min-width:10px;")
        self.recordBtn.setObjectName("recordBtn")

        # Clear Button
        self.clearBtn.setGeometry(QtCore.QRect(445, 700, 101, 34))
        self.clearBtn.setStyleSheet("background-color:rgb(243, 93, 26);\n"
                                    "color: whrgb(0, 0, 0)irgb(0, 0, 0)te;\n"
                                    "border-style: outset;\n"
                                    "border-width:2px;\n"
                                    "border-radius:10px;\n"
                                    "border-color:black;\n"
                                    "font:bold 20px;\n"
                                    "padding :6px;\n"
                                    "min-width:10px;")
        self.clearBtn.setObjectName("clearBtn")
        self.clearBtn.clicked.connect(self.clear_record_display)

        # # Uploading Window
        # self.upload_window = Uploading()

        # Record Button Event
        self.recordBtn.clicked.connect(self.record_window.show)

        # Start Recording Button Event
        self.record_window.start.clicked.connect(self.start_record_display)

        # Stop Recording Button Event
        self.record_window.stop.clicked.connect(self.stop_record_display)

        # Submit Recording for audio prediction
        self.record_window.submit.clicked.connect(self.submit_record_display)

        # Upload Button
        self.uploadBtn.setGeometry(QtCore.QRect(640, 180, 181, 51))
        self.uploadBtn.setIcon(QIcon("resources/upload.png"))
        self.uploadBtn.setIconSize(QSize(20, 20))
        self.uploadBtn.setStyleSheet("background-color:rgb(147, 111, 255);\n"
                                     "color: whrgb(0, 0, 0)irgb(0, 0, 0)te;\n"
                                     "border-style: outset;\n"
                                     "border-width:2px;\n"
                                     "border-radius:10px;\n"
                                     "border-color:black;\n"
                                     "font:bold 20px;\n"
                                     "padding :6px;\n"
                                     "min-width:10px;")
        self.uploadBtn.setObjectName("uploadBtn")
        self.uploadBtn.clicked.connect(self.upload_play_window.show)

        # Record Label
        self.labelRecord.setText("Press this button to record live audio")
        self.labelRecord.setStyleSheet("color:rgb(93, 225, 255);\n"
                                       "font-size:14px;\n"
                                       "font:bold 16px;\n"
                                       "text-decoration: underline;\n")
        self.labelRecord.move(125, 155)

        # Upload Label
        self.labelUpload.setText("Press this button to upload recorded audio")
        self.labelUpload.setStyleSheet("color:rgb(93, 225, 255);\n"
                                       "font-size:14px;\n"
                                       "font:bold 16px;\n"
                                       "text-decoration: underline;\n")
        self.labelUpload.move(560, 155)

        # Output Label
        self.labelOutput.setText("Output")
        self.labelOutput.setStyleSheet("color:rgb(57, 98, 140);\n"
                                       "font-size:14px;\n"
                                       "font:bold 15px;\n"
                                       "text-decoration: underline;\n")
        self.labelOutput.move(10, 544)

        # Recorded Audios Hyperlink Label
        self.labelRecordedAudios.setStyleSheet('font-size: 20px')
        self.labelRecordedAudios.setOpenExternalLinks(True)
        self.labelRecordedAudios.setText(f"<a href={'file:///E:/skills/audio-predictor/recorded-audios'}>"
                                         f"{'Recorded Audios'}</a>")
        self.labelRecordedAudios.move(145, 740)

        # Audio Details Hyperlink Label
        self.labelAudioDetails.setStyleSheet('font-size: 20px')
        self.labelAudioDetails.setOpenExternalLinks(True)
        self.labelAudioDetails.setText(f"<a href={'file:///E:/skills/audio-predictor/audio-records.csv'}>"
                                       f"{'Audio Details'}</a>")
        self.labelAudioDetails.move(710, 740)

        # Text Browser
        self.text.setGeometry(QtCore.QRect(0, 565, 1200, 120))
        self.text.setAlignment(Qt.AlignCenter)
        self.text.setStyleSheet("font-size:60px;\n"
                                "font:bold 40px;\n")

        mainwindow.setCentralWidget(self.centralwidget)

        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)

        # copyrights statusbar
        self.statusbar.showMessage("Copyright © 2021 BFSR. All Rights Reserved.")

        self.retranslate_ui(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def start_record_display(self):
        self.text.setText("Recording Started...")
        self.recorder.startrecording()

    def stop_record_display(self):
        self.text.setText("Recording Stopped!!")
        self.recorder.stoprecording()

    def submit_record_display(self):
        # if self.record_window.distance.text() and self.record_window.speed.text() and
        # self.record_window.angle.text() \
        #         and self.record_window.actual.text():
        #     self.final_result = self.recorder.submitrecording(float(self.record_window.distance.text()),
        #                                                       float(self.record_window.speed.text()),
        #                                                       float(self.record_window.angle.text()),
        #                                                       self.record_window.actual.text())
        #     self.text.setText(self.final_result)
        #     self.record_window.close()
        # else:
        #     self.text.setText("Kindly enter all the required fields")
        self.final_result = self.recorder.submitrecording()
        self.text.setText(self.final_result)
        self.record_window.close()

    def clear_record_display(self):
        self.text.clear()

    # def submit_upload_display(self):
    #     try:
    #         self.result = self.model.preprocessing_modelling(self.filename, float(self.upload_window.distance.text()),
    #         float(self.upload_window.speed.text()), float(self.upload_window.angle.text()),
    #                                                          self.upload_window.actual.text())
    #         self.text.setText(self.result)
    #         self.upload_window.close()
    #     except:
    #         self.text.setText("Error occured during model prediction")

    def retranslate_ui(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("MainWindow", "Audio Predictor"))
        mainwindow.setWindowIcon(QIcon("resources/mainwindow.png"))
        stylesheet = """
            QMainWindow {
                width:1200px;
                height:542px;
                background-image: url("resources/background_image.png");
                background-repeat: no-repeat; 
                background-size: initial; 
                background-position: center top;
            }
        """
        mainwindow.setStyleSheet(stylesheet)

        self.recordBtn.setText(_translate("MainWindow", "Record"))
        self.uploadBtn.setText(_translate("MainWindow", "Upload"))
        self.clearBtn.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
