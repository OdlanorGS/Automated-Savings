### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.picture.html "openpyxl.drawing.picture module") |
  * [previous](openpyxl.drawing.image.html "openpyxl.drawing.image module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.drawing package](openpyxl.drawing.html) »
  * [openpyxl.drawing.line module]()



# openpyxl.drawing.line module

_class _openpyxl.drawing.line.DashStop(_d =0_, _sp =0_)[[source]](../_modules/openpyxl/drawing/line.html#DashStop)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

d
    

Values must be of type <class ‘int’>

length
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

sp
    

Values must be of type <class ‘int’>

space
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

tagname _ = 'ds'_
    

_class _openpyxl.drawing.line.DashStopList(_ds =None_)[[source]](../_modules/openpyxl/drawing/line.html#DashStopList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

ds
    

A sequence (list or tuple) that may only contain objects of the declared type

_class _openpyxl.drawing.line.LineEndProperties(_type =None_, _w =None_, _len =None_)[[source]](../_modules/openpyxl/drawing/line.html#LineEndProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

len
    

Value must be one of {‘lg’, ‘med’, ‘sm’}

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

tagname _ = 'end'_
    

type
    

Value must be one of {‘oval’, ‘diamond’, ‘triangle’, ‘arrow’, ‘none’, ‘stealth’}

w
    

Value must be one of {‘lg’, ‘med’, ‘sm’}

_class _openpyxl.drawing.line.LineProperties(_w =None_, _cap =None_, _cmpd =None_, _algn =None_, _noFill =None_, _solidFill =None_, _gradFill =None_, _pattFill =None_, _prstDash =None_, _custDash =None_, _round =None_, _bevel =None_, _miter =None_, _headEnd =None_, _tailEnd =None_, _extLst =None_)[[source]](../_modules/openpyxl/drawing/line.html#LineProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

algn
    

Value must be one of {‘in’, ‘ctr’}

bevel
    

Values must be of type <class ‘bool’>

cap
    

Value must be one of {‘sq’, ‘flat’, ‘rnd’}

cmpd
    

Value must be one of {‘tri’, ‘sng’, ‘dbl’, ‘thinThick’, ‘thickThin’}

custDash
    

Values must be of type <class ‘openpyxl.drawing.line.DashStop’>

dashStyle
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

gradFill
    

Values must be of type <class ‘openpyxl.drawing.fill.GradientFillProperties’>

headEnd
    

Values must be of type <class ‘openpyxl.drawing.line.LineEndProperties’>

miter
    

Values must be of type <class ‘int’>

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

noFill
    

Values must be of type <class ‘bool’>

pattFill
    

Values must be of type <class ‘openpyxl.drawing.fill.PatternFillProperties’>

prstDash
    

Value must be one of {‘sysDot’, ‘solid’, ‘sysDashDot’, ‘lgDashDot’, ‘lgDashDotDot’, ‘dashDot’, ‘lgDash’, ‘sysDash’, ‘sysDashDotDot’, ‘dash’, ‘dot’}

round
    

Values must be of type <class ‘bool’>

solidFill
    

Values must be of type <class ‘openpyxl.drawing.colors.ColorChoice’>

tagname _ = 'ln'_
    

tailEnd
    

Values must be of type <class ‘openpyxl.drawing.line.LineEndProperties’>

w
    

Values must be of type <class ‘float’>

width
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.drawing.line module
    * `DashStop`
      * `DashStop.d`
      * `DashStop.length`
      * `DashStop.namespace`
      * `DashStop.sp`
      * `DashStop.space`
      * `DashStop.tagname`
    * `DashStopList`
      * `DashStopList.ds`
    * `LineEndProperties`
      * `LineEndProperties.len`
      * `LineEndProperties.namespace`
      * `LineEndProperties.tagname`
      * `LineEndProperties.type`
      * `LineEndProperties.w`
    * `LineProperties`
      * `LineProperties.algn`
      * `LineProperties.bevel`
      * `LineProperties.cap`
      * `LineProperties.cmpd`
      * `LineProperties.custDash`
      * `LineProperties.dashStyle`
      * `LineProperties.extLst`
      * `LineProperties.gradFill`
      * `LineProperties.headEnd`
      * `LineProperties.miter`
      * `LineProperties.namespace`
      * `LineProperties.noFill`
      * `LineProperties.pattFill`
      * `LineProperties.prstDash`
      * `LineProperties.round`
      * `LineProperties.solidFill`
      * `LineProperties.tagname`
      * `LineProperties.tailEnd`
      * `LineProperties.w`
      * `LineProperties.width`



#### Previous topic

[openpyxl.drawing.image module](openpyxl.drawing.image.html "previous chapter")

#### Next topic

[openpyxl.drawing.picture module](openpyxl.drawing.picture.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.drawing.line.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.picture.html "openpyxl.drawing.picture module") |
  * [previous](openpyxl.drawing.image.html "openpyxl.drawing.image module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.drawing package](openpyxl.drawing.html) »
  * [openpyxl.drawing.line module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
