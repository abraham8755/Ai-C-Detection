import sys
from ui_interface import *
import numpy as np
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QFileDialog, QMessageBox, QToolButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap, QWheelEvent, QPalette, QColor
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import os
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from PySide6.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect the actionOpen triggered signal to open_file method
        self.ui.actionOpen.triggered.connect(self.open_file)

        # Create a QLabel to display the image
        self.image_label = QLabel()
        self.image_label.setScaledContents(True)  # Scale the image to fit the label

        # Create a QVBoxLayout to hold the image label
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)

        # Set the layout on the frame widget
        self.ui.frame.setLayout(layout)

        # Set the size policy of the frame to Expanding in both directions
        frame_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        frame_policy.setHorizontalStretch(1)  # Allow horizontal expansion
        frame_policy.setVerticalStretch(1)    # Allow vertical expansion
        self.ui.frame.setSizePolicy(frame_policy)

    def open_file(self):
    # Open file dialog to select a file
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'All Files (*)')
        if file_path:
            # Load the image from file
            pixmap = QPixmap(file_path)

            # Set the pixmap on the QLabel to display the image
            self.image_label.setPixmap(pixmap)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
