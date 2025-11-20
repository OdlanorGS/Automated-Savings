### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.worksheet.html "openpyxl.worksheet.worksheet module") |
  * [previous](openpyxl.worksheet.table.html "openpyxl.worksheet.table module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.views module]()



# openpyxl.worksheet.views module

_class _openpyxl.worksheet.views.Pane(_xSplit =None_, _ySplit =None_, _topLeftCell =None_, _activePane ='topLeft'_, _state ='split'_)[[source]](../_modules/openpyxl/worksheet/views.html#Pane)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

activePane
    

Value must be one of {‘bottomLeft’, ‘bottomRight’, ‘topLeft’, ‘topRight’}

state
    

Value must be one of {‘split’, ‘frozen’, ‘frozenSplit’}

topLeftCell
    

Values must be of type <class ‘str’>

xSplit
    

Values must be of type <class ‘float’>

ySplit
    

Values must be of type <class ‘float’>

_class _openpyxl.worksheet.views.Selection(_pane =None_, _activeCell ='A1'_, _activeCellId =None_, _sqref ='A1'_)[[source]](../_modules/openpyxl/worksheet/views.html#Selection)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

activeCell
    

Values must be of type <class ‘str’>

activeCellId
    

Values must be of type <class ‘int’>

pane
    

Value must be one of {‘bottomLeft’, ‘bottomRight’, ‘topLeft’, ‘topRight’}

sqref
    

Values must be of type <class ‘str’>

_class _openpyxl.worksheet.views.SheetView(_windowProtection =None_, _showFormulas =None_, _showGridLines =None_, _showRowColHeaders =None_, _showZeros =None_, _rightToLeft =None_, _tabSelected =None_, _showRuler =None_, _showOutlineSymbols =None_, _defaultGridColor =None_, _showWhiteSpace =None_, _view =None_, _topLeftCell =None_, _colorId =None_, _zoomScale =None_, _zoomScaleNormal =None_, _zoomScaleSheetLayoutView =None_, _zoomScalePageLayoutView =None_, _zoomToFit =None_, _workbookViewId =0_, _selection =None_, _pane =None_)[[source]](../_modules/openpyxl/worksheet/views.html#SheetView)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

Information about the visible portions of this sheet.

colorId
    

Values must be of type <class ‘int’>

defaultGridColor
    

Values must be of type <class ‘bool’>

pane
    

Values must be of type <class ‘openpyxl.worksheet.views.Pane’>

rightToLeft
    

Values must be of type <class ‘bool’>

selection
    

A sequence (list or tuple) that may only contain objects of the declared type

showFormulas
    

Values must be of type <class ‘bool’>

showGridLines
    

Values must be of type <class ‘bool’>

showOutlineSymbols
    

Values must be of type <class ‘bool’>

showRowColHeaders
    

Values must be of type <class ‘bool’>

showRuler
    

Values must be of type <class ‘bool’>

showWhiteSpace
    

Values must be of type <class ‘bool’>

showZeros
    

Values must be of type <class ‘bool’>

tabSelected
    

Values must be of type <class ‘bool’>

tagname _ = 'sheetView'_
    

topLeftCell
    

Values must be of type <class ‘str’>

view
    

Value must be one of {‘pageLayout’, ‘normal’, ‘pageBreakPreview’}

windowProtection
    

Values must be of type <class ‘bool’>

workbookViewId
    

Values must be of type <class ‘int’>

zoomScale
    

Values must be of type <class ‘int’>

zoomScaleNormal
    

Values must be of type <class ‘int’>

zoomScalePageLayoutView
    

Values must be of type <class ‘int’>

zoomScaleSheetLayoutView
    

Values must be of type <class ‘int’>

zoomToFit
    

Values must be of type <class ‘bool’>

_class _openpyxl.worksheet.views.SheetViewList(_sheetView =None_, _extLst =None_)[[source]](../_modules/openpyxl/worksheet/views.html#SheetViewList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

_property _active
    

Returns the first sheet view which is assumed to be active

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

sheetView
    

A sequence (list or tuple) that may only contain objects of the declared type

tagname _ = 'sheetViews'_
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.worksheet.views module
    * `Pane`
      * `Pane.activePane`
      * `Pane.state`
      * `Pane.topLeftCell`
      * `Pane.xSplit`
      * `Pane.ySplit`
    * `Selection`
      * `Selection.activeCell`
      * `Selection.activeCellId`
      * `Selection.pane`
      * `Selection.sqref`
    * `SheetView`
      * `SheetView.colorId`
      * `SheetView.defaultGridColor`
      * `SheetView.pane`
      * `SheetView.rightToLeft`
      * `SheetView.selection`
      * `SheetView.showFormulas`
      * `SheetView.showGridLines`
      * `SheetView.showOutlineSymbols`
      * `SheetView.showRowColHeaders`
      * `SheetView.showRuler`
      * `SheetView.showWhiteSpace`
      * `SheetView.showZeros`
      * `SheetView.tabSelected`
      * `SheetView.tagname`
      * `SheetView.topLeftCell`
      * `SheetView.view`
      * `SheetView.windowProtection`
      * `SheetView.workbookViewId`
      * `SheetView.zoomScale`
      * `SheetView.zoomScaleNormal`
      * `SheetView.zoomScalePageLayoutView`
      * `SheetView.zoomScaleSheetLayoutView`
      * `SheetView.zoomToFit`
    * `SheetViewList`
      * `SheetViewList.active`
      * `SheetViewList.extLst`
      * `SheetViewList.sheetView`
      * `SheetViewList.tagname`



#### Previous topic

[openpyxl.worksheet.table module](openpyxl.worksheet.table.html "previous chapter")

#### Next topic

[openpyxl.worksheet.worksheet module](openpyxl.worksheet.worksheet.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.worksheet.views.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.worksheet.html "openpyxl.worksheet.worksheet module") |
  * [previous](openpyxl.worksheet.table.html "openpyxl.worksheet.table module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.views module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
