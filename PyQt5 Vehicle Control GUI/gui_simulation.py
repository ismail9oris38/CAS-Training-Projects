import sys
import os
import random
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout, QLineEdit, QTextEdit, QSizePolicy
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, QTimer

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kullanıcı Girişi")
        self.setGeometry(400, 400, 500, 400)
        self.setStyleSheet("background-color: #2c3e50; color: white; font-family: Arial; font-size: 14px;")

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Mesaj
        self.message = QLabel("Hoş Geldiniz")
        self.message.setStyleSheet("font-size:18px; font-weight:bold; margin-bottom:15px;")
        self.layout.addWidget(self.message, 3, 0, 1, 2)

        # Kullanıcı adı
        self.name_label = QLabel("Kullanıcı Adı: ")
        self.name_textbox = QLineEdit()
        self.name_textbox.setStyleSheet(
            "padding: 8px; border-radius: 8px; border: 1px solid #bdc3c7; background-color: #ecf0f1; color: black;"
        )

        # Şifre
        self.password_label = QLabel("Şifre: ")
        self.password_textbox = QLineEdit()
        self.password_textbox.setEchoMode(QLineEdit.Password)
        self.password_textbox.setStyleSheet(
            "padding: 8px; border-radius: 8px; border: 1px solid #bdc3c7; background-color: #ecf0f1; color: black;"
        )

        # Buton
        self.button = QPushButton("Giriş Yap")
        self.button.setStyleSheet(
            "background-color: #3498db; padding: 10px; border-radius: 8px; font-weight:bold; color:white;"
        )
        self.button.clicked.connect(self.check_entry)

        # Layout ekleme
        self.layout.addWidget(self.name_label, 0, 0)
        self.layout.addWidget(self.name_textbox, 0, 1)
        self.layout.addWidget(self.password_label, 1, 0)
        self.layout.addWidget(self.password_textbox, 1, 1)
        self.layout.addWidget(self.button, 2, 0, 1, 2)

    def check_entry(self):
        if self.name_textbox.text() == "kullanıcı adı" and self.password_textbox.text() == "şifre":
            self.open_main_window()
        else:
            self.message.setText("❌ Kullanıcı Adı veya Şifreniz Yanlış!")

    def open_main_window(self):
        self.hide()
        self.main_window = QWidget()
        self.main_window.setWindowTitle("Temel Prototip")
        self.main_window.setGeometry(400, 400, 900, 600)
        self.main_window.setStyleSheet("background-color: #34495e; color: white; font-family: Arial;")

        self.main_layout = QGridLayout()
        self.main_window.setLayout(self.main_layout)

        # Video widget
        self.video_widget = QVideoWidget()
        self.video_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.main_layout.addWidget(self.video_widget, 0, 0, 3, 2)

        # Player
        self.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.player.setVideoOutput(self.video_widget)
        self.video_path = os.path.join(os.path.dirname(__file__), "Line.mp4")
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.video_path)))

        # Mission buttons
        self.btn_start_mission = QPushButton("Start Mission")
        self.btn_stop_mission = QPushButton("Stop Mission")
        for btn in [self.btn_start_mission, self.btn_stop_mission]:
            btn.setStyleSheet(
                "background-color: #1abc9c; padding:8px; border-radius:10px; font-weight:bold; color:white;"
            )
        self.main_layout.addWidget(self.btn_start_mission, 3, 0)
        self.main_layout.addWidget(self.btn_stop_mission, 3, 1)

        # Mission text
        self.mission_text = QTextEdit()
        self.mission_text.setStyleSheet(
            "background-color: #ecf0f1; color: black; border-radius:10px; padding:5px;"
        )
        self.main_layout.addWidget(self.mission_text, 4, 0, 2, 2)

        # Sağ panel
        self.time_label = QLabel("Süre: ")
        self.time_label.setStyleSheet(
            "font-weight: bold; font-size: 18px; border: 2px solid #2c3e50; border-radius: 10px; padding:6px; background-color:#2980b9; color:white;"
        )

        self.btn_start = QPushButton("Başlat")
        self.btn_stop = QPushButton("Durdur")
        self.btn_finish = QPushButton("Bitir")
        for btn in [self.btn_start, self.btn_stop, self.btn_finish]:
            btn.setStyleSheet(
                "background-color: #e67e22; padding:8px; border-radius:10px; font-weight:bold; color:white;"
            )

        self.data = QLabel("Araç Verileri")
        self.press = QLabel("Basınç: 25")
        self.heat = QLabel("Sıcaklık: 17 Derece")

        self.data.setStyleSheet(
            "font-size:18px; font-weight:bold; padding:5px; background-color:#16a085; border-radius:10px; color:white;"
        )
        for lbl in [self.press, self.heat]:
            lbl.setStyleSheet(
                "font-size:16px; font-weight:bold; background-color: #2980b9; border-radius: 15px; padding:10px; color:white;"
            )

        self.main_layout.addWidget(self.time_label, 0, 2, 1, 3)
        self.main_layout.addWidget(self.btn_start, 1, 2)
        self.main_layout.addWidget(self.btn_stop, 1, 3)
        self.main_layout.addWidget(self.btn_finish, 1, 4)
        self.main_layout.addWidget(self.data, 2, 2, 1, 3)
        self.main_layout.addWidget(self.press, 3, 2, 1, 3)
        self.main_layout.addWidget(self.heat, 4, 2, 1, 3)

        # Timer
        self.timer = QTimer()
        self.counter = 0
        self.timer.timeout.connect(self.update_counter)
        self.btn_start.clicked.connect(self.start_timer)
        self.btn_stop.clicked.connect(self.stop_timer)
        self.btn_finish.clicked.connect(self.finish)

        # Grid Stretch ile boyutları dengeli yap
        self.main_layout.setColumnStretch(0, 3)
        self.main_layout.setColumnStretch(1, 3)
        self.main_layout.setColumnStretch(2, 1)
        self.main_layout.setColumnStretch(3, 1)
        self.main_layout.setColumnStretch(4, 1)

        self.main_layout.setRowStretch(0, 1)
        self.main_layout.setRowStretch(1, 1)
        self.main_layout.setRowStretch(2, 1)
        self.main_layout.setRowStretch(3, 1)
        self.main_layout.setRowStretch(4, 1)
        self.main_layout.setRowStretch(5, 2)

        self.main_window.show()

    def start_timer(self):
        self.timer.start(1000)
        self.player.play()

    def stop_timer(self):
        self.timer.stop()
        self.player.stop()

    def update_counter(self):
        self.counter += 1
        self.time_label.setText(f"Süre: {self.counter}")
        self.press.setText(f"Basınç: {random.randint(20,30)}")
        self.heat.setText(f"Sıcaklık: {random.randint(10, 25)}")

    def finish(self):
        self.main_window.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec_())
