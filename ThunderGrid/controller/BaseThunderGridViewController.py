

import copy
import functools
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QTableView





from .ThunderGridEditorDelegate import ThunderGridEditorDelegate, Thunder_Grid_Editor_Style










# thunder grid column item data
class ThunderGridColItem:

    def __init__(self):
        self.caption_name = ''
        self.data_property_name = ''
        self.display_style = Thunder_Grid_Editor_Style.none
        self.combobox_items = []
        self.edit_enable = True
        self.col_width = None






# base thnder grid view controller
class BaseThunderGridViewController:


    def __init__(self):
        self.show_debug = True
        self.__model = QStandardItemModel()
        self.__model.itemChanged.connect(functools.partial(self.on_itemchanged))
        self._dataitemlist = None
        self._tableview = None
        self._colitems = []
        self.get_cellstyle_event = None





    #--------------property begin----------------------


    #data model
    @property
    def model(self):
        return self.__model


    #column items
    @property
    def colitems(self):
        return self._colitems

    # --------------property end----------------------






    # --------------private begin----------------------




    # bind tableview
    def _bind_tableview(self):
        if self._tableview is None:
            return

        self._tableview.setItemDelegate(ThunderGridEditorDelegate(self._tableview, self))




    def __get_current_row_col(self):
        sender_comp = self._tableview.sender()
        print(sender_comp)
        current_index = sender_comp.current_index
        return current_index.row(), current_index.column()



    # --------------private end----------------------







    # --------------event begin----------------------


    #
    # just print some info,
    #
    def print_debug(self, index):
        if self.show_debug:
            print("Check {0}:{1} Value: {2}".format(index.row(), index.column(), index.data()))



    def get_cellstyle_by_index(self, index):
        column = index.column()
        org_cellstyle = self.colitems[column]
        if self.get_cellstyle_event is not None:
            return self.get_cellstyle_event(index, copy.copy(org_cellstyle))
        else:
            return org_cellstyle



    #
    # Implements clicked event from the check box
    #
    def checkbox_clicked(self, value):
        # current_index = self._tableview.currentIndex()

        row, col = self.__get_current_row_col()
        if row < 0 or col < 0:
            return

        datamodel = self.__model
        if datamodel is None:
            return


        index = datamodel.index(row, col)

        if self.show_debug:
            self.print_debug(index)

        try:
            datamodel.setData(index, value)
        except Exception as e:
            print(e)

        if self.show_debug:
            self.print_debug(index)





    #
    # Implements currentTextChanged event from the combo box
    #
    def combobox_text_changed(self, text):
        row, col = self.__get_current_row_col()
        if row < 0 or col < 0:
            return

        datamodel = self.__model
        if datamodel is None:
            return

        index = datamodel.index(row, col)

        if self.show_debug:
            self.print_debug(index)
        try:
            datamodel.setData(index, text)
        except Exception as e:
            print(e)

        if self.show_debug:
            self.print_debug(index)




    #
    # Implements currentIndexChanged event from the combo box
    #
    def dropdownlist_index_changed(self, val_ind):
        row, col = self.__get_current_row_col()
        if row < 0 or col < 0:
            return

        datamodel = self.__model
        if datamodel is None:
            return

        index = datamodel.index(row, col)
        cell_style = self.get_cellstyle_by_index(index)

        value = cell_style.combobox_items[val_ind]

        if self.show_debug:
            self.print_debug(index)
        try:
            datamodel.setData(index, value)
        except Exception as e:
            print(e)

        if self.show_debug:
            self.print_debug(index)




    def on_itemchanged(self, qs_item,):
        dataitem = self.get_dataitem_by_row(qs_item.row())
        if dataitem is None:
            return
        propname = self._colitems[qs_item.column()].data_property_name
        if hasattr(dataitem, propname):
            text_val = str(getattr(dataitem, propname))
            if text_val != qs_item.text():
                print('on_itemchanged: new value(' + str(qs_item.text()) + '), old value(' + text_val + ')')
                setattr(dataitem, propname, qs_item.text())
                # if readonly, reset value
                new_text_val = str(getattr(dataitem, propname))
                if new_text_val != qs_item.text():
                    qs_item.setText(new_text_val)



    # --------------event end----------------------











    # --------------public begin----------------------

    def addcolumn(self, colname, colprop, dispstyle, cb_items = [], ed_enable = True, col_width = None):
        colitem = ThunderGridColItem()
        colitem.caption_name = colname
        colitem.data_property_name = colprop
        colitem.display_style = dispstyle
        colitem.combobox_items = cb_items
        colitem.edit_enable = ed_enable
        colitem.col_width = col_width
        self._colitems.append(colitem)
        return colitem




    def set_dataitemlist(self, dataitemlist):
        self._dataitemlist = dataitemlist




    def set_tableview(self, tableview):
        if not isinstance(tableview, QTableView):
            return

        self._tableview = tableview
        self._bind_tableview()

        # set model
        self._tableview.setModel(self.model)




    def get_dataitem_by_row(self, row):
        if self._dataitemlist is None:
            return None
        else:
            if row >= 0 and row < len(self._dataitemlist):
                return self._dataitemlist[row]
            else:
                return None



    def _bind_columns(self):
        # create columns
        caps = [colitem.caption_name for colitem in self._colitems]
        self.__model.setHorizontalHeaderLabels(caps)

        # set column width
        for column, columnitem in enumerate(self._colitems):
            if not columnitem.col_width is None:
                self._tableview.setColumnWidth(column, columnitem.col_width)


    def databind(self):
        self.__model.clear()
        if self._dataitemlist is None:
            return

        if self._tableview is None:
            return

        # bind columns
        self._bind_columns()





    # --------------public end----------------------




