### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.properties.html "openpyxl.drawing.properties module") |
  * [previous](openpyxl.drawing.line.html "openpyxl.drawing.line module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.drawing package](openpyxl.drawing.html) »
  * [openpyxl.drawing.picture module]()



# openpyxl.drawing.picture module

_class _openpyxl.drawing.picture.NonVisualPictureProperties(_preferRelativeResize =None_, _picLocks =None_, _extLst =None_)[[source]](../_modules/openpyxl/drawing/picture.html#NonVisualPictureProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

picLocks
    

Values must be of type <class ‘openpyxl.drawing.picture.PictureLocking’>

preferRelativeResize
    

Values must be of type <class ‘bool’>

tagname _ = 'cNvPicPr'_
    

_class _openpyxl.drawing.picture.PictureFrame(_macro =None_, _fPublished =None_, _nvPicPr =None_, _blipFill =None_, _spPr =None_, _style =None_)[[source]](../_modules/openpyxl/drawing/picture.html#PictureFrame)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

blipFill
    

Values must be of type <class ‘openpyxl.drawing.fill.BlipFillProperties’>

fPublished
    

Values must be of type <class ‘bool’>

graphicalProperties
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

macro
    

Values must be of type <class ‘str’>

nvPicPr
    

Values must be of type <class ‘openpyxl.drawing.picture.PictureNonVisual’>

spPr
    

Values must be of type <class ‘openpyxl.chart.shapes.GraphicalProperties’>

style
    

Values must be of type <class ‘openpyxl.drawing.geometry.ShapeStyle’>

tagname _ = 'pic'_
    

_class _openpyxl.drawing.picture.PictureLocking(_noCrop =None_, _noGrp =None_, _noSelect =None_, _noRot =None_, _noChangeAspect =None_, _noMove =None_, _noResize =None_, _noEditPoints =None_, _noAdjustHandles =None_, _noChangeArrowheads =None_, _noChangeShapeType =None_, _extLst =None_)[[source]](../_modules/openpyxl/drawing/picture.html#PictureLocking)
    

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

noCrop
    

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

tagname _ = 'picLocks'_
    

_class _openpyxl.drawing.picture.PictureNonVisual(_cNvPr =None_, _cNvPicPr =None_)[[source]](../_modules/openpyxl/drawing/picture.html#PictureNonVisual)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

cNvPicPr
    

Values must be of type <class ‘openpyxl.drawing.picture.NonVisualPictureProperties’>

cNvPr
    

Values must be of type <class ‘openpyxl.drawing.properties.NonVisualDrawingProps’>

tagname _ = 'nvPicPr'_
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.drawing.picture module
    * `NonVisualPictureProperties`
      * `NonVisualPictureProperties.extLst`
      * `NonVisualPictureProperties.picLocks`
      * `NonVisualPictureProperties.preferRelativeResize`
      * `NonVisualPictureProperties.tagname`
    * `PictureFrame`
      * `PictureFrame.blipFill`
      * `PictureFrame.fPublished`
      * `PictureFrame.graphicalProperties`
      * `PictureFrame.macro`
      * `PictureFrame.nvPicPr`
      * `PictureFrame.spPr`
      * `PictureFrame.style`
      * `PictureFrame.tagname`
    * `PictureLocking`
      * `PictureLocking.extLst`
      * `PictureLocking.namespace`
      * `PictureLocking.noAdjustHandles`
      * `PictureLocking.noChangeArrowheads`
      * `PictureLocking.noChangeAspect`
      * `PictureLocking.noChangeShapeType`
      * `PictureLocking.noCrop`
      * `PictureLocking.noEditPoints`
      * `PictureLocking.noGrp`
      * `PictureLocking.noMove`
      * `PictureLocking.noResize`
      * `PictureLocking.noRot`
      * `PictureLocking.noSelect`
      * `PictureLocking.tagname`
    * `PictureNonVisual`
      * `PictureNonVisual.cNvPicPr`
      * `PictureNonVisual.cNvPr`
      * `PictureNonVisual.tagname`



#### Previous topic

[openpyxl.drawing.line module](openpyxl.drawing.line.html "previous chapter")

#### Next topic

[openpyxl.drawing.properties module](openpyxl.drawing.properties.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.drawing.picture.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.properties.html "openpyxl.drawing.properties module") |
  * [previous](openpyxl.drawing.line.html "openpyxl.drawing.line module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.drawing package](openpyxl.drawing.html) »
  * [openpyxl.drawing.picture module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
