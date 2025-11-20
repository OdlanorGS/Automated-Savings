### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chart.text.html "openpyxl.chart.text module") |
  * [previous](openpyxl.chart.stock_chart.html "openpyxl.chart.stock_chart module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.chart package](openpyxl.chart.html) »
  * [openpyxl.chart.surface_chart module]()



# openpyxl.chart.surface_chart module

_class _openpyxl.chart.surface_chart.BandFormat(_idx =0_, _spPr =None_)[[source]](../_modules/openpyxl/chart/surface_chart.html#BandFormat)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

graphicalProperties
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

idx
    

Values must be of type <class ‘int’>

spPr
    

Values must be of type <class ‘openpyxl.chart.shapes.GraphicalProperties’>

tagname _ = 'bandFmt'_
    

_class _openpyxl.chart.surface_chart.BandFormatList(_bandFmt =()_)[[source]](../_modules/openpyxl/chart/surface_chart.html#BandFormatList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

bandFmt
    

A sequence (list or tuple) that may only contain objects of the declared type

tagname _ = 'bandFmts'_
    

_class _openpyxl.chart.surface_chart.SurfaceChart(_** kw_)[[source]](../_modules/openpyxl/chart/surface_chart.html#SurfaceChart)
    

Bases: `SurfaceChart3D`

bandFmts
    

Values must be of type <class ‘openpyxl.chart.surface_chart.BandFormatList’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

ser
    

A sequence (list or tuple) that may only contain objects of the declared type

tagname _ = 'surfaceChart'_
    

wireframe
    

Values must be of type <class ‘bool’>

_class _openpyxl.chart.surface_chart.SurfaceChart3D(_** kw_)[[source]](../_modules/openpyxl/chart/surface_chart.html#SurfaceChart3D)
    

Bases: `_SurfaceChartBase`, `_3DBase`

bandFmts
    

Values must be of type <class ‘openpyxl.chart.surface_chart.BandFormatList’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

ser
    

A sequence (list or tuple) that may only contain objects of the declared type

tagname _ = 'surface3DChart'_
    

wireframe
    

Values must be of type <class ‘bool’>

x_axis
    

Values must be of type <class ‘openpyxl.chart.axis.TextAxis’>

y_axis
    

Values must be of type <class ‘openpyxl.chart.axis.NumericAxis’>

z_axis
    

Values must be of type <class ‘openpyxl.chart.axis.SeriesAxis’>

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.chart.surface_chart module
    * `BandFormat`
      * `BandFormat.graphicalProperties`
      * `BandFormat.idx`
      * `BandFormat.spPr`
      * `BandFormat.tagname`
    * `BandFormatList`
      * `BandFormatList.bandFmt`
      * `BandFormatList.tagname`
    * `SurfaceChart`
      * `SurfaceChart.bandFmts`
      * `SurfaceChart.extLst`
      * `SurfaceChart.ser`
      * `SurfaceChart.tagname`
      * `SurfaceChart.wireframe`
    * `SurfaceChart3D`
      * `SurfaceChart3D.bandFmts`
      * `SurfaceChart3D.extLst`
      * `SurfaceChart3D.ser`
      * `SurfaceChart3D.tagname`
      * `SurfaceChart3D.wireframe`
      * `SurfaceChart3D.x_axis`
      * `SurfaceChart3D.y_axis`
      * `SurfaceChart3D.z_axis`



#### Previous topic

[openpyxl.chart.stock_chart module](openpyxl.chart.stock_chart.html "previous chapter")

#### Next topic

[openpyxl.chart.text module](openpyxl.chart.text.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.chart.surface_chart.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chart.text.html "openpyxl.chart.text module") |
  * [previous](openpyxl.chart.stock_chart.html "openpyxl.chart.stock_chart module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.chart package](openpyxl.chart.html) »
  * [openpyxl.chart.surface_chart module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
