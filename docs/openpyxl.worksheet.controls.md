### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.copier.html "openpyxl.worksheet.copier module") |
  * [previous](openpyxl.worksheet.cell_watch.html "openpyxl.worksheet.cell_watch module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.controls module]()



# openpyxl.worksheet.controls module

_class _openpyxl.worksheet.controls.Control(_controlPr =None_, _shapeId =None_, _name =None_)[[source]](../_modules/openpyxl/worksheet/controls.html#Control)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

controlPr
    

Values must be of type <class ‘openpyxl.worksheet.controls.ControlProperty’>

name
    

Values must be of type <class ‘str’>

shapeId
    

Values must be of type <class ‘int’>

tagname _ = 'control'_
    

_class _openpyxl.worksheet.controls.ControlProperty(_anchor =None_, _locked =True_, _defaultSize =True_, __print =True_, _disabled =False_, _recalcAlways =False_, _uiObject =False_, _autoFill =True_, _autoLine =True_, _autoPict =True_, _macro =None_, _altText =None_, _linkedCell =None_, _listFillRange =None_, _cf ='pict'_, _id =None_)[[source]](../_modules/openpyxl/worksheet/controls.html#ControlProperty)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

altText
    

Values must be of type <class ‘str’>

anchor
    

Values must be of type <class ‘openpyxl.worksheet.ole.ObjectAnchor’>

autoFill
    

Values must be of type <class ‘bool’>

autoLine
    

Values must be of type <class ‘bool’>

autoPict
    

Values must be of type <class ‘bool’>

cf
    

Values must be of type <class ‘str’>

defaultSize
    

Values must be of type <class ‘bool’>

disabled
    

Values must be of type <class ‘bool’>

id
    

Values must be of type <class ‘str’>

linkedCell
    

Values must be of type <class ‘str’>

listFillRange
    

Values must be of type <class ‘str’>

locked
    

Values must be of type <class ‘bool’>

macro
    

Values must be of type <class ‘str’>

recalcAlways
    

Values must be of type <class ‘bool’>

tagname _ = 'controlPr'_
    

uiObject
    

Values must be of type <class ‘bool’>

_class _openpyxl.worksheet.controls.Controls(_control =()_)[[source]](../_modules/openpyxl/worksheet/controls.html#Controls)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

control
    

A sequence (list or tuple) that may only contain objects of the declared type

tagname _ = 'controls'_
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.worksheet.controls module
    * `Control`
      * `Control.controlPr`
      * `Control.name`
      * `Control.shapeId`
      * `Control.tagname`
    * `ControlProperty`
      * `ControlProperty.altText`
      * `ControlProperty.anchor`
      * `ControlProperty.autoFill`
      * `ControlProperty.autoLine`
      * `ControlProperty.autoPict`
      * `ControlProperty.cf`
      * `ControlProperty.defaultSize`
      * `ControlProperty.disabled`
      * `ControlProperty.id`
      * `ControlProperty.linkedCell`
      * `ControlProperty.listFillRange`
      * `ControlProperty.locked`
      * `ControlProperty.macro`
      * `ControlProperty.recalcAlways`
      * `ControlProperty.tagname`
      * `ControlProperty.uiObject`
    * `Controls`
      * `Controls.control`
      * `Controls.tagname`



#### Previous topic

[openpyxl.worksheet.cell_watch module](openpyxl.worksheet.cell_watch.html "previous chapter")

#### Next topic

[openpyxl.worksheet.copier module](openpyxl.worksheet.copier.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.worksheet.controls.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.copier.html "openpyxl.worksheet.copier module") |
  * [previous](openpyxl.worksheet.cell_watch.html "openpyxl.worksheet.cell_watch module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.controls module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
