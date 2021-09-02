from PyQt5 import QtCore,  QtWidgets
from PyQt5.QtWidgets import  QWidget, QPushButton, QTextBrowser, QFileDialog, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
import model
import recorder

class Recording(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400,300)
        self.setWindowTitle("Recorder")
        self.setWindowIcon(QIcon("resources/microphone.png"))
        self.setStyleSheet("background-color:#e6ffff")
        self.create_buttons()


    def create_buttons(self):

        # Start Button
        self.start = QPushButton(self)
        self.start.setText("Start")
        self.start.setGeometry(40,80, 121, 35)
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
        self.stop = QPushButton(self)
        self.stop.setText("Stop")
        self.stop.setGeometry(245, 80, 121, 35)
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
        self.submit = QPushButton(self)
        self.submit.setText("SUBMIT")
        self.submit.setGeometry(145, 190, 121, 35)
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



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000,800)
        # MainWindow.setFixedWidth(1000)
        # MainWindow.setFixedHeight(800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Record Button
        self.recordBtn = QtWidgets.QPushButton(self.centralwidget)
        self.recordBtn.setGeometry(QtCore.QRect(180, 180, 181, 51))
        self.recordBtn.setIcon(QIcon("resources/microphone.png"))
        self.recordBtn.setIconSize(QSize(20,20))
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
        self.clearBtn = QtWidgets.QPushButton(self.centralwidget)
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

        # Model class object
        self.model = model.Model()

        # Recorder class object
        self.recorder = recorder.Recorder()

        # Recording Window
        self.record_window = Recording()

        # Record Button Event
        self.recordBtn.clicked.connect(self.record_window.show)

        # Start Recording Button Event
        self.record_window.start.clicked.connect(self.start_record_display)

        # Stop Recording Button Event
        self.record_window.stop.clicked.connect(self.stop_record_display)

        # Submit Recording for audio prediction
        self.record_window.submit.clicked.connect(self.submit_record_display)

        # Upload Button
        self.uploadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.uploadBtn.setGeometry(QtCore.QRect(640, 180, 181, 51))
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
        self.uploadBtn.clicked.connect(self.open_file_dialog)

        # Record Label
        self.labelRecord = QLabel(self.centralwidget)
        self.labelRecord.setText("Press this button to record live audio")
        self.labelRecord.setStyleSheet("color:rgb(93, 225, 255);\n"
                                "font-size:14px;\n"
                                "font:bold 16px;\n"
                                "text-decoration: underline;\n")
        self.labelRecord.move(125,155)

        # Upload Label
        self.labelUpload = QLabel(self.centralwidget)
        self.labelUpload.setText("Press this button to upload recorded audio")
        self.labelUpload.setStyleSheet("color:rgb(93, 225, 255);\n"
                                       "font-size:14px;\n"
                                       "font:bold 16px;\n"
                                       "text-decoration: underline;\n")
        self.labelUpload.move(560, 155)

        # Output Label
        self.labelOutput = QLabel(self.centralwidget)
        self.labelOutput.setText("Output")
        self.labelOutput.setStyleSheet("color:rgb(57, 98, 140);\n"
                                       "font-size:14px;\n"
                                       "font:bold 15px;\n"
                                       "text-decoration: underline;\n")
        self.labelOutput.move(10, 544)

        # Recorded Audios Hyperlink Label
        self.labelRecordedAudios = QLabel(self.centralwidget)
        self.labelRecordedAudios.setStyleSheet('font-size: 20px')
        self.labelRecordedAudios.setOpenExternalLinks(True)
        self.labelRecordedAudios.setText(f"<a href={'file:///E:/skills/audio-predictor/recorded-audios'}>{'Recorded Audios'}</a>")
        self.labelRecordedAudios.move(145, 740)

        # Audio Details Hyperlink Label
        self.labelAudioDetails = QLabel(self.centralwidget)
        self.labelAudioDetails.setStyleSheet('font-size: 20px')
        self.labelAudioDetails.setOpenExternalLinks(True)
        self.labelAudioDetails.setText(f"<a href={'file:///E:/skills/audio-predictor/audio-records.csv'}>{'Audio Details'}</a>")
        self.labelAudioDetails.move(710, 740)

        # Text Browser
        self.text = QTextBrowser(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(0, 565, 1200, 120))
        self.text.setAlignment(Qt.AlignCenter)
        self.text.setStyleSheet("font-size:60px;\n"
                                "font:bold 40px;\n")


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # copyrights statusbar
        self.statusbar.showMessage("Copyright © 2021 BFSR. All Rights Reserved.")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def hyperlink_display(self):
        pass

    def start_record_display(self):
        self.text.setText("Recording Started...")
        self.recorder.startrecording()

    def stop_record_display(self):
        self.text.setText("Recording Stopped!!")
        self.recorder.stoprecording()

    def submit_record_display(self):
        self.final_result = self.recorder.submitrecording()
        self.text.setText(self.final_result)
        self.record_window.close()

    def clear_record_display(self):
        self.text.clear()

    def open_file_dialog(self):
        filename, _ = QFileDialog.getOpenFileName()
        self.text.setText(filename)
        self.result = self.model.preprocessing_modelling(filename)
        self.text.setText(self.result)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Audio Predictor"))
        MainWindow.setWindowIcon(QIcon("resources/mainwindow.png"))
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
        MainWindow.setStyleSheet(stylesheet)

        self.recordBtn.setText(_translate("MainWindow", "Record"))
        self.uploadBtn.setText(_translate("MainWindow", "Upload"))
        self.clearBtn.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
