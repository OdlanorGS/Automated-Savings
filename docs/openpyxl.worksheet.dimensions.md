### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.drawing.html "openpyxl.worksheet.drawing module") |
  * [previous](openpyxl.worksheet.datavalidation.html "openpyxl.worksheet.datavalidation module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.dimensions module]()



# openpyxl.worksheet.dimensions module

_class _openpyxl.worksheet.dimensions.ColumnDimension(_worksheet_ , _index ='A'_, _width =13_, _bestFit =False_, _hidden =False_, _outlineLevel =0_, _outline_level =None_, _collapsed =False_, _style =None_, _min =None_, _max =None_, _customWidth =False_, _visible =None_, _auto_size =None_)[[source]](../_modules/openpyxl/worksheet/dimensions.html#ColumnDimension)
    

Bases: `Dimension`

Information about the display properties of a column.

auto_size
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

bestFit
    

Values must be of type <class ‘bool’>

collapsed
    

Values must be of type <class ‘bool’>

_property _customWidth
    

Always true if there is a width for the column

index
    

Values must be of type <class ‘str’>

max
    

Values must be of type <class ‘int’>

min
    

Values must be of type <class ‘int’>

parent
    

_property _range
    

Return the range of cells actually covered

reindex()[[source]](../_modules/openpyxl/worksheet/dimensions.html#ColumnDimension.reindex)
    

Set boundaries for column definition

to_tree()[[source]](../_modules/openpyxl/worksheet/dimensions.html#ColumnDimension.to_tree)
    

width
    

Values must be of type <class ‘float’>

_class _openpyxl.worksheet.dimensions.Dimension(_index_ , _hidden_ , _outlineLevel_ , _collapsed_ , _worksheet_ , _visible =True_, _style =None_)[[source]](../_modules/openpyxl/worksheet/dimensions.html#Dimension)
    

Bases: [`Strict`](openpyxl.descriptors.html#openpyxl.descriptors.Strict "openpyxl.descriptors.Strict"), [`StyleableObject`](openpyxl.styles.styleable.html#openpyxl.styles.styleable.StyleableObject "openpyxl.styles.styleable.StyleableObject")

Information about the display properties of a row or column.

collapsed
    

Values must be of type <class ‘bool’>

hidden
    

Values must be of type <class ‘bool’>

index
    

Values must be of type <class ‘int’>

outlineLevel
    

Values must be of type <class ‘int’>

outline_level
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

parent
    

style
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

_class _openpyxl.worksheet.dimensions.DimensionHolder(_worksheet_ , _reference ='index'_, _default_factory =None_)[[source]](../_modules/openpyxl/worksheet/dimensions.html#DimensionHolder)
    

Bases: [`BoundDictionary`](openpyxl.utils.bound_dictionary.html#openpyxl.utils.bound_dictionary.BoundDictionary "openpyxl.utils.bound_dictionary.BoundDictionary")

Allow columns to be grouped

group(_start_ , _end =None_, _outline_level =1_, _hidden =False_)[[source]](../_modules/openpyxl/worksheet/dimensions.html#DimensionHolder.group)
    

allow grouping a range of consecutive rows or columns together

Parameters:
    

  * **start** – first row or column to be grouped (mandatory)

  * **end** – last row or column to be grouped (optional, default to start)

  * **outline_level** – outline level

  * **hidden** – should the group be hidden on workbook open or not




to_tree()[[source]](../_modules/openpyxl/worksheet/dimensions.html#DimensionHolder.to_tree)
    

_class _openpyxl.worksheet.dimensions.RowDimension(_worksheet_ , _index =0_, _ht =None_, _customHeight =None_, _s =None_, _customFormat =None_, _hidden =False_, _outlineLevel =0_, _outline_level =None_, _collapsed =False_, _visible =None_, _height =None_, _r =None_, _spans =None_, _thickBot =None_, _thickTop =None_, _** kw_)[[source]](../_modules/openpyxl/worksheet/dimensions.html#RowDimension)
    

Bases: `Dimension`

Information about the display properties of a row.

_property _customFormat
    

Always true if there is a style for the row

_property _customHeight
    

Always true if there is a height for the row

height
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

ht
    

Values must be of type <class ‘float’>

parent
    

r
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

s
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

thickBot
    

Values must be of type <class ‘bool’>

thickTop
    

Values must be of type <class ‘bool’>

_class _openpyxl.worksheet.dimensions.SheetDimension(_ref =None_)[[source]](../_modules/openpyxl/worksheet/dimensions.html#SheetDimension)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

_property _boundaries
    

ref
    

Values must be of type <class ‘str’>

tagname _ = 'dimension'_
    

_class _openpyxl.worksheet.dimensions.SheetFormatProperties(_baseColWidth =8_, _defaultColWidth =None_, _defaultRowHeight =15_, _customHeight =None_, _zeroHeight =None_, _thickTop =None_, _thickBottom =None_, _outlineLevelRow =None_, _outlineLevelCol =None_)[[source]](../_modules/openpyxl/worksheet/dimensions.html#SheetFormatProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

baseColWidth
    

Values must be of type <class ‘int’>

customHeight
    

Values must be of type <class ‘bool’>

defaultColWidth
    

Values must be of type <class ‘float’>

defaultRowHeight
    

Values must be of type <class ‘float’>

outlineLevelCol
    

Values must be of type <class ‘int’>

outlineLevelRow
    

Values must be of type <class ‘int’>

tagname _ = 'sheetFormatPr'_
    

thickBottom
    

Values must be of type <class ‘bool’>

thickTop
    

Values must be of type <class ‘bool’>

zeroHeight
    

Values must be of type <class ‘bool’>

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.worksheet.dimensions module
    * `ColumnDimension`
      * `ColumnDimension.auto_size`
      * `ColumnDimension.bestFit`
      * `ColumnDimension.collapsed`
      * `ColumnDimension.customWidth`
      * `ColumnDimension.index`
      * `ColumnDimension.max`
      * `ColumnDimension.min`
      * `ColumnDimension.parent`
      * `ColumnDimension.range`
      * `ColumnDimension.reindex()`
      * `ColumnDimension.to_tree()`
      * `ColumnDimension.width`
    * `Dimension`
      * `Dimension.collapsed`
      * `Dimension.hidden`
      * `Dimension.index`
      * `Dimension.outlineLevel`
      * `Dimension.outline_level`
      * `Dimension.parent`
      * `Dimension.style`
    * `DimensionHolder`
      * `DimensionHolder.group()`
      * `DimensionHolder.to_tree()`
    * `RowDimension`
      * `RowDimension.customFormat`
      * `RowDimension.customHeight`
      * `RowDimension.height`
      * `RowDimension.ht`
      * `RowDimension.parent`
      * `RowDimension.r`
      * `RowDimension.s`
      * `RowDimension.thickBot`
      * `RowDimension.thickTop`
    * `SheetDimension`
      * `SheetDimension.boundaries`
      * `SheetDimension.ref`
      * `SheetDimension.tagname`
    * `SheetFormatProperties`
      * `SheetFormatProperties.baseColWidth`
      * `SheetFormatProperties.customHeight`
      * `SheetFormatProperties.defaultColWidth`
      * `SheetFormatProperties.defaultRowHeight`
      * `SheetFormatProperties.outlineLevelCol`
      * `SheetFormatProperties.outlineLevelRow`
      * `SheetFormatProperties.tagname`
      * `SheetFormatProperties.thickBottom`
      * `SheetFormatProperties.thickTop`
      * `SheetFormatProperties.zeroHeight`



#### Previous topic

[openpyxl.worksheet.datavalidation module](openpyxl.worksheet.datavalidation.html "previous chapter")

#### Next topic

[openpyxl.worksheet.drawing module](openpyxl.worksheet.drawing.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.worksheet.dimensions.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.drawing.html "openpyxl.worksheet.drawing module") |
  * [previous](openpyxl.worksheet.datavalidation.html "openpyxl.worksheet.datavalidation module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.dimensions module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
