"""Object Detector App Entry Point"""

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Real-Time Object Tracker App")
        self.setGeometry(100, 100, 400, 300)

        start_button = QPushButton("Start Detection", self)
        start_button.clicked.connect(self.start_detection)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("put camera window"))
        layout.addWidget(start_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def start_detection(self):
        """Object detection starting point and switch to camera window"""
        print("Starting detection")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
