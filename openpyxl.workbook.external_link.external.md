### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.workbook.child.html "openpyxl.workbook.child module") |
  * [previous](openpyxl.workbook.external_link.html "openpyxl.workbook.external_link package") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.workbook package](openpyxl.workbook.html) »
  * [openpyxl.workbook.external_link package](openpyxl.workbook.external_link.html) »
  * [openpyxl.workbook.external_link.external module]()



# openpyxl.workbook.external_link.external module

_class _openpyxl.workbook.external_link.external.ExternalBook(_sheetNames =None_, _definedNames =()_, _sheetDataSet =None_, _id =None_)[[source]](../_modules/openpyxl/workbook/external_link/external.html#ExternalBook)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

definedNames
    

Wrap a sequence in an containing object

id
    

Values must be of type <class ‘str’>

sheetDataSet
    

Values must be of type <class ‘openpyxl.workbook.external_link.external.ExternalSheetDataSet’>

sheetNames
    

Values must be of type <class ‘openpyxl.workbook.external_link.external.ExternalSheetNames’>

tagname _ = 'externalBook'_
    

_class _openpyxl.workbook.external_link.external.ExternalCell(_r =None_, _t =None_, _vm =None_, _v =None_)[[source]](../_modules/openpyxl/workbook/external_link/external.html#ExternalCell)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

r
    

Values must be of type <class ‘str’>

t
    

Value must be one of {‘str’, ‘b’, ‘n’, ‘inlineStr’, ‘d’, ‘s’, ‘e’}

v
    

Values must be of type <class ‘str’>

vm
    

Values must be of type <class ‘int’>

_class _openpyxl.workbook.external_link.external.ExternalDefinedName(_name =None_, _refersTo =None_, _sheetId =None_)[[source]](../_modules/openpyxl/workbook/external_link/external.html#ExternalDefinedName)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

name
    

Values must be of type <class ‘str’>

refersTo
    

Values must be of type <class ‘str’>

sheetId
    

Values must be of type <class ‘int’>

tagname _ = 'definedName'_
    

_class _openpyxl.workbook.external_link.external.ExternalLink(_externalBook =None_, _ddeLink =None_, _oleLink =None_, _extLst =None_)[[source]](../_modules/openpyxl/workbook/external_link/external.html#ExternalLink)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

externalBook
    

Values must be of type <class ‘openpyxl.workbook.external_link.external.ExternalBook’>

file_link
    

Values must be of type <class ‘openpyxl.packaging.relationship.Relationship’>

mime_type _ = 'application/vnd.openxmlformats-officedocument.spreadsheetml.externalLink+xml'_
    

_property _path
    

tagname _ = 'externalLink'_
    

to_tree()[[source]](../_modules/openpyxl/workbook/external_link/external.html#ExternalLink.to_tree)
    

_class _openpyxl.workbook.external_link.external.ExternalRow(_r =()_, _cell =None_)[[source]](../_modules/openpyxl/workbook/external_link/external.html#ExternalRow)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

cell
    

A sequence (list or tuple) that may only contain objects of the declared type

r
    

Values must be of type <class ‘int’>

_class _openpyxl.workbook.external_link.external.ExternalSheetData(_sheetId =None_, _refreshError =None_, _row =()_)[[source]](../_modules/openpyxl/workbook/external_link/external.html#ExternalSheetData)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

refreshError
    

Values must be of type <class ‘bool’>

row
    

A sequence (list or tuple) that may only contain objects of the declared type

sheetId
    

Values must be of type <class ‘int’>

_class _openpyxl.workbook.external_link.external.ExternalSheetDataSet(_sheetData =None_)[[source]](../_modules/openpyxl/workbook/external_link/external.html#ExternalSheetDataSet)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

sheetData
    

A sequence (list or tuple) that may only contain objects of the declared type

_class _openpyxl.workbook.external_link.external.ExternalSheetNames(_sheetName =()_)[[source]](../_modules/openpyxl/workbook/external_link/external.html#ExternalSheetNames)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

sheetName
    

A sequence of primitive types that are stored as a single attribute. “val” is the default attribute

openpyxl.workbook.external_link.external.read_external_link(_archive_ , _book_path_)[[source]](../_modules/openpyxl/workbook/external_link/external.html#read_external_link)
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.workbook.external_link.external module
    * `ExternalBook`
      * `ExternalBook.definedNames`
      * `ExternalBook.id`
      * `ExternalBook.sheetDataSet`
      * `ExternalBook.sheetNames`
      * `ExternalBook.tagname`
    * `ExternalCell`
      * `ExternalCell.r`
      * `ExternalCell.t`
      * `ExternalCell.v`
      * `ExternalCell.vm`
    * `ExternalDefinedName`
      * `ExternalDefinedName.name`
      * `ExternalDefinedName.refersTo`
      * `ExternalDefinedName.sheetId`
      * `ExternalDefinedName.tagname`
    * `ExternalLink`
      * `ExternalLink.externalBook`
      * `ExternalLink.file_link`
      * `ExternalLink.mime_type`
      * `ExternalLink.path`
      * `ExternalLink.tagname`
      * `ExternalLink.to_tree()`
    * `ExternalRow`
      * `ExternalRow.cell`
      * `ExternalRow.r`
    * `ExternalSheetData`
      * `ExternalSheetData.refreshError`
      * `ExternalSheetData.row`
      * `ExternalSheetData.sheetId`
    * `ExternalSheetDataSet`
      * `ExternalSheetDataSet.sheetData`
    * `ExternalSheetNames`
      * `ExternalSheetNames.sheetName`
    * `read_external_link()`



#### Previous topic

[openpyxl.workbook.external_link package](openpyxl.workbook.external_link.html "previous chapter")

#### Next topic

[openpyxl.workbook.child module](openpyxl.workbook.child.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.workbook.external_link.external.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.workbook.child.html "openpyxl.workbook.child module") |
  * [previous](openpyxl.workbook.external_link.html "openpyxl.workbook.external_link package") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.workbook package](openpyxl.workbook.html) »
  * [openpyxl.workbook.external_link package](openpyxl.workbook.external_link.html) »
  * [openpyxl.workbook.external_link.external module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
