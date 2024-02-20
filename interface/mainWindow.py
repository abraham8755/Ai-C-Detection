import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QFileDialog, QMessageBox, QToolButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QWheelEvent, QPalette, QColor
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import os
import pydicom
from matplotlib import pyplot as plt
from Ui2 import Ui_From  # Ui2'den Ui_From'u içe aktar
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class CancerApp(QMainWindow, Ui_From):
    def __init__(self):
        super(CancerApp, self).__init__()
        self.ui = Ui_From()
        self.ui.setupUi(self)
        icon_path = os.path.join('photos', 'icon.png')
        self.setWindowIcon(QIcon(icon_path))

        self.ui.openFButton.clicked.connect(self.open_file)
        self.ui.nextButton.clicked.connect(self.show_next)
        self.ui.prevButton.clicked.connect(self.show_prev)
        self.ui.horizontalScrollBar.valueChanged.connect(self.scroll_changed)
        self.ui.constrastButton.clicked.connect(self.toggle_contrast)

        # "Rotate" butonlarına bağlantıları ekle
        self.ui.rotateBtn_1.clicked.connect(lambda: self.rotate_image(90))
        self.ui.rotateBtn_2.clicked.connect(lambda: self.rotate_image(-90))
        
        # DicomImageView oluştur
        self.dicom_view = DicomImageView(self)

        # "Reset" butonuna bağlantı ekle
        self.ui.rstBtn.clicked.connect(self.dicom_view.reset_image)
    
        # Klasördeki DICOM dosyalarını tutacak liste
        self.dicom_files = []
        # Mevcut dosyanın indeksini tutacak değişken
        self.current_file_index = 0
        self.setFixedSize(1000, 900)

        # DicomImageView'ı yerleştir
        layout = QVBoxLayout()
        layout.addWidget(self.dicom_view)
        self.ui.DicomImageView.setLayout(layout)

    def rotate_image(self, angle):
        if self.dicom_files and self.dicom_view.hasDicomFile():
            self.dicom_view.rotate_image(angle)

    def toggle_contrast(self):
        if self.dicom_files and self.dicom_view.hasDicomFile():
            self.dicom_view.toggleContrast()

    def scroll_changed(self, value):
        # ScrollBar değisiğiğinde dosya indeksini güncelle
        if self.dicom_files:
            self.current_file_index = value
            self.dicom_view.setDicomFile(self.dicom_files[self.current_file_index])
            self.update_index_label()

    def open_file(self):
        file_dialog = QFileDialog()
        folder_path = file_dialog.getExistingDirectory(self, 'Select Folder Containing DICOM Files', '')
        if folder_path:
            # Dosya seçimi sırasında klasördeki tüm DICOM dosyalarını al
            self.dicom_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if
                                os.path.splitext(file.lower())[1] == '.dcm']

            # İlk dosyayı göster
            if self.dicom_files:
                self.current_file_index = 0
                self.dicom_view.setDicomFile(self.dicom_files[self.current_file_index])
                self.update_index_label()

                # ScrollBar'ın maksimum değerini güncelle
                self.ui.horizontalScrollBar.setMaximum(len(self.dicom_files) - 1)
            else:
                # Geçersiz klasör seçildiğinde uyarı ver
                QMessageBox.warning(self, 'Uyarı', 'Geçersiz klasör - Tekrar seçiniz.')

    def show_prev(self):
        if self.dicom_files:
            self.current_file_index -= 1
            if self.current_file_index < 0:
                self.current_file_index = len(self.dicom_files) - 1
            self.dicom_view.setDicomFile(self.dicom_files[self.current_file_index])
            self.ui.horizontalScrollBar.setValue(self.current_file_index)
            self.update_index_label()

    def show_next(self):
        if self.dicom_files:
            self.current_file_index += 1
            if self.current_file_index >= len(self.dicom_files):
                self.current_file_index = 0
            self.dicom_view.setDicomFile(self.dicom_files[self.current_file_index])
            self.ui.horizontalScrollBar.setValue(self.current_file_index)
            self.update_index_label()

    def update_index_label(self):
        # Güncellenmiş dosya indeksini labela yaz
        total_files = len(self.dicom_files)
        current_index = self.current_file_index + 1
        self.ui.index_label.setText(f"{current_index}/{total_files}")

    def wheelEvent(self, event):
        # Mouse wheel olayını yakala
        if self.dicom_files and event.angleDelta().y() > 0:
            # Mouse tekerleği yukarı doğru hareket ettiğinde bir önceki resmi göster
            self.show_prev()
        elif self.dicom_files:
            # Mouse tekerleği aşağı doğru hareket ettiğinde bir sonraki resmi göster
            self.show_next()


class DicomImageView(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()
        self.parent = parent  # Parent sınıf referansını sakla


    def initUI(self):
        # Matplotlib için bir figür ve canvas oluştur
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        # Canvas'ı yerleştir
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.contrast_inverted = False  # Başlangıçta kontrast tersine çevirilmedi
        self.current_dicom_file = None  # Mevcut DICOM dosyasının yolu

         # NavigationToolbar'ı ekleyin
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.layout().addWidget(self.toolbar)
        
        # Boyut politikasını sabit boyut olarak ayarla
        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.canvas.setSizePolicy(size_policy)

    def resizeEvent(self, event):
        # Yeniden boyutlandırma olayını ele al
        new_size = event.size()
        self.canvas.setFixedSize(new_size)  # Canvas'ı label boyutlarına eşitle
        self.figure.set_size_inches(new_size.width() / self.figure.get_dpi(), new_size.height() / self.figure.get_dpi())
        self.canvas.draw()

    def rotate_image(self, angle):
        if self.hasDicomFile():
            # Mevcut görüntüyü belirtilen açıda çevir
            image = self.ax.get_images()[0]
            data = image.get_array()
            rotated_data = np.rot90(data, k=int(angle / 90))
            image.set_array(rotated_data)
            self.canvas.draw()

    def setDicomFile(self, file_path):
        dicom_image = pydicom.dcmread(file_path)
        image_array = dicom_image.pixel_array

        # Rescale Slope ve Rescale Intercept değerlerini kontrol et
        if 'RescaleSlope' in dicom_image and 'RescaleIntercept' in dicom_image:
            slope = dicom_image.RescaleSlope
            intercept = dicom_image.RescaleIntercept
            # Görüntüyü düzelt
            image_array = image_array * slope + intercept

        # Eski içeriği temizle
        self.ax.clear()

        # Yeni görüntüyü çiz
        height, width = image_array.shape
        extent = [0, width, height, 0]  # Görüntüyü tamamen dolduracak şekilde ayarla
        self.ax.imshow(image_array, cmap='gray', aspect='auto', extent=extent)
        self.ax.axis('off')  # Eksenleri kapat

        self.current_dicom_file = file_path  # Mevcut dosya yolu güncelle
        self.zoom_factor = 1.0  # Her yeni dosyada zoom faktörünü sıfırla
        self.canvas.draw()

    def hasDicomFile(self):
        return hasattr(self, 'ax') and self.ax.has_data()

    def toggleContrast(self):
        if self.hasDicomFile():
            # Renk kontrastını tersine çevir
            image = self.ax.get_images()[0]
            data = image.get_array()
            inverted_data = np.amax(data) - data
            image.set_array(inverted_data)
            self.canvas.draw()

    def reset_image(self):
        # Mevcut görüntüyü orijinal haline getir
        if self.hasDicomFile():
            file_path = self.current_dicom_file
            self.setDicomFile(file_path)

def app():
    app = QApplication(sys.argv)
    win = CancerApp()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()
