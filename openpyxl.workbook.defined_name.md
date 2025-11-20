### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.workbook.external_reference.html "openpyxl.workbook.external_reference module") |
  * [previous](openpyxl.workbook.child.html "openpyxl.workbook.child module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.workbook package](openpyxl.workbook.html) »
  * [openpyxl.workbook.defined_name module]()



# openpyxl.workbook.defined_name module

_class _openpyxl.workbook.defined_name.DefinedName(_name =None_, _comment =None_, _customMenu =None_, _description =None_, _help =None_, _statusBar =None_, _localSheetId =None_, _hidden =None_, _function =None_, _vbProcedure =None_, _xlm =None_, _functionGroupId =None_, _shortcutKey =None_, _publishToServer =None_, _workbookParameter =None_, _attr_text =None_)[[source]](../_modules/openpyxl/workbook/defined_name.html#DefinedName)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

attr_text
    

comment
    

Values must be of type <class ‘str’>

customMenu
    

Values must be of type <class ‘str’>

description
    

Values must be of type <class ‘str’>

_property _destinations
    

function
    

Values must be of type <class ‘bool’>

functionGroupId
    

Values must be of type <class ‘int’>

help
    

Values must be of type <class ‘str’>

hidden
    

Values must be of type <class ‘bool’>

_property _is_external
    

_property _is_reserved
    

localSheetId
    

Values must be of type <class ‘int’>

name
    

Values must be of type <class ‘str’>

publishToServer
    

Values must be of type <class ‘bool’>

shortcutKey
    

Values must be of type <class ‘str’>

statusBar
    

Values must be of type <class ‘str’>

tagname _ = 'definedName'_
    

_property _type
    

value
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

vbProcedure
    

Values must be of type <class ‘bool’>

workbookParameter
    

Values must be of type <class ‘bool’>

xlm
    

Values must be of type <class ‘bool’>

_class _openpyxl.workbook.defined_name.DefinedNameDict[[source]](../_modules/openpyxl/workbook/defined_name.html#DefinedNameDict)
    

Bases: `dict`

Utility class for storing defined names. Allows access by name and separation of global and scoped names

add(_value_)[[source]](../_modules/openpyxl/workbook/defined_name.html#DefinedNameDict.add)
    

Add names without worrying about key and name matching.

_class _openpyxl.workbook.defined_name.DefinedNameList(_definedName =()_)[[source]](../_modules/openpyxl/workbook/defined_name.html#DefinedNameList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

by_sheet()[[source]](../_modules/openpyxl/workbook/defined_name.html#DefinedNameList.by_sheet)
    

Break names down into sheet locals and globals

definedName
    

A sequence (list or tuple) that may only contain objects of the declared type

tagname _ = 'definedNames'_
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.workbook.defined_name module
    * `DefinedName`
      * `DefinedName.attr_text`
      * `DefinedName.comment`
      * `DefinedName.customMenu`
      * `DefinedName.description`
      * `DefinedName.destinations`
      * `DefinedName.function`
      * `DefinedName.functionGroupId`
      * `DefinedName.help`
      * `DefinedName.hidden`
      * `DefinedName.is_external`
      * `DefinedName.is_reserved`
      * `DefinedName.localSheetId`
      * `DefinedName.name`
      * `DefinedName.publishToServer`
      * `DefinedName.shortcutKey`
      * `DefinedName.statusBar`
      * `DefinedName.tagname`
      * `DefinedName.type`
      * `DefinedName.value`
      * `DefinedName.vbProcedure`
      * `DefinedName.workbookParameter`
      * `DefinedName.xlm`
    * `DefinedNameDict`
      * `DefinedNameDict.add()`
    * `DefinedNameList`
      * `DefinedNameList.by_sheet()`
      * `DefinedNameList.definedName`
      * `DefinedNameList.tagname`



#### Previous topic

[openpyxl.workbook.child module](openpyxl.workbook.child.html "previous chapter")

#### Next topic

[openpyxl.workbook.external_reference module](openpyxl.workbook.external_reference.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.workbook.defined_name.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.workbook.external_reference.html "openpyxl.workbook.external_reference module") |
  * [previous](openpyxl.workbook.child.html "openpyxl.workbook.child module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.workbook package](openpyxl.workbook.html) »
  * [openpyxl.workbook.defined_name module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
