### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.drawing.html "openpyxl.drawing.drawing module") |
  * [previous](openpyxl.drawing.colors.html "openpyxl.drawing.colors module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.drawing package](openpyxl.drawing.html) »
  * [openpyxl.drawing.connector module]()



# openpyxl.drawing.connector module

_class _openpyxl.drawing.connector.Connection(_id =None_, _idx =None_)[[source]](../_modules/openpyxl/drawing/connector.html#Connection)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

id
    

Values must be of type <class ‘int’>

idx
    

Values must be of type <class ‘int’>

_class _openpyxl.drawing.connector.ConnectorLocking(_extLst =None_)[[source]](../_modules/openpyxl/drawing/connector.html#ConnectorLocking)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

_class _openpyxl.drawing.connector.ConnectorNonVisual(_cNvPr =None_, _cNvCxnSpPr =None_)[[source]](../_modules/openpyxl/drawing/connector.html#ConnectorNonVisual)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

cNvCxnSpPr
    

Values must be of type <class ‘openpyxl.drawing.connector.NonVisualConnectorProperties’>

cNvPr
    

Values must be of type <class ‘openpyxl.drawing.properties.NonVisualDrawingProps’>

_class _openpyxl.drawing.connector.ConnectorShape(_nvCxnSpPr =None_, _spPr =None_, _style =None_, _macro =None_, _fPublished =None_)[[source]](../_modules/openpyxl/drawing/connector.html#ConnectorShape)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

fPublished
    

Values must be of type <class ‘bool’>

macro
    

Values must be of type <class ‘str’>

nvCxnSpPr
    

Values must be of type <class ‘openpyxl.drawing.connector.ConnectorNonVisual’>

spPr
    

Values must be of type <class ‘openpyxl.chart.shapes.GraphicalProperties’>

style
    

Values must be of type <class ‘openpyxl.drawing.geometry.ShapeStyle’>

tagname _ = 'cxnSp'_
    

_class _openpyxl.drawing.connector.NonVisualConnectorProperties(_cxnSpLocks =None_, _stCxn =None_, _endCxn =None_, _extLst =None_)[[source]](../_modules/openpyxl/drawing/connector.html#NonVisualConnectorProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

cxnSpLocks
    

Values must be of type <class ‘openpyxl.drawing.connector.ConnectorLocking’>

endCxn
    

Values must be of type <class ‘openpyxl.drawing.connector.Connection’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

stCxn
    

Values must be of type <class ‘openpyxl.drawing.connector.Connection’>

_class _openpyxl.drawing.connector.Shape(_macro =None_, _textlink =None_, _fPublished =None_, _fLocksText =None_, _nvSpPr =None_, _spPr =None_, _style =None_, _txBody =None_)[[source]](../_modules/openpyxl/drawing/connector.html#Shape)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

fLocksText
    

Values must be of type <class ‘bool’>

fPublished
    

Values must be of type <class ‘bool’>

graphicalProperties
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

macro
    

Values must be of type <class ‘str’>

meta
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

nvSpPr
    

Values must be of type <class ‘openpyxl.drawing.connector.ShapeMeta’>

spPr
    

Values must be of type <class ‘openpyxl.chart.shapes.GraphicalProperties’>

style
    

Values must be of type <class ‘openpyxl.drawing.geometry.ShapeStyle’>

textlink
    

Values must be of type <class ‘str’>

txBody
    

Values must be of type <class ‘openpyxl.chart.text.RichText’>

_class _openpyxl.drawing.connector.ShapeMeta(_cNvPr =None_, _cNvSpPr =None_)[[source]](../_modules/openpyxl/drawing/connector.html#ShapeMeta)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

cNvPr
    

Values must be of type <class ‘openpyxl.drawing.properties.NonVisualDrawingProps’>

cNvSpPr
    

Values must be of type <class ‘openpyxl.drawing.properties.NonVisualDrawingShapeProps’>

tagname _ = 'nvSpPr'_
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.drawing.connector module
    * `Connection`
      * `Connection.id`
      * `Connection.idx`
    * `ConnectorLocking`
      * `ConnectorLocking.extLst`
    * `ConnectorNonVisual`
      * `ConnectorNonVisual.cNvCxnSpPr`
      * `ConnectorNonVisual.cNvPr`
    * `ConnectorShape`
      * `ConnectorShape.fPublished`
      * `ConnectorShape.macro`
      * `ConnectorShape.nvCxnSpPr`
      * `ConnectorShape.spPr`
      * `ConnectorShape.style`
      * `ConnectorShape.tagname`
    * `NonVisualConnectorProperties`
      * `NonVisualConnectorProperties.cxnSpLocks`
      * `NonVisualConnectorProperties.endCxn`
      * `NonVisualConnectorProperties.extLst`
      * `NonVisualConnectorProperties.stCxn`
    * `Shape`
      * `Shape.fLocksText`
      * `Shape.fPublished`
      * `Shape.graphicalProperties`
      * `Shape.macro`
      * `Shape.meta`
      * `Shape.nvSpPr`
      * `Shape.spPr`
      * `Shape.style`
      * `Shape.textlink`
      * `Shape.txBody`
    * `ShapeMeta`
      * `ShapeMeta.cNvPr`
      * `ShapeMeta.cNvSpPr`
      * `ShapeMeta.tagname`



#### Previous topic

[openpyxl.drawing.colors module](openpyxl.drawing.colors.html "previous chapter")

#### Next topic

[openpyxl.drawing.drawing module](openpyxl.drawing.drawing.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.drawing.connector.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.drawing.html "openpyxl.drawing.drawing module") |
  * [previous](openpyxl.drawing.colors.html "openpyxl.drawing.colors module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.drawing package](openpyxl.drawing.html) »
  * [openpyxl.drawing.connector module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
