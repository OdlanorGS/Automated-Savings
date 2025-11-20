### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.workbook.web.html "openpyxl.workbook.web module") |
  * [previous](openpyxl.workbook.smart_tags.html "openpyxl.workbook.smart_tags module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.workbook package](openpyxl.workbook.html) »
  * [openpyxl.workbook.views module]()



# openpyxl.workbook.views module

_class _openpyxl.workbook.views.BookView(_visibility ='visible'_, _minimized =False_, _showHorizontalScroll =True_, _showVerticalScroll =True_, _showSheetTabs =True_, _xWindow =None_, _yWindow =None_, _windowWidth =None_, _windowHeight =None_, _tabRatio =600_, _firstSheet =0_, _activeTab =0_, _autoFilterDateGrouping =True_, _extLst =None_)[[source]](../_modules/openpyxl/workbook/views.html#BookView)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

activeTab
    

Values must be of type <class ‘int’>

autoFilterDateGrouping
    

Values must be of type <class ‘bool’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

firstSheet
    

Values must be of type <class ‘int’>

minimized
    

Values must be of type <class ‘bool’>

showHorizontalScroll
    

Values must be of type <class ‘bool’>

showSheetTabs
    

Values must be of type <class ‘bool’>

showVerticalScroll
    

Values must be of type <class ‘bool’>

tabRatio
    

Values must be of type <class ‘int’>

tagname _ = 'workbookView'_
    

visibility
    

Value must be one of {‘veryHidden’, ‘hidden’, ‘visible’}

windowHeight
    

Values must be of type <class ‘int’>

windowWidth
    

Values must be of type <class ‘int’>

xWindow
    

Values must be of type <class ‘int’>

yWindow
    

Values must be of type <class ‘int’>

_class _openpyxl.workbook.views.CustomWorkbookView(_name =None_, _guid =None_, _autoUpdate =None_, _mergeInterval =None_, _changesSavedWin =None_, _onlySync =None_, _personalView =None_, _includePrintSettings =None_, _includeHiddenRowCol =None_, _maximized =None_, _minimized =None_, _showHorizontalScroll =None_, _showVerticalScroll =None_, _showSheetTabs =None_, _xWindow =None_, _yWindow =None_, _windowWidth =None_, _windowHeight =None_, _tabRatio =None_, _activeSheetId =None_, _showFormulaBar =None_, _showStatusbar =None_, _showComments ='commIndicator'_, _showObjects ='all'_, _extLst =None_)[[source]](../_modules/openpyxl/workbook/views.html#CustomWorkbookView)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

activeSheetId
    

Values must be of type <class ‘int’>

autoUpdate
    

Values must be of type <class ‘bool’>

changesSavedWin
    

Values must be of type <class ‘bool’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

guid
    

includeHiddenRowCol
    

Values must be of type <class ‘bool’>

includePrintSettings
    

Values must be of type <class ‘bool’>

maximized
    

Values must be of type <class ‘bool’>

mergeInterval
    

Values must be of type <class ‘int’>

minimized
    

Values must be of type <class ‘bool’>

name
    

Values must be of type <class ‘str’>

onlySync
    

Values must be of type <class ‘bool’>

personalView
    

Values must be of type <class ‘bool’>

showComments
    

Value must be one of {‘commIndicator’, ‘commNone’, ‘commIndAndComment’}

showFormulaBar
    

Values must be of type <class ‘bool’>

showHorizontalScroll
    

Values must be of type <class ‘bool’>

showObjects
    

Value must be one of {‘placeholders’, ‘all’}

showSheetTabs
    

Values must be of type <class ‘bool’>

showStatusbar
    

Values must be of type <class ‘bool’>

showVerticalScroll
    

Values must be of type <class ‘bool’>

tabRatio
    

Values must be of type <class ‘int’>

tagname _ = 'customWorkbookView'_
    

windowHeight
    

Values must be of type <class ‘int’>

windowWidth
    

Values must be of type <class ‘int’>

xWindow
    

Values must be of type <class ‘int’>

yWindow
    

Values must be of type <class ‘int’>

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.workbook.views module
    * `BookView`
      * `BookView.activeTab`
      * `BookView.autoFilterDateGrouping`
      * `BookView.extLst`
      * `BookView.firstSheet`
      * `BookView.minimized`
      * `BookView.showHorizontalScroll`
      * `BookView.showSheetTabs`
      * `BookView.showVerticalScroll`
      * `BookView.tabRatio`
      * `BookView.tagname`
      * `BookView.visibility`
      * `BookView.windowHeight`
      * `BookView.windowWidth`
      * `BookView.xWindow`
      * `BookView.yWindow`
    * `CustomWorkbookView`
      * `CustomWorkbookView.activeSheetId`
      * `CustomWorkbookView.autoUpdate`
      * `CustomWorkbookView.changesSavedWin`
      * `CustomWorkbookView.extLst`
      * `CustomWorkbookView.guid`
      * `CustomWorkbookView.includeHiddenRowCol`
      * `CustomWorkbookView.includePrintSettings`
      * `CustomWorkbookView.maximized`
      * `CustomWorkbookView.mergeInterval`
      * `CustomWorkbookView.minimized`
      * `CustomWorkbookView.name`
      * `CustomWorkbookView.onlySync`
      * `CustomWorkbookView.personalView`
      * `CustomWorkbookView.showComments`
      * `CustomWorkbookView.showFormulaBar`
      * `CustomWorkbookView.showHorizontalScroll`
      * `CustomWorkbookView.showObjects`
      * `CustomWorkbookView.showSheetTabs`
      * `CustomWorkbookView.showStatusbar`
      * `CustomWorkbookView.showVerticalScroll`
      * `CustomWorkbookView.tabRatio`
      * `CustomWorkbookView.tagname`
      * `CustomWorkbookView.windowHeight`
      * `CustomWorkbookView.windowWidth`
      * `CustomWorkbookView.xWindow`
      * `CustomWorkbookView.yWindow`



#### Previous topic

[openpyxl.workbook.smart_tags module](openpyxl.workbook.smart_tags.html "previous chapter")

#### Next topic

[openpyxl.workbook.web module](openpyxl.workbook.web.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.workbook.views.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.workbook.web.html "openpyxl.workbook.web module") |
  * [previous](openpyxl.workbook.smart_tags.html "openpyxl.workbook.smart_tags module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.workbook package](openpyxl.workbook.html) »
  * [openpyxl.workbook.views module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
