### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.pagebreak.html "openpyxl.worksheet.pagebreak module") |
  * [previous](openpyxl.worksheet.ole.html "openpyxl.worksheet.ole module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.page module]()



# openpyxl.worksheet.page module

_class _openpyxl.worksheet.page.PageMargins(_left =0.75_, _right =0.75_, _top =1_, _bottom =1_, _header =0.5_, _footer =0.5_)[[source]](../_modules/openpyxl/worksheet/page.html#PageMargins)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

Information about page margins for view/print layouts. Standard values (in inches) left, right = 0.75 top, bottom = 1 header, footer = 0.5

bottom
    

Values must be of type <class ‘float’>

footer
    

Values must be of type <class ‘float’>

header
    

Values must be of type <class ‘float’>

left
    

Values must be of type <class ‘float’>

right
    

Values must be of type <class ‘float’>

tagname _ = 'pageMargins'_
    

top
    

Values must be of type <class ‘float’>

_class _openpyxl.worksheet.page.PrintOptions(_horizontalCentered =None_, _verticalCentered =None_, _headings =None_, _gridLines =None_, _gridLinesSet =None_)[[source]](../_modules/openpyxl/worksheet/page.html#PrintOptions)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

Worksheet print options

gridLines
    

Values must be of type <class ‘bool’>

gridLinesSet
    

Values must be of type <class ‘bool’>

headings
    

Values must be of type <class ‘bool’>

horizontalCentered
    

Values must be of type <class ‘bool’>

tagname _ = 'printOptions'_
    

verticalCentered
    

Values must be of type <class ‘bool’>

_class _openpyxl.worksheet.page.PrintPageSetup(_worksheet =None_, _orientation =None_, _paperSize =None_, _scale =None_, _fitToHeight =None_, _fitToWidth =None_, _firstPageNumber =None_, _useFirstPageNumber =None_, _paperHeight =None_, _paperWidth =None_, _pageOrder =None_, _usePrinterDefaults =None_, _blackAndWhite =None_, _draft =None_, _cellComments =None_, _errors =None_, _horizontalDpi =None_, _verticalDpi =None_, _copies =None_, _id =None_)[[source]](../_modules/openpyxl/worksheet/page.html#PrintPageSetup)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

Worksheet print page setup

_property _autoPageBreaks
    

blackAndWhite
    

Values must be of type <class ‘bool’>

cellComments
    

Value must be one of {‘atEnd’, ‘asDisplayed’}

copies
    

Values must be of type <class ‘int’>

draft
    

Values must be of type <class ‘bool’>

errors
    

Value must be one of {‘dash’, ‘blank’, ‘displayed’, ‘NA’}

firstPageNumber
    

Values must be of type <class ‘int’>

fitToHeight
    

Values must be of type <class ‘int’>

_property _fitToPage
    

fitToWidth
    

Values must be of type <class ‘int’>

_classmethod _from_tree(_node_)[[source]](../_modules/openpyxl/worksheet/page.html#PrintPageSetup.from_tree)
    

Create object from XML

horizontalDpi
    

Values must be of type <class ‘int’>

id
    

Values must be of type <class ‘str’>

orientation
    

Value must be one of {‘portrait’, ‘default’, ‘landscape’}

pageOrder
    

Value must be one of {‘downThenOver’, ‘overThenDown’}

paperHeight
    

paperSize
    

Values must be of type <class ‘int’>

paperWidth
    

scale
    

Values must be of type <class ‘int’>

_property _sheet_properties
    

Proxy property

tagname _ = 'pageSetup'_
    

useFirstPageNumber
    

Values must be of type <class ‘bool’>

usePrinterDefaults
    

Values must be of type <class ‘bool’>

verticalDpi
    

Values must be of type <class ‘int’>

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.worksheet.page module
    * `PageMargins`
      * `PageMargins.bottom`
      * `PageMargins.footer`
      * `PageMargins.header`
      * `PageMargins.left`
      * `PageMargins.right`
      * `PageMargins.tagname`
      * `PageMargins.top`
    * `PrintOptions`
      * `PrintOptions.gridLines`
      * `PrintOptions.gridLinesSet`
      * `PrintOptions.headings`
      * `PrintOptions.horizontalCentered`
      * `PrintOptions.tagname`
      * `PrintOptions.verticalCentered`
    * `PrintPageSetup`
      * `PrintPageSetup.autoPageBreaks`
      * `PrintPageSetup.blackAndWhite`
      * `PrintPageSetup.cellComments`
      * `PrintPageSetup.copies`
      * `PrintPageSetup.draft`
      * `PrintPageSetup.errors`
      * `PrintPageSetup.firstPageNumber`
      * `PrintPageSetup.fitToHeight`
      * `PrintPageSetup.fitToPage`
      * `PrintPageSetup.fitToWidth`
      * `PrintPageSetup.from_tree()`
      * `PrintPageSetup.horizontalDpi`
      * `PrintPageSetup.id`
      * `PrintPageSetup.orientation`
      * `PrintPageSetup.pageOrder`
      * `PrintPageSetup.paperHeight`
      * `PrintPageSetup.paperSize`
      * `PrintPageSetup.paperWidth`
      * `PrintPageSetup.scale`
      * `PrintPageSetup.sheet_properties`
      * `PrintPageSetup.tagname`
      * `PrintPageSetup.useFirstPageNumber`
      * `PrintPageSetup.usePrinterDefaults`
      * `PrintPageSetup.verticalDpi`



#### Previous topic

[openpyxl.worksheet.ole module](openpyxl.worksheet.ole.html "previous chapter")

#### Next topic

[openpyxl.worksheet.pagebreak module](openpyxl.worksheet.pagebreak.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.worksheet.page.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.pagebreak.html "openpyxl.worksheet.pagebreak module") |
  * [previous](openpyxl.worksheet.ole.html "openpyxl.worksheet.ole module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.page module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
