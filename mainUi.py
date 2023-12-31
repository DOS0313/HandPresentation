# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\default.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QFontDatabase, QImage, QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 629)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 600))
        MainWindow.setStyleSheet("background-color:rgb(17, 17, 17);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Video_Space = QtWidgets.QVBoxLayout()
        self.Video_Space.setObjectName("Video_Space")
        self.Video_Title = QtWidgets.QLabel(self.centralwidget)
        self.Video_Title.setStyleSheet("color: rgb(255, 255, 255);")
        self.Video_Title.setObjectName("Video_Title")
        self.Video_Space.addWidget(self.Video_Title)
        self.Video = QtWidgets.QGraphicsView(self.centralwidget)
        self.Video.setStyleSheet("background-color: rgb(213, 213, 213);\n"
"border-radius: 8px;")
        self.Video.setObjectName("Video")
        self.Video_Space.addWidget(self.Video)
        self.horizontalLayout.addLayout(self.Video_Space)
        self.Options_Space = QtWidgets.QVBoxLayout()
        self.Options_Space.setObjectName("Options_Space")
        self.Input_Title = QtWidgets.QLabel(self.centralwidget)
        self.Input_Title.setStyleSheet("color: rgb(255, 255, 255);")
        self.Input_Title.setObjectName("Input_Title")
        self.Options_Space.addWidget(self.Input_Title)
        self.Input_Combo = QtWidgets.QComboBox(self.centralwidget)
        self.Input_Combo.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 1px solid #444;\n"
"background-color: #202020;")
        self.Input_Combo.setObjectName("Input_Combo")
        self.Input_Combo.addItem("")
        self.Input_Combo.addItem("")
        self.gesture_type = 'rock'  # 초기값 설정
        self.action_key = 'space'  # 초기값 설정
        self.Input_Combo.currentIndexChanged.connect(self.onInputComboChanged)
        self.Options_Space.addWidget(self.Input_Combo)
        self.Move_Title = QtWidgets.QLabel(self.centralwidget)
        self.Move_Title.setStyleSheet("color: rgb(255, 255, 255);")
        self.Move_Title.setObjectName("Move_Title")
        self.Options_Space.addWidget(self.Move_Title)
        self.Move_Slider = QtWidgets.QSlider(self.centralwidget)
        self.Move_Slider.setMinimum(1)
        self.Move_Slider.setMaximum(100)
        self.Move_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Move_Slider.setInvertedAppearance(False)
        self.Move_Slider.setInvertedControls(False)
        self.Move_Slider.setObjectName("Move_Slider")
        self.Move_Slider.valueChanged.connect(self.updateMove_Title)
        self.Options_Space.addWidget(self.Move_Slider)
        self.Gesture_Title = QtWidgets.QLabel(self.centralwidget)
        self.Gesture_Title.setStyleSheet("color: rgb(255, 255, 255);")
        self.Gesture_Title.setObjectName("Gesture_Title")
        self.Options_Space.addWidget(self.Gesture_Title)
        self.Gesture_Slider = QtWidgets.QComboBox(self.centralwidget)
        self.Gesture_Slider.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 1px solid #444;\n"
"background-color: #202020;")
        self.Gesture_Slider.setObjectName("Gesture_Slider")
        self.Gesture_Slider.addItem("")
        self.Gesture_Slider.addItem("")
        self.Gesture_Slider.addItem("")
        self.Options_Space.addWidget(self.Gesture_Slider)

        self.Gesture_Title.hide()
        self.Gesture_Slider.hide()

        self.Action_Title = QtWidgets.QLabel(self.centralwidget)
        self.Action_Title.setStyleSheet("color: rgb(255, 255, 255);")
        self.Action_Title.setObjectName("Action_Title")
        self.Options_Space.addWidget(self.Action_Title)
        self.Action_Key = QtWidgets.QKeySequenceEdit(self.centralwidget)
        self.Action_Key.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 1px solid #444;\n"
