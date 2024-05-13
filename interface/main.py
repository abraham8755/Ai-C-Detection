import sys
from ui_interface import *
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFileDialog, QLabel, QSizePolicy
from PySide6.QtGui import QPixmap
import os
import pydicom
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import subprocess


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect the actionOpen triggered signal to open_file method
        self.ui.actionOpen.triggered.connect(self.open_file)

        # Create a QVBoxLayout to hold the image label
        self.layout = QVBoxLayout(self.ui.frame)

        # Set the size policy of the frame to Expanding in both directions
        frame_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        frame_policy.setHorizontalStretch(1)  # Allow horizontal expansion
        frame_policy.setVerticalStretch(1)    # Allow vertical expansion
        self.ui.frame.setSizePolicy(frame_policy)

    def open_file(self):
        # Open file dialog to select a file
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'All Files (*)')
        if file_path:
            # Check if the file is a DICOM file
            if self.is_dicom(file_path):
                # Load DICOM image
                dicom_image = self.load_dicom(file_path)
                # Display DICOM image
                self.display_dicom(dicom_image)
                # Pass the file path to mask.py
                self.process_dicom_file(file_path)
            else:
                # Load the image from file
                pixmap = QPixmap(file_path)
                # Set the pixmap on the QLabel to display the image
                image_label = QLabel()
                image_label.setPixmap(pixmap)
                # Clear previous images
                for i in reversed(range(self.layout.count())):
                    widget = self.layout.itemAt(i).widget()
                    if widget is not None:
                        widget.deleteLater()
                # Add the image label to the layout
                self.layout.addWidget(image_label)

    def is_dicom(self, file_path):
        try:
            # Try to read the DICOM file
            pydicom.dcmread(file_path)
            return True
        except pydicom.errors.InvalidDicomError:
            return False

    def load_dicom(self, file_path):
        return pydicom.dcmread(file_path)

    def display_dicom(self, dicom_image):
        # Clear previous images
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # Create a figure for displaying DICOM image
        fig = Figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        ax.imshow(dicom_image.pixel_array, cmap='gray')
        ax.axis('off')  # Hide axis
        self.layout.addWidget(canvas)

    def process_dicom_file(self, file_path):
        # Call mask.py with the file path
        subprocess.run(["python", "mask.py", file_path])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
