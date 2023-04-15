import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from subprocess import Popen, PIPE
from PyQt5.QtCore import QObject, pyqtSignal

class App(QWidget):

    def __init__(self):
        super().__init__()

        
        self.setWindowTitle('App Output')
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('icon.png'))

        
        label = QLabel(self)
        pixmap = QPixmap('image.png')
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)

        
        self.output = QTextEdit(self)
        self.output.setReadOnly(True)
        font = QFont('Arial', 12)
        self.output.setFont(font)

        
        self.button = QPushButton('Run App', self)
        self.button.clicked.connect(self.run_app_threaded)
        self.button.setStyleSheet('background-color: #4CAF50; color: white; font-size: 18px; padding: 10px 20px; border: none; border-radius: 5px;')

        
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.output)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def run_app_threaded(self):
        
        self.thread = QThread()
        self.worker = AppWorker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run_app)
        self.worker.finished.connect(self.thread.quit)
        self.worker.output_updated.connect(self.update_output)
        self.thread.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

    def update_output(self, line):
        self.output.insertPlainText(line)

class AppWorker(QObject):

    finished = pyqtSignal()
    output_updated = pyqtSignal(str)

    def run_app(self):
        # Start the 'app.py' file in the background
        proc = Popen(['python', 'app.py'], stdout=PIPE, stderr=PIPE)

        
        while proc.poll() is None:
            line = proc.stdout.readline().decode('utf-8')
            self.output_updated.emit(line)

        self.finished.emit()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
