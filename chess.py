# This Python file uses the following encoding: utf-8
import sys, datetime, random, os, pickle
#from PySide2.QtWidgets import *
#from PySide2.QtGui import *
#from PySide2.QtCore import Qt, QRect, QPoint, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QOpenGLWidget, QLabel, QPushButton, QLineEdit, QTextEdit, QComboBox, QGroupBox, QMenuBar, QMenu, QDialog, QListWidget, QMessageBox
from PyQt5.QtGui import QPalette, QColor, QBrush, QPen, QFont, QPainter, QImage
from PyQt5.QtCore import Qt, QRect, QPoint, QSize, QRectF, QPointF, QSizeF

tColumn = ("A", "B", "C", "D", "E", "F", "G", "H")
tRow = (1, 2, 3, 4, 5, 6, 7, 8)
tColour = (Qt.white, Qt.black)
tPresent = (True, False)


class Chessman():
    def __init__(self, column, row, colour):
        self.dataColumn = column
        self.dataRow = row
        self.dataColour = colour
        self.dataPresent = True
        self.__name__ = "Chessman"
    def __del__(self):
        self.dataPresent = False
    def getColumn(self):
        return self.dataColumn
    def getRow(self):
        return self.dataRow
    def getColour(self):
        return self.dataColour
    def isPresent(self):
        return self.dataPresent
    def display(self, qp, getCoordX, getCoordY):
        image = QImage("C:\\Users\\Teosoph\\Documents\\Teo\\res_chess\\KnightBlack.bmp")
        if self.dataColour == Qt.white:
            qp.setPen(QPen(Qt.cyan, Qt.SolidPattern))
            qp.setFont(QFont("times", 16))
            #qp.drawText(getCoordX(self.dataColumn), getCoordY(self.dataRow), getCoordX("H") / 8, getCoordY(1) / 8, Qt.AlignCenter, "CM")
            image.invertPixels()
            #qp.drawImage(getCoordX(self.dataColumn), getCoordY(self.dataRow), image.transformed(QTransform.scale(QTransform(), 1, 0.5)))
            qp.drawImage(getCoordX(self.dataColumn), getCoordY(self.dataRow), image.smoothScaled(int(getCoordX("H") / 8), int(getCoordY(1) / 8)))
        elif self.dataColour == Qt.black:
            qp.setPen(QPen(Qt.blue, Qt.SolidPattern))
            qp.setFont(QFont("times", 16))
            #qp.drawText(getCoordX(self.dataColumn), getCoordY(self.dataRow), getCoordX("H") / 8, getCoordY(1) / 8, Qt.AlignCenter, "CM")
            #qp.drawImage(getCoordX(self.dataColumn), getCoordY(self.dataRow), image.transformed(QTransform.scale(QTransform(), 1, 0.5)))
            qp.drawImage(getCoordX(self.dataColumn), getCoordY(self.dataRow), image.smoothScaled(int(getCoordX("H") / 8), int(getCoordY(1) / 8)))
    def isMoveRight(self, column1, row1, column2, row2):
        return True
    def isAttackRight(self, column1, row1, column2, row2):
        return True
    def isJumpRight(self, column, row, find):
        return True
    def errorMessage(self, qp, getCoordX, getCoordY, message):
        oldFont = qp.font()
        oldPen = qp.pen()
        oldBrush = qp.brush()
        qp.setFont(QFont("times", 14))
        qp.setPen(QPen(Qt.red, Qt.SolidPattern))
        qp.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        qp.drawRect(getCoordX("A"), getCoordY(1) + 100, 400, 150)
        qp.drawText(getCoordX("A"), getCoordY(1) + 100, 400, 150, Qt.AlignLeft, message)
        qp.setFont(oldFont)
        qp.setPen(oldPen)
        qp.setBrush(oldBrush)
    #def move(self, qp, column, row, widget):
    #    if self.isMoveRight(self.dataColumn, self.dataRow, column, row):
    #        res = self.moveCounter(qp, self.dataColumn, self.dataRow, column, row)
    #        self.dataColumn = column
    #        self.dataRow = row
    #        self.display(qp, widget.getCoordX, widget.getCoordY)
    #        widget.update()
    #    else:
    #        self.errorMessage(qp, widget.getCoordX, widget.getCoordY, f"This step is incorrectly:\n{self.__name__}: {self.dataColumn}{self.dataRow} - {column}{row}\n")
    #        res = "Error"
    #    return res
    def moveCounter(self, qp, column1, row1, column2, row2):
        return f"{self.__name__}: {column1}{row1} - {column2}{row2}"

class King(Chessman):
    def __init__(self, column, row, colour):
        super().__init__(column, row, colour)
        self.__name__ = "King"
    def display(self, qp, getCoordX, getCoordY):
        image = QImage("C:\\Users\\Teosoph\\Documents\\Teo\\res_chess\\KingBlack.bmp")
        if self.dataColour == Qt.white:
            qp.setPen(QPen(Qt.cyan, Qt.SolidPattern))
            qp.setFont(QFont("times", 16))
            qp.drawText(QRectF(getCoordX(self.dataColumn), getCoordY(self.dataRow), getCoordX("H") / 8, getCoordY(1) / 8), Qt.AlignCenter, self.__name__)
            image.invertPixels()
            qp.drawImage(getCoordX(self.dataColumn), getCoordY(self.dataRow), image.smoothScaled(int(getCoordX("H") / 8), int(getCoordY(1) / 8)))
        elif self.dataColour == Qt.black:
            qp.setPen(QPen(Qt.blue, Qt.SolidPattern))
            qp.setFont(QFont("times", 16))
            qp.drawText(QRectF(getCoordX(self.dataColumn), getCoordY(self.dataRow), getCoordX("H") / 8, getCoordY(1) / 8), Qt.AlignCenter, self.__name__)
            qp.drawImage(getCoordX(self.dataColumn), getCoordY(self.dataRow), image.smoothScaled(int(getCoordX("H") / 8), int(getCoordY(1) / 8)))
    def isMoveRight(self, oldColumn, oldRow, newColumn, newRow):
        if (abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 1 and abs(tRow.index(oldRow) - tRow.index(newRow)) == 0) or (abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 0 and abs(tRow.index(oldRow) - tRow.index(newRow)) == 1) or (abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 1 and abs(tRow.index(oldRow) - tRow.index(newRow)) == 1):
            return True
        else:
            return False


