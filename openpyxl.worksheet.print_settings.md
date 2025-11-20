### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.properties.html "openpyxl.worksheet.properties module") |
  * [previous](openpyxl.worksheet.picture.html "openpyxl.worksheet.picture module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.print_settings module]()



# openpyxl.worksheet.print_settings module

_class _openpyxl.worksheet.print_settings.ColRange(_range_string =None_, _min_col =None_, _max_col =None_)[[source]](../_modules/openpyxl/worksheet/print_settings.html#ColRange)
    

Bases: [`Strict`](openpyxl.descriptors.html#openpyxl.descriptors.Strict "openpyxl.descriptors.Strict")

Represent a range of at least one column

max_col
    

Values must be of type <class ‘str’>

min_col
    

Values must be of type <class ‘str’>

_class _openpyxl.worksheet.print_settings.PrintArea(_ranges =()_, _title =''_)[[source]](../_modules/openpyxl/worksheet/print_settings.html#PrintArea)
    

Bases: [`MultiCellRange`](openpyxl.worksheet.cell_range.html#openpyxl.worksheet.cell_range.MultiCellRange "openpyxl.worksheet.cell_range.MultiCellRange")

_classmethod _from_string(_value_)[[source]](../_modules/openpyxl/worksheet/print_settings.html#PrintArea.from_string)
    

_class _openpyxl.worksheet.print_settings.PrintTitles(_cols =None_, _rows =None_, _title =''_)[[source]](../_modules/openpyxl/worksheet/print_settings.html#PrintTitles)
    

Bases: [`Strict`](openpyxl.descriptors.html#openpyxl.descriptors.Strict "openpyxl.descriptors.Strict")

Contains at least either a range of rows or columns

cols
    

Values must be of type <class ‘openpyxl.worksheet.print_settings.ColRange’>

_classmethod _from_string(_value_)[[source]](../_modules/openpyxl/worksheet/print_settings.html#PrintTitles.from_string)
    

rows
    

Values must be of type <class ‘openpyxl.worksheet.print_settings.RowRange’>

title
    

Values must be of type <class ‘str’>

_class _openpyxl.worksheet.print_settings.RowRange(_range_string =None_, _min_row =None_, _max_row =None_)[[source]](../_modules/openpyxl/worksheet/print_settings.html#RowRange)
    

Bases: [`Strict`](openpyxl.descriptors.html#openpyxl.descriptors.Strict "openpyxl.descriptors.Strict")

Represent a range of at least one row

max_row
    

Values must be of type <class ‘int’>

min_row
    

Values must be of type <class ‘int’>

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.worksheet.print_settings module
    * `ColRange`
      * `ColRange.max_col`
      * `ColRange.min_col`
    * `PrintArea`
      * `PrintArea.from_string()`
    * `PrintTitles`
      * `PrintTitles.cols`
      * `PrintTitles.from_string()`
      * `PrintTitles.rows`
      * `PrintTitles.title`
    * `RowRange`
      * `RowRange.max_row`
      * `RowRange.min_row`



#### Previous topic

[openpyxl.worksheet.picture module](openpyxl.worksheet.picture.html "previous chapter")

#### Next topic

[openpyxl.worksheet.properties module](openpyxl.worksheet.properties.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.worksheet.print_settings.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.properties.html "openpyxl.worksheet.properties module") |
  * [previous](openpyxl.worksheet.picture.html "openpyxl.worksheet.picture module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.print_settings module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
