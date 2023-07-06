# This Python file uses the following encoding: utf-8
import sys, datetime, random, os, pickle
#from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QLineEdit, QTextEdit, QComboBox, QGroupBox, QMenuBar, QMenu, QDialog, QListWidget, QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QOpenGLWidget, QLabel, QPushButton, QLineEdit, QTextEdit, QComboBox, QGroupBox, QMenuBar, QMenu, QDialog, QListWidget, QMessageBox
from PyQt5.QtGui import QPalette, QColor, QBrush, QPen, QFont, QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtOpenGL import QGLWidget
#from PySide6.QtGui import QPalette, QColor, QBrush, QPen, QFont, QPainter, QOpenGLFunctions
#from PySide6.QtCore import Qt
#from PySide6.QtOpenGL import QGLWidget
from chess import Chess

class GLWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moj Draw")
        self.setGeometry(450, 200, 450, 450)

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setViewport(self.rect())
        qp.drawRect(0, 0, 200, 200)
        qp.setBrush(QBrush(Qt.blue, Qt.VerPattern))
        qp.setPen(QPen(Qt.yellow, 5, Qt.SolidLine))
        qp.drawEllipse(25, 25, 250, 250)
        qp.drawEllipse(25, 25, 250, 25)
        qp.drawEllipse(25, 25, 25, 250)
        print(self.rect())

    def initializeGL(self):
        pass

    def resizeGL(self, w, h):
        #viewport = self.rect()
        #w = viewport.width()
        #h = viewport.height()
        #QOpenGLFunctions.glViewport(0, 0, w, h)
        #QOpenGLFunctions.glMatrixMode(QOpenGLFunctions.GL_PROJECTION)
        #QOpenGLFunctions.glLoadIdentity()
        #QOpenGLFunctions.glMatrixMode(QOpenGLFunctions.GL_MODELVIEW)
        #QOpenGLFunctions.glLoadIdentity()
        pass

    def paintGL(self):
        #QOpenGLFunctions.glClear(QOpenGLFunctions.GL_COLOR_BUFFER_BIT|QOpenGLFunctions.GL_DEPTH_BUFFER_BIT)
        #QOpenGLFunctions.glColor3f(1.0, 0.0, 0.0)
        #QOpenGLFunctions.glBegin(QOpenGLFunctions.GL_QUADS)
        #QOpenGLFunctions.glVertex3f(-0.5, -0.5)
        #QOpenGLFunctions.glVertex3f(0.5, -0.5)
        #QOpenGLFunctions.glVertex3f(-0.5, 0.5)
        #QOpenGLFunctions.glVertex3f(0.5, 0.5)
        #QOpenGLFunctions.glEnd()
        #QOpenGLFunctions.glFlush()
        pass


