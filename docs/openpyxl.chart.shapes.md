### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chart.stock_chart.html "openpyxl.chart.stock_chart module") |
  * [previous](openpyxl.chart.series_factory.html "openpyxl.chart.series_factory module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.chart package](openpyxl.chart.html) »
  * [openpyxl.chart.shapes module]()



# openpyxl.chart.shapes module

_class _openpyxl.chart.shapes.GraphicalProperties(_bwMode =None_, _xfrm =None_, _noFill =None_, _solidFill =None_, _gradFill =None_, _pattFill =None_, _ln =None_, _scene3d =None_, _custGeom =None_, _prstGeom =None_, _sp3d =None_, _extLst =None_)[[source]](../_modules/openpyxl/chart/shapes.html#GraphicalProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

Somewhat vaguely 21.2.2.197 says this:

This element specifies the formatting for the parent chart element. The custGeom, prstGeom, scene3d, and xfrm elements are not supported. The bwMode attribute is not supported.

This doesn’t leave much. And the element is used in different places.

bwMode
    

Value must be one of {‘grayWhite’, ‘gray’, ‘blackWhite’, ‘black’, ‘blackGray’, ‘invGray’, ‘white’, ‘clr’, ‘hidden’, ‘auto’, ‘ltGray’}

custGeom
    

Values must be of type <class ‘openpyxl.drawing.geometry.CustomGeometry2D’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

gradFill
    

Values must be of type <class ‘openpyxl.drawing.fill.GradientFillProperties’>

line
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

ln
    

Values must be of type <class ‘openpyxl.drawing.line.LineProperties’>

noFill
    

Values must be of type <class ‘bool’>

pattFill
    

Values must be of type <class ‘openpyxl.drawing.fill.PatternFillProperties’>

prstGeom
    

Values must be of type <class ‘openpyxl.drawing.geometry.PresetGeometry2D’>

scene3d
    

Values must be of type <class ‘openpyxl.drawing.geometry.Scene3D’>

shape3D
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

solidFill
    

Values must be of type <class ‘openpyxl.drawing.colors.ColorChoice’>

sp3d
    

Values must be of type <class ‘openpyxl.drawing.geometry.Shape3D’>

tagname _ = 'spPr'_
    

transform
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

xfrm
    

Values must be of type <class ‘openpyxl.drawing.geometry.Transform2D’>

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.chart.shapes module
    * `GraphicalProperties`
      * `GraphicalProperties.bwMode`
      * `GraphicalProperties.custGeom`
      * `GraphicalProperties.extLst`
      * `GraphicalProperties.gradFill`
      * `GraphicalProperties.line`
      * `GraphicalProperties.ln`
      * `GraphicalProperties.noFill`
      * `GraphicalProperties.pattFill`
      * `GraphicalProperties.prstGeom`
      * `GraphicalProperties.scene3d`
      * `GraphicalProperties.shape3D`
      * `GraphicalProperties.solidFill`
      * `GraphicalProperties.sp3d`
      * `GraphicalProperties.tagname`
      * `GraphicalProperties.transform`
      * `GraphicalProperties.xfrm`



#### Previous topic

[openpyxl.chart.series_factory module](openpyxl.chart.series_factory.html "previous chapter")

#### Next topic

[openpyxl.chart.stock_chart module](openpyxl.chart.stock_chart.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.chart.shapes.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chart.stock_chart.html "openpyxl.chart.stock_chart module") |
  * [previous](openpyxl.chart.series_factory.html "openpyxl.chart.series_factory module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.chart package](openpyxl.chart.html) »
  * [openpyxl.chart.shapes module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
