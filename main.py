from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from waitingspinnerwidget import QtWaitingSpinner
import sys
from youtube_converter import YouTubeManager


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("YouTube Converter")
        self.setGeometry(100, 100, 1000, 600)
        self.setStyleSheet("background-color: #2c3e50;")

        # toolbar
        # self.statusBar()
        self.menu_bar = self.menuBar()
        self.menu_bar.setStyleSheet("""
        
        QMenuBar {
             background-color: white;
        }
        QMenuBar::item {
            spacing: 3px;           
            padding: 2px 10px;
            background-color: white;
            color: rgb(0,0,0);  
           
        }
        QMenuBar::item:selected {    
                background-color:white;
            }
        QMenuBar::item:pressed {
                background: white;
            }
        """)

        file_menu = self.menu_bar.addMenu('&File')
        file_menu.addAction("Open Download Location")
        settings = self.menu_bar.addMenu("Settings")
        help = self.menu_bar.addMenu("Help")

        # fileMenu.addAction(exitAct)

        # loading image
        self.spinner = QtWaitingSpinner(self)
        self.spinner.setRoundness(70.0)
        self.spinner.setMinimumTrailOpacity(15.0)
        self.spinner.setTrailFadePercentage(70.0)
        self.spinner.setNumberOfLines(12)
        self.spinner.setLineLength(10)
        self.spinner.setLineWidth(5)
        self.spinner.setInnerRadius(10)
        self.spinner.setRevolutionsPerSecond(1)
        self.spinner.setColor(QColor(81, 4, 71))
        self.spinner.start()
        self.spinner.hide()

        self.logo = QLabel()
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pixmap = QPixmap('logo.png')
        self.logo.setPixmap(self.pixmap.scaled(400, 300))
        self.text_box = QLineEdit()
        self.text_box.setText("https://music.youtube.com/watch?v=b1HsNByXsdc&list=RDAMVMb1HsNByXsdc")
        self.text_box.setStyleSheet("background-color: White")
        self.text_box.setFixedWidth(600)

        self.status_label = QLabel("Downloading Video...")
        self.status_label.setStyleSheet("color:white")
        self.status_label.hide()

        self.convert_button = QPushButton("Convert")
        self.convert_button.setFixedWidth(100)
        self.convert_button.setStyleSheet("background-color: White")
        self.convert_button.clicked.connect(self.convert)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.logo)
        self.layout.addWidget(self.text_box)
        self.layout.addWidget(self.status_label)
        self.layout.addWidget(self.spinner)
        self.layout.addWidget(self.convert_button)
        self.layout.setContentsMargins(200, 0, 200, 0)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

        # after everything is created we pass to the YouTube manager

    def convert(self):
        pass


############## Style

qss = """
QMenuBar {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                      stop:0 lightgray, stop:1 darkgray);
}
QMenuBar::item {
    spacing: 3px;           
    padding: 2px 10px;
    background-color: rgb(210,105,30);
    color: rgb(255,255,255);  
    border-radius: 5px;
}
QMenuBar::item:selected {    
    background-color: rgb(244,164,96);
}
QMenuBar::item:pressed {
    background: rgb(128,0,0);
}

/* +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ */  

QMenu {
    background-color: #ABABAB;   
    border: 1px solid black;
    margin: 2px;
}
QMenu::item {
    background-color: transparent;
}
QMenu::item:selected { 
    background-color: #654321;
    color: rgb(255,255,255);
}
"""

app = QApplication(sys.argv)
window = MainWindow()
# window.setStyleSheet(qss)
window.show()
# Start the event loop.
app.exec()
