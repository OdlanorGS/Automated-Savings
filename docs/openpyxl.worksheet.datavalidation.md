### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.dimensions.html "openpyxl.worksheet.dimensions module") |
  * [previous](openpyxl.worksheet.custom.html "openpyxl.worksheet.custom module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.datavalidation module]()



# openpyxl.worksheet.datavalidation module

_class _openpyxl.worksheet.datavalidation.DataValidation(_type =None_, _formula1 =None_, _formula2 =None_, _showErrorMessage =False_, _showInputMessage =False_, _showDropDown =False_, _allowBlank =False_, _sqref =()_, _promptTitle =None_, _errorStyle =None_, _error =None_, _prompt =None_, _errorTitle =None_, _imeMode =None_, _operator =None_, _allow_blank =None_)[[source]](../_modules/openpyxl/worksheet/datavalidation.html#DataValidation)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

add(_cell_)[[source]](../_modules/openpyxl/worksheet/datavalidation.html#DataValidation.add)
    

Adds a cell or cell coordinate to this validator

allowBlank
    

Values must be of type <class ‘bool’>

allow_blank
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

cells
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

error
    

Values must be of type <class ‘str’>

errorStyle
    

Value must be one of {‘information’, ‘stop’, ‘warning’}

errorTitle
    

Values must be of type <class ‘str’>

formula1
    

Values must be of type <class ‘str’>

formula2
    

Values must be of type <class ‘str’>

hide_drop_down
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

imeMode
    

Value must be one of {‘fullKatakana’, ‘fullAlpha’, ‘disabled’, ‘fullHangul’, ‘halfAlpha’, ‘halfKatakana’, ‘noControl’, ‘off’, ‘hiragana’, ‘halfHangul’, ‘on’}

operator
    

Value must be one of {‘lessThanOrEqual’, ‘notBetween’, ‘lessThan’, ‘greaterThan’, ‘equal’, ‘greaterThanOrEqual’, ‘notEqual’, ‘between’}

prompt
    

Values must be of type <class ‘str’>

promptTitle
    

Values must be of type <class ‘str’>

ranges
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

showDropDown
    

Values must be of type <class ‘bool’>

showErrorMessage
    

Values must be of type <class ‘bool’>

showInputMessage
    

Values must be of type <class ‘bool’>

sqref
    

Values must be of type <class ‘openpyxl.worksheet.cell_range.MultiCellRange’>

tagname _ = 'dataValidation'_
    

type
    

Value must be one of {‘whole’, ‘custom’, ‘time’, ‘list’, ‘decimal’, ‘textLength’, ‘date’}

validation_type
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

_class _openpyxl.worksheet.datavalidation.DataValidationList(_disablePrompts =None_, _xWindow =None_, _yWindow =None_, _count =None_, _dataValidation =()_)[[source]](../_modules/openpyxl/worksheet/datavalidation.html#DataValidationList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

append(_dv_)[[source]](../_modules/openpyxl/worksheet/datavalidation.html#DataValidationList.append)
    

_property _count
    

dataValidation
    

A sequence (list or tuple) that may only contain objects of the declared type

disablePrompts
    

Values must be of type <class ‘bool’>

tagname _ = 'dataValidations'_
    

to_tree(_tagname =None_)[[source]](../_modules/openpyxl/worksheet/datavalidation.html#DataValidationList.to_tree)
    

Need to skip validations that have no cell ranges

xWindow
    

Values must be of type <class ‘int’>

yWindow
    

Values must be of type <class ‘int’>

openpyxl.worksheet.datavalidation.collapse_cell_addresses(_cells_ , _input_ranges =()_)[[source]](../_modules/openpyxl/worksheet/datavalidation.html#collapse_cell_addresses)
    

Collapse a collection of cell co-ordinates down into an optimal range or collection of ranges.

E.g. Cells A1, A2, A3, B1, B2 and B3 should have the data-validation object applied, attempt to collapse down to a single range, A1:B3.

Currently only collapsing contiguous vertical ranges (i.e. above example results in A1:A3 B1:B3).

openpyxl.worksheet.datavalidation.expand_cell_ranges(_range_string_)[[source]](../_modules/openpyxl/worksheet/datavalidation.html#expand_cell_ranges)
    

Expand cell ranges to a sequence of addresses. Reverse of collapse_cell_addresses Eg. converts “A1:A2 B1:B2” to (A1, A2, B1, B2)

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.worksheet.datavalidation module
    * `DataValidation`
      * `DataValidation.add()`
      * `DataValidation.allowBlank`
      * `DataValidation.allow_blank`
      * `DataValidation.cells`
      * `DataValidation.error`
      * `DataValidation.errorStyle`
      * `DataValidation.errorTitle`
      * `DataValidation.formula1`
      * `DataValidation.formula2`
      * `DataValidation.hide_drop_down`
      * `DataValidation.imeMode`
      * `DataValidation.operator`
      * `DataValidation.prompt`
      * `DataValidation.promptTitle`
      * `DataValidation.ranges`
      * `DataValidation.showDropDown`
      * `DataValidation.showErrorMessage`
      * `DataValidation.showInputMessage`
      * `DataValidation.sqref`
      * `DataValidation.tagname`
      * `DataValidation.type`
      * `DataValidation.validation_type`
    * `DataValidationList`
      * `DataValidationList.append()`
      * `DataValidationList.count`
      * `DataValidationList.dataValidation`
      * `DataValidationList.disablePrompts`
      * `DataValidationList.tagname`
      * `DataValidationList.to_tree()`
      * `DataValidationList.xWindow`
      * `DataValidationList.yWindow`
    * `collapse_cell_addresses()`
    * `expand_cell_ranges()`



#### Previous topic

[openpyxl.worksheet.custom module](openpyxl.worksheet.custom.html "previous chapter")

#### Next topic

[openpyxl.worksheet.dimensions module](openpyxl.worksheet.dimensions.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.worksheet.datavalidation.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.dimensions.html "openpyxl.worksheet.dimensions module") |
  * [previous](openpyxl.worksheet.custom.html "openpyxl.worksheet.custom module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.datavalidation module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
