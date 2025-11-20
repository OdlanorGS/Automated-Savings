### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.pivot.html "openpyxl.pivot package") |
  * [previous](openpyxl.packaging.relationship.html "openpyxl.packaging.relationship module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.packaging package](openpyxl.packaging.html) »
  * [openpyxl.packaging.workbook module]()



# openpyxl.packaging.workbook module

_class _openpyxl.packaging.workbook.ChildSheet(_name =None_, _sheetId =None_, _state ='visible'_, _id =None_)[[source]](../_modules/openpyxl/packaging/workbook.html#ChildSheet)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

Represents a reference to a worksheet or chartsheet in workbook.xml

It contains the title, order and state but only an indirect reference to the objects themselves.

id
    

Values must be of type <class ‘str’>

name
    

Values must be of type <class ‘str’>

sheetId
    

Values must be of type <class ‘int’>

state
    

Value must be one of {‘veryHidden’, ‘hidden’, ‘visible’}

tagname _ = 'sheet'_
    

_class _openpyxl.packaging.workbook.FileRecoveryProperties(_autoRecover =None_, _crashSave =None_, _dataExtractLoad =None_, _repairLoad =None_)[[source]](../_modules/openpyxl/packaging/workbook.html#FileRecoveryProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

autoRecover
    

Values must be of type <class ‘bool’>

crashSave
    

Values must be of type <class ‘bool’>

dataExtractLoad
    

Values must be of type <class ‘bool’>

repairLoad
    

Values must be of type <class ‘bool’>

tagname _ = 'fileRecoveryPr'_
    

_class _openpyxl.packaging.workbook.PivotCache(_cacheId =None_, _id =None_)[[source]](../_modules/openpyxl/packaging/workbook.html#PivotCache)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

cacheId
    

Values must be of type <class ‘int’>

id
    

Values must be of type <class ‘str’>

tagname _ = 'pivotCache'_
    

_class _openpyxl.packaging.workbook.WorkbookPackage(_conformance =None_, _fileVersion =None_, _fileSharing =None_, _workbookPr =None_, _workbookProtection =None_, _bookViews =()_, _sheets =()_, _functionGroups =None_, _externalReferences =()_, _definedNames =None_, _calcPr =None_, _oleSize =None_, _customWorkbookViews =()_, _pivotCaches =()_, _smartTagPr =None_, _smartTagTypes =None_, _webPublishing =None_, _fileRecoveryPr =None_, _webPublishObjects =None_, _extLst =None_, _Ignorable =None_)[[source]](../_modules/openpyxl/packaging/workbook.html#WorkbookPackage)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

Represent the workbook file in the archive

Ignorable
    

Values must be of type <class ‘str’>

_property _active
    

bookViews
    

Wrap a sequence in an containing object

calcPr
    

Values must be of type <class ‘openpyxl.workbook.properties.CalcProperties’>

conformance
    

Value must be one of {‘strict’, ‘transitional’}

customWorkbookViews
    

Wrap a sequence in an containing object

definedNames
    

Values must be of type <class ‘openpyxl.workbook.defined_name.DefinedNameList’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

externalReferences
    

Wrap a sequence in an containing object

fileRecoveryPr
    

Values must be of type <class ‘openpyxl.packaging.workbook.FileRecoveryProperties’>

fileSharing
    

Values must be of type <class ‘openpyxl.workbook.protection.FileSharing’>

fileVersion
    

Values must be of type <class ‘openpyxl.workbook.properties.FileVersion’>

functionGroups
    

Values must be of type <class ‘openpyxl.workbook.function_group.FunctionGroupList’>

oleSize
    

Values must be of type <class ‘str’>

pivotCaches
    

Wrap a sequence in an containing object

properties
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

sheets
    

Wrap a sequence in an containing object

smartTagPr
    

Values must be of type <class ‘openpyxl.workbook.smart_tags.SmartTagProperties’>

smartTagTypes
    

Values must be of type <class ‘openpyxl.workbook.smart_tags.SmartTagList’>

tagname _ = 'workbook'_
    

to_tree()[[source]](../_modules/openpyxl/packaging/workbook.html#WorkbookPackage.to_tree)
    

webPublishObjects
    

Values must be of type <class ‘openpyxl.workbook.web.WebPublishObjectList’>

webPublishing
    

Values must be of type <class ‘openpyxl.workbook.web.WebPublishing’>

workbookPr
    

Values must be of type <class ‘openpyxl.workbook.properties.WorkbookProperties’>

workbookProtection
    

Values must be of type <class ‘openpyxl.workbook.protection.WorkbookProtection’>

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.packaging.workbook module
    * `ChildSheet`
      * `ChildSheet.id`
      * `ChildSheet.name`
      * `ChildSheet.sheetId`
      * `ChildSheet.state`
      * `ChildSheet.tagname`
    * `FileRecoveryProperties`
      * `FileRecoveryProperties.autoRecover`
      * `FileRecoveryProperties.crashSave`
      * `FileRecoveryProperties.dataExtractLoad`
      * `FileRecoveryProperties.repairLoad`
      * `FileRecoveryProperties.tagname`
    * `PivotCache`
      * `PivotCache.cacheId`
      * `PivotCache.id`
      * `PivotCache.tagname`
    * `WorkbookPackage`
      * `WorkbookPackage.Ignorable`
      * `WorkbookPackage.active`
      * `WorkbookPackage.bookViews`
      * `WorkbookPackage.calcPr`
      * `WorkbookPackage.conformance`
      * `WorkbookPackage.customWorkbookViews`
      * `WorkbookPackage.definedNames`
      * `WorkbookPackage.extLst`
      * `WorkbookPackage.externalReferences`
      * `WorkbookPackage.fileRecoveryPr`
      * `WorkbookPackage.fileSharing`
      * `WorkbookPackage.fileVersion`
      * `WorkbookPackage.functionGroups`
      * `WorkbookPackage.oleSize`
      * `WorkbookPackage.pivotCaches`
      * `WorkbookPackage.properties`
      * `WorkbookPackage.sheets`
      * `WorkbookPackage.smartTagPr`
      * `WorkbookPackage.smartTagTypes`
      * `WorkbookPackage.tagname`
      * `WorkbookPackage.to_tree()`
      * `WorkbookPackage.webPublishObjects`
      * `WorkbookPackage.webPublishing`
      * `WorkbookPackage.workbookPr`
      * `WorkbookPackage.workbookProtection`



#### Previous topic

[openpyxl.packaging.relationship module](openpyxl.packaging.relationship.html "previous chapter")

#### Next topic

[openpyxl.pivot package](openpyxl.pivot.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.packaging.workbook.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.pivot.html "openpyxl.pivot package") |
  * [previous](openpyxl.packaging.relationship.html "openpyxl.packaging.relationship module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.packaging package](openpyxl.packaging.html) »
  * [openpyxl.packaging.workbook module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