"background-color: #202020;")
        self.Action_Key.setKeySequence("")
        self.Action_Key.setObjectName("Action_Key")
        self.Action_Key.keySequenceChanged.connect(self.limitKeySequence)
        self.Options_Space.addWidget(self.Action_Key)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Options_Space.addItem(spacerItem)
        self.Apply_Btn = QtWidgets.QPushButton(self.centralwidget)
        self.Apply_Btn.setStyleSheet("color: #ffffff;\n"
"border-radius: 8px;\n"
"border: 1px solid #ffffff;")
        self.Apply_Btn.setCheckable(False)
        self.Apply_Btn.setAutoDefault(False)
        self.Apply_Btn.setDefault(False)
        self.Apply_Btn.setFlat(False)
        self.Apply_Btn.setObjectName("Apply_Btn")
        self.Apply_Btn.setMinimumHeight(72)
        self.Apply_Btn.clicked.connect(self.apply_button_clicked)
        self.Options_Space.addWidget(self.Apply_Btn)
        self.horizontalLayout.addLayout(self.Options_Space)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HandPresentation"))
        self.Video_Title.setText(_translate("MainWindow", "Video Source"))
        self.Input_Title.setText(_translate("MainWindow", "Input Type"))
        self.Input_Combo.setItemText(0, _translate("MainWindow", "Movement"))
        self.Input_Combo.setItemText(1, _translate("MainWindow", "Gesture"))
        self.Move_Title.setText(_translate("MainWindow", "Movement Value - 1"))
        self.Gesture_Title.setText(_translate("MainWindow", "Gesture Type"))
        self.Gesture_Slider.setItemText(0, _translate("MainWindow", "Rock"))
        self.Gesture_Slider.setItemText(1, _translate("MainWindow", "Scissor"))
        self.Gesture_Slider.setItemText(2, _translate("MainWindow", "Paper"))
        self.Action_Title.setText(_translate("MainWindow", "Action Key"))
        self.Apply_Btn.setText(_translate("MainWindow", "Apply"))

    def onInputComboChanged(self, index):
        if index == 0:  # Movement 선택 시
            self.Move_Title.show()
            self.Move_Slider.show()
            self.Gesture_Title.hide()
            self.Gesture_Slider.hide()
        elif index == 1:  # Gesture 선택 시
            self.Move_Title.hide()
            self.Move_Slider.hide()
            self.Gesture_Title.show()
            self.Gesture_Slider.show()

    # 'Apply' 버튼이 눌렸을 때의 동작 추가
    def apply_button_clicked(self):
        # Gesture Combo의 현재 선택값을 gesture_type 변수에 할당
        gesture_type_index = self.Gesture_Slider.currentIndex()
        if gesture_type_index == 0:
            self.gesture_type = 'rock'
        elif gesture_type_index == 1:
            self.gesture_type = 'scissor'
        elif gesture_type_index == 2:
            self.gesture_type = 'paper'

        # Action Key 값
        action_key_sequence = self.Action_Key.keySequence()
        self.action_key = action_key_sequence.toString()

    def display_frame(self, img):
        """
        OpenCV의 Mat 형식 영상을 PyQt5의 QGraphicsView에 표시
        """
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg.rgbSwapped())

        # 이미지 크기가 QGraphicsView보다 크면 축소하여 표시
        view_width = self.Video.width()
        view_height = self.Video.height()

        # 이미지를 QGraphicsView에 맞도록 크기 조절
        if width > view_width or height > view_height:
            aspect_ratio = width / height
            if aspect_ratio >= view_width / view_height:
                new_width = view_width
                new_height = int(view_width / aspect_ratio)
            else:
                new_height = view_height
                new_width = int(view_height * aspect_ratio)

            pixmap = pixmap.scaled(new_width, new_height, Qt.KeepAspectRatio)

        # QGraphicsScene에 pixmap을 추가하여 QGraphicsView에 표시
        scene = QtWidgets.QGraphicsScene()
        scene.addPixmap(pixmap)

        # Video에 scene 설정
        self.Video.setScene(scene)
        self.Video.show()

    # Move_Slider의 값에 따라 Move_Title 변경 함수
    def updateMove_Title(self, value):
        self.Move_Title.setText(f"Movement Value - {value}")

    def limitKeySequence(self, key_sequence):
        if len(key_sequence.toString()) > 1:  # 허용된 최대 키 개수 이상 입력된 경우
            keys = key_sequence.toString().split(', ')[:1]  # 쉼표로 구분된 키들을 가져옴 (최대 2개)
            new_sequence = ', '.join(keys)  # 최대 2개의 키로 조합된 새로운 시퀀스 생성
            self.Action_Key.setKeySequence(new_sequence) # 새로운 시퀀스로 설정

            print(str(new_sequence))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Pretendard Variable 폰트 적용
    fontDB = QFontDatabase()
    fontDB.addApplicationFont('./font/PretendardVariable.ttf')
    app.setFont(QFont('Pretendard'))

    import cv2
    import mediapipe as mp
    import numpy as np
    import keyboard

    max_num_hands = 2
    gesture = {
        0: 'fist', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'rock', 8: 'spiderman', 9: 'yeah', 10: 'ok',
    }  # 사용 안함
    rps_gesture = {0: 'rock', 5: 'paper', 9: 'scissors'}

    flag = False

    # MediaPipe Hand landmark 모델
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    hands = mp_hands.Hands(
        max_num_hands=max_num_hands,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5)

    # 제스쳐 인식 모델
    file = np.genfromtxt('data/gesture_train.csv', delimiter=',')
    angle = file[:, :-1].astype(np.float32)
    label = file[:, -1].astype(np.float32)
    knn = cv2.ml.KNearest_create()
    knn.train(angle, cv2.ml.ROW_SAMPLE, label)

    cap = cv2.VideoCapture(0)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = hands.process(frame)

        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        if result.multi_hand_landmarks is not None:
            for res in result.multi_hand_landmarks:
                joint = np.zeros((21, 3))
                for j, lm in enumerate(res.landmark):
                    joint[j] = [lm.x, lm.y, lm.z]

                # 관절끼리의 각도 계산
                v1 = joint[[0, 1, 2, 3, 0, 5, 6, 7, 0, 9, 10, 11, 0, 13, 14, 15, 0, 17, 18, 19], :]  # Parent joint
                v2 = joint[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], :]  # Child joint
                v = v2 - v1  # [20,3]
                # v로 정규화
                v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

                # Get angle using arcos of dot product
                angle = np.arccos(np.einsum('nt,nt->n',
                                            v[[0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14, 16, 17, 18], :],
                                            v[[1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19], :]))  # [15,]

                angle = np.degrees(angle)  # Convert radian to degree

                # 제스처 인터페이스
                data = np.array([angle], dtype=np.float32)
                ret, results, neighbours, dist = knn.findNearest(data, 3)
                idx = int(results[0][0])

                # 결과값 인터페이스에 표기
                if idx in rps_gesture.keys():
                    cv2.putText(frame, text=rps_gesture[idx].upper(),
                                org=(int(res.landmark[0].x * frame.shape[1]), int(res.landmark[0].y * frame.shape[0] + 20)),
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 255, 255), thickness=2)

                    # print(res.landmark)

                    if rps_gesture [idx] == ui.gesture_type: # 해당 부분이 키보드 입력부
                        if not flag:
                            keyboard.send(ui.action_key)
                            flag = True
                    else:
                        flag = False

                mp_drawing.draw_landmarks(frame, res, mp_hands.HAND_CONNECTIONS)

        # frame을 mainUi.py의 Video에 표시
        ui.display_frame(frame)

        # Qt 이벤트 루프 처리
        QtWidgets.QApplication.processEvents()

        # 영상 재생 종료 시 해제
    cap.release()
    cv2.destroyAllWindows()

    sys.exit(app.exec_())
