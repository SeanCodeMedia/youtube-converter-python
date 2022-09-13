from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from waitingspinnerwidget import QtWaitingSpinner
import sys
import requests
from youtube_converter import YouTubeManager


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("YouTube Converter")
        self.setGeometry(100, 100, 1000, 600)
        self.setStyleSheet("background-color: #2c3e50;")
        self.object_dict = {}


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

        # menu bar
        file_menu = self.menu_bar.addMenu('&File')
        file_menu.addAction("Open Download Location")
        settings = self.menu_bar.addMenu("Settings")
        settings.addAction("Set Download Location")
        help = self.menu_bar.addMenu("Help")
        help.addAction("About")
        help.addAction("Version")

        # loading widget
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

        # logo image
        self.logo = QLabel()
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pixmap = QPixmap('logo.png')
        self.logo.setPixmap(self.pixmap.scaled(400, 300))

        # thumbnail

        self.url = 'https://www.techsmith.com/blog/wp-content/uploads/2019/06/YouTube-Thumbnail-Sizes.png'
        self.thumbnail_image_data = QImage()
        self.thumbnail_image_data.loadFromData(requests.get(self.url).content)
        self.thumbnail_image = QLabel()
        self.thumbnail_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.thumbnail_image.setPixmap(QPixmap(self.thumbnail_image_data).scaled(300, 200))
        self.thumbnail_image.show()

        # text input
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

        self.stack_layout = QStackedLayout()
        self.stack_layout.addWidget(self.logo)
        self.stack_layout.addWidget(self.thumbnail_image)
        self.stack_layout.setCurrentIndex(0)

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.stack_layout)
        self.layout.addWidget(self.text_box)
        self.layout.addWidget(self.status_label)
        self.layout.addWidget(self.convert_button)
        self.layout.setContentsMargins(200, 100, 200, 200)
        self.layout.addWidget(self.spinner)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

        self.object_dict["stack_layout"] = self.stack_layout
        self.object_dict["thumbnail_image_data"] = self.thumbnail_image_data
        self.object_dict["thumbnail_image"] = self.thumbnail_image
        self.object_dict["status_label"] = self.status_label
        self.object_dict["spinner"] = self.spinner
        self.object_dict["convert_button"] = self.convert_button
        self.object_dict["text_box"] = self.text_box
        self.object_dict["logo"] = self.logo
        self.youtube_manager = YouTubeManager(self.object_dict)

    def convert(self):
        url = self.text_box.text()
        self.youtube_manager.download(url)


# ------------------Style

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
