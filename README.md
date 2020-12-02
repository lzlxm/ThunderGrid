# ThunderGrid
a python datagrid based on pyqt5


install pyqt5 first


# Easy Example

1.import library
from ThunderGrid.controller import *

2.init dataitemlist
it's a list, such as  self._dataitemlist = []
item's property corresponding the columns

3.init thundergridcontroller
  //step 1: create controller and add column
  gvc_ThunderGrid = ThunderGridViewController()

  //step 2: add columns
  gvc_ThunderGrid.addcolumn('orderid', 'orderid', Thunder_Grid_Editor_Style.textbox, col_width = 120)
  gvc_ThunderGrid.addcolumn('goods', 'goods', Thunder_Grid_Editor_Style.combobox,
                               ['', 'goods1', 'goods2', 'goods3'], col_width = 120)
  gvc_ThunderGrid.addcolumn('destination', 'destination', Thunder_Grid_Editor_Style.dropdownlist,
                               ['U.S.A', 'Britain', 'France'], col_width = 120)
  gvc_ThunderGrid.addcolumn('delivered', 'delivered', Thunder_Grid_Editor_Style.checkbox, col_width = 50)


  //step 3: set tableview
  gvc_ThunderGrid.set_tableview(self.tv_ThunderGrid)
  
  //step 4: set dataitemlist
  gvc_ThunderGrid.set_dataitemlist(self._dataitemlist)

  //thundergrid controller databind
  gvc_ThunderGrid.databind()
  
 
 it begin work.




# Complex Example

it can handle complex grid inplace editor.append next 2 step based on Easy Example

  //step 5: bind get cellstyle event, handle ccomplex grid inplace editor
  gvc_ThunderGrid.get_cellstyle_event = self.get_gvc_ThunderGrid_cellstyle



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



