### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.writer.html "openpyxl.writer package") |
  * [previous](openpyxl.worksheet.views.html "openpyxl.worksheet.views module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.worksheet module]()



# openpyxl.worksheet.worksheet module

Worksheet is the 2nd-level container in Excel.

_class _openpyxl.worksheet.worksheet.Worksheet(_parent_ , _title =None_)[[source]](../_modules/openpyxl/worksheet/worksheet.html#Worksheet)
    

Bases: `_WorkbookChild`

Represents a worksheet.

Do not create worksheets yourself, use `openpyxl.workbook.Workbook.create_sheet()` instead

BREAK_COLUMN _ = 2_
    

BREAK_NONE _ = 0_
    

BREAK_ROW _ = 1_
    

ORIENTATION_LANDSCAPE _ = 'landscape'_
    

ORIENTATION_PORTRAIT _ = 'portrait'_
    

PAPERSIZE_A3 _ = '8'_
    

PAPERSIZE_A4 _ = '9'_
    

PAPERSIZE_A4_SMALL _ = '10'_
    

PAPERSIZE_A5 _ = '11'_
    

PAPERSIZE_EXECUTIVE _ = '7'_
    

PAPERSIZE_LEDGER _ = '4'_
    

PAPERSIZE_LEGAL _ = '5'_
    

PAPERSIZE_LETTER _ = '1'_
    

PAPERSIZE_LETTER_SMALL _ = '2'_
    

PAPERSIZE_STATEMENT _ = '6'_
    

PAPERSIZE_TABLOID _ = '3'_
    

SHEETSTATE_HIDDEN _ = 'hidden'_
    

SHEETSTATE_VERYHIDDEN _ = 'veryHidden'_
    

SHEETSTATE_VISIBLE _ = 'visible'_
    

_property _active_cell
    

add_chart(_chart_ , _anchor =None_)[[source]](../_modules/openpyxl/worksheet/worksheet.html#Worksheet.add_chart)
    

Add a chart to the sheet Optionally provide a cell for the top-left anchor

add_data_validation(_data_validation_)[[source]](../_modules/openpyxl/worksheet/worksheet.html#Worksheet.add_data_validation)
    

Add a data-validation object to the sheet. The data-validation object defines the type of data-validation to be applied and the cell or range of cells it should apply to.

add_image(_img_ , _anchor =None_)[[source]](../_modules/openpyxl/worksheet/worksheet.html#Worksheet.add_image)
    

Add an image to the sheet. Optionally provide a cell for the top-left anchor

add_pivot(_pivot_)[[source]](../_modules/openpyxl/worksheet/worksheet.html#Worksheet.add_pivot)
    

add_table(_table_)[[source]](../_modules/openpyxl/worksheet/worksheet.html#Worksheet.add_table)
    

Check for duplicate name in definedNames and other worksheet tables before adding table.

append(_iterable_)[[source]](../_modules/openpyxl/worksheet/worksheet.html#Worksheet.append)
    

Appends a group of values at the bottom of the current sheet.

  * If it’s a list: all values are added in order, starting from the first column

  * If it’s a dict: values are assigned to the columns indicated by the keys (numbers or letters)




Parameters:
    

**iterable** (_list_ _|__tuple_ _|__range_ _|__generator_ _or_ _dict_) – list, range or generator, or dict containing values to append

Usage:

  * append([‘This is A1’, ‘This is B1’, ‘This is C1’])

  * **or** append({‘A’ : ‘This is A1’, ‘C’ : ‘This is C1’})

  * **or** append({1 : ‘This is A1’, 3 : ‘This is C1’})




Raise:
    

TypeError when iterable is neither a list/tuple nor a dict

_property _array_formulae
    

Returns a dictionary of cells with array formulae and the cells in array

calculate_dimension()[[source]](../_modules/openpyxl/worksheet/worksheet.html#Worksheet.calculate_dimension)
    

Return the minimum bounding range for all cells containing data (ex. ‘A1:M24’)

Return type:
    

string

cell(_row_ , _column_ , _value =None_)[[source]](../_modules/openpyxl/worksheet/worksheet.html#Worksheet.cell)
    

Returns a cell object based on the given coordinates.

Usage: cell(row=15, column=1, value=5)

Calling cell creates cells in memory when they are first accessed.

Parameters:
    

  * **row** (_int_) – row index of the cell (e.g. 4)

  * **column** (_int_) – column index of the cell (e.g. 3)

  * **value** (_numeric_ _or_ _time_ _or_ _string_ _or_ _bool_ _or_ _none_) – value of the cell (e.g. 5)



Return type:
    

[openpyxl.cell.cell.Cell](openpyxl.cell.cell.html#openpyxl.cell.cell.Cell "openpyxl.cell.cell.Cell")

_property _column_groups
    

Return a list of column ranges where more than one column

_property _columns
    

Produces all cells in the worksheet, by column (see `iter_cols()`)

delete_cols(_idx_ , _amount =1_)[[source]](../_modules/openpyxl/worksheet/worksheet.html#Worksheet.delete_cols)
    

Delete column or columns from col==idx

delete_rows(_idx_ , _amount =1_)[[source]](../_modules/openpyxl/worksheet/worksheet.html#Worksheet.delete_rows)
    

Delete row or rows from row==idx

_property _dimensions
    

Returns the result of `calculate_dimension()`

_property _freeze_panes
    

insert_cols(_idx_ , _amount =1_)[[source]](../_modules/openpyxl/worksheet/worksheet.html#Worksheet.insert_cols)
    

Insert column or columns before col==idx

insert_rows(_idx_ , _amount =1_)[[source]](../_modules/openpyxl/worksheet/worksheet.html#Worksheet.insert_rows)
    

Insert row or rows before row==idx

iter_cols(_min_col =None_, _max_col =None_, _min_row =None_, _max_row =None_, _values_only =False_)[[source]](../_modules/openpyxl/worksheet/worksheet.html#Worksheet.iter_cols)
    

Produces cells from the worksheet, by column. Specify the iteration range using indices of rows and columns.

If no indices are specified the range starts at A1.

If no cells are in the worksheet an empty tuple will be returned.

Parameters:
    

  * **min_col** (_int_) – smallest column index (1-based index)

  * **min_row** (_int_) – smallest row index (1-based index)

  * **max_col** (_int_) – largest column index (1-based index)

  * **max_row** (_int_) – largest row index (1-based index)

  * **values_only** (_bool_) – whether only cell values should be returned



Return type:
    

generator

iter_rows(_min_row =None_, _max_row =None_, _min_col =None_, _max_col =None_, _values_only =False_)[[source]](../_modules/openpyxl/worksheet/worksheet.html#Worksheet.iter_rows)
    

Produces cells from the worksheet, by row. Specify the iteration range using indices of rows and columns.

If no indices are specified the range starts at A1.

If no cells are in the worksheet an empty tuple will be returned.

Parameters:
    

  * **min_col** (_int_) – smallest column index (1-based index)

  * **min_row** (_int_) – smallest row index (1-based index)

  * **max_col** (_int_) – largest column index (1-based index)

  * **max_row** (_int_) – largest row index (1-based index)

  * **values_only** (_bool_) – whether only cell values should be returned



Return type:
    

generator

_property _max_column
    

The maximum column index containing data (1-based)

Type:
    

int

_property _max_row
    

The maximum row index containing data (1-based)

Type:
    

int

merge_cells(_range_string =None_, _start_row =None_, _start_column =None_, _end_row =None_, _end_column =None_)[[source]](../_modules/openpyxl/worksheet/worksheet.html#Worksheet.merge_cells)
    

Set merge on a cell range. Range is a cell range (e.g. A1:E1)

_property _merged_cell_ranges
    

Return a copy of cell ranges

Note

Deprecated: Use ws.merged_cells.ranges

mime_type _ = 'application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml'_
    

_property _min_column
    

The minimum column index containing data (1-based)

Type:
    

int

_property _min_row
    

The minimum row index containing data (1-based)

Type:
    

int

move_range(_cell_range_ , _rows =0_, _cols =0_, _translate =False_)[[source]](../_modules/openpyxl/worksheet/worksheet.html#Worksheet.move_range)
    

Move a cell range by the number of rows and/or columns: down if rows > 0 and up if rows < 0 right if cols > 0 and left if cols < 0 Existing cells will be overwritten. Formulae and references will not be updated.

_property _print_area
    

The print area for the worksheet, or None if not set. To set, supply a range like ‘A1:D4’ or a list of ranges.

_property _print_title_cols
    

Columns to be printed at the left side of every page (ex: ‘A:C’)

_property _print_title_rows
    

Rows to be printed at the top of every page (ex: ‘1:3’)

_property _print_titles
    

_property _rows
    

Produces all cells in the worksheet, by row (see `iter_rows()`)

Type:
    

generator

_property _selected_cell
    

set_printer_settings(_paper_size_ , _orientation_)[[source]](../_modules/openpyxl/worksheet/worksheet.html#Worksheet.set_printer_settings)
    

Set printer settings

_property _sheet_view
    

_property _show_gridlines
    

_property _tables
    

unmerge_cells(_range_string =None_, _start_row =None_, _start_column =None_, _end_row =None_, _end_column =None_)[[source]](../_modules/openpyxl/worksheet/worksheet.html#Worksheet.unmerge_cells)
    

Remove merge on a cell range. Range is a cell range (e.g. A1:E1)

_property _values
    

Produces all cell values in the worksheet, by row

Type:
    

generator

openpyxl.worksheet.worksheet.isgenerator(_obj_)
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.worksheet.worksheet module
    * `Worksheet`
      * `Worksheet.BREAK_COLUMN`
      * `Worksheet.BREAK_NONE`
      * `Worksheet.BREAK_ROW`
      * `Worksheet.ORIENTATION_LANDSCAPE`
      * `Worksheet.ORIENTATION_PORTRAIT`
      * `Worksheet.PAPERSIZE_A3`
      * `Worksheet.PAPERSIZE_A4`
      * `Worksheet.PAPERSIZE_A4_SMALL`
      * `Worksheet.PAPERSIZE_A5`
      * `Worksheet.PAPERSIZE_EXECUTIVE`
      * `Worksheet.PAPERSIZE_LEDGER`
      * `Worksheet.PAPERSIZE_LEGAL`
      * `Worksheet.PAPERSIZE_LETTER`
      * `Worksheet.PAPERSIZE_LETTER_SMALL`
      * `Worksheet.PAPERSIZE_STATEMENT`
      * `Worksheet.PAPERSIZE_TABLOID`
      * `Worksheet.SHEETSTATE_HIDDEN`
      * `Worksheet.SHEETSTATE_VERYHIDDEN`
      * `Worksheet.SHEETSTATE_VISIBLE`
      * `Worksheet.active_cell`
      * `Worksheet.add_chart()`
      * `Worksheet.add_data_validation()`
      * `Worksheet.add_image()`
      * `Worksheet.add_pivot()`
      * `Worksheet.add_table()`
      * `Worksheet.append()`
      * `Worksheet.array_formulae`
      * `Worksheet.calculate_dimension()`
      * `Worksheet.cell()`
      * `Worksheet.column_groups`
      * `Worksheet.columns`
      * `Worksheet.delete_cols()`
      * `Worksheet.delete_rows()`
      * `Worksheet.dimensions`
      * `Worksheet.freeze_panes`
      * `Worksheet.insert_cols()`
      * `Worksheet.insert_rows()`
      * `Worksheet.iter_cols()`
      * `Worksheet.iter_rows()`
      * `Worksheet.max_column`
      * `Worksheet.max_row`
      * `Worksheet.merge_cells()`
      * `Worksheet.merged_cell_ranges`
      * `Worksheet.mime_type`
      * `Worksheet.min_column`
      * `Worksheet.min_row`
      * `Worksheet.move_range()`
      * `Worksheet.print_area`
      * `Worksheet.print_title_cols`
      * `Worksheet.print_title_rows`
      * `Worksheet.print_titles`
      * `Worksheet.rows`
      * `Worksheet.selected_cell`
      * `Worksheet.set_printer_settings()`
      * `Worksheet.sheet_view`
      * `Worksheet.show_gridlines`
      * `Worksheet.tables`
      * `Worksheet.unmerge_cells()`
      * `Worksheet.values`
    * `isgenerator()`



#### Previous topic

[openpyxl.worksheet.views module](openpyxl.worksheet.views.html "previous chapter")

#### Next topic

[openpyxl.writer package](openpyxl.writer.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.worksheet.worksheet.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.writer.html "openpyxl.writer package") |
  * [previous](openpyxl.worksheet.views.html "openpyxl.worksheet.views module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.worksheet module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
