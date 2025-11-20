### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chartsheet.custom.html "openpyxl.chartsheet.custom module") |
  * [previous](openpyxl.chartsheet.html "openpyxl.chartsheet package") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.chartsheet package](openpyxl.chartsheet.html) »
  * [openpyxl.chartsheet.chartsheet module]()



# openpyxl.chartsheet.chartsheet module

_class _openpyxl.chartsheet.chartsheet.Chartsheet(_sheetPr =None_, _sheetViews =None_, _sheetProtection =None_, _customSheetViews =None_, _pageMargins =None_, _pageSetup =None_, _headerFooter =None_, _drawing =None_, _drawingHF =None_, _picture =None_, _webPublishItems =None_, _extLst =None_, _parent =None_, _title =''_, _sheet_state ='visible'_)[[source]](../_modules/openpyxl/chartsheet/chartsheet.html#Chartsheet)
    

Bases: `_WorkbookChild`, [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

HeaderFooter
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

add_chart(_chart_)[[source]](../_modules/openpyxl/chartsheet/chartsheet.html#Chartsheet.add_chart)
    

customSheetViews
    

Values must be of type <class ‘openpyxl.chartsheet.custom.CustomChartsheetViews’>

drawing
    

Values must be of type <class ‘openpyxl.worksheet.drawing.Drawing’>

drawingHF
    

Values must be of type <class ‘openpyxl.chartsheet.relation.DrawingHF’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

headerFooter
    

Values must be of type <class ‘openpyxl.worksheet.header_footer.HeaderFooter’>

mime_type _ = 'application/vnd.openxmlformats-officedocument.spreadsheetml.chartsheet+xml'_
    

pageMargins
    

Values must be of type <class ‘openpyxl.worksheet.page.PageMargins’>

pageSetup
    

Values must be of type <class ‘openpyxl.worksheet.page.PrintPageSetup’>

picture
    

Values must be of type <class ‘openpyxl.chartsheet.relation.SheetBackgroundPicture’>

sheetPr
    

Values must be of type <class ‘openpyxl.chartsheet.properties.ChartsheetProperties’>

sheetProtection
    

Values must be of type <class ‘openpyxl.chartsheet.protection.ChartsheetProtection’>

sheetViews
    

Values must be of type <class ‘openpyxl.chartsheet.views.ChartsheetViewList’>

sheet_state
    

Value must be one of {‘veryHidden’, ‘hidden’, ‘visible’}

tagname _ = 'chartsheet'_
    

to_tree()[[source]](../_modules/openpyxl/chartsheet/chartsheet.html#Chartsheet.to_tree)
    

webPublishItems
    

Values must be of type <class ‘openpyxl.chartsheet.publish.WebPublishItems’>

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.chartsheet.chartsheet module
    * `Chartsheet`
      * `Chartsheet.HeaderFooter`
      * `Chartsheet.add_chart()`
      * `Chartsheet.customSheetViews`
      * `Chartsheet.drawing`
      * `Chartsheet.drawingHF`
      * `Chartsheet.extLst`
      * `Chartsheet.headerFooter`
      * `Chartsheet.mime_type`
      * `Chartsheet.pageMargins`
      * `Chartsheet.pageSetup`
      * `Chartsheet.picture`
      * `Chartsheet.sheetPr`
      * `Chartsheet.sheetProtection`
      * `Chartsheet.sheetViews`
      * `Chartsheet.sheet_state`
      * `Chartsheet.tagname`
      * `Chartsheet.to_tree()`
      * `Chartsheet.webPublishItems`



#### Previous topic

[openpyxl.chartsheet package](openpyxl.chartsheet.html "previous chapter")

#### Next topic

[openpyxl.chartsheet.custom module](openpyxl.chartsheet.custom.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.chartsheet.chartsheet.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chartsheet.custom.html "openpyxl.chartsheet.custom module") |
  * [previous](openpyxl.chartsheet.html "openpyxl.chartsheet package") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.chartsheet package](openpyxl.chartsheet.html) »
  * [openpyxl.chartsheet.chartsheet module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