class MainWindow(QMainWindow):
    def __init__(self, folder):
        super().__init__()
        self.package = list()
        files = self.parser(folder)
        keys = list(files.keys())
        self.menu(self, keys, files)

        QLabel("What is Your name?", self).setGeometry(50, 50, 100, 25)
        self.name = QLineEdit("lorem ipsum", self)
        self.name.setGeometry(150, 50, 100, 25)

        self.button = QPushButton("Let's welcome", self)
        self.button.setGeometry(50, 100, 100, 25)
        self.button.clicked.connect(lambda: self.func(self.name.text()))

        self.output = QTextEdit(self)
        self.output.setGeometry(150, 100, 300, 25)

        R = random.Random()
        QLabel(f"Кидок кубика - {random.Random.randint(R, 1, 20)}", self).setGeometry(50, 150, 300, 25)
        print(f"Кидок кубика - {random.Random.randint(R, 1, 20)}")

        D = datetime.datetime.date(datetime.datetime.today()).weekday() + 1
        QLabel(f"Поточний день тижня - {D}", self).setGeometry(50, 200, 300, 25)
        print("Поточний день тижня - ", D)

        QGroupBox(f"Parsing of the folder {folder}", self).setGeometry(10, 220, 400, 650)
        for i in range(len(keys)):
            QLabel(keys[i], self).setGeometry(50, 250+20*i, 300, 25)
            type_files_1 = QComboBox(self)
            type_files_1.setGeometry(100, 250+20*i, 300, 25)
            type_files_1.addItems(files[keys[i]])

    def func(self, text):
        print(f"Hello dear, {text} !!!")
        self.output.setText(f"Hello dear, {text} !!!")

    def parser(self, folder):
        cortImage = (".jpeg", ".png", ".jpg", ".svg")
        cortVideo = (".avi", ".mp4", ".mov", ".mpg")
        cortText = (".doc", ".ini", ".txt", ".odt")
        cortMusic = (".mp3", ".ogg", ".wav", ".amr")
        cortVarious = (".bak", ".dmp", ".log", ".tga")
        result = {"folder": [], "other": []}
        result.update({j: [] for j in cortImage})
        result.update({j: [] for j in cortVideo})
        result.update({j: [] for j in cortText})
        result.update({j: [] for j in cortMusic})
        result.update({j: [] for j in cortVarious})

        for path, folder, file in os.walk(folder):
            for i in range(len(folder)):
                result["folder"] += (lambda temp: (temp.append(f"{path}\\{folder[i]}") == None and temp))([])
            for i in range(len(file)):
                for key in list(result.keys()):
                    if key in file[i]:
                        result[key] += (lambda temp: (temp.append(f"{path}\\{file[i]}") == None and temp))([])
                if not set(result.keys()).isdisjoint(set(file[i].split("."))):
                    result["other"] += (lambda temp: (temp.append(f"{path}\\{file[i]}") == None and temp))([])
        return result

    def menu(self, oldwindow, keys, files):
        menubar = QMenuBar(oldwindow)
        menubar.setGeometry(0, 0, 500, 25)
        menu1 = QMenu("Window #1", self)
        menu1.addAction("Action #1")
        menu1.addAction("Action #2")
        menu1.addSeparator()
        menu1.addAction("Save package", lambda: self.save_package(self))
        menu1.addAction("Load package", lambda: self.load_package(self))
        menubar.addMenu(menu1)
        menu2 = QMenu("Window #2", self)
        menu2.addAction("Action #1")
        menu2.addAction("Action #2")
        menu2.addSeparator()
        menu2.addAction("Action #3")
        menubar.addMenu(menu2)
        menu3 = QMenu("Painting", self)
        menu3.addAction("QOpenGLWidget", lambda: self.f_paint())
        menu3.addAction("QChessWidget", lambda: self.f_chess())
        menubar.addMenu(menu3)
        menu4 = QMenu("Parsing folder", self)
        menu4.addAction(keys[0], lambda: self.f1(oldwindow, keys, files))
        menu4.addAction(keys[1], lambda: self.f2(oldwindow, keys, files))
        menu4.addAction(keys[2], lambda: self.f3(oldwindow, keys, files))
        menu4.addAction(keys[3], lambda: self.f4(oldwindow, keys, files))
        menu4.addAction(keys[4], lambda: self.f5(oldwindow, keys, files))
        menu4.addAction(keys[5], lambda: self.f6(oldwindow, keys, files))
        menu4.addAction(keys[6], lambda: self.f7(oldwindow, keys, files))
        menu4.addAction(keys[7], lambda: self.f8(oldwindow, keys, files))
        menu4.addAction(keys[8], lambda: self.f9(oldwindow, keys, files))
        menubar.addMenu(menu4)
        menu5 = QMenu("Help", self)
        menu5.addAction("About me", lambda: self.f_about(oldwindow))
        menubar.addMenu(menu5)

    def save_package(self, oldwindow):
        with open("Woohoo_Moodlets.package", "wb") as file1:
            pickle.dump(self.package, file1)
        dialog = QMessageBox(oldwindow)
        dialog.setWindowTitle("The inbox of the package been saved")
        dialog.resize(250, 250)
        dialog.setModal(True)
        dialog.setText("The inbox of the package been saved")
        dialog.exec_()

    def load_package(self, oldwindow):
        with open("Woohoo_Moodlets.package", "rb") as file1:
            self.package = pickle.load(file1)
        print("The inbox of the package")
        print(self.package)
        dialog = QDialog(oldwindow)
        dialog.setWindowTitle("The inbox of the package")
        dialog.resize(500, 500)
        dialog.setModal(True)
        label = QLabel("The inbox of the package", dialog)
        #label.setGeometry(200, 0, 100, 50)
        #label.setFont(QFont("Times", 20))
        #listwidget = QListWidget(dialog)
        #listwidget.setGeometry(50, 50, 400, 400)
        #listwidget.addItems(self.package)
        dialog.exec_()

    def f_paint(self):
        global paint_window
        paint_window = GLWidget()
        paint_window.show()

    def f_chess(self):
        global chess_window
        chess_window = Chess()
        chess_window.show()

    def f1(self, oldwindow, keys, files):
        print("The list of the folders by primery folder")
        dialog = QDialog(oldwindow)
        dialog.setWindowTitle("Moj Dialog")
        dialog.resize(500, 500)
        dialog.setModal(True)
        label = QLabel(keys[0], dialog)
        label.setGeometry(200, 0, 100, 50)
        label.setFont(QFont("Times", 20))
        listwidget = QListWidget(dialog)
        listwidget.setGeometry(50, 50, 400, 400)
        listwidget.addItems(files[keys[0]])
        dialog.exec_()

    def f2(self, oldwindow, keys, files):
        print(f"The list of the files ({keys[1]}) by primery folder")
        dialog = QDialog(oldwindow)
        dialog.setWindowTitle("Moj Dialog")
        dialog.resize(500, 500)
        dialog.setModal(True)
        label = QLabel(keys[1], dialog)
        label.setGeometry(200, 0, 100, 50)
        label.setFont(QFont("Times", 20))
        listwidget = QListWidget(dialog)
        listwidget.setGeometry(50, 50, 400, 400)
        listwidget.addItems(files[keys[1]])
        dialog.exec_()

    def f3(self, oldwindow, keys, files):
        print(f"The list of the files ({keys[2]}) by primery folder")
        dialog = QDialog(oldwindow)
        dialog.setWindowTitle("Moj Dialog")
        dialog.resize(500, 500)
        dialog.setModal(True)
        label = QLabel(keys[2], dialog)
        label.setGeometry(200, 0, 100, 50)
        label.setFont(QFont("Times", 20))
        listwidget = QListWidget(dialog)
        listwidget.setGeometry(50, 50, 400, 400)
        listwidget.addItems(files[keys[2]])
        dialog.exec_()

    def f4(self, oldwindow, keys, files):
        print(f"The list of the files ({keys[3]}) by primery folder")
        dialog = QDialog(oldwindow)
        dialog.setWindowTitle("Moj Dialog")
        dialog.resize(500, 500)
        dialog.setModal(True)
        label = QLabel(keys[3], dialog)
        label.setGeometry(200, 0, 100, 50)
        label.setFont(QFont("Times", 20))
        listwidget = QListWidget(dialog)
        listwidget.setGeometry(50, 50, 400, 400)
        listwidget.addItems(files[keys[3]])
        dialog.exec_()

    def f5(self, oldwindow, keys, files):
        print(f"The list of the files ({keys[4]}) by primery folder")
        dialog = QDialog(oldwindow)
        dialog.setWindowTitle("Moj Dialog")
        dialog.resize(500, 500)
        dialog.setModal(True)
        label = QLabel(keys[4], dialog)
        label.setGeometry(200, 0, 100, 50)
        label.setFont(QFont("Times", 20))
        listwidget = QListWidget(dialog)
        listwidget.setGeometry(50, 50, 400, 400)
        listwidget.addItems(files[keys[4]])
        dialog.exec_()

    def f6(self, oldwindow, keys, files):
        print(f"The list of the files ({keys[5]}) by primery folder")
        dialog = QDialog(oldwindow)
        dialog.setWindowTitle("Moj Dialog")
        dialog.resize(500, 500)
        dialog.setModal(True)
        label = QLabel(keys[5], dialog)
        label.setGeometry(200, 0, 100, 50)
        label.setFont(QFont("Times", 20))
        listwidget = QListWidget(dialog)
        listwidget.setGeometry(50, 50, 400, 400)
        listwidget.addItems(files[keys[5]])
        dialog.exec_()

    def f7(self, oldwindow, keys, files):
        print(f"The list of the files ({keys[6]}) by primery folder")
        dialog = QDialog(oldwindow)
        dialog.setWindowTitle("Moj Dialog")
        dialog.resize(500, 500)
        dialog.setModal(True)
        label = QLabel(keys[6], dialog)
        label.setGeometry(200, 0, 100, 50)
        label.setFont(QFont("Times", 20))
        listwidget = QListWidget(dialog)
        listwidget.setGeometry(50, 50, 400, 400)
        listwidget.addItems(files[keys[6]])
        dialog.exec_()

    def f8(self, oldwindow, keys, files):
        print(f"The list of the files ({keys[7]}) by primery folder")
        dialog = QDialog(oldwindow)
        dialog.setWindowTitle("Moj Dialog")
        dialog.resize(500, 500)
        dialog.setModal(True)
        label = QLabel(keys[7], dialog)
        label.setGeometry(200, 0, 100, 50)
        label.setFont(QFont("Times", 20))
        listwidget = QListWidget(dialog)
        listwidget.setGeometry(50, 50, 400, 400)
        listwidget.addItems(files[keys[7]])
        dialog.exec_()

    def f9(self, oldwindow, keys, files):
        print(f"The list of the files ({keys[8]}) by primery folder")
        dialog = QDialog(oldwindow)
        dialog.setWindowTitle("Moj Dialog")
        dialog.resize(500, 500)
        dialog.setModal(True)
        label = QLabel(keys[8], dialog)
        label.setGeometry(200, 0, 100, 50)
        label.setFont(QFont("Times", 20))
        listwidget = QListWidget(dialog)
        listwidget.setGeometry(50, 50, 400, 400)
        listwidget.addItems(files[keys[8]])
        dialog.exec_()

    def f_about(self, oldwindow):
        dialog = QMessageBox(oldwindow)
        dialog.setWindowTitle("About me")
        dialog.resize(250, 250)
        dialog.setModal(True)
        dialog.setText("The program by Teosoph Geliebter")
        dialog.exec_()


if __name__ == "__main__":
    folder = "C:\\Users\\Teosoph\\Documents\\My Games"
    app = QApplication([])
    window = MainWindow(folder)
    window.setWindowTitle("Moja Applikacja")
    window.setFixedSize(1000, 1000)
    window.show()
    sys.exit(app.exec_())