class Queen(Chessman):
    def __init__(self, column, row, colour):
        super().__init__(column, row, colour)
        self.__name__ = "Queen"
    def display(self, qp, getCoordX, getCoordY):
        image = QImage("C:\\Users\\Teosoph\\Documents\\Teo\\res_chess\\QueenBlack.bmp")
        if self.dataColour == Qt.white:
            qp.setPen(QPen(Qt.cyan, Qt.SolidPattern))
            qp.setFont(QFont("times", 16))
            qp.drawText(QRectF(getCoordX(self.dataColumn), getCoordY(self.dataRow), getCoordX("H") / 8, getCoordY(1) / 8), Qt.AlignCenter, self.__name__)
            image.invertPixels()
            qp.drawImage(getCoordX(self.dataColumn), getCoordY(self.dataRow), image.smoothScaled(int(getCoordX("H") / 8), int(getCoordY(1) / 8)))
        elif self.dataColour == Qt.black:
            qp.setPen(QPen(Qt.blue, Qt.SolidPattern))
            qp.setFont(QFont("times", 16))
            qp.drawText(QRectF(getCoordX(self.dataColumn), getCoordY(self.dataRow), getCoordX("H") / 8, getCoordY(1) / 8), Qt.AlignCenter, self.__name__)
            qp.drawImage(getCoordX(self.dataColumn), getCoordY(self.dataRow), image.smoothScaled(int(getCoordX("H") / 8), int(getCoordY(1) / 8)))
    def isMoveRight(self, oldColumn, oldRow, newColumn, newRow):
        #if list(filter(lambda x: x==True, [(abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == i and abs(tRow.index(oldRow) - tRow.index(newRow)) == i)  or (oldColumn == newColumn and oldRow != newRow) or (oldColumn != newColumn and oldRow == newRow) for i in range(1, 8)])):
        #    return True
        #else:
        #    return False
        if ((abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 1 and abs(tRow.index(oldRow) - tRow.index(newRow)) == 1) or (abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 2 and abs(tRow.index(oldRow) - tRow.index(newRow)) == 2) or (abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 3 and abs(tRow.index(oldRow) - tRow.index(newRow)) == 3) or (abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 4 and abs(tRow.index(oldRow) - tRow.index(newRow)) == 4) or (abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 5 and abs(tRow.index(oldRow) - tRow.index(newRow)) == 5) or (abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 6 and abs(tRow.index(oldRow) - tRow.index(newRow)) == 6) or (abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 7 and abs(tRow.index(oldRow) - tRow.index(newRow)) == 7) or (oldColumn == newColumn and oldRow != newRow) or (oldColumn != newColumn and oldRow == newRow)):
            return True
        else:
            return False
    def isJumpRight(self, column, row, find):
        column_index = tColumn.index(column)
        row_index = tRow.index(row)
        if (column == self.dataColumn and row != self.dataRow) or (column != self.dataColumn and row == self.dataRow):
            while abs(column_index - tColumn.index(self.dataColumn)) > 1:
                if column_index < tColumn.index(self.dataColumn):
                    column_index += 1
                else:
                    column_index -= 1
                if find(tColumn[column_index], tRow[row_index]) != None:
                    return False
            while abs(row_index - tRow.index(self.dataRow)) > 1:
                if row_index < tRow.index(self.dataRow):
                    row_index += 1
                else:
                    row_index -= 1
                if find(tColumn[column_index], tRow[row_index]) != None:
                    return False
        elif column != self.dataColumn and row != self.dataRow:
            while (abs(column_index - tColumn.index(self.dataColumn)) > 1) and (abs(row_index - tRow.index(self.dataRow)) > 1):
                if column_index < tColumn.index(self.dataColumn):
                    column_index += 1
                else:
                    column_index -= 1
                if row_index < tRow.index(self.dataRow):
                    row_index += 1
                else:
                    row_index -= 1
                if find(tColumn[column_index], tRow[row_index]) != None:
                    return False
        return True


