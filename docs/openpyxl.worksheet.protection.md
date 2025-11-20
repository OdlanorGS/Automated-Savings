### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.related.html "openpyxl.worksheet.related module") |
  * [previous](openpyxl.worksheet.properties.html "openpyxl.worksheet.properties module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.protection module]()



# openpyxl.worksheet.protection module

_class _openpyxl.worksheet.protection.SheetProtection(_sheet =False_, _objects =False_, _scenarios =False_, _formatCells =True_, _formatRows =True_, _formatColumns =True_, _insertColumns =True_, _insertRows =True_, _insertHyperlinks =True_, _deleteColumns =True_, _deleteRows =True_, _selectLockedCells =False_, _selectUnlockedCells =False_, _sort =True_, _autoFilter =True_, _pivotTables =True_, _password =None_, _algorithmName =None_, _saltValue =None_, _spinCount =None_, _hashValue =None_)[[source]](../_modules/openpyxl/worksheet/protection.html#SheetProtection)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable"), `_Protected`

Information about protection of various aspects of a sheet. True values mean that protection for the object or action is active This is the **default** when protection is active, ie. users cannot do something

algorithmName
    

Values must be of type <class ‘str’>

autoFilter
    

Values must be of type <class ‘bool’>

deleteColumns
    

Values must be of type <class ‘bool’>

deleteRows
    

Values must be of type <class ‘bool’>

disable()[[source]](../_modules/openpyxl/worksheet/protection.html#SheetProtection.disable)
    

enable()[[source]](../_modules/openpyxl/worksheet/protection.html#SheetProtection.enable)
    

enabled
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

formatCells
    

Values must be of type <class ‘bool’>

formatColumns
    

Values must be of type <class ‘bool’>

formatRows
    

Values must be of type <class ‘bool’>

hashValue
    

insertColumns
    

Values must be of type <class ‘bool’>

insertHyperlinks
    

Values must be of type <class ‘bool’>

insertRows
    

Values must be of type <class ‘bool’>

objects
    

Values must be of type <class ‘bool’>

pivotTables
    

Values must be of type <class ‘bool’>

saltValue
    

scenarios
    

Values must be of type <class ‘bool’>

selectLockedCells
    

Values must be of type <class ‘bool’>

selectUnlockedCells
    

Values must be of type <class ‘bool’>

set_password(_value =''_, _already_hashed =False_)[[source]](../_modules/openpyxl/worksheet/protection.html#SheetProtection.set_password)
    

Set a password on this sheet.

sheet
    

Values must be of type <class ‘bool’>

sort
    

Values must be of type <class ‘bool’>

spinCount
    

Values must be of type <class ‘int’>

tagname _ = 'sheetProtection'_
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.worksheet.protection module
    * `SheetProtection`
      * `SheetProtection.algorithmName`
      * `SheetProtection.autoFilter`
      * `SheetProtection.deleteColumns`
      * `SheetProtection.deleteRows`
      * `SheetProtection.disable()`
      * `SheetProtection.enable()`
      * `SheetProtection.enabled`
      * `SheetProtection.formatCells`
      * `SheetProtection.formatColumns`
      * `SheetProtection.formatRows`
      * `SheetProtection.hashValue`
      * `SheetProtection.insertColumns`
      * `SheetProtection.insertHyperlinks`
      * `SheetProtection.insertRows`
      * `SheetProtection.objects`
      * `SheetProtection.pivotTables`
      * `SheetProtection.saltValue`
      * `SheetProtection.scenarios`
      * `SheetProtection.selectLockedCells`
      * `SheetProtection.selectUnlockedCells`
      * `SheetProtection.set_password()`
      * `SheetProtection.sheet`
      * `SheetProtection.sort`
      * `SheetProtection.spinCount`
      * `SheetProtection.tagname`



#### Previous topic

[openpyxl.worksheet.properties module](openpyxl.worksheet.properties.html "previous chapter")

#### Next topic

[openpyxl.worksheet.related module](openpyxl.worksheet.related.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.worksheet.protection.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.related.html "openpyxl.worksheet.related module") |
  * [previous](openpyxl.worksheet.properties.html "openpyxl.worksheet.properties module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.protection module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
