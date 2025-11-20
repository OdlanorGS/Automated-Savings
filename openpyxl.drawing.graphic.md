### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.image.html "openpyxl.drawing.image module") |
  * [previous](openpyxl.drawing.geometry.html "openpyxl.drawing.geometry module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.drawing package](openpyxl.drawing.html) »
  * [openpyxl.drawing.graphic module]()



# openpyxl.drawing.graphic module

_class _openpyxl.drawing.graphic.GraphicData(_uri ='http://schemas.openxmlformats.org/drawingml/2006/chart'_, _chart =None_)[[source]](../_modules/openpyxl/drawing/graphic.html#GraphicData)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

chart
    

Values must be of type <class ‘openpyxl.drawing.relation.ChartRelation’>

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

tagname _ = 'graphicData'_
    

uri
    

Values must be of type <class ‘str’>

_class _openpyxl.drawing.graphic.GraphicFrame(_nvGraphicFramePr =None_, _xfrm =None_, _graphic =None_, _macro =None_, _fPublished =None_)[[source]](../_modules/openpyxl/drawing/graphic.html#GraphicFrame)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

fPublished
    

Values must be of type <class ‘bool’>

graphic
    

Values must be of type <class ‘openpyxl.drawing.graphic.GraphicObject’>

macro
    

Values must be of type <class ‘str’>

nvGraphicFramePr
    

Values must be of type <class ‘openpyxl.drawing.graphic.NonVisualGraphicFrame’>

tagname _ = 'graphicFrame'_
    

xfrm
    

Values must be of type <class ‘openpyxl.drawing.xdr.XDRTransform2D’>

_class _openpyxl.drawing.graphic.GraphicFrameLocking(_noGrp =None_, _noDrilldown =None_, _noSelect =None_, _noChangeAspect =None_, _noMove =None_, _noResize =None_, _extLst =None_)[[source]](../_modules/openpyxl/drawing/graphic.html#GraphicFrameLocking)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

noChangeAspect
    

Values must be of type <class ‘bool’>

noDrilldown
    

Values must be of type <class ‘bool’>

noGrp
    

Values must be of type <class ‘bool’>

noMove
    

Values must be of type <class ‘bool’>

noResize
    

Values must be of type <class ‘bool’>

noSelect
    

Values must be of type <class ‘bool’>

_class _openpyxl.drawing.graphic.GraphicObject(_graphicData =None_)[[source]](../_modules/openpyxl/drawing/graphic.html#GraphicObject)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

graphicData
    

Values must be of type <class ‘openpyxl.drawing.graphic.GraphicData’>

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

tagname _ = 'graphic'_
    

_class _openpyxl.drawing.graphic.GroupShape(_nvGrpSpPr =None_, _grpSpPr =None_, _pic =None_)[[source]](../_modules/openpyxl/drawing/graphic.html#GroupShape)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

grpSpPr
    

Values must be of type <class ‘openpyxl.drawing.properties.GroupShapeProperties’>

nonVisualProperties
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

nvGrpSpPr
    

Values must be of type <class ‘openpyxl.drawing.properties.NonVisualGroupShape’>

pic
    

Values must be of type <class ‘openpyxl.drawing.picture.PictureFrame’>

visualProperties
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

_class _openpyxl.drawing.graphic.NonVisualGraphicFrame(_cNvPr =None_, _cNvGraphicFramePr =None_)[[source]](../_modules/openpyxl/drawing/graphic.html#NonVisualGraphicFrame)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

cNvGraphicFramePr
    

Values must be of type <class ‘openpyxl.drawing.graphic.NonVisualGraphicFrameProperties’>

cNvPr
    

Values must be of type <class ‘openpyxl.drawing.properties.NonVisualDrawingProps’>

tagname _ = 'nvGraphicFramePr'_
    

_class _openpyxl.drawing.graphic.NonVisualGraphicFrameProperties(_graphicFrameLocks =None_, _extLst =None_)[[source]](../_modules/openpyxl/drawing/graphic.html#NonVisualGraphicFrameProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

graphicFrameLocks
    

Values must be of type <class ‘openpyxl.drawing.graphic.GraphicFrameLocking’>

tagname _ = 'cNvGraphicFramePr'_
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.drawing.graphic module
    * `GraphicData`
      * `GraphicData.chart`
      * `GraphicData.namespace`
      * `GraphicData.tagname`
      * `GraphicData.uri`
    * `GraphicFrame`
      * `GraphicFrame.fPublished`
      * `GraphicFrame.graphic`
      * `GraphicFrame.macro`
      * `GraphicFrame.nvGraphicFramePr`
      * `GraphicFrame.tagname`
      * `GraphicFrame.xfrm`
    * `GraphicFrameLocking`
      * `GraphicFrameLocking.extLst`
      * `GraphicFrameLocking.noChangeAspect`
      * `GraphicFrameLocking.noDrilldown`
      * `GraphicFrameLocking.noGrp`
      * `GraphicFrameLocking.noMove`
      * `GraphicFrameLocking.noResize`
      * `GraphicFrameLocking.noSelect`
    * `GraphicObject`
      * `GraphicObject.graphicData`
      * `GraphicObject.namespace`
      * `GraphicObject.tagname`
    * `GroupShape`
      * `GroupShape.grpSpPr`
      * `GroupShape.nonVisualProperties`
      * `GroupShape.nvGrpSpPr`
      * `GroupShape.pic`
      * `GroupShape.visualProperties`
    * `NonVisualGraphicFrame`
      * `NonVisualGraphicFrame.cNvGraphicFramePr`
      * `NonVisualGraphicFrame.cNvPr`
      * `NonVisualGraphicFrame.tagname`
    * `NonVisualGraphicFrameProperties`
      * `NonVisualGraphicFrameProperties.extLst`
      * `NonVisualGraphicFrameProperties.graphicFrameLocks`
      * `NonVisualGraphicFrameProperties.tagname`



#### Previous topic

[openpyxl.drawing.geometry module](openpyxl.drawing.geometry.html "previous chapter")

#### Next topic

[openpyxl.drawing.image module](openpyxl.drawing.image.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.drawing.graphic.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.image.html "openpyxl.drawing.image module") |
  * [previous](openpyxl.drawing.geometry.html "openpyxl.drawing.geometry module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.drawing package](openpyxl.drawing.html) »
  * [openpyxl.drawing.graphic module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
