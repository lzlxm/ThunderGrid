





from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

from .Ui_MainForm import Ui_MainForm
from .Tab_EasyExample import Tab_EasyExample
from .Tab_ComplexExample import Tab_ComplexExample




class MainForm(QMainWindow, Ui_MainForm):

    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.setupUi(self)
        self._bindevent()
        self._bindtabs()
        self._center()



    def _center(self):
        screen = QDesktopWidget().screenGeometry()
        progrem_size = self.geometry()
        newLeft = (screen.width() - progrem_size.width()) / 2
        newtop = max((screen.height() - progrem_size.height()) / 2 - 40, 0)
        self.move(newLeft, newtop)




    def _bindevent(self):
        self.pb_Exit.clicked.connect(self.on_click_pb_Exit)



    def _bindtabs(self):
        self._tab_easyexample = Tab_EasyExample(self.tab_EasyExample)
        self._tab_complexexample = Tab_ComplexExample(self.tab_ComplexExample)



    def on_click_pb_Exit(self):
        self.close()