class Bishop(Chessman):
    def __init__(self, column, row, colour):
        super().__init__(column, row, colour)
        self.__name__ = "Bishop"
    def display(self, qp, getCoordX, getCoordY):
        image = QImage("C:\\Users\\Teosoph\\Documents\\Teo\\res_chess\\BishopBlack.bmp")
        if self.dataColour == Qt.white:
            qp.setPen(QPen(Qt.cyan, Qt.SolidPattern))
            qp.setFont(QFont("times", 16))
            qp.drawText(QRectF(getCoordX(self.dataColumn), getCoordY(self.dataRow), getCoordX("H") / 8, getCoordY(1) / 8), Qt.AlignCenter, self.__name__)
            image.invertPixels()
            qp.drawImage(getCoordX(self.dataColumn), getCoordY(self.dataRow), image.smoothScaled(int(getCoordX("H") / 8), int(getCoordY(1) / 8)))
        elif self.dataColour == Qt.black:
            qp.setPen(QPen(Qt.blue, Qt.SolidPattern))
            qp.setFont(QFont("times", 16))
            qp.drawText(QRectF(getCoordX(self.dataColumn), getCoordY(self.dataRow), getCoordX("H") / 8, getCoordY(1) / 8), Qt.AlignCenter, self.__name__)
            qp.drawImage(getCoordX(self.dataColumn), getCoordY(self.dataRow), image.smoothScaled(int(getCoordX("H") / 8), int(getCoordY(1) / 8)))
    def isMoveRight(self, oldColumn, oldRow, newColumn, newRow):
        #if list(filter(lambda x: x==True, [abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == i and abs(tRow.index(oldRow) - tRow.index(newRow)) == i for i in range(1, 8)])):
        #    return True
        #else:
        #    return False
        if (abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 1 and abs(tRow.index(oldRow) - tRow.index(newRow)) == 1) or (abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 2 and abs(tRow.index(oldRow) - tRow.index(newRow)) == 2) or (abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 3 and abs(tRow.index(oldRow) - tRow.index(newRow)) == 3) or (abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 4 and abs(tRow.index(oldRow) - tRow.index(newRow)) == 4) or (abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 5 and abs(tRow.index(oldRow) - tRow.index(newRow)) == 5) or (abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 6 and abs(tRow.index(oldRow) - tRow.index(newRow)) == 6) or (abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 7 and abs(tRow.index(oldRow) - tRow.index(newRow)) == 7):
            return True
        else:
            return False
    def isJumpRight(self, column, row, find):
        column_index = tColumn.index(column)
        row_index = tRow.index(row)
        while (abs(column_index - tColumn.index(self.dataColumn)) > 1) and (abs(row_index - tRow.index(self.dataRow)) > 1):
            if column_index < tColumn.index(self.dataColumn):
                column_index += 1
            else:
                column_index -= 1
            if row_index < tRow.index(self.dataRow):
                row_index += 1
            else:
                row_index -= 1
            if find(tColumn[column_index], tRow[row_index]) != None:
                return False
        return True


class Castle(Chessman):
    def __init__(self, column, row, colour):
        super().__init__(column, row, colour)
        self.__name__ = "Castle"
    def display(self, qp, getCoordX, getCoordY):
        image = QImage("C:\\Users\\Teosoph\\Documents\\Teo\\res_chess\\CastleBlack.bmp")
        if self.dataColour == Qt.white:
            qp.setPen(QPen(Qt.cyan, Qt.SolidPattern))
            qp.setFont(QFont("times", 16))
            qp.drawText(QRectF(getCoordX(self.dataColumn), getCoordY(self.dataRow), getCoordX("H") / 8, getCoordY(1) / 8), Qt.AlignCenter, self.__name__)
            image.invertPixels()
            qp.drawImage(getCoordX(self.dataColumn), getCoordY(self.dataRow), image.smoothScaled(int(getCoordX("H") / 8), int(getCoordY(1) / 8)))
        elif self.dataColour == Qt.black:
            qp.setPen(QPen(Qt.blue, Qt.SolidPattern))
            qp.setFont(QFont("times", 16))
            qp.drawText(QRectF(getCoordX(self.dataColumn), getCoordY(self.dataRow), getCoordX("H") / 8, getCoordY(1) / 8), Qt.AlignCenter, self.__name__)
            qp.drawImage(getCoordX(self.dataColumn), getCoordY(self.dataRow), image.smoothScaled(int(getCoordX("H") / 8), int(getCoordY(1) / 8)))
    def isMoveRight(self, oldColumn, oldRow, newColumn, newRow):
        if (oldColumn == newColumn and oldRow != newRow) or (oldColumn != newColumn and oldRow == newRow):
            return True
        else:
            return False
    def isJumpRight(self, column, row, find):
        column_index = tColumn.index(column)
        row_index = tRow.index(row)
        while abs(column_index - tColumn.index(self.dataColumn)) > 1:
            if column_index < tColumn.index(self.dataColumn):
                column_index += 1
            else:
                column_index -= 1
            if find(tColumn[column_index], tRow[row_index]) != None:
                return False
        while abs(row_index - tRow.index(self.dataRow)) > 1:
            if row_index < tRow.index(self.dataRow):
                row_index += 1
            else:
                row_index -= 1
            if find(tColumn[column_index], tRow[row_index]) != None:
                return False
        return True


class Knight(Chessman):
    def __init__(self, column, row, colour):
        super().__init__(column, row, colour)
        self.__name__ = "Knight"
    def display(self, qp, getCoordX, getCoordY):
        image = QImage("C:\\Users\\Teosoph\\Documents\\Teo\\res_chess\\KnightBlack.bmp")
        if self.dataColour == Qt.white:
            qp.setPen(QPen(Qt.cyan, Qt.SolidPattern))
            qp.setFont(QFont("times", 16))
            qp.drawText(QRectF(getCoordX(self.dataColumn), getCoordY(self.dataRow), getCoordX("H") / 8, getCoordY(1) / 8), Qt.AlignCenter, self.__name__)
            image.invertPixels()
            qp.drawImage(getCoordX(self.dataColumn), getCoordY(self.dataRow), image.smoothScaled(int(getCoordX("H") / 8), int(getCoordY(1) / 8)))
        elif self.dataColour == Qt.black:
            qp.setPen(QPen(Qt.blue, Qt.SolidPattern))
            qp.setFont(QFont("times", 16))
            qp.drawText(QRectF(getCoordX(self.dataColumn), getCoordY(self.dataRow), getCoordX("H") / 8, getCoordY(1) / 8), Qt.AlignCenter, self.__name__)
            qp.drawImage(getCoordX(self.dataColumn), getCoordY(self.dataRow), image.smoothScaled(int(getCoordX("H") / 8), int(getCoordY(1) / 8)))
    def isMoveRight(self, oldColumn, oldRow, newColumn, newRow):
        if ((abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 1) and (abs(tRow.index(oldRow) - tRow.index(newRow)) == 2)) or ((abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 2) and (abs(tRow.index(oldRow) - tRow.index(newRow)) == 1)):
            return True
        else:
            return False


