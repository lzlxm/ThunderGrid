import sys

from PyQt5.QtWidgets import QApplication




from Forms.MainForm import MainForm




if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWin = MainForm()
    mainWin.show()
    sys.exit(app.exec_())



