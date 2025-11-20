### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.filters.html "openpyxl.worksheet.filters module") |
  * [previous](openpyxl.worksheet.drawing.html "openpyxl.worksheet.drawing module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.errors module]()



# openpyxl.worksheet.errors module

_class _openpyxl.worksheet.errors.Extension(_uri =None_)[[source]](../_modules/openpyxl/worksheet/errors.html#Extension)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

tagname _ = 'extension'_
    

uri
    

Values must be of type <class ‘str’>

_class _openpyxl.worksheet.errors.ExtensionList(_ext =()_)[[source]](../_modules/openpyxl/worksheet/errors.html#ExtensionList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

ext
    

A sequence (list or tuple) that may only contain objects of the declared type

tagname _ = 'extensionList'_
    

_class _openpyxl.worksheet.errors.IgnoredError(_sqref =None_, _evalError =False_, _twoDigitTextYear =False_, _numberStoredAsText =False_, _formula =False_, _formulaRange =False_, _unlockedFormula =False_, _emptyCellReference =False_, _listDataValidation =False_, _calculatedColumn =False_)[[source]](../_modules/openpyxl/worksheet/errors.html#IgnoredError)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

calculatedColumn
    

Values must be of type <class ‘bool’>

emptyCellReference
    

Values must be of type <class ‘bool’>

evalError
    

Values must be of type <class ‘bool’>

formula
    

Values must be of type <class ‘bool’>

formulaRange
    

Values must be of type <class ‘bool’>

listDataValidation
    

Values must be of type <class ‘bool’>

numberStoredAsText
    

Values must be of type <class ‘bool’>

sqref
    

alias of [`CellRange`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.CellRange "openpyxl.descriptors.excel.CellRange")

tagname _ = 'ignoredError'_
    

twoDigitTextYear
    

Values must be of type <class ‘bool’>

unlockedFormula
    

Values must be of type <class ‘bool’>

_class _openpyxl.worksheet.errors.IgnoredErrors(_ignoredError =()_, _extLst =None_)[[source]](../_modules/openpyxl/worksheet/errors.html#IgnoredErrors)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

extLst
    

Values must be of type <class ‘openpyxl.worksheet.errors.ExtensionList’>

ignoredError
    

A sequence (list or tuple) that may only contain objects of the declared type

tagname _ = 'ignoredErrors'_
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.worksheet.errors module
    * `Extension`
      * `Extension.tagname`
      * `Extension.uri`
    * `ExtensionList`
      * `ExtensionList.ext`
      * `ExtensionList.tagname`
    * `IgnoredError`
      * `IgnoredError.calculatedColumn`
      * `IgnoredError.emptyCellReference`
      * `IgnoredError.evalError`
      * `IgnoredError.formula`
      * `IgnoredError.formulaRange`
      * `IgnoredError.listDataValidation`
      * `IgnoredError.numberStoredAsText`
      * `IgnoredError.sqref`
      * `IgnoredError.tagname`
      * `IgnoredError.twoDigitTextYear`
      * `IgnoredError.unlockedFormula`
    * `IgnoredErrors`
      * `IgnoredErrors.extLst`
      * `IgnoredErrors.ignoredError`
      * `IgnoredErrors.tagname`



#### Previous topic

[openpyxl.worksheet.drawing module](openpyxl.worksheet.drawing.html "previous chapter")

#### Next topic

[openpyxl.worksheet.filters module](openpyxl.worksheet.filters.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.worksheet.errors.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.filters.html "openpyxl.worksheet.filters module") |
  * [previous](openpyxl.worksheet.drawing.html "openpyxl.worksheet.drawing module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.errors module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
