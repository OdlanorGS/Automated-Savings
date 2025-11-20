### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.html "openpyxl.worksheet package") |
  * [previous](openpyxl.workbook.web.html "openpyxl.workbook.web module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.workbook package](openpyxl.workbook.html) »
  * [openpyxl.workbook.workbook module]()



# openpyxl.workbook.workbook module

Workbook is the top-level container for all document information.

_class _openpyxl.workbook.workbook.Workbook(_write_only =False_, _iso_dates =False_)[[source]](../_modules/openpyxl/workbook/workbook.html#Workbook)
    

Bases: `object`

Workbook is the container for all other parts of the document.

_property _active
    

Get the currently active sheet or None

Type:
    

[`openpyxl.worksheet.worksheet.Worksheet`](openpyxl.worksheet.worksheet.html#openpyxl.worksheet.worksheet.Worksheet "openpyxl.worksheet.worksheet.Worksheet")

add_named_style(_style_)[[source]](../_modules/openpyxl/workbook/workbook.html#Workbook.add_named_style)
    

Add a named style

_property _chartsheets
    

A list of Chartsheets in this workbook

Type:
    

list of [`openpyxl.chartsheet.chartsheet.Chartsheet`](openpyxl.chartsheet.chartsheet.html#openpyxl.chartsheet.chartsheet.Chartsheet "openpyxl.chartsheet.chartsheet.Chartsheet")

close()[[source]](../_modules/openpyxl/workbook/workbook.html#Workbook.close)
    

Close workbook file if open. Only affects read-only and write-only modes.

copy_worksheet(_from_worksheet_)[[source]](../_modules/openpyxl/workbook/workbook.html#Workbook.copy_worksheet)
    

Copy an existing worksheet in the current workbook

Warning

This function cannot copy worksheets between workbooks. worksheets can only be copied within the workbook that they belong

Parameters:
    

**from_worksheet** – the worksheet to be copied from

Returns:
    

copy of the initial worksheet

create_chartsheet(_title =None_, _index =None_)[[source]](../_modules/openpyxl/workbook/workbook.html#Workbook.create_chartsheet)
    

create_named_range(_name_ , _worksheet =None_, _value =None_, _scope =None_)[[source]](../_modules/openpyxl/workbook/workbook.html#Workbook.create_named_range)
    

Create a new named_range on a worksheet

Note

Deprecated: Assign scoped named ranges directly to worksheets or global ones to the workbook. Deprecated in 3.1

create_sheet(_title =None_, _index =None_)[[source]](../_modules/openpyxl/workbook/workbook.html#Workbook.create_sheet)
    

Create a worksheet (at an optional index).

Parameters:
    

  * **title** (_str_) – optional title of the sheet

  * **index** (_int_) – optional position at which the sheet will be inserted




_property _data_only
    

_property _epoch
    

_property _excel_base_date
    

get_index(_worksheet_)[[source]](../_modules/openpyxl/workbook/workbook.html#Workbook.get_index)
    

Return the index of the worksheet.

Note

Deprecated: Use wb.index(worksheet)

get_sheet_by_name(_name_)[[source]](../_modules/openpyxl/workbook/workbook.html#Workbook.get_sheet_by_name)
    

Returns a worksheet by its name.

> param name:
>     
> 
> the name of the worksheet to look for
> 
> type name:
>     
> 
> string

Note

Deprecated: Use wb[sheetname]

get_sheet_names()[[source]](../_modules/openpyxl/workbook/workbook.html#Workbook.get_sheet_names)
    

Note

Deprecated: Use wb.sheetnames

index(_worksheet_)[[source]](../_modules/openpyxl/workbook/workbook.html#Workbook.index)
    

Return the index of a worksheet.

_property _mime_type
    

The mime type is determined by whether a workbook is a template or not and whether it contains macros or not. Excel requires the file extension to match but openpyxl does not enforce this.

move_sheet(_sheet_ , _offset =0_)[[source]](../_modules/openpyxl/workbook/workbook.html#Workbook.move_sheet)
    

Move a sheet or sheetname

_property _named_styles
    

List available named styles

path _ = '/xl/workbook.xml'_
    

_property _read_only
    

remove(_worksheet_)[[source]](../_modules/openpyxl/workbook/workbook.html#Workbook.remove)
    

Remove worksheet from this workbook.

remove_sheet(_worksheet_)[[source]](../_modules/openpyxl/workbook/workbook.html#Workbook.remove_sheet)
    

Remove worksheet from this workbook.

Note

Deprecated: Use wb.remove(worksheet) or del wb[sheetname]

save(_filename_)[[source]](../_modules/openpyxl/workbook/workbook.html#Workbook.save)
    

Save the current workbook under the given filename. Use this function instead of using an ExcelWriter.

Warning

When creating your workbook using write_only set to True, you will only be able to call this function once. Subsequent attempts to modify or save the file will raise an `openpyxl.shared.exc.WorkbookAlreadySaved` exception.

_property _sheetnames
    

Returns the list of the names of worksheets in this workbook.

Names are returned in the worksheets order.

Type:
    

list of strings

_property _style_names
    

List of named styles

template _ = False_
    

_property _worksheets
    

A list of sheets in this workbook

Type:
    

list of [`openpyxl.worksheet.worksheet.Worksheet`](openpyxl.worksheet.worksheet.html#openpyxl.worksheet.worksheet.Worksheet "openpyxl.worksheet.worksheet.Worksheet")

_property _write_only
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.workbook.workbook module
    * `Workbook`
      * `Workbook.active`
      * `Workbook.add_named_style()`
      * `Workbook.chartsheets`
      * `Workbook.close()`
      * `Workbook.copy_worksheet()`
      * `Workbook.create_chartsheet()`
      * `Workbook.create_named_range()`
      * `Workbook.create_sheet()`
      * `Workbook.data_only`
      * `Workbook.epoch`
      * `Workbook.excel_base_date`
      * `Workbook.get_index()`
      * `Workbook.get_sheet_by_name()`
      * `Workbook.get_sheet_names()`
      * `Workbook.index()`
      * `Workbook.mime_type`
      * `Workbook.move_sheet()`
      * `Workbook.named_styles`
      * `Workbook.path`
      * `Workbook.read_only`
      * `Workbook.remove()`
      * `Workbook.remove_sheet()`
      * `Workbook.save()`
      * `Workbook.sheetnames`
      * `Workbook.style_names`
      * `Workbook.template`
      * `Workbook.worksheets`
      * `Workbook.write_only`



#### Previous topic

[openpyxl.workbook.web module](openpyxl.workbook.web.html "previous chapter")

#### Next topic

[openpyxl.worksheet package](openpyxl.worksheet.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.workbook.workbook.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.html "openpyxl.worksheet package") |
  * [previous](openpyxl.workbook.web.html "openpyxl.workbook.web module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.workbook package](openpyxl.workbook.html) »
  * [openpyxl.workbook.workbook module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
