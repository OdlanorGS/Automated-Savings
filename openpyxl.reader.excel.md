### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.reader.strings.html "openpyxl.reader.strings module") |
  * [previous](openpyxl.reader.drawings.html "openpyxl.reader.drawings module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.reader package](openpyxl.reader.html) »
  * [openpyxl.reader.excel module]()



# openpyxl.reader.excel module

Read an xlsx file into Python

_class _openpyxl.reader.excel.ExcelReader(_fn_ , _read_only =False_, _keep_vba =False_, _data_only =False_, _keep_links =True_, _rich_text =False_)[[source]](../_modules/openpyxl/reader/excel.html#ExcelReader)
    

Bases: `object`

Read an Excel package and dispatch the contents to the relevant modules

read()[[source]](../_modules/openpyxl/reader/excel.html#ExcelReader.read)
    

read_chartsheet(_sheet_ , _rel_)[[source]](../_modules/openpyxl/reader/excel.html#ExcelReader.read_chartsheet)
    

read_custom()[[source]](../_modules/openpyxl/reader/excel.html#ExcelReader.read_custom)
    

read_manifest()[[source]](../_modules/openpyxl/reader/excel.html#ExcelReader.read_manifest)
    

read_properties()[[source]](../_modules/openpyxl/reader/excel.html#ExcelReader.read_properties)
    

read_strings()[[source]](../_modules/openpyxl/reader/excel.html#ExcelReader.read_strings)
    

read_theme()[[source]](../_modules/openpyxl/reader/excel.html#ExcelReader.read_theme)
    

read_workbook()[[source]](../_modules/openpyxl/reader/excel.html#ExcelReader.read_workbook)
    

read_worksheets()[[source]](../_modules/openpyxl/reader/excel.html#ExcelReader.read_worksheets)
    

openpyxl.reader.excel.load_workbook(_filename_ , _read_only =False_, _keep_vba =False_, _data_only =False_, _keep_links =True_, _rich_text =False_)[[source]](../_modules/openpyxl/reader/excel.html#load_workbook)
    

Open the given filename and return the workbook

Parameters:
    

  * **filename** (string or a file-like object open in binary mode c.f., `zipfile.ZipFile`) – the path to open or a file-like object

  * **read_only** (_bool_) – optimised for reading, content cannot be edited

  * **keep_vba** (_bool_) – preserve vba content (this does NOT mean you can use it)

  * **data_only** (_bool_) – controls whether cells with formulae have either the formula (default) or the value stored the last time Excel read the sheet

  * **keep_links** (_bool_) – whether links to external workbooks should be preserved. The default is True

  * **rich_text** (_bool_) – if set to True openpyxl will preserve any rich text formatting in cells. The default is False



Return type:
    

`openpyxl.workbook.Workbook`

Note

When using lazy load, all worksheets will be `openpyxl.worksheet.iter_worksheet.IterableWorksheet` and the returned workbook will be read-only.

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.reader.excel module
    * `ExcelReader`
      * `ExcelReader.read()`
      * `ExcelReader.read_chartsheet()`
      * `ExcelReader.read_custom()`
      * `ExcelReader.read_manifest()`
      * `ExcelReader.read_properties()`
      * `ExcelReader.read_strings()`
      * `ExcelReader.read_theme()`
      * `ExcelReader.read_workbook()`
      * `ExcelReader.read_worksheets()`
    * `load_workbook()`



#### Previous topic

[openpyxl.reader.drawings module](openpyxl.reader.drawings.html "previous chapter")

#### Next topic

[openpyxl.reader.strings module](openpyxl.reader.strings.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.reader.excel.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.reader.strings.html "openpyxl.reader.strings module") |
  * [previous](openpyxl.reader.drawings.html "openpyxl.reader.drawings module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.reader package](openpyxl.reader.html) »
  * [openpyxl.reader.excel module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