class Pawn(Chessman):
    def __init__(self, column, row, colour):
        super().__init__(column, row, colour)
        self.__name__ = "Pawn"
    def display(self, qp, getCoordX, getCoordY):
        image = QImage("C:\\Users\\Teosoph\\Documents\\Teo\\res_chess\\PawnBlack.bmp")
        if self.dataColour == Qt.white:
            qp.setPen(QPen(Qt.cyan, Qt.SolidPattern))
            qp.setFont(QFont("times", 16))
            qp.drawText(QRectF(getCoordX(self.dataColumn), getCoordY(self.dataRow), getCoordX("H") / 8, getCoordY(1) / 8), Qt.AlignCenter, self.__name__)
            image.invertPixels()
            qp.drawImage(getCoordX(self.dataColumn), getCoordY(self.dataRow), image.smoothScaled(int(getCoordX("H") / 8), int(getCoordY(1) / 8)))
        elif self.dataColour == Qt.black:
            qp.setPen(QPen(Qt.blue, Qt.SolidPattern))
            qp.setFont(QFont("times", 16))
            qp.drawText(QRectF(getCoordX(self.dataColumn), getCoordY(self.dataRow), getCoordX("H") / 8, getCoordY(1) / 8), Qt.AlignCenter, self.__name__)
            qp.drawImage(getCoordX(self.dataColumn), getCoordY(self.dataRow), image.smoothScaled(int(getCoordX("H") / 8), int(getCoordY(1) / 8)))
    def isMoveRight(self, oldColumn, oldRow, newColumn, newRow):
        if (((abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 0) and (tRow.index(oldRow) - tRow.index(newRow) == -1)) and (self.dataColour == Qt.white)) or (((abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 0) and (tRow.index(oldRow) - tRow.index(newRow) == -2) and (oldRow == 2)) and (self.dataColour == Qt.white)):
            return True
        elif (((abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 0) and (tRow.index(oldRow) - tRow.index(newRow) == 1)) and (self.dataColour == Qt.black)) or (((abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 0) and (tRow.index(oldRow) - tRow.index(newRow) == 2) and (oldRow == 7)) and (self.dataColour == Qt.black)):
            return True
        else:
            return False
    def isAttackRight(self, oldColumn, oldRow, newColumn, newRow):
        if (((abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 1) and (tRow.index(oldRow) - tRow.index(newRow)) == -1) and (self.dataColour == Qt.white)):
            return True
        elif (((abs(tColumn.index(oldColumn) - tColumn.index(newColumn)) == 1) and (tRow.index(oldRow) - tRow.index(newRow)) == 1) and (self.dataColour == Qt.black)):
            return True
        else:
            return False
    def isJumpRight(self, column, row, find):
        column_index = tColumn.index(column)
        row_index = tRow.index(row)
        if abs(row_index - tRow.index(self.dataRow)) == 2:
            if row_index < tRow.index(self.dataRow):
                row_index += 1
            else:
                row_index -= 1
            if find(tColumn[column_index], tRow[row_index]) != None:
                return False
        return True


