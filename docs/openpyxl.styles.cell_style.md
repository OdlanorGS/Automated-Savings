### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.styles.colors.html "openpyxl.styles.colors module") |
  * [previous](openpyxl.styles.builtins.html "openpyxl.styles.builtins module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.styles package](openpyxl.styles.html) »
  * [openpyxl.styles.cell_style module]()



# openpyxl.styles.cell_style module

_class _openpyxl.styles.cell_style.ArrayDescriptor(_key_)[[source]](../_modules/openpyxl/styles/cell_style.html#ArrayDescriptor)
    

Bases: `object`

_class _openpyxl.styles.cell_style.CellStyle(_numFmtId =0_, _fontId =0_, _fillId =0_, _borderId =0_, _xfId =None_, _quotePrefix =None_, _pivotButton =None_, _applyNumberFormat =None_, _applyFont =None_, _applyFill =None_, _applyBorder =None_, _applyAlignment =None_, _applyProtection =None_, _alignment =None_, _protection =None_, _extLst =None_)[[source]](../_modules/openpyxl/styles/cell_style.html#CellStyle)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

alignment
    

Values must be of type <class ‘openpyxl.styles.alignment.Alignment’>

_property _applyAlignment
    

applyBorder
    

Values must be of type <class ‘bool’>

applyFill
    

Values must be of type <class ‘bool’>

applyFont
    

Values must be of type <class ‘bool’>

applyNumberFormat
    

Values must be of type <class ‘bool’>

_property _applyProtection
    

borderId
    

Values must be of type <class ‘int’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

fillId
    

Values must be of type <class ‘int’>

fontId
    

Values must be of type <class ‘int’>

_classmethod _from_array(_style_)[[source]](../_modules/openpyxl/styles/cell_style.html#CellStyle.from_array)
    

Convert from StyleArray

numFmtId
    

Values must be of type <class ‘int’>

pivotButton
    

Values must be of type <class ‘bool’>

protection
    

Values must be of type <class ‘openpyxl.styles.protection.Protection’>

quotePrefix
    

Values must be of type <class ‘bool’>

tagname _ = 'xf'_
    

to_array()[[source]](../_modules/openpyxl/styles/cell_style.html#CellStyle.to_array)
    

Convert to StyleArray

xfId
    

Values must be of type <class ‘int’>

_class _openpyxl.styles.cell_style.CellStyleList(_count =None_, _xf =()_)[[source]](../_modules/openpyxl/styles/cell_style.html#CellStyleList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

alignment
    

A sequence (list or tuple) that may only contain objects of the declared type

_property _count
    

protection
    

A sequence (list or tuple) that may only contain objects of the declared type

tagname _ = 'cellXfs'_
    

xf
    

A sequence (list or tuple) that may only contain objects of the declared type

_class _openpyxl.styles.cell_style.StyleArray(_args =[0, 0, 0, 0, 0, 0, 0, 0, 0]_)[[source]](../_modules/openpyxl/styles/cell_style.html#StyleArray)
    

Bases: `array`

Simplified named tuple with an array

alignmentId
    

borderId
    

fillId
    

fontId
    

numFmtId
    

pivotButton
    

protectionId
    

quotePrefix
    

tagname _ = 'xf'_
    

xfId
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.styles.cell_style module
    * `ArrayDescriptor`
    * `CellStyle`
      * `CellStyle.alignment`
      * `CellStyle.applyAlignment`
      * `CellStyle.applyBorder`
      * `CellStyle.applyFill`
      * `CellStyle.applyFont`
      * `CellStyle.applyNumberFormat`
      * `CellStyle.applyProtection`
      * `CellStyle.borderId`
      * `CellStyle.extLst`
      * `CellStyle.fillId`
      * `CellStyle.fontId`
      * `CellStyle.from_array()`
      * `CellStyle.numFmtId`
      * `CellStyle.pivotButton`
      * `CellStyle.protection`
      * `CellStyle.quotePrefix`
      * `CellStyle.tagname`
      * `CellStyle.to_array()`
      * `CellStyle.xfId`
    * `CellStyleList`
      * `CellStyleList.alignment`
      * `CellStyleList.count`
      * `CellStyleList.protection`
      * `CellStyleList.tagname`
      * `CellStyleList.xf`
    * `StyleArray`
      * `StyleArray.alignmentId`
      * `StyleArray.borderId`
      * `StyleArray.fillId`
      * `StyleArray.fontId`
      * `StyleArray.numFmtId`
      * `StyleArray.pivotButton`
      * `StyleArray.protectionId`
      * `StyleArray.quotePrefix`
      * `StyleArray.tagname`
      * `StyleArray.xfId`



#### Previous topic

[openpyxl.styles.builtins module](openpyxl.styles.builtins.html "previous chapter")

#### Next topic

[openpyxl.styles.colors module](openpyxl.styles.colors.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.styles.cell_style.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.styles.colors.html "openpyxl.styles.colors module") |
  * [previous](openpyxl.styles.builtins.html "openpyxl.styles.builtins module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.styles package](openpyxl.styles.html) »
  * [openpyxl.styles.cell_style module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
