### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.utils.html "openpyxl.utils package") |
  * [previous](openpyxl.styles.stylesheet.html "openpyxl.styles.stylesheet module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.styles package](openpyxl.styles.html) »
  * [openpyxl.styles.table module]()



# openpyxl.styles.table module

_class _openpyxl.styles.table.TableStyle(_name =None_, _pivot =None_, _table =None_, _count =None_, _tableStyleElement =()_)[[source]](../_modules/openpyxl/styles/table.html#TableStyle)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

count
    

Values must be of type <class ‘int’>

name
    

Values must be of type <class ‘str’>

pivot
    

Values must be of type <class ‘bool’>

table
    

Values must be of type <class ‘bool’>

tableStyleElement
    

A sequence (list or tuple) that may only contain objects of the declared type

tagname _ = 'tableStyle'_
    

_class _openpyxl.styles.table.TableStyleElement(_type =None_, _size =None_, _dxfId =None_)[[source]](../_modules/openpyxl/styles/table.html#TableStyleElement)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

dxfId
    

Values must be of type <class ‘int’>

size
    

Values must be of type <class ‘int’>

tagname _ = 'tableStyleElement'_
    

type
    

Value must be one of {‘lastTotalCell’, ‘lastHeaderCell’, ‘pageFieldValues’, ‘wholeTable’, ‘secondSubtotalRow’, ‘thirdSubtotalRow’, ‘firstColumnStripe’, ‘firstRowStripe’, ‘firstRowSubheading’, ‘secondColumnSubheading’, ‘firstSubtotalColumn’, ‘totalRow’, ‘thirdRowSubheading’, ‘firstSubtotalRow’, ‘secondColumnStripe’, ‘firstTotalCell’, ‘secondSubtotalColumn’, ‘secondRowSubheading’, ‘thirdColumnSubheading’, ‘headerRow’, ‘firstColumn’, ‘thirdSubtotalColumn’, ‘lastColumn’, ‘firstColumnSubheading’, ‘pageFieldLabels’, ‘secondRowStripe’, ‘blankRow’, ‘firstHeaderCell’}

_class _openpyxl.styles.table.TableStyleList(_count =None_, _defaultTableStyle ='TableStyleMedium9'_, _defaultPivotStyle ='PivotStyleLight16'_, _tableStyle =()_)[[source]](../_modules/openpyxl/styles/table.html#TableStyleList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

_property _count
    

defaultPivotStyle
    

Values must be of type <class ‘str’>

defaultTableStyle
    

Values must be of type <class ‘str’>

tableStyle
    

A sequence (list or tuple) that may only contain objects of the declared type

tagname _ = 'tableStyles'_
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.styles.table module
    * `TableStyle`
      * `TableStyle.count`
      * `TableStyle.name`
      * `TableStyle.pivot`
      * `TableStyle.table`
      * `TableStyle.tableStyleElement`
      * `TableStyle.tagname`
    * `TableStyleElement`
      * `TableStyleElement.dxfId`
      * `TableStyleElement.size`
      * `TableStyleElement.tagname`
      * `TableStyleElement.type`
    * `TableStyleList`
      * `TableStyleList.count`
      * `TableStyleList.defaultPivotStyle`
      * `TableStyleList.defaultTableStyle`
      * `TableStyleList.tableStyle`
      * `TableStyleList.tagname`



#### Previous topic

[openpyxl.styles.stylesheet module](openpyxl.styles.stylesheet.html "previous chapter")

#### Next topic

[openpyxl.utils package](openpyxl.utils.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.styles.table.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.utils.html "openpyxl.utils package") |
  * [previous](openpyxl.styles.stylesheet.html "openpyxl.styles.stylesheet module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.styles package](openpyxl.styles.html) »
  * [openpyxl.styles.table module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
