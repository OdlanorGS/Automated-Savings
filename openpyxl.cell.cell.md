### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.cell.read_only.html "openpyxl.cell.read_only module") |
  * [previous](openpyxl.cell.html "openpyxl.cell package") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.cell package](openpyxl.cell.html) »
  * [openpyxl.cell.cell module]()



# openpyxl.cell.cell module

Manage individual cells in a spreadsheet.

The Cell class is required to know its value and type, display options, and any other features of an Excel cell. Utilities for referencing cells using Excel’s ‘A1’ column/row nomenclature are also provided.

_class _openpyxl.cell.cell.Cell(_worksheet_ , _row =None_, _column =None_, _value =None_, _style_array =None_)[[source]](../_modules/openpyxl/cell/cell.html#Cell)
    

Bases: [`StyleableObject`](openpyxl.styles.styleable.html#openpyxl.styles.styleable.StyleableObject "openpyxl.styles.styleable.StyleableObject")

Describes cell associated properties.

Properties of interest include style, type, value, and address.

_property _base_date
    

check_error(_value_)[[source]](../_modules/openpyxl/cell/cell.html#Cell.check_error)
    

Tries to convert Error” else N/A

check_string(_value_)[[source]](../_modules/openpyxl/cell/cell.html#Cell.check_string)
    

Check string coding, length, and line break character

_property _col_idx
    

The numerical index of the column

column
    

Column number of this cell (1-based)

_property _column_letter
    

_property _comment
    

Returns the comment associated with this cell

Type:
    

`openpyxl.comments.Comment`

_property _coordinate
    

This cell’s coordinate (ex. ‘A5’)

data_type
    

_property _encoding
    

_property _hyperlink
    

Return the hyperlink target or an empty string

_property _internal_value
    

Always returns the value for excel.

_property _is_date
    

True if the value is formatted as a date

Type:
    

bool

offset(_row =0_, _column =0_)[[source]](../_modules/openpyxl/cell/cell.html#Cell.offset)
    

Returns a cell location relative to this cell.

Parameters:
    

  * **row** (_int_) – number of rows to offset

  * **column** (_int_) – number of columns to offset



Return type:
    

`openpyxl.cell.Cell`

parent
    

row
    

Row number of this cell (1-based)

_property _value
    

Get or set the value held in the cell.

Type:
    

depends on the value (string, float, int or `datetime.datetime`)

_class _openpyxl.cell.cell.MergedCell(_worksheet_ , _row =None_, _column =None_)[[source]](../_modules/openpyxl/cell/cell.html#MergedCell)
    

Bases: [`StyleableObject`](openpyxl.styles.styleable.html#openpyxl.styles.styleable.StyleableObject "openpyxl.styles.styleable.StyleableObject")

Describes the properties of a cell in a merged cell and helps to display the borders of the merged cell.

The value of a MergedCell is always None.

column
    

comment _ = None_
    

_property _coordinate
    

This cell’s coordinate (ex. ‘A5’)

data_type _ = 'n'_
    

hyperlink _ = None_
    

row
    

value _ = None_
    

openpyxl.cell.cell.WriteOnlyCell(_ws =None_, _value =None_)[[source]](../_modules/openpyxl/cell/cell.html#WriteOnlyCell)
    

openpyxl.cell.cell.get_time_format(_t_)[[source]](../_modules/openpyxl/cell/cell.html#get_time_format)
    

openpyxl.cell.cell.get_type(_t_ , _value_)[[source]](../_modules/openpyxl/cell/cell.html#get_type)
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.cell.cell module
    * `Cell`
      * `Cell.base_date`
      * `Cell.check_error()`
      * `Cell.check_string()`
      * `Cell.col_idx`
      * `Cell.column`
      * `Cell.column_letter`
      * `Cell.comment`
      * `Cell.coordinate`
      * `Cell.data_type`
      * `Cell.encoding`
      * `Cell.hyperlink`
      * `Cell.internal_value`
      * `Cell.is_date`
      * `Cell.offset()`
      * `Cell.parent`
      * `Cell.row`
      * `Cell.value`
    * `MergedCell`
      * `MergedCell.column`
      * `MergedCell.comment`
      * `MergedCell.coordinate`
      * `MergedCell.data_type`
      * `MergedCell.hyperlink`
      * `MergedCell.row`
      * `MergedCell.value`
    * `WriteOnlyCell()`
    * `get_time_format()`
    * `get_type()`



#### Previous topic

[openpyxl.cell package](openpyxl.cell.html "previous chapter")

#### Next topic

[openpyxl.cell.read_only module](openpyxl.cell.read_only.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.cell.cell.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.cell.read_only.html "openpyxl.cell.read_only module") |
  * [previous](openpyxl.cell.html "openpyxl.cell package") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.cell package](openpyxl.cell.html) »
  * [openpyxl.cell.cell module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
