import sys
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PySide6.QtGui import QAction, QImage, QPixmap
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QMainWindow, 
    QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Photoshop")

        # 메뉴바 만들기
        self.menu = self.menuBar()
        self.menu_file = self.menu.addMenu("파일")
        exit = QAction("나가기", self, triggered=qApp.quit)
        self.menu_file.addAction(exit)


        # 메인화면 레이아웃
        main_layout = QHBoxLayout()

        # 사이드바 메뉴버튼
        sidebar = QVBoxLayout()
        button1 = QPushButton("이미지 열기")
        button2 = QPushButton("새로고침")
        button3 = QPushButton("좌우반전")
        button4 = QPushButton("상하반전")
        button5 = QPushButton("흑백변환")
        button6 = QPushButton("노이즈제거")
        button7 = QPushButton("원마스크")
        button8 = QPushButton("회전")
        button9 = QPushButton("확대")
        button10 = QPushButton("축소")
        button11 = QPushButton("히스토그램")
       
       
       
        
        button1.clicked.connect(self.show_file_dialog)
        button2.clicked.connect(self.clear_label)
        button3.clicked.connect(self.flip_image)
        button4.clicked.connect(self.flip_image2)
        button5.clicked.connect(self.image_grey)
        button6.clicked.connect(self.denoise)
        button7.clicked.connect(self.circle_image)
        button8.clicked.connect(self.rotate_image)
        button9.clicked.connect(self.big_image)
        button10.clicked.connect(self.small_image)
        button11.clicked.connect(self.hist)
      
        sidebar.addWidget(button1)
        sidebar.addWidget(button2)
        sidebar.addWidget(button3)
        sidebar.addWidget(button4)
        sidebar.addWidget(button5)
        sidebar.addWidget(button6)
        sidebar.addWidget(button7)
        sidebar.addWidget(button8)
        sidebar.addWidget(button9)
        sidebar.addWidget(button10)
        sidebar.addWidget(button11)
     

        main_layout.addLayout(sidebar)

        self.label1 = QLabel(self)
        self.label1.setFixedSize(640, 480)
        main_layout.addWidget(self.label1)

        self.label2 = QLabel(self)
        self.label2.setFixedSize(640, 480)
        main_layout.addWidget(self.label2)

        widget = QWidget(self)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
    
    def show_file_dialog(self):
        file_name = QFileDialog.getOpenFileName(self, "이미지 열기", "./")
        self.image = cv2.imread(file_name[0])
        h, w, _ = self.image.shape
        bytes_per_line = 3 * w
        image = QImage(
            self.image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label1.setPixmap(pixmap)
    
   

    def flip_image(self):
        image = cv2.flip(self.image, 1)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

    def flip_image2(self):
        img = self.image
        image = cv2.flip(img, 0)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

    def clear_label(self):
        self.label2.clear()

    def image_grey(self):
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        h, w = image.shape
        bytes_per_line = 1 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_Grayscale8
        )
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
       
    def denoise(self):
        image = cv2.fastNlMeansDenoisingColored(self.image, None, 15, 15, 5, 10)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

    def circle_image(self):
        img = self.image
        h, w,_= img.shape[:3]
        mask = np.zeros_like(img)
        cv2.circle(mask, (h//2, h//2), h//3, (255, 255, 255), -1)
        image = cv2.bitwise_and(img, mask)
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label1.setPixmap(pixmap)

    def rotate_image(self):
        src=self.image
        h, w, _ = src.shape
        matrix = cv2.getRotationMatrix2D((w/2, h/2), 90, 1)
        image = cv2.warpAffine(src, matrix, (w, h))
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label1.setPixmap(pixmap)

    def big_image(self):
        image = cv2.resize(self.image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

    def small_image(self):
        image = cv2.resize(self.image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

    def hist(self):
        img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        image = cv2.calcHist([img], [0], None, [256], [0, 256])
        h, w = image.shape
        bytes_per_line = 1 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_Grayscale8
        )
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        

        

    
   








if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())