class Chess(QWidget):
    def __init__(self):
        super().__init__()
        self.release_pos = QPoint()
        self.press_pos = QPoint()
        self.dataChessmans = []
        self.step_white = []
        self.step_black = []
        self.stepsChessmans = []
        self.AI_White = False
        self.AI_Black = False
        self.setWindowTitle("The chess")
        self.setFixedSize(800, 800)
        menubar = QMenuBar(self)
        menubar.setGeometry(0, 0, 800, 25)
        menu1 = QMenu("File", self)
        menu1.addAction("New game", lambda: self.new_game())
        menu1.addSeparator()
        menu1.addAction("Save game", lambda: self.save_game())
        menu1.addAction("Load game", lambda: self.load_game())
        menu1.addSeparator()
        menu1.addAction("Clear desk", lambda: self.clear_desk())
        menu1.addSeparator()
        menu1.addAction("Exit", lambda: self.exit())
        menubar.addMenu(menu1)
        menu2 = QMenu("Choice AI for...", self)
        menu2.addAction("Nothing", lambda: self.ai_nothing())
        menu2.addAction("Steps on the whiteside", lambda: self.ai_white())
        menu2.addAction("Steps on the blackside", lambda: self.ai_black())
        menu2.addAction("Both", lambda: self.ai_both())
        menubar.addMenu(menu2)
        menu3 = QMenu("Step of the blackside", self)
        menu3.addAction("Menu #1")
        menu3.addAction("Menu #2")
        menu3.addAction("Menu #3")
        menubar.addMenu(menu3)
        menu4 = QMenu("Help", self)
        menu4.addAction("About me", lambda: self.help())
        menubar.addMenu(menu4)
        self.label_step_white = QLabel(self)
        self.label_step_white.setGeometry(self.getCoordX("H") + 70, self.getCoordY(1) + 40, 150, 30)
        self.label_step_white.setText("Steps of the white chessmans")
        self.label_step_white.setFont(QFont("times", 14))
        self.output_step_white = QListWidget(self)
        self.output_step_white.setGeometry(self.getCoordX("H") + 70, self.getCoordY(1) + 70, 150, 300)
        self.output_step_white.setFont(QFont("times", 14))
        self.label_step_black = QLabel(self)
        self.label_step_black.setGeometry(self.getCoordX("H") + 70 + 150, self.getCoordY(1) + 40, 150, 30)
        self.label_step_black.setText("Steps of the black chessmans")
        self.label_step_black.setFont(QFont("times", 14))
        self.output_step_black = QListWidget(self)
        self.output_step_black.setGeometry(self.getCoordX("H") + 70 + 150, self.getCoordY(1) + 70, 150, 300)
        self.output_step_black.setFont(QFont("times", 14))

    def new_game(self):
        #white chessmans
        WKg = King("E", 1, Qt.white)
        WQ = Queen("D", 1, Qt.white)
        WB1 = Bishop("C", 1, Qt.white)
        WB2 = Bishop("F", 1, Qt.white)
        WC1 = Castle("A", 1, Qt.white)
        WC2 = Castle("H", 1, Qt.white)
        WK1 = Knight("B", 1, Qt.white)
        WK2 = Knight("G", 1, Qt.white)
        WP1 = Pawn("A", 2, Qt.white)
        WP2 = Pawn("B", 2, Qt.white)
        WP3 = Pawn("C", 2, Qt.white)
        WP4 = Pawn("D", 2, Qt.white)
        WP5 = Pawn("E", 2, Qt.white)
        WP6 = Pawn("F", 2, Qt.white)
        WP7 = Pawn("G", 2, Qt.white)
        WP8 = Pawn("H", 2, Qt.white)
        #black chessmans
        BKg = King("E", 8, Qt.black)
        BQ = Queen("D", 8, Qt.black)
        BB1 = Bishop("C", 8, Qt.black)
        BB2 = Bishop("F", 8, Qt.black)
        BC1 = Castle("A", 8, Qt.black)
        BC2 = Castle("H", 8, Qt.black)
        BK1 = Knight("B", 8, Qt.black)
        BK2 = Knight("G", 8, Qt.black)
        BP1 = Pawn("A", 7, Qt.black)
        BP2 = Pawn("B", 7, Qt.black)
        BP3 = Pawn("C", 7, Qt.black)
        BP4 = Pawn("D", 7, Qt.black)
        BP5 = Pawn("E", 7, Qt.black)
        BP6 = Pawn("F", 7, Qt.black)
        BP7 = Pawn("G", 7, Qt.black)
        BP8 = Pawn("H", 7, Qt.black)
        #CM1 = Chessman("A", 4, Qt.white)
        #CM2 = Chessman("A", 5, Qt.black)
        #CM3 = Chessman("B", 4, Qt.white)
        #CM4 = Chessman("B", 5, Qt.black)
        #CM5 = Chessman("C", 4, Qt.black)
        self.dataChessmans = [WKg, WQ, WB1, WB2, WC1, WC2, WK1, WK2, WP1, WP2, WP3, WP4, WP5, WP6, WP7, WP8, BKg, BQ, BB1, BB2, BC1, BC2, BK1, BK2, BP1, BP2, BP3, BP4, BP5, BP6, BP7, BP8]
        self.step_white, self.step_black = [], []
        self.stepsChessmans = []
        self.output_step_white.clear()
        self.output_step_black.clear()
        self.release_pos = QPoint()
        self.press_pos = QPoint()
        self.update()

    def save_game(self):
        for step in self.step_white:
            step = self.output_step_white.currentItem()
        for step in self.step_black:
            step = self.output_step_black.currentItem()
        with open("chess.bin", "wb") as file1:
            pickle.dump(self.dataChessmans, file1)
        with open("step_white.bin", "wb") as file2:
            pickle.dump(self.step_white, file2)
        with open("step_black.bin", "wb") as file3:
            pickle.dump(self.step_black, file3)
        with open("stepsChessmans.bin", "wb") as file4:
            pickle.dump(self.stepsChessmans, file4)
        self.update()

    def load_game(self):
        with open("chess.bin", "rb") as file1:
            self.dataChessmans = pickle.load(file1)
        with open("step_white.bin", "rb") as file2:
            self.step_white = pickle.load(file2)
        with open("step_black.bin", "rb") as file3:
            self.step_black = pickle.load(file3)
        with open("stepsChessmans.bin", "rb") as file4:
            self.stepsChessmans = pickle.load(file4)
        self.output_step_white.clear()
        self.output_step_black.clear()
        for step in self.step_white:
            self.output_step_white.addItem(step)
        for step in self.step_black:
            self.output_step_black.addItem(step)
        self.release_pos = QPoint()
        self.press_pos = QPoint()
        self.update()

    def clear_desk(self):
        for mychessman in self.dataChessmans:
            mychessman.__del__()
        self.dataChessmans, self.step_white, self.step_black = [], [], []
        self.stepsChessmans = []
        self.output_step_white.clear()
        self.output_step_black.clear()
        self.release_pos = QPoint()
        self.press_pos = QPoint()
        self.update()

    def exit(self):
        self.close()

    def ai_nothing(self):
        self.AI_White = False
        self.AI_Black = False

    def ai_white(self):
        self.AI_White = True
        self.AI_Black = False

    def ai_black(self):
        self.AI_White = False
        self.AI_Black = True

    def ai_both(self):
        self.AI_White = True
        self.AI_Black = True

    def ai_steping(self, qp, chessman):
        mychessman_ai = random.choice(chessman)
        #if mychessman_ai != None and self.stepsChessmans != [] and mychessman_ai.dataColour != self.stepsChessmans[-1].dataColour:
        #    while True:
        #        column_ai = random.choice(tColumn)
        #        row_ai = random.choice(tRow)
        #        result_ai = self.find(column_ai, row_ai)
        #        if (mychessman_ai.__name__ == "Pawn" and result_ai != None and mychessman_ai.isAttackRight(mychessman_ai.dataColumn, mychessman_ai.dataRow, column_ai, row_ai)) or (mychessman_ai.__name__ == "Pawn" and result_ai == None and mychessman_ai.isMoveRight(mychessman_ai.dataColumn, mychessman_ai.dataRow, column_ai, row_ai) and mychessman_ai.isJumpRight(column_ai, row_ai, self.find)) or (mychessman_ai.__name__ != "Pawn" and mychessman_ai.isMoveRight(mychessman_ai.dataColumn, mychessman_ai.dataRow, column_ai, row_ai) and mychessman_ai.isJumpRight(column_ai, row_ai, self.find)):
        #            break
        #        if mychessman_ai.__name__ == "Pawn" and result_ai != None and mychessman_ai.isMoveRight(mychessman_ai.dataColumn, mychessman_ai.dataRow, column_ai, row_ai) and mychessman_ai.isJumpRight(column_ai, row_ai, self.find):
        #            mychessman_ai = random.choice(chessman)
        #    print(f"{mychessman_ai} {mychessman_ai.dataColour}: {column_ai} - {row_ai}")
        #    self.move(qp, mychessman_ai, column_ai, row_ai)
        #elif mychessman_ai != None and self.stepsChessmans == [] and mychessman_ai.dataColour == Qt.white:
        while True:
            column_ai = random.choice(tColumn)
            row_ai = random.choice(tRow)
            result_ai = self.find(column_ai, row_ai)
            if (mychessman_ai.__name__ == "Pawn" and result_ai != None and mychessman_ai.isAttackRight(mychessman_ai.dataColumn, mychessman_ai.dataRow, column_ai, row_ai)) or (mychessman_ai.__name__ == "Pawn" and result_ai == None and mychessman_ai.isMoveRight(mychessman_ai.dataColumn, mychessman_ai.dataRow, column_ai, row_ai) and mychessman_ai.isJumpRight(column_ai, row_ai, self.find)) or (mychessman_ai.__name__ != "Pawn" and mychessman_ai.isMoveRight(mychessman_ai.dataColumn, mychessman_ai.dataRow, column_ai, row_ai) and mychessman_ai.isJumpRight(column_ai, row_ai, self.find)):
                break
            if mychessman_ai.__name__ == "Pawn" and result_ai != None and mychessman_ai.isMoveRight(mychessman_ai.dataColumn, mychessman_ai.dataRow, column_ai, row_ai) and mychessman_ai.isJumpRight(column_ai, row_ai, self.find):
                mychessman_ai = random.choice(chessman)
        print(f"{mychessman_ai} {mychessman_ai.dataColour}: {column_ai} - {row_ai}")
        self.move(qp, mychessman_ai, column_ai, row_ai)

    def help(self):
        box = QMessageBox(self)
        box.setWindowTitle("Hello my dear")
        box.setModal(True)
        box.resize(250, 250)
        box.setText("The program by Teosoph Geliebter!")
        box.exec_()

    def mousePressEvent(self, event):
        self.press_pos = event.pos()

    def mouseReleaseEvent(self, event):
        self.release_pos = event.pos()
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setViewport(self.rect())
        oldFont = qp.font()
        oldBrush = qp.brush()
        qp.setFont(QFont("times", 16))
        qp.drawText(self.getCoordX("A") + 25, self.getCoordY(1) + 50, 450, 25, 0, "A     B     C     D     E     F     G     H")
        qp.drawText(self.getCoordX("A") - 25, self.getCoordY(8), 25, 450, 0, "8\n\n7\n\n6\n\n5\n\n4\n\n3\n\n2\n\n1")
        qp.setFont(oldFont)
        qp.setBrush(oldBrush)
        for i in tColumn:
            for j in tRow:
                self.drawfield(qp, i, j)
        self.drawcounter(qp)
        for mychessman in self.dataChessmans:
            mychessman.display(qp, self.getCoordX, self.getCoordY)
        mychessman_white = [i for i in self.dataChessmans if i.dataColour == Qt.white]
        mychessman_black = [i for i in self.dataChessmans if i.dataColour == Qt.black]
        column_press = self.setCoordX(self.press_pos.x())
        row_press = self.setCoordY(self.press_pos.y())
        column_release = self.setCoordX(self.release_pos.x())
        row_release = self.setCoordY(self.release_pos.y())
        result_press = self.find(column_press, row_press)
        if result_press != None and self.stepsChessmans != [] and result_press.dataColour != self.stepsChessmans[-1].dataColour:
            self.move(qp, result_press, column_release, row_release)
        elif result_press != None and self.stepsChessmans == [] and result_press.dataColour == Qt.white:
            self.move(qp, result_press, column_release, row_release)
        elif result_press == None and self.AI_White and not self.AI_Black:
            self.ai_steping(qp, mychessman_white)
        elif result_press == None and not self.AI_White and self.AI_Black:
            self.ai_steping(qp, mychessman_black)
        elif result_press == None and self.AI_White and self.AI_Black:
            self.ai_steping(qp, mychessman_white)
            self.ai_steping(qp, mychessman_black)
        else:
            Chessman("A", 1, Qt.white).errorMessage(qp, self.getCoordX, self.getCoordY, f"Waiting next step")

    def move(self, qp, result_press, column_release, row_release):
        result_release = self.find(column_release, row_release)
        if result_press != None and result_release == None and result_press.isJumpRight(column_release, row_release, self.find):
            # -------The moving black chessman-------
            if result_press.dataColour == Qt.black:
                if result_press.isMoveRight(result_press.dataColumn, result_press.dataRow, column_release, row_release):
                    self.step_black.append(str(self.output_step_black.count()) + " - " + result_press.moveCounter(qp, result_press.dataColumn, result_press.dataRow, column_release, row_release))
                    self.output_step_black.addItem(str(self.output_step_black.count()) + " - " + result_press.moveCounter(qp, result_press.dataColumn, result_press.dataRow, column_release, row_release))
                    self.stepsChessmans.append(result_press)
                    result_press.dataColumn = column_release
                    result_press.dataRow = row_release
                    result_press.display(qp, self.getCoordX, self.getCoordY)
                    self.update()
                else:
                    result_press.errorMessage(qp, self.getCoordX, self.getCoordY, f"This step is incorrectly:\n{result_press.__name__}: {result_press.dataColumn}{result_press.dataRow} - {column_release}{row_release}\n")
            # -------The moving white chessman-------
            elif result_press.dataColour == Qt.white:
                if result_press.isMoveRight(result_press.dataColumn, result_press.dataRow, column_release, row_release):
                    self.step_white.append(str(self.output_step_white.count()) + " - " + result_press.moveCounter(qp, result_press.dataColumn, result_press.dataRow, column_release, row_release))
                    self.output_step_white.addItem(str(self.output_step_white.count()) + " - " + result_press.moveCounter(qp, result_press.dataColumn, result_press.dataRow, column_release, row_release))
                    self.stepsChessmans.append(result_press)
                    result_press.dataColumn = column_release
                    result_press.dataRow = row_release
                    result_press.display(qp, self.getCoordX, self.getCoordY)
                    self.update()
                else:
                    result_press.errorMessage(qp, self.getCoordX, self.getCoordY, f"This step is incorrectly:\n{result_press.__name__}: {result_press.dataColumn}{result_press.dataRow} - {column_release}{row_release}\n")
        elif result_press != None and result_release != None and result_press.dataColour != result_release.dataColour and result_press.isJumpRight(column_release, row_release, self.find):
            # -------The fighting black chessman-------
            if (result_press.dataColour == Qt.black) and (result_press.__name__ != "Pawn"):
                if result_press.isMoveRight(result_press.dataColumn, result_press.dataRow, column_release, row_release):
                    self.dataChessmans.remove(result_release)
                    result_release.__del__()
                    self.step_black.append(str(self.output_step_black.count()) + " - " + result_press.moveCounter(qp, result_press.dataColumn, result_press.dataRow, column_release, row_release))
                    self.output_step_black.addItem(str(self.output_step_black.count()) + " - " + result_press.moveCounter(qp, result_press.dataColumn, result_press.dataRow, column_release, row_release))
                    self.stepsChessmans.append(result_press)
                    result_press.dataColumn = column_release
                    result_press.dataRow = row_release
                    result_press.display(qp, self.getCoordX, self.getCoordY)
                    self.update()
                else:
                    result_press.errorMessage(qp, self.getCoordX, self.getCoordY, f"This step is incorrectly:\n{result_press.__name__}: {result_press.dataColumn}{result_press.dataRow} - {column_release}{row_release}\n")
            elif (result_press.dataColour == Qt.black) and (result_press.__name__ == "Pawn"):
                if result_press.isAttackRight(result_press.dataColumn, result_press.dataRow, column_release, row_release):
                    self.dataChessmans.remove(result_release)
                    result_release.__del__()
                    self.step_black.append(str(self.output_step_black.count()) + " - " + result_press.moveCounter(qp, result_press.dataColumn, result_press.dataRow, column_release, row_release))
                    self.output_step_black.addItem(str(self.output_step_black.count()) + " - " + result_press.moveCounter(qp, result_press.dataColumn, result_press.dataRow, column_release, row_release))
                    self.stepsChessmans.append(result_press)
                    result_press.dataColumn = column_release
                    result_press.dataRow = row_release
                    result_press.display(qp, self.getCoordX, self.getCoordY)
                    self.update()
                else:
                    result_press.errorMessage(qp, self.getCoordX, self.getCoordY, f"This step is incorrectly:\n{result_press.__name__}: {result_press.dataColumn}{result_press.dataRow} - {column_release}{row_release}\n")
            # -------The fighting white chessman-------
            elif (result_press.dataColour == Qt.white) and (result_press.__name__ != "Pawn"):
                if result_press.isMoveRight(result_press.dataColumn, result_press.dataRow, column_release, row_release):
                    self.dataChessmans.remove(result_release)
                    result_release.__del__()
                    self.step_white.append(str(self.output_step_white.count()) + " - " + result_press.moveCounter(qp, result_press.dataColumn, result_press.dataRow, column_release, row_release))
                    self.output_step_white.addItem(str(self.output_step_white.count()) + " - " + result_press.moveCounter(qp, result_press.dataColumn, result_press.dataRow, column_release, row_release))
                    self.stepsChessmans.append(result_press)
                    result_press.dataColumn = column_release
                    result_press.dataRow = row_release
                    result_press.display(qp, self.getCoordX, self.getCoordY)
                    self.update()
                else:
                    result_press.errorMessage(qp, self.getCoordX, self.getCoordY, f"This step is incorrectly:\n{result_press.__name__}: {result_press.dataColumn}{result_press.dataRow} - {column_release}{row_release}\n")
            elif (result_press.dataColour == Qt.white) and (result_press.__name__ == "Pawn"):
                if result_press.isAttackRight(result_press.dataColumn, result_press.dataRow, column_release, row_release):
                    self.dataChessmans.remove(result_release)
                    result_release.__del__()
                    self.step_white.append(str(self.output_step_white.count()) + " - " + result_press.moveCounter(qp, result_press.dataColumn, result_press.dataRow, column_release, row_release))
                    self.output_step_white.addItem(str(self.output_step_white.count()) + " - " + result_press.moveCounter(qp, result_press.dataColumn, result_press.dataRow, column_release, row_release))
                    self.stepsChessmans.append(result_press)
                    result_press.dataColumn = column_release
                    result_press.dataRow = row_release
                    result_press.display(qp, self.getCoordX, self.getCoordY)
                    self.update()
                else:
                    result_press.errorMessage(qp, self.getCoordX, self.getCoordY, f"This step is incorrectly:\n{result_press.__name__}: {result_press.dataColumn}{result_press.dataRow} - {column_release}{row_release}\n")
        elif result_press != None and not(result_press.isJumpRight(column_release, row_release, self.find)):
            result_press.errorMessage(qp, self.getCoordX, self.getCoordY, f"This step is incorrectly:\n{result_press.__name__}: {result_press.dataColumn}{result_press.dataRow} - {column_release}{row_release}\nThis chessman can't jumping over other chessmans\n")
        if result_press.__name__ == "Pawn" and result_press.dataColour == Qt.white and result_press.dataRow == 8:
            new_result_press = random.choice([Queen(result_press.dataColumn, result_press.dataRow, result_press.dataColour), Bishop(result_press.dataColumn, result_press.dataRow, result_press.dataColour), Castle(result_press.dataColumn, result_press.dataRow, result_press.dataColour), Knight(result_press.dataColumn, result_press.dataRow, result_press.dataColour)])
            self.dataChessmans.remove(result_press)
            result_press.__del__()
            self.dataChessmans.append(new_result_press)
            new_result_press.display(qp, self.getCoordX, self.getCoordY)
            self.update()
        if result_press.__name__ == "Pawn" and result_press.dataColour == Qt.black and result_press.dataRow == 1:
            new_result_press = random.choice([Queen(result_press.dataColumn, result_press.dataRow, result_press.dataColour), Bishop(result_press.dataColumn, result_press.dataRow, result_press.dataColour), Castle(result_press.dataColumn, result_press.dataRow, result_press.dataColour), Knight(result_press.dataColumn, result_press.dataRow, result_press.dataColour)])
            self.dataChessmans.remove(result_press)
            result_press.__del__()
            self.dataChessmans.append(new_result_press)
            new_result_press.display(qp, self.getCoordX, self.getCoordY)
            self.update()

    def drawfield(self, qp, column, row):
        oldPen = qp.pen()
        oldBrush = qp.brush()
        qp.setPen(QPen(Qt.yellow, 2, Qt.SolidLine))
        qp.setBrush(QBrush(self.getColour(column, row), Qt.SolidPattern))
        qp.drawRect(self.getCoordX(column), self.getCoordY(row), 50, 50)
        qp.setPen(oldPen)
        qp.setBrush(oldBrush)

    def drawcounter(self, qp):
        oldFont = qp.font()
        oldPen = qp.pen()
        oldBrush = qp.brush()
        qp.setFont(QFont("times", 14))
        qp.setPen(QPen(Qt.black, Qt.SolidPattern))
        qp.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        step_white_str = ""
        step_black_str = ""
        for temp in self.step_white:
            step_white_str += temp + "\n"
        for temp in self.step_black:
            step_black_str += temp + "\n"
        qp.drawRect(self.getCoordX("H") + 70, self.getCoordY(8), 300, 400)
        qp.drawText(self.getCoordX("H") + 70, self.getCoordY(8), 300, 400, Qt.AlignLeft, step_white_str)
        qp.drawText(self.getCoordX("H") + 70, self.getCoordY(8), 300, 400, Qt.AlignRight, step_black_str)
        qp.setFont(oldFont)
        qp.setPen(oldPen)
        qp.setBrush(oldBrush)

    def getCoordX(self, column):
        if column == tColumn[0]:
            return 45
        elif column == tColumn[1]:
            return 95
        elif column == tColumn[2]:
            return 145
        elif column == tColumn[3]:
            return 195
        elif column == tColumn[4]:
            return 245
        elif column == tColumn[5]:
            return 295
        elif column == tColumn[6]:
            return 345
        elif column == tColumn[7]:
            return 395

    def getCoordY(self, row):
        if row == tRow[-1]:
            return 45
        elif row == tRow[-2]:
            return 95
        elif row == tRow[-3]:
            return 145
        elif row == tRow[-4]:
            return 195
        elif row == tRow[-5]:
            return 245
        elif row == tRow[-6]:
            return 295
        elif row == tRow[-7]:
            return 345
        elif row == tRow[-8]:
            return 395

    def getColour(self, column, row):
        cl_1 = [i for i in tColumn if tColumn.index(i) % 2 == 0]
        rw_1 = [i for i in tRow if tRow.index(i) % 2 == 1]
        cl_2 = [i for i in tColumn if tColumn.index(i) % 2 == 1]
        rw_2 = [i for i in tRow if tRow.index(i) % 2 == 0]
        if (column in cl_1 and row in rw_1) or (column in cl_2 and row in rw_2):
            return Qt.white
        else:
            return Qt.black

    def setCoordX(self, X):
        if X > 45 and X < 95:
            return tColumn[0]
        elif X > 95 and X < 145:
            return tColumn[1]
        elif X > 145 and X < 195:
            return tColumn[2]
        elif X > 195 and X < 245:
            return tColumn[3]
        elif X > 245 and X < 295:
            return tColumn[4]
        elif X > 295 and X < 345:
            return tColumn[5]
        elif X > 345 and X < 395:
            return tColumn[6]
        elif X > 395 and X < 445:
            return tColumn[7]

    def setCoordY(self, Y):
        if Y > 45 and Y < 95:
            return tRow[-1]
        elif Y > 95 and Y < 145:
            return tRow[-2]
        elif Y > 145 and Y < 195:
            return tRow[-3]
        elif Y > 195 and Y < 245:
            return tRow[-4]
        elif Y > 245 and Y < 295:
            return tRow[-5]
        elif Y > 295 and Y < 345:
            return tRow[-6]
        elif Y > 345 and Y < 395:
            return tRow[-7]
        elif Y > 395 and Y < 445:
            return tRow[-8]

    def find(self, column, row):
        for mychessman in self.dataChessmans:
            if mychessman.dataColumn == column and mychessman.dataRow == row:
                return mychessman


def main():
    app = QApplication([])
    window = Chess()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
