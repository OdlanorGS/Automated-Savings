### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.views.html "openpyxl.worksheet.views module") |
  * [previous](openpyxl.worksheet.smart_tag.html "openpyxl.worksheet.smart_tag module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.table module]()



# openpyxl.worksheet.table module

_class _openpyxl.worksheet.table.Table(_id =1_, _displayName =None_, _ref =None_, _name =None_, _comment =None_, _tableType =None_, _headerRowCount =1_, _insertRow =None_, _insertRowShift =None_, _totalsRowCount =None_, _totalsRowShown =None_, _published =None_, _headerRowDxfId =None_, _dataDxfId =None_, _totalsRowDxfId =None_, _headerRowBorderDxfId =None_, _tableBorderDxfId =None_, _totalsRowBorderDxfId =None_, _headerRowCellStyle =None_, _dataCellStyle =None_, _totalsRowCellStyle =None_, _connectionId =None_, _autoFilter =None_, _sortState =None_, _tableColumns =()_, _tableStyleInfo =None_, _extLst =None_)[[source]](../_modules/openpyxl/worksheet/table.html#Table)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

autoFilter
    

Values must be of type <class ‘openpyxl.worksheet.filters.AutoFilter’>

_property _column_names
    

comment
    

Values must be of type <class ‘str’>

connectionId
    

Values must be of type <class ‘int’>

dataCellStyle
    

Values must be of type <class ‘str’>

dataDxfId
    

Values must be of type <class ‘int’>

displayName
    

Values must be of type <class ‘str’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

headerRowBorderDxfId
    

Values must be of type <class ‘int’>

headerRowCellStyle
    

Values must be of type <class ‘str’>

headerRowCount
    

Values must be of type <class ‘int’>

headerRowDxfId
    

Values must be of type <class ‘int’>

id
    

Values must be of type <class ‘int’>

insertRow
    

Values must be of type <class ‘bool’>

insertRowShift
    

Values must be of type <class ‘bool’>

mime_type _ = 'application/vnd.openxmlformats-officedocument.spreadsheetml.table+xml'_
    

name
    

Values must be of type <class ‘str’>

_property _path
    

Return path within the archive

published
    

Values must be of type <class ‘bool’>

ref
    

sortState
    

Values must be of type <class ‘openpyxl.worksheet.filters.SortState’>

tableBorderDxfId
    

Values must be of type <class ‘int’>

tableColumns
    

Wrap a sequence in an containing object

tableStyleInfo
    

Values must be of type <class ‘openpyxl.worksheet.table.TableStyleInfo’>

tableType
    

Value must be one of {‘xml’, ‘worksheet’, ‘queryTable’}

tagname _ = 'table'_
    

to_tree()[[source]](../_modules/openpyxl/worksheet/table.html#Table.to_tree)
    

totalsRowBorderDxfId
    

Values must be of type <class ‘int’>

totalsRowCellStyle
    

Values must be of type <class ‘str’>

totalsRowCount
    

Values must be of type <class ‘int’>

totalsRowDxfId
    

Values must be of type <class ‘int’>

totalsRowShown
    

Values must be of type <class ‘bool’>

_class _openpyxl.worksheet.table.TableColumn(_id =None_, _uniqueName =None_, _name =None_, _totalsRowFunction =None_, _totalsRowLabel =None_, _queryTableFieldId =None_, _headerRowDxfId =None_, _dataDxfId =None_, _totalsRowDxfId =None_, _headerRowCellStyle =None_, _dataCellStyle =None_, _totalsRowCellStyle =None_, _calculatedColumnFormula =None_, _totalsRowFormula =None_, _xmlColumnPr =None_, _extLst =None_)[[source]](../_modules/openpyxl/worksheet/table.html#TableColumn)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

calculatedColumnFormula
    

Values must be of type <class ‘openpyxl.worksheet.table.TableFormula’>

dataCellStyle
    

Values must be of type <class ‘str’>

dataDxfId
    

Values must be of type <class ‘int’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

_classmethod _from_tree(_node_)[[source]](../_modules/openpyxl/worksheet/table.html#TableColumn.from_tree)
    

Create object from XML

headerRowCellStyle
    

Values must be of type <class ‘str’>

headerRowDxfId
    

Values must be of type <class ‘int’>

id
    

Values must be of type <class ‘int’>

name
    

Values must be of type <class ‘str’>

queryTableFieldId
    

Values must be of type <class ‘int’>

tagname _ = 'tableColumn'_
    

totalsRowCellStyle
    

Values must be of type <class ‘str’>

totalsRowDxfId
    

Values must be of type <class ‘int’>

totalsRowFormula
    

Values must be of type <class ‘openpyxl.worksheet.table.TableFormula’>

totalsRowFunction
    

Value must be one of {‘min’, ‘count’, ‘countNums’, ‘var’, ‘average’, ‘custom’, ‘max’, ‘sum’, ‘stdDev’}

totalsRowLabel
    

Values must be of type <class ‘str’>

uniqueName
    

Values must be of type <class ‘str’>

xmlColumnPr
    

Values must be of type <class ‘openpyxl.worksheet.table.XMLColumnProps’>

_class _openpyxl.worksheet.table.TableFormula(_array =None_, _attr_text =None_)[[source]](../_modules/openpyxl/worksheet/table.html#TableFormula)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

array
    

Values must be of type <class ‘bool’>

attr_text
    

tagname _ = 'tableFormula'_
    

text
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

_class _openpyxl.worksheet.table.TableList[[source]](../_modules/openpyxl/worksheet/table.html#TableList)
    

Bases: `dict`

add(_table_)[[source]](../_modules/openpyxl/worksheet/table.html#TableList.add)
    

get(_name =None_, _table_range =None_)[[source]](../_modules/openpyxl/worksheet/table.html#TableList.get)
    

Return the value for key if key is in the dictionary, else default.

items() → a set-like object providing a view on D's items[[source]](../_modules/openpyxl/worksheet/table.html#TableList.items)
    

_class _openpyxl.worksheet.table.TableNameDescriptor(_* args_, _** kw_)[[source]](../_modules/openpyxl/worksheet/table.html#TableNameDescriptor)
    

Bases: [`String`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.String "openpyxl.descriptors.base.String")

Table names cannot have spaces in them

_class _openpyxl.worksheet.table.TablePartList(_count =None_, _tablePart =()_)[[source]](../_modules/openpyxl/worksheet/table.html#TablePartList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

append(_part_)[[source]](../_modules/openpyxl/worksheet/table.html#TablePartList.append)
    

_property _count
    

tablePart
    

A sequence (list or tuple) that may only contain objects of the declared type

tagname _ = 'tableParts'_
    

_class _openpyxl.worksheet.table.TableStyleInfo(_name =None_, _showFirstColumn =None_, _showLastColumn =None_, _showRowStripes =None_, _showColumnStripes =None_)[[source]](../_modules/openpyxl/worksheet/table.html#TableStyleInfo)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

name
    

Values must be of type <class ‘str’>

showColumnStripes
    

Values must be of type <class ‘bool’>

showFirstColumn
    

Values must be of type <class ‘bool’>

showLastColumn
    

Values must be of type <class ‘bool’>

showRowStripes
    

Values must be of type <class ‘bool’>

tagname _ = 'tableStyleInfo'_
    

_class _openpyxl.worksheet.table.XMLColumnProps(_mapId =None_, _xpath =None_, _denormalized =None_, _xmlDataType =None_, _extLst =None_)[[source]](../_modules/openpyxl/worksheet/table.html#XMLColumnProps)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

denormalized
    

Values must be of type <class ‘bool’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

mapId
    

Values must be of type <class ‘int’>

tagname _ = 'xmlColumnPr'_
    

xmlDataType
    

Values must be of type <class ‘str’>

xpath
    

Values must be of type <class ‘str’>

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.worksheet.table module
    * `Table`
      * `Table.autoFilter`
      * `Table.column_names`
      * `Table.comment`
      * `Table.connectionId`
      * `Table.dataCellStyle`
      * `Table.dataDxfId`
      * `Table.displayName`
      * `Table.extLst`
      * `Table.headerRowBorderDxfId`
      * `Table.headerRowCellStyle`
      * `Table.headerRowCount`
      * `Table.headerRowDxfId`
      * `Table.id`
      * `Table.insertRow`
      * `Table.insertRowShift`
      * `Table.mime_type`
      * `Table.name`
      * `Table.path`
      * `Table.published`
      * `Table.ref`
      * `Table.sortState`
      * `Table.tableBorderDxfId`
      * `Table.tableColumns`
      * `Table.tableStyleInfo`
      * `Table.tableType`
      * `Table.tagname`
      * `Table.to_tree()`
      * `Table.totalsRowBorderDxfId`
      * `Table.totalsRowCellStyle`
      * `Table.totalsRowCount`
      * `Table.totalsRowDxfId`
      * `Table.totalsRowShown`
    * `TableColumn`
      * `TableColumn.calculatedColumnFormula`
      * `TableColumn.dataCellStyle`
      * `TableColumn.dataDxfId`
      * `TableColumn.extLst`
      * `TableColumn.from_tree()`
      * `TableColumn.headerRowCellStyle`
      * `TableColumn.headerRowDxfId`
      * `TableColumn.id`
      * `TableColumn.name`
      * `TableColumn.queryTableFieldId`
      * `TableColumn.tagname`
      * `TableColumn.totalsRowCellStyle`
      * `TableColumn.totalsRowDxfId`
      * `TableColumn.totalsRowFormula`
      * `TableColumn.totalsRowFunction`
      * `TableColumn.totalsRowLabel`
      * `TableColumn.uniqueName`
      * `TableColumn.xmlColumnPr`
    * `TableFormula`
      * `TableFormula.array`
      * `TableFormula.attr_text`
      * `TableFormula.tagname`
      * `TableFormula.text`
    * `TableList`
      * `TableList.add()`
      * `TableList.get()`
      * `TableList.items()`
    * `TableNameDescriptor`
    * `TablePartList`
      * `TablePartList.append()`
      * `TablePartList.count`
      * `TablePartList.tablePart`
      * `TablePartList.tagname`
    * `TableStyleInfo`
      * `TableStyleInfo.name`
      * `TableStyleInfo.showColumnStripes`
      * `TableStyleInfo.showFirstColumn`
      * `TableStyleInfo.showLastColumn`
      * `TableStyleInfo.showRowStripes`
      * `TableStyleInfo.tagname`
    * `XMLColumnProps`
      * `XMLColumnProps.denormalized`
      * `XMLColumnProps.extLst`
      * `XMLColumnProps.mapId`
      * `XMLColumnProps.tagname`
      * `XMLColumnProps.xmlDataType`
      * `XMLColumnProps.xpath`



#### Previous topic

[openpyxl.worksheet.smart_tag module](openpyxl.worksheet.smart_tag.html "previous chapter")

#### Next topic

[openpyxl.worksheet.views module](openpyxl.worksheet.views.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.worksheet.table.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.views.html "openpyxl.worksheet.views module") |
  * [previous](openpyxl.worksheet.smart_tag.html "openpyxl.worksheet.smart_tag module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.table module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
