### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.utils.dataframe.html "openpyxl.utils.dataframe module") |
  * [previous](openpyxl.utils.bound_dictionary.html "openpyxl.utils.bound_dictionary module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.utils package](openpyxl.utils.html) »
  * [openpyxl.utils.cell module]()



# openpyxl.utils.cell module

Collection of utilities used within the package and also available for client code

openpyxl.utils.cell.absolute_coordinate(_coord_string_)[[source]](../_modules/openpyxl/utils/cell.html#absolute_coordinate)
    

Convert a coordinate to an absolute coordinate string (B12 -> $B$12)

openpyxl.utils.cell.cols_from_range(_range_string_)[[source]](../_modules/openpyxl/utils/cell.html#cols_from_range)
    

Get individual addresses for every cell in a range. Yields one row at a time.

openpyxl.utils.cell.column_index_from_string(_col_)[[source]](../_modules/openpyxl/utils/cell.html#column_index_from_string)
    

Convert ASCII column name (base 26) to decimal with 1-based index

Characters represent descending multiples of powers of 26

“AFZ” == 26 * pow(26, 0) + 6 * pow(26, 1) + 1 * pow(26, 2)

openpyxl.utils.cell.coordinate_from_string(_coord_string_)[[source]](../_modules/openpyxl/utils/cell.html#coordinate_from_string)
    

Convert a coordinate string like ‘B12’ to a tuple (‘B’, 12)

openpyxl.utils.cell.coordinate_to_tuple(_coordinate_)[[source]](../_modules/openpyxl/utils/cell.html#coordinate_to_tuple)
    

Convert an Excel style coordinate to (row, column) tuple

openpyxl.utils.cell.get_column_interval(_start_ , _end_)[[source]](../_modules/openpyxl/utils/cell.html#get_column_interval)
    

Given the start and end columns, return all the columns in the series.

The start and end columns can be either column letters or 1-based indexes.

openpyxl.utils.cell.get_column_letter(_col_idx_)[[source]](../_modules/openpyxl/utils/cell.html#get_column_letter)
    

Convert decimal column position to its ASCII (base 26) form.

Because column indices are 1-based, strides are actually pow(26, n) + 26 Hence, a correction is applied between pow(26, n) and pow(26, 2) + 26 to prevent and additional column letter being prepended

“A” == 1 == pow(26, 0) “Z” == 26 == pow(26, 0) + 26 // decimal equivalent 10 “AA” == 27 == pow(26, 1) + 1 “ZZ” == 702 == pow(26, 2) + 26 // decimal equivalent 100

openpyxl.utils.cell.quote_sheetname(_sheetname_)[[source]](../_modules/openpyxl/utils/cell.html#quote_sheetname)
    

Add quotes around sheetnames if they contain spaces.

openpyxl.utils.cell.range_boundaries(_range_string_)[[source]](../_modules/openpyxl/utils/cell.html#range_boundaries)
    

Convert a range string into a tuple of boundaries: (min_col, min_row, max_col, max_row) Cell coordinates will be converted into a range with the cell at both end

openpyxl.utils.cell.range_to_tuple(_range_string_)[[source]](../_modules/openpyxl/utils/cell.html#range_to_tuple)
    

Convert a worksheet range to the sheetname and maximum and minimum coordinate indices

openpyxl.utils.cell.rows_from_range(_range_string_)[[source]](../_modules/openpyxl/utils/cell.html#rows_from_range)
    

Get individual addresses for every cell in a range. Yields one row at a time.

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.utils.cell module
    * `absolute_coordinate()`
    * `cols_from_range()`
    * `column_index_from_string()`
    * `coordinate_from_string()`
    * `coordinate_to_tuple()`
    * `get_column_interval()`
    * `get_column_letter()`
    * `quote_sheetname()`
    * `range_boundaries()`
    * `range_to_tuple()`
    * `rows_from_range()`



#### Previous topic

[openpyxl.utils.bound_dictionary module](openpyxl.utils.bound_dictionary.html "previous chapter")

#### Next topic

[openpyxl.utils.dataframe module](openpyxl.utils.dataframe.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.utils.cell.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.utils.dataframe.html "openpyxl.utils.dataframe module") |
  * [previous](openpyxl.utils.bound_dictionary.html "openpyxl.utils.bound_dictionary module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.utils package](openpyxl.utils.html) »
  * [openpyxl.utils.cell module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
