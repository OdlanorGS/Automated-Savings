### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.workbook.smart_tags.html "openpyxl.workbook.smart_tags module") |
  * [previous](openpyxl.workbook.properties.html "openpyxl.workbook.properties module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.workbook package](openpyxl.workbook.html) »
  * [openpyxl.workbook.protection module]()



# openpyxl.workbook.protection module

openpyxl.workbook.protection.DocumentSecurity
    

alias of `WorkbookProtection`

_class _openpyxl.workbook.protection.FileSharing(_readOnlyRecommended =None_, _userName =None_, _reservationPassword =None_, _algorithmName =None_, _hashValue =None_, _saltValue =None_, _spinCount =None_)[[source]](../_modules/openpyxl/workbook/protection.html#FileSharing)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

algorithmName
    

Values must be of type <class ‘str’>

hashValue
    

readOnlyRecommended
    

Values must be of type <class ‘bool’>

reservationPassword
    

saltValue
    

spinCount
    

Values must be of type <class ‘int’>

tagname _ = 'fileSharing'_
    

userName
    

Values must be of type <class ‘str’>

_class _openpyxl.workbook.protection.WorkbookProtection(_workbookPassword =None_, _workbookPasswordCharacterSet =None_, _revisionsPassword =None_, _revisionsPasswordCharacterSet =None_, _lockStructure =None_, _lockWindows =None_, _lockRevision =None_, _revisionsAlgorithmName =None_, _revisionsHashValue =None_, _revisionsSaltValue =None_, _revisionsSpinCount =None_, _workbookAlgorithmName =None_, _workbookHashValue =None_, _workbookSaltValue =None_, _workbookSpinCount =None_)[[source]](../_modules/openpyxl/workbook/protection.html#WorkbookProtection)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

_classmethod _from_tree(_node_)[[source]](../_modules/openpyxl/workbook/protection.html#WorkbookProtection.from_tree)
    

Don’t hash passwords when deserialising from XML

lockRevision
    

Values must be of type <class ‘bool’>

lockStructure
    

Values must be of type <class ‘bool’>

lockWindows
    

Values must be of type <class ‘bool’>

lock_revision
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

lock_structure
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

lock_windows
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

revision_password
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

revisionsAlgorithmName
    

Values must be of type <class ‘str’>

revisionsHashValue
    

_property _revisionsPassword
    

Return the revisions password value, regardless of hash.

revisionsPasswordCharacterSet
    

Values must be of type <class ‘str’>

revisionsSaltValue
    

revisionsSpinCount
    

Values must be of type <class ‘int’>

set_revisions_password(_value =''_, _already_hashed =False_)[[source]](../_modules/openpyxl/workbook/protection.html#WorkbookProtection.set_revisions_password)
    

Set a revision password on this workbook.

set_workbook_password(_value =''_, _already_hashed =False_)[[source]](../_modules/openpyxl/workbook/protection.html#WorkbookProtection.set_workbook_password)
    

Set a password on this workbook.

tagname _ = 'workbookPr'_
    

workbookAlgorithmName
    

Values must be of type <class ‘str’>

workbookHashValue
    

_property _workbookPassword
    

Return the workbook password value, regardless of hash.

workbookPasswordCharacterSet
    

Values must be of type <class ‘str’>

workbookSaltValue
    

workbookSpinCount
    

Values must be of type <class ‘int’>

workbook_password
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.workbook.protection module
    * `DocumentSecurity`
    * `FileSharing`
      * `FileSharing.algorithmName`
      * `FileSharing.hashValue`
      * `FileSharing.readOnlyRecommended`
      * `FileSharing.reservationPassword`
      * `FileSharing.saltValue`
      * `FileSharing.spinCount`
      * `FileSharing.tagname`
      * `FileSharing.userName`
    * `WorkbookProtection`
      * `WorkbookProtection.from_tree()`
      * `WorkbookProtection.lockRevision`
      * `WorkbookProtection.lockStructure`
      * `WorkbookProtection.lockWindows`
      * `WorkbookProtection.lock_revision`
      * `WorkbookProtection.lock_structure`
      * `WorkbookProtection.lock_windows`
      * `WorkbookProtection.revision_password`
      * `WorkbookProtection.revisionsAlgorithmName`
      * `WorkbookProtection.revisionsHashValue`
      * `WorkbookProtection.revisionsPassword`
      * `WorkbookProtection.revisionsPasswordCharacterSet`
      * `WorkbookProtection.revisionsSaltValue`
      * `WorkbookProtection.revisionsSpinCount`
      * `WorkbookProtection.set_revisions_password()`
      * `WorkbookProtection.set_workbook_password()`
      * `WorkbookProtection.tagname`
      * `WorkbookProtection.workbookAlgorithmName`
      * `WorkbookProtection.workbookHashValue`
      * `WorkbookProtection.workbookPassword`
      * `WorkbookProtection.workbookPasswordCharacterSet`
      * `WorkbookProtection.workbookSaltValue`
      * `WorkbookProtection.workbookSpinCount`
      * `WorkbookProtection.workbook_password`



#### Previous topic

[openpyxl.workbook.properties module](openpyxl.workbook.properties.html "previous chapter")

#### Next topic

[openpyxl.workbook.smart_tags module](openpyxl.workbook.smart_tags.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.workbook.protection.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.workbook.smart_tags.html "openpyxl.workbook.smart_tags module") |
  * [previous](openpyxl.workbook.properties.html "openpyxl.workbook.properties module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.workbook package](openpyxl.workbook.html) »
  * [openpyxl.workbook.protection module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
