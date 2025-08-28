from PySide6.QtCore import (
    Qt,
    QSize,
    QRect,

    
)
from PySide6.QtGui import QPixmap,QColor
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QLabel,
    QDateEdit,
    QLineEdit,
    QTextEdit,
    QGridLayout,
    QHBoxLayout,
    QVBoxLayout,
    QDateTimeEdit,
     QGraphicsDropShadowEffect,
    QStackedLayout,
    QStackedWidget,
    QSizePolicy
)

class PageOne(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("One")


        #  main variable 
        Vertical = QVBoxLayout() # main
        # Vertical.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)

        # first row

        header = QHBoxLayout()
        header.setAlignment(Qt.AlignmentFlag.AlignTop)
        header.setContentsMargins(5,5,5,5)



        box1 = QWidget()
        box1.setFixedHeight(80)
        box1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        # box1.setStyleSheet("background-color: black;")

        child = QHBoxLayout()

        # box1 ka ander kam ho ga

        boxchild1 = QWidget()
        boxchild1.setFixedHeight(60)
        # boxchild1.setStyleSheet("background-color: blue;")


        # eis ka ander logo icon ha

        iconlayout = QHBoxLayout()

        iconlabel  = QLabel()
        iconlabel.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop )
        pixamp = QPixmap("icon.png")

        iconlabel.setPixmap(pixamp.scaled(40,40,Qt.KeepAspectRatio,Qt.SmoothTransformation))

        iconlayout.addWidget(iconlabel)

        boxchild1.setLayout(iconlayout)







        #  eis main kuch man icons aingin

        boxchild2 = QWidget()
        boxchild2.setFixedHeight(60)
        # boxchild2.setStyleSheet("background-color: white;")

        group1 = QHBoxLayout()
        group1.setAlignment(Qt.AlignmentFlag.AlignRight)
        group1.setSpacing(20)

        loginbtn = QPushButton("Log in")
        loginbtn.setFixedSize(QSize(100,40))
        loginbtn.setStyleSheet("""
        background-color: #151515;
        color: white;
        border-radius: 20px;
        """)

        Siginbtn = QPushButton("Sign up for free")
        Siginbtn.setFixedSize(QSize(200,40))
        Siginbtn.setStyleSheet("""
            background-color: #F4F4F1;
            color: black;
            border:1px solid #e6e6e4;
            border-radius: 20px;
        """)


        group1.addWidget(loginbtn)
        group1.addWidget(Siginbtn)

        boxchild2.setLayout(group1)


        child.addWidget(boxchild1)
        child.addWidget(boxchild2)
        box1.setLayout(child)


        header.addWidget(box1)

        Vertical.addLayout(header)



        # End Header

        # Strat center 

        second_heder = QHBoxLayout()
        # second_heder.setAlignment(Qt.AlignmentFlag.Align)
        center = QWidget()
        center.setFixedHeight(460)
        # center.setStyleSheet("background-color : Red;")

        #  first box lyout

        second_chid = QVBoxLayout()
        second_chid.setAlignment(Qt.AlignmentFlag.AlignTop)
        second_chid.setSpacing(40)

        under_child1 = QHBoxLayout()
        under_child1.setAlignment(Qt.AlignmentFlag.AlignTop)

        label_under_Child = QLabel("ChatGPT")
        label_under_Child.setStyleSheet("color : Black; font-size : 32px; font-weight: 600;")
        label_under_Child.setAlignment(Qt.AlignmentFlag.AlignCenter)

        under_child1.addWidget(label_under_Child)



        center.setLayout(second_chid)
        second_chid.addLayout(under_child1)


        under_child2 = QHBoxLayout()
        under_child2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        text_box_child = QWidget()
        text_box_child.setFixedSize(QSize(700,95))
        text_box_child.setStyleSheet("""
                                     QWidget{
                                        background-color:#F4F4F1 ;
                                        border-radius: 26px;
                                        border:1px solid #0d0d0d0d;

                                     }""")
        
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(10)
        shadow.setOffset(1,1)
        shadow.setColor(QColor(13, 13, 13, 40)) 

        text_box_child.setGraphicsEffect(shadow)


        # Box ka ander work
        box_under_vector = QVBoxLayout()
        box_under_vector.setSpacing(10)

        # index 1 
        input_index_1 = QHBoxLayout()
        input_index_1.setAlignment(Qt.AlignmentFlag.AlignTop)
        input_index_1.setContentsMargins(10,2,2,2)


        input_layout = QLineEdit()
        input_layout.setPlaceholderText("Ask anything")
        # input_layout.setFixedSize(QSize(600,30))
        input_layout.setFixedHeight(40)
        input_layout.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        input_layout.setStyleSheet("background-color:#F4F4F1; color:black; border:noune;font-size:16px ")

        input_index_1.addWidget(input_layout)
        box_under_vector.addLayout(input_index_1)

        under_cild_icon_box = QHBoxLayout()


        input_index_2 = QHBoxLayout()
        input_index_2.setAlignment(Qt.AlignmentFlag.AlignLeft)

        for label in ["Attach","Search","Study"]:
            btn = QPushButton(label)
            btn.setFixedSize(70,35)
            btn.setStyleSheet("border-radius: 17px;background-color:#F4F4F1; color:#A7A5A3; border:1px solid #0d0d0d0d ;font-size:14px; font-weight:600;")
            input_index_2.addWidget(btn)



        input_index_Tow_2 = QHBoxLayout()
        input_index_Tow_2.setAlignment(Qt.AlignmentFlag.AlignRight)

        btne = QPushButton("Voice")
        btne.setFixedSize(70,35)
        btne.setStyleSheet("border-radius: 17px;background-color:#E3E4E4; color:#A7A5A3; border:1px solid #0d0d0d0d ;font-size:14px; font-weight:600;")
        input_index_Tow_2.addWidget(btne)


        under_cild_icon_box.addLayout(input_index_2)
        under_cild_icon_box.addLayout(input_index_Tow_2)

        box_under_vector.addLayout(under_cild_icon_box)








        text_box_child.setLayout(box_under_vector)

        

        under_child2.addWidget(text_box_child)
        second_chid.addLayout(under_child2)
        second_heder.addWidget(center)




        # _______-

        
        Vertical.addLayout(second_heder)
        self.setLayout(Vertical)





class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(QRect(200,30,1200,780))
        self.setMinimumSize(QSize(1200,780))
        self.setWindowTitle('RTIF')

class WindowsAdd(MainWindow):
    def __init__(self):
        super().__init__()

        self.setCentralWidget(PageOne())


app = QApplication()

Window = WindowsAdd()
Window.show()
app.exec()
