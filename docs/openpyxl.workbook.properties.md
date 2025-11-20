### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.workbook.protection.html "openpyxl.workbook.protection module") |
  * [previous](openpyxl.workbook.function_group.html "openpyxl.workbook.function_group module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.workbook package](openpyxl.workbook.html) »
  * [openpyxl.workbook.properties module]()



# openpyxl.workbook.properties module

_class _openpyxl.workbook.properties.CalcProperties(_calcId =124519_, _calcMode =None_, _fullCalcOnLoad =True_, _refMode =None_, _iterate =None_, _iterateCount =None_, _iterateDelta =None_, _fullPrecision =None_, _calcCompleted =None_, _calcOnSave =None_, _concurrentCalc =None_, _concurrentManualCount =None_, _forceFullCalc =None_)[[source]](../_modules/openpyxl/workbook/properties.html#CalcProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

calcCompleted
    

Values must be of type <class ‘bool’>

calcId
    

Values must be of type <class ‘int’>

calcMode
    

Value must be one of {‘manual’, ‘autoNoTable’, ‘auto’}

calcOnSave
    

Values must be of type <class ‘bool’>

concurrentCalc
    

Values must be of type <class ‘bool’>

concurrentManualCount
    

Values must be of type <class ‘int’>

forceFullCalc
    

Values must be of type <class ‘bool’>

fullCalcOnLoad
    

Values must be of type <class ‘bool’>

fullPrecision
    

Values must be of type <class ‘bool’>

iterate
    

Values must be of type <class ‘bool’>

iterateCount
    

Values must be of type <class ‘int’>

iterateDelta
    

Values must be of type <class ‘float’>

refMode
    

Value must be one of {‘R1C1’, ‘A1’}

tagname _ = 'calcPr'_
    

_class _openpyxl.workbook.properties.FileVersion(_appName =None_, _lastEdited =None_, _lowestEdited =None_, _rupBuild =None_, _codeName =None_)[[source]](../_modules/openpyxl/workbook/properties.html#FileVersion)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

appName
    

Values must be of type <class ‘str’>

codeName
    

lastEdited
    

Values must be of type <class ‘str’>

lowestEdited
    

Values must be of type <class ‘str’>

rupBuild
    

Values must be of type <class ‘str’>

tagname _ = 'fileVersion'_
    

_class _openpyxl.workbook.properties.WorkbookProperties(_date1904 =None_, _dateCompatibility =None_, _showObjects =None_, _showBorderUnselectedTables =None_, _filterPrivacy =None_, _promptedSolutions =None_, _showInkAnnotation =None_, _backupFile =None_, _saveExternalLinkValues =None_, _updateLinks =None_, _codeName =None_, _hidePivotFieldList =None_, _showPivotChartFilter =None_, _allowRefreshQuery =None_, _publishItems =None_, _checkCompatibility =None_, _autoCompressPictures =None_, _refreshAllConnections =None_, _defaultThemeVersion =None_)[[source]](../_modules/openpyxl/workbook/properties.html#WorkbookProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

allowRefreshQuery
    

Values must be of type <class ‘bool’>

autoCompressPictures
    

Values must be of type <class ‘bool’>

backupFile
    

Values must be of type <class ‘bool’>

checkCompatibility
    

Values must be of type <class ‘bool’>

codeName
    

Values must be of type <class ‘str’>

date1904
    

Values must be of type <class ‘bool’>

dateCompatibility
    

Values must be of type <class ‘bool’>

defaultThemeVersion
    

Values must be of type <class ‘int’>

filterPrivacy
    

Values must be of type <class ‘bool’>

hidePivotFieldList
    

Values must be of type <class ‘bool’>

promptedSolutions
    

Values must be of type <class ‘bool’>

publishItems
    

Values must be of type <class ‘bool’>

refreshAllConnections
    

Values must be of type <class ‘bool’>

saveExternalLinkValues
    

Values must be of type <class ‘bool’>

showBorderUnselectedTables
    

Values must be of type <class ‘bool’>

showInkAnnotation
    

Values must be of type <class ‘bool’>

showObjects
    

Value must be one of {‘placeholders’, ‘all’}

showPivotChartFilter
    

Values must be of type <class ‘bool’>

tagname _ = 'workbookPr'_
    

updateLinks
    

Value must be one of {‘never’, ‘userSet’, ‘always’}

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.workbook.properties module
    * `CalcProperties`
      * `CalcProperties.calcCompleted`
      * `CalcProperties.calcId`
      * `CalcProperties.calcMode`
      * `CalcProperties.calcOnSave`
      * `CalcProperties.concurrentCalc`
      * `CalcProperties.concurrentManualCount`
      * `CalcProperties.forceFullCalc`
      * `CalcProperties.fullCalcOnLoad`
      * `CalcProperties.fullPrecision`
      * `CalcProperties.iterate`
      * `CalcProperties.iterateCount`
      * `CalcProperties.iterateDelta`
      * `CalcProperties.refMode`
      * `CalcProperties.tagname`
    * `FileVersion`
      * `FileVersion.appName`
      * `FileVersion.codeName`
      * `FileVersion.lastEdited`
      * `FileVersion.lowestEdited`
      * `FileVersion.rupBuild`
      * `FileVersion.tagname`
    * `WorkbookProperties`
      * `WorkbookProperties.allowRefreshQuery`
      * `WorkbookProperties.autoCompressPictures`
      * `WorkbookProperties.backupFile`
      * `WorkbookProperties.checkCompatibility`
      * `WorkbookProperties.codeName`
      * `WorkbookProperties.date1904`
      * `WorkbookProperties.dateCompatibility`
      * `WorkbookProperties.defaultThemeVersion`
      * `WorkbookProperties.filterPrivacy`
      * `WorkbookProperties.hidePivotFieldList`
      * `WorkbookProperties.promptedSolutions`
      * `WorkbookProperties.publishItems`
      * `WorkbookProperties.refreshAllConnections`
      * `WorkbookProperties.saveExternalLinkValues`
      * `WorkbookProperties.showBorderUnselectedTables`
      * `WorkbookProperties.showInkAnnotation`
      * `WorkbookProperties.showObjects`
      * `WorkbookProperties.showPivotChartFilter`
      * `WorkbookProperties.tagname`
      * `WorkbookProperties.updateLinks`



#### Previous topic

[openpyxl.workbook.function_group module](openpyxl.workbook.function_group.html "previous chapter")

#### Next topic

[openpyxl.workbook.protection module](openpyxl.workbook.protection.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.workbook.properties.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.workbook.protection.html "openpyxl.workbook.protection module") |
  * [previous](openpyxl.workbook.function_group.html "openpyxl.workbook.function_group module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.workbook package](openpyxl.workbook.html) »
  * [openpyxl.workbook.properties module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
