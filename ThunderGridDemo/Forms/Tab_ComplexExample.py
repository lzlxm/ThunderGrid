
from PyQt5.QtWidgets import QFrame


# from ThunderGrid.controller.ThunderGridViewController import ThunderGridViewController
# from ThunderGrid.controller.ThunderGridEditorDelegate import Thunder_Grid_Editor_Style

from ThunderGrid.controller import *

from OrderItem import OrderItem


from .Ui_EasyExample import Ui_EasyExample



class Tab_ComplexExample(QFrame, Ui_EasyExample):


    def __init__(self, parent=None):
        super(Tab_ComplexExample, self).__init__(parent)
        self.setupUi(self)
        self._bindevent()

        #step 1: init dataitemlist
        self.init_datamitemlist()
        #step 2: init thundergrid controller
        self.init_thundergridcontroller()



    def _bindevent(self):
        pass





    # step 1: init dataitemlist
    def init_datamitemlist(self):
        self._dataitemlist = []
        for i in range(1, 11):
            item = OrderItem()
            item.orderid = 'od' + str(i).rjust(6, '0')
            item.goods = ''
            self._dataitemlist.append(item)


    # step 2: init thundergrid controller
    def init_thundergridcontroller(self):
        # step 1: create controller and add column
        gvc_ThunderGrid = ThunderGridViewController()

        # step 2: add columns
        gvc_ThunderGrid.addcolumn('orderid', 'orderid', Thunder_Grid_Editor_Style.textbox, col_width = 120)
        gvc_ThunderGrid.addcolumn('goods', 'goods', Thunder_Grid_Editor_Style.combobox,
                               ['', 'goods1', 'goods2', 'goods3'], col_width = 120)
        gvc_ThunderGrid.addcolumn('destination', 'destination', Thunder_Grid_Editor_Style.dropdownlist,
                               ['U.S.A', 'Britain', 'France'], col_width = 120)
        gvc_ThunderGrid.addcolumn('delivered', 'delivered', Thunder_Grid_Editor_Style.checkbox, col_width = 50)


        # step 3: set tableview
        gvc_ThunderGrid.set_tableview(self.tv_ThunderGrid)

        # step 4: set dataitemlist
        gvc_ThunderGrid.set_dataitemlist(self._dataitemlist)

        # step 5: bind get cellstyle event, handle ccomplex grid inplace editor
        gvc_ThunderGrid.get_cellstyle_event = self.get_gvc_ThunderGrid_cellstyle

        # thundergrid controller databind
        gvc_ThunderGrid.databind()
        self._gvc_ThunderGrid = gvc_ThunderGrid




    def get_gvc_ThunderGrid_cellstyle(self, index, org_cellstyle):
        new_cellstyle = org_cellstyle

        row = index.row()
        col = index.column()

        # special inplace editor
        if row == 1 and col == 2:
            new_cellstyle.display_style = Thunder_Grid_Editor_Style.none

        if row == 2 and col == 1:
            new_cellstyle.display_style = Thunder_Grid_Editor_Style.textbox

        if row == 3 and col == 2:
            new_cellstyle.display_style = Thunder_Grid_Editor_Style.checkbox

        return new_cellstyle


