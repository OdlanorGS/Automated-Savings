### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.relation.html "openpyxl.drawing.relation module") |
  * [previous](openpyxl.drawing.picture.html "openpyxl.drawing.picture module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.drawing package](openpyxl.drawing.html) »
  * [openpyxl.drawing.properties module]()



# openpyxl.drawing.properties module

_class _openpyxl.drawing.properties.GroupLocking(_noGrp =None_, _noUngrp =None_, _noSelect =None_, _noRot =None_, _noChangeAspect =None_, _noChangeArrowheads =None_, _noMove =None_, _noResize =None_, _noEditPoints =None_, _noAdjustHandles =None_, _noChangeShapeType =None_, _extLst =None_)[[source]](../_modules/openpyxl/drawing/properties.html#GroupLocking)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

noAdjustHandles
    

Values must be of type <class ‘bool’>

noChangeArrowheads
    

Values must be of type <class ‘bool’>

noChangeAspect
    

Values must be of type <class ‘bool’>

noChangeShapeType
    

Values must be of type <class ‘bool’>

noEditPoints
    

Values must be of type <class ‘bool’>

noGrp
    

Values must be of type <class ‘bool’>

noMove
    

Values must be of type <class ‘bool’>

noResize
    

Values must be of type <class ‘bool’>

noRot
    

Values must be of type <class ‘bool’>

noSelect
    

Values must be of type <class ‘bool’>

noUngrp
    

Values must be of type <class ‘bool’>

tagname _ = 'grpSpLocks'_
    

_class _openpyxl.drawing.properties.GroupShapeProperties(_bwMode =None_, _xfrm =None_, _scene3d =None_, _extLst =None_)[[source]](../_modules/openpyxl/drawing/properties.html#GroupShapeProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

bwMode
    

Value must be one of {‘grayWhite’, ‘gray’, ‘blackWhite’, ‘black’, ‘blackGray’, ‘invGray’, ‘white’, ‘clr’, ‘hidden’, ‘auto’, ‘ltGray’}

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

scene3d
    

Values must be of type <class ‘openpyxl.drawing.geometry.Scene3D’>

tagname _ = 'grpSpPr'_
    

xfrm
    

Values must be of type <class ‘openpyxl.drawing.geometry.GroupTransform2D’>

_class _openpyxl.drawing.properties.NonVisualDrawingProps(_id =None_, _name =None_, _descr =None_, _hidden =None_, _title =None_, _hlinkClick =None_, _hlinkHover =None_, _extLst =None_)[[source]](../_modules/openpyxl/drawing/properties.html#NonVisualDrawingProps)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

descr
    

Values must be of type <class ‘str’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

hidden
    

Values must be of type <class ‘bool’>

hlinkClick
    

Values must be of type <class ‘openpyxl.drawing.text.Hyperlink’>

hlinkHover
    

Values must be of type <class ‘openpyxl.drawing.text.Hyperlink’>

id
    

Values must be of type <class ‘int’>

name
    

Values must be of type <class ‘str’>

tagname _ = 'cNvPr'_
    

title
    

Values must be of type <class ‘str’>

_class _openpyxl.drawing.properties.NonVisualDrawingShapeProps(_spLocks =None_, _txBox =None_, _extLst =None_)[[source]](../_modules/openpyxl/drawing/properties.html#NonVisualDrawingShapeProps)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

spLocks
    

Values must be of type <class ‘openpyxl.drawing.properties.GroupLocking’>

tagname _ = 'cNvSpPr'_
    

txBax
    

Values must be of type <class ‘bool’>

_class _openpyxl.drawing.properties.NonVisualGroupDrawingShapeProps(_grpSpLocks =None_, _extLst =None_)[[source]](../_modules/openpyxl/drawing/properties.html#NonVisualGroupDrawingShapeProps)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

grpSpLocks
    

Values must be of type <class ‘openpyxl.drawing.properties.GroupLocking’>

tagname _ = 'cNvGrpSpPr'_
    

_class _openpyxl.drawing.properties.NonVisualGroupShape(_cNvPr =None_, _cNvGrpSpPr =None_)[[source]](../_modules/openpyxl/drawing/properties.html#NonVisualGroupShape)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

cNvGrpSpPr
    

Values must be of type <class ‘openpyxl.drawing.properties.NonVisualGroupDrawingShapeProps’>

cNvPr
    

Values must be of type <class ‘openpyxl.drawing.properties.NonVisualDrawingProps’>

tagname _ = 'nvGrpSpPr'_
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.drawing.properties module
    * `GroupLocking`
      * `GroupLocking.extLst`
      * `GroupLocking.namespace`
      * `GroupLocking.noAdjustHandles`
      * `GroupLocking.noChangeArrowheads`
      * `GroupLocking.noChangeAspect`
      * `GroupLocking.noChangeShapeType`
      * `GroupLocking.noEditPoints`
      * `GroupLocking.noGrp`
      * `GroupLocking.noMove`
      * `GroupLocking.noResize`
      * `GroupLocking.noRot`
      * `GroupLocking.noSelect`
      * `GroupLocking.noUngrp`
      * `GroupLocking.tagname`
    * `GroupShapeProperties`
      * `GroupShapeProperties.bwMode`
      * `GroupShapeProperties.extLst`
      * `GroupShapeProperties.scene3d`
      * `GroupShapeProperties.tagname`
      * `GroupShapeProperties.xfrm`
    * `NonVisualDrawingProps`
      * `NonVisualDrawingProps.descr`
      * `NonVisualDrawingProps.extLst`
      * `NonVisualDrawingProps.hidden`
      * `NonVisualDrawingProps.hlinkClick`
      * `NonVisualDrawingProps.hlinkHover`
      * `NonVisualDrawingProps.id`
      * `NonVisualDrawingProps.name`
      * `NonVisualDrawingProps.tagname`
      * `NonVisualDrawingProps.title`
    * `NonVisualDrawingShapeProps`
      * `NonVisualDrawingShapeProps.extLst`
      * `NonVisualDrawingShapeProps.spLocks`
      * `NonVisualDrawingShapeProps.tagname`
      * `NonVisualDrawingShapeProps.txBax`
    * `NonVisualGroupDrawingShapeProps`
      * `NonVisualGroupDrawingShapeProps.extLst`
      * `NonVisualGroupDrawingShapeProps.grpSpLocks`
      * `NonVisualGroupDrawingShapeProps.tagname`
    * `NonVisualGroupShape`
      * `NonVisualGroupShape.cNvGrpSpPr`
      * `NonVisualGroupShape.cNvPr`
      * `NonVisualGroupShape.tagname`



#### Previous topic

[openpyxl.drawing.picture module](openpyxl.drawing.picture.html "previous chapter")

#### Next topic

[openpyxl.drawing.relation module](openpyxl.drawing.relation.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.drawing.properties.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.relation.html "openpyxl.drawing.relation module") |
  * [previous](openpyxl.drawing.picture.html "openpyxl.drawing.picture module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.drawing package](openpyxl.drawing.html) »
  * [openpyxl.drawing.properties module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
