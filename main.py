"""Object Tracker App Entry Point"""

import sys
import cv2 as cv
import numpy as np
from ultralytics import YOLO
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
        """Starts object detection in the new camera window"""
        print("Starting detection")
        cap = cv.VideoCapture(0)
        model = YOLO("yolo11n.pt")

        if not cap.isOpened():
            print("Cannot open camera")
            exit()

        while True:
            # Read a frame
            success, frame = cap.read()

            if not success:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            # Run YOLO11 tracking on the frame, persisting tracks between frames
            results = model.track(frame, persist=True)

            # Visualize the results on the frame
            annotated_frame = results[0].plot()

            # Display the annotated frame
            cv.imshow("YOLO11 Tracking", annotated_frame)
            if cv.waitKey(1) == ord("q"):
                break

        # When everything done, release the capture
        cap.release()
        cv.destroyAllWindows()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
