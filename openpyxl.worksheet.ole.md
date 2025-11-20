### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.page.html "openpyxl.worksheet.page module") |
  * [previous](openpyxl.worksheet.merge.html "openpyxl.worksheet.merge module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.ole module]()



# openpyxl.worksheet.ole module

_class _openpyxl.worksheet.ole.ObjectAnchor(__from =None_, _to =None_, _moveWithCells =False_, _sizeWithCells =False_, _z_order =None_)[[source]](../_modules/openpyxl/worksheet/ole.html#ObjectAnchor)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

moveWithCells
    

Values must be of type <class ‘bool’>

sizeWithCells
    

Values must be of type <class ‘bool’>

tagname _ = 'anchor'_
    

to
    

Values must be of type <class ‘openpyxl.drawing.spreadsheet_drawing.AnchorMarker’>

z_order
    

Values must be of type <class ‘int’>

_class _openpyxl.worksheet.ole.ObjectPr(_anchor =None_, _locked =True_, _defaultSize =True_, __print =True_, _disabled =False_, _uiObject =False_, _autoFill =True_, _autoLine =True_, _autoPict =True_, _macro =None_, _altText =None_, _dde =False_)[[source]](../_modules/openpyxl/worksheet/ole.html#ObjectPr)
    

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

dde
    

Values must be of type <class ‘bool’>

defaultSize
    

Values must be of type <class ‘bool’>

disabled
    

Values must be of type <class ‘bool’>

locked
    

Values must be of type <class ‘bool’>

macro
    

Values must be of type <class ‘str’>

tagname _ = 'objectPr'_
    

uiObject
    

Values must be of type <class ‘bool’>

_class _openpyxl.worksheet.ole.OleObject(_objectPr =None_, _progId =None_, _dvAspect ='DVASPECT_CONTENT'_, _link =None_, _oleUpdate =None_, _autoLoad =False_, _shapeId =None_)[[source]](../_modules/openpyxl/worksheet/ole.html#OleObject)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

autoLoad
    

Values must be of type <class ‘bool’>

dvAspect
    

Value must be one of {‘DVASPECT_ICON’, ‘DVASPECT_CONTENT’}

link
    

Values must be of type <class ‘str’>

objectPr
    

Values must be of type <class ‘openpyxl.worksheet.ole.ObjectPr’>

oleUpdate
    

Value must be one of {‘OLEUPDATE_ONCALL’, ‘OLEUPDATE_ALWAYS’}

progId
    

Values must be of type <class ‘str’>

shapeId
    

Values must be of type <class ‘int’>

tagname _ = 'oleObject'_
    

_class _openpyxl.worksheet.ole.OleObjects(_oleObject =()_)[[source]](../_modules/openpyxl/worksheet/ole.html#OleObjects)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

oleObject
    

A sequence (list or tuple) that may only contain objects of the declared type

tagname _ = 'oleObjects'_
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.worksheet.ole module
    * `ObjectAnchor`
      * `ObjectAnchor.moveWithCells`
      * `ObjectAnchor.sizeWithCells`
      * `ObjectAnchor.tagname`
      * `ObjectAnchor.to`
      * `ObjectAnchor.z_order`
    * `ObjectPr`
      * `ObjectPr.altText`
      * `ObjectPr.anchor`
      * `ObjectPr.autoFill`
      * `ObjectPr.autoLine`
      * `ObjectPr.autoPict`
      * `ObjectPr.dde`
      * `ObjectPr.defaultSize`
      * `ObjectPr.disabled`
      * `ObjectPr.locked`
      * `ObjectPr.macro`
      * `ObjectPr.tagname`
      * `ObjectPr.uiObject`
    * `OleObject`
      * `OleObject.autoLoad`
      * `OleObject.dvAspect`
      * `OleObject.link`
      * `OleObject.objectPr`
      * `OleObject.oleUpdate`
      * `OleObject.progId`
      * `OleObject.shapeId`
      * `OleObject.tagname`
    * `OleObjects`
      * `OleObjects.oleObject`
      * `OleObjects.tagname`



#### Previous topic

[openpyxl.worksheet.merge module](openpyxl.worksheet.merge.html "previous chapter")

#### Next topic

[openpyxl.worksheet.page module](openpyxl.worksheet.page.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.worksheet.ole.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.page.html "openpyxl.worksheet.page module") |
  * [previous](openpyxl.worksheet.merge.html "openpyxl.worksheet.merge module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.ole module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
