


##
## Grid Editor Delegate in the a QTableView widget
##

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from enum import Enum







class Thunder_Grid_Editor_Style(Enum):
    none = 0
    textbox = 1
    checkbox = 2
    combobox = 3
    dropdownlist = 4




class ThunderGridEditorDelegate(QtWidgets.QItemDelegate):
    def __init__(self, parent, dataview):
        QtWidgets.QItemDelegate.__init__(self, parent)
        self._dataview = dataview






    # --------------private begin----------------------


    # get cell item by index
    def __get_cellitem_by_index(self, index):
        return self._dataview.get_cellstyle_by_index(index)



    # --------------private end----------------------









    # --------------create inplace editor begin----------------------


    # none editor
    def __create_none_editor(self, index):
        self.parent().setIndexWidget(index, None)




    # create checkbox
    def __create_checkbox(self, index):
        checkbox = self.parent().indexWidget(index)

        if checkbox is None:
            widget = QtWidgets.QWidget()
            checkbox = QtWidgets.QCheckBox(self.parent())
            layout = QtWidgets.QHBoxLayout()
            layout.addWidget(checkbox)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setAlignment(QtCore.Qt.AlignCenter)
            widget.setLayout(layout)
            checkbox.current_index = index
            self.parent().setIndexWidget(index, widget)

            if index.data() and index.data().lower() == 'true':
                checkbox.setChecked(True)
            else:
                checkbox.setChecked(False)

            if hasattr(self._dataview, 'checkbox_clicked'):
                checkbox.clicked.connect(self._dataview.checkbox_clicked)





    # create combox(include editable and uneditable
    def __create_combobox(self, index, combobox_items, edit_able):
        combo = self.parent().indexWidget(index)
        if not combo:
            # first time create
            combo = QtWidgets.QComboBox(self.parent())
            combo.setEditable(edit_able)  # 可编辑
            combo.addItems(combobox_items)
            combo.current_index = index
            combo.setCurrentText(index.data())
            self.parent().setIndexWidget(index, combo)
            if hasattr(self._dataview, 'dropdownlist_index_changed'):
                combo.currentIndexChanged.connect(self._dataview.dropdownlist_index_changed)
        else:
            # be created before
            org_items = [combo.itemText(i) for i in range(combo.count())]
            if org_items != combobox_items:
                if hasattr(self._dataview, 'dropdownlist_index_changed'):
                    combo.currentIndexChanged.disconnect(self._dataview.dropdownlist_index_changed)
                combo.clear()
                combo.addItems(combobox_items)
                if hasattr(self._dataview, 'dropdownlist_index_changed'):
                    combo.currentIndexChanged.connect(self._dataview.dropdownlist_index_changed)


    # --------------create inplace editor end----------------------









    # --------------override begin----------------------

    def createEditor(self, parent, option, index):
        cellitem = self.__get_cellitem_by_index(index)
        if not cellitem.edit_enable:
            return None
        elif cellitem.display_style == Thunder_Grid_Editor_Style.none:
            return None
        else:
            return QtWidgets.QItemDelegate.createEditor(self, parent, option, index)






    def paint(self, painter, option, index):
        if self._dataview is None:
            return

        cellitem = self.__get_cellitem_by_index(index)

        combobox_items = cellitem.combobox_items


        if cellitem.display_style == Thunder_Grid_Editor_Style.textbox:
            QtWidgets.QItemDelegate.paint(self, painter, option, index)
        elif cellitem.display_style == Thunder_Grid_Editor_Style.checkbox:
            self.__create_checkbox(index)
        elif cellitem.display_style == Thunder_Grid_Editor_Style.combobox:
            # editable combobox
            self.__create_combobox(index, combobox_items, True)
        elif cellitem.display_style == Thunder_Grid_Editor_Style.dropdownlist:
            # uneditable combobox
            self.__create_combobox(index, combobox_items, False)
        elif cellitem.display_style == Thunder_Grid_Editor_Style.none:
            # none editor
            self.__create_none_editor(index)
        else:
            pass



    # --------------override end----------------------






