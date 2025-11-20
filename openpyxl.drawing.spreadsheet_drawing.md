### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.text.html "openpyxl.drawing.text module") |
  * [previous](openpyxl.drawing.relation.html "openpyxl.drawing.relation module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.drawing package](openpyxl.drawing.html) »
  * [openpyxl.drawing.spreadsheet_drawing module]()



# openpyxl.drawing.spreadsheet_drawing module

_class _openpyxl.drawing.spreadsheet_drawing.AbsoluteAnchor(_pos =None_, _ext =None_, _** kw_)[[source]](../_modules/openpyxl/drawing/spreadsheet_drawing.html#AbsoluteAnchor)
    

Bases: `_AnchorBase`

clientData
    

Values must be of type <class ‘openpyxl.drawing.spreadsheet_drawing.AnchorClientData’>

contentPart
    

Values must be of type <class ‘str’>

cxnSp
    

Values must be of type <class ‘openpyxl.drawing.connector.Shape’>

ext
    

Values must be of type <class ‘openpyxl.drawing.xdr.XDRPositiveSize2D’>

graphicFrame
    

Values must be of type <class ‘openpyxl.drawing.graphic.GraphicFrame’>

grpSp
    

Values must be of type <class ‘openpyxl.drawing.graphic.GroupShape’>

pic
    

Values must be of type <class ‘openpyxl.drawing.picture.PictureFrame’>

pos
    

Values must be of type <class ‘openpyxl.drawing.xdr.XDRPoint2D’>

sp
    

Values must be of type <class ‘openpyxl.drawing.connector.Shape’>

tagname _ = 'absoluteAnchor'_
    

_class _openpyxl.drawing.spreadsheet_drawing.AnchorClientData(_fLocksWithSheet =None_, _fPrintsWithSheet =None_)[[source]](../_modules/openpyxl/drawing/spreadsheet_drawing.html#AnchorClientData)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

fLocksWithSheet
    

Values must be of type <class ‘bool’>

fPrintsWithSheet
    

Values must be of type <class ‘bool’>

_class _openpyxl.drawing.spreadsheet_drawing.AnchorMarker(_col =0_, _colOff =0_, _row =0_, _rowOff =0_)[[source]](../_modules/openpyxl/drawing/spreadsheet_drawing.html#AnchorMarker)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

col
    

Values must be of type <class ‘int’>

colOff
    

Values must be of type <class ‘int’>

row
    

Values must be of type <class ‘int’>

rowOff
    

Values must be of type <class ‘int’>

tagname _ = 'marker'_
    

_class _openpyxl.drawing.spreadsheet_drawing.OneCellAnchor(__from =None_, _ext =None_, _** kw_)[[source]](../_modules/openpyxl/drawing/spreadsheet_drawing.html#OneCellAnchor)
    

Bases: `_AnchorBase`

clientData
    

Values must be of type <class ‘openpyxl.drawing.spreadsheet_drawing.AnchorClientData’>

contentPart
    

Values must be of type <class ‘str’>

cxnSp
    

Values must be of type <class ‘openpyxl.drawing.connector.Shape’>

ext
    

Values must be of type <class ‘openpyxl.drawing.xdr.XDRPositiveSize2D’>

graphicFrame
    

Values must be of type <class ‘openpyxl.drawing.graphic.GraphicFrame’>

grpSp
    

Values must be of type <class ‘openpyxl.drawing.graphic.GroupShape’>

pic
    

Values must be of type <class ‘openpyxl.drawing.picture.PictureFrame’>

sp
    

Values must be of type <class ‘openpyxl.drawing.connector.Shape’>

tagname _ = 'oneCellAnchor'_
    

_class _openpyxl.drawing.spreadsheet_drawing.SpreadsheetDrawing(_twoCellAnchor =()_, _oneCellAnchor =()_, _absoluteAnchor =()_)[[source]](../_modules/openpyxl/drawing/spreadsheet_drawing.html#SpreadsheetDrawing)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

PartName _ = '/xl/drawings/drawing{0}.xml'_
    

absoluteAnchor
    

A sequence (list or tuple) that may only contain objects of the declared type

mime_type _ = 'application/vnd.openxmlformats-officedocument.drawing+xml'_
    

oneCellAnchor
    

A sequence (list or tuple) that may only contain objects of the declared type

_property _path
    

tagname _ = 'wsDr'_
    

twoCellAnchor
    

A sequence (list or tuple) that may only contain objects of the declared type

_class _openpyxl.drawing.spreadsheet_drawing.TwoCellAnchor(_editAs =None_, __from =None_, _to =None_, _** kw_)[[source]](../_modules/openpyxl/drawing/spreadsheet_drawing.html#TwoCellAnchor)
    

Bases: `_AnchorBase`

clientData
    

Values must be of type <class ‘openpyxl.drawing.spreadsheet_drawing.AnchorClientData’>

contentPart
    

Values must be of type <class ‘str’>

cxnSp
    

Values must be of type <class ‘openpyxl.drawing.connector.Shape’>

editAs
    

Value must be one of {‘twoCell’, ‘oneCell’, ‘absolute’}

graphicFrame
    

Values must be of type <class ‘openpyxl.drawing.graphic.GraphicFrame’>

grpSp
    

Values must be of type <class ‘openpyxl.drawing.graphic.GroupShape’>

pic
    

Values must be of type <class ‘openpyxl.drawing.picture.PictureFrame’>

sp
    

Values must be of type <class ‘openpyxl.drawing.connector.Shape’>

tagname _ = 'twoCellAnchor'_
    

to
    

Values must be of type <class ‘openpyxl.drawing.spreadsheet_drawing.AnchorMarker’>

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.drawing.spreadsheet_drawing module
    * `AbsoluteAnchor`
      * `AbsoluteAnchor.clientData`
      * `AbsoluteAnchor.contentPart`
      * `AbsoluteAnchor.cxnSp`
      * `AbsoluteAnchor.ext`
      * `AbsoluteAnchor.graphicFrame`
      * `AbsoluteAnchor.grpSp`
      * `AbsoluteAnchor.pic`
      * `AbsoluteAnchor.pos`
      * `AbsoluteAnchor.sp`
      * `AbsoluteAnchor.tagname`
    * `AnchorClientData`
      * `AnchorClientData.fLocksWithSheet`
      * `AnchorClientData.fPrintsWithSheet`
    * `AnchorMarker`
      * `AnchorMarker.col`
      * `AnchorMarker.colOff`
      * `AnchorMarker.row`
      * `AnchorMarker.rowOff`
      * `AnchorMarker.tagname`
    * `OneCellAnchor`
      * `OneCellAnchor.clientData`
      * `OneCellAnchor.contentPart`
      * `OneCellAnchor.cxnSp`
      * `OneCellAnchor.ext`
      * `OneCellAnchor.graphicFrame`
      * `OneCellAnchor.grpSp`
      * `OneCellAnchor.pic`
      * `OneCellAnchor.sp`
      * `OneCellAnchor.tagname`
    * `SpreadsheetDrawing`
      * `SpreadsheetDrawing.PartName`
      * `SpreadsheetDrawing.absoluteAnchor`
      * `SpreadsheetDrawing.mime_type`
      * `SpreadsheetDrawing.oneCellAnchor`
      * `SpreadsheetDrawing.path`
      * `SpreadsheetDrawing.tagname`
      * `SpreadsheetDrawing.twoCellAnchor`
    * `TwoCellAnchor`
      * `TwoCellAnchor.clientData`
      * `TwoCellAnchor.contentPart`
      * `TwoCellAnchor.cxnSp`
      * `TwoCellAnchor.editAs`
      * `TwoCellAnchor.graphicFrame`
      * `TwoCellAnchor.grpSp`
      * `TwoCellAnchor.pic`
      * `TwoCellAnchor.sp`
      * `TwoCellAnchor.tagname`
      * `TwoCellAnchor.to`



#### Previous topic

[openpyxl.drawing.relation module](openpyxl.drawing.relation.html "previous chapter")

#### Next topic

[openpyxl.drawing.text module](openpyxl.drawing.text.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.drawing.spreadsheet_drawing.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.text.html "openpyxl.drawing.text module") |
  * [previous](openpyxl.drawing.relation.html "openpyxl.drawing.relation module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.drawing package](openpyxl.drawing.html) »
  * [openpyxl.drawing.spreadsheet_drawing module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
