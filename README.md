# 포토샵 프로그램 만들기
> Open-cv와 Python을 이용한 간단한 포토샵 프로그램 구현

## 프로그램 기능 
  * 이미지 폴더에서 선택하여 열기
  * 다양한 기능 이미지에 적용
    > 반전, 흑백효과, 노이즈제거, 마스크, 회전, 확대축소, 히스토그램, 블러, 캐니엣지, 볼록렌즈, 관심 영역 지정, 얼굴 인식 
  * 메뉴바 파일-닫기 or x버튼으로 프로그램 종료

## 개발환경
Python Version 3.9 (Window)  
Visual Studio Code(version 1.73)


## 설치
```
pip install opencv-python
pip install pyside6
pip install matplotlib
pip install numpy
```
```
import sys
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PySide6.QtGui import QAction, QImage, QPixmap
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QMainWindow, 
    QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog
)
```
## 업데이트 내역

* 0.1.0
  * 프로그램 첫 출시
* 0.1.1
  * 작동 오류 수정
  
## 프로젝트 예시
![프로그램 실행 예시 화면](https://user-images.githubusercontent.com/117658776/200847048-d93b4546-32b4-4b05-abb7-35536f1e7388.jpg)
