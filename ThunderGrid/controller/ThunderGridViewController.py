


from PyQt5 import QtCore
from PyQt5.QtGui import QStandardItem



from .BaseThunderGridViewController import BaseThunderGridViewController











# thundergrid view controller
class ThunderGridViewController(BaseThunderGridViewController):


    def __init__(self):
        BaseThunderGridViewController.__init__(self)





    # --------------public begin----------------------



    def databind(self):
        datamodel = self.model
        datamodel.clear()
        if self._dataitemlist is None:
            return

        if self._tableview is None:
            return

        # bind columns
        self._bind_columns()

        # set model data
        for row, dataitem in enumerate(self._dataitemlist):
            for column, columnitem in enumerate(self._colitems):
                if hasattr(dataitem, columnitem.data_property_name):
                    text_item = str(getattr(dataitem, columnitem.data_property_name))
                else:
                    text_item = ''
                qs_item = QStandardItem(text_item)
                # set text alignment center
                qs_item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                # set index item
                datamodel.setItem(row, column, qs_item)




    # --------------public end----------------------




