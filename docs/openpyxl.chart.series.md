### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chart.series_factory.html "openpyxl.chart.series_factory module") |
  * [previous](openpyxl.chart.scatter_chart.html "openpyxl.chart.scatter_chart module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.chart package](openpyxl.chart.html) »
  * [openpyxl.chart.series module]()



# openpyxl.chart.series module

_class _openpyxl.chart.series.Series(_idx =0_, _order =0_, _tx =None_, _spPr =None_, _pictureOptions =None_, _dPt =()_, _dLbls =None_, _trendline =None_, _errBars =None_, _cat =None_, _val =None_, _invertIfNegative =None_, _shape =None_, _xVal =None_, _yVal =None_, _bubbleSize =None_, _bubble3D =None_, _marker =None_, _smooth =None_, _explosion =None_, _extLst =None_)[[source]](../_modules/openpyxl/chart/series.html#Series)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

Generic series object. Should not be instantiated directly. User the chart.Series factory instead.

bubble3D
    

Values must be of type <class ‘bool’>

bubbleSize
    

Values must be of type <class ‘openpyxl.chart.data_source.NumDataSource’>

cat
    

Values must be of type <class ‘openpyxl.chart.data_source.AxDataSource’>

dLbls
    

Values must be of type <class ‘openpyxl.chart.label.DataLabelList’>

dPt
    

A sequence (list or tuple) that may only contain objects of the declared type

data_points
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

errBars
    

Values must be of type <class ‘openpyxl.chart.error_bar.ErrorBars’>

explosion
    

Values must be of type <class ‘int’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

graphicalProperties
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

identifiers
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

idx
    

Values must be of type <class ‘int’>

invertIfNegative
    

Values must be of type <class ‘bool’>

labels
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

marker
    

Values must be of type <class ‘openpyxl.chart.marker.Marker’>

order
    

Values must be of type <class ‘int’>

pictureOptions
    

Values must be of type <class ‘openpyxl.chart.picture.PictureOptions’>

shape
    

Value must be one of {‘pyramidToMax’, ‘coneToMax’, ‘cone’, ‘cylinder’, ‘box’, ‘pyramid’}

smooth
    

Values must be of type <class ‘bool’>

spPr
    

Values must be of type <class ‘openpyxl.chart.shapes.GraphicalProperties’>

tagname _ = 'ser'_
    

title
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

to_tree(_tagname =None_, _idx =None_)[[source]](../_modules/openpyxl/chart/series.html#Series.to_tree)
    

The index can need rebasing

trendline
    

Values must be of type <class ‘openpyxl.chart.trendline.Trendline’>

tx
    

Values must be of type <class ‘openpyxl.chart.series.SeriesLabel’>

val
    

Values must be of type <class ‘openpyxl.chart.data_source.NumDataSource’>

xVal
    

Values must be of type <class ‘openpyxl.chart.data_source.AxDataSource’>

yVal
    

Values must be of type <class ‘openpyxl.chart.data_source.NumDataSource’>

zVal
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

_class _openpyxl.chart.series.SeriesLabel(_strRef =None_, _v =None_)[[source]](../_modules/openpyxl/chart/series.html#SeriesLabel)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

strRef
    

Values must be of type <class ‘openpyxl.chart.data_source.StrRef’>

tagname _ = 'tx'_
    

v
    

Values must be of type <class ‘str’>

value
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

_class _openpyxl.chart.series.XYSeries(_idx =0_, _order =0_, _tx =None_, _spPr =None_, _pictureOptions =None_, _dPt =()_, _dLbls =None_, _trendline =None_, _errBars =None_, _cat =None_, _val =None_, _invertIfNegative =None_, _shape =None_, _xVal =None_, _yVal =None_, _bubbleSize =None_, _bubble3D =None_, _marker =None_, _smooth =None_, _explosion =None_, _extLst =None_)[[source]](../_modules/openpyxl/chart/series.html#XYSeries)
    

Bases: `Series`

Dedicated series for charts that have x and y series

bubble3D
    

Values must be of type <class ‘bool’>

bubbleSize
    

Values must be of type <class ‘openpyxl.chart.data_source.NumDataSource’>

dLbls
    

Values must be of type <class ‘openpyxl.chart.label.DataLabelList’>

dPt
    

A sequence (list or tuple) that may only contain objects of the declared type

errBars
    

Values must be of type <class ‘openpyxl.chart.error_bar.ErrorBars’>

idx
    

Values must be of type <class ‘int’>

invertIfNegative
    

Values must be of type <class ‘bool’>

marker
    

Values must be of type <class ‘openpyxl.chart.marker.Marker’>

order
    

Values must be of type <class ‘int’>

smooth
    

Values must be of type <class ‘bool’>

spPr
    

Values must be of type <class ‘openpyxl.chart.shapes.GraphicalProperties’>

trendline
    

Values must be of type <class ‘openpyxl.chart.trendline.Trendline’>

tx
    

Values must be of type <class ‘openpyxl.chart.series.SeriesLabel’>

xVal
    

Values must be of type <class ‘openpyxl.chart.data_source.AxDataSource’>

yVal
    

Values must be of type <class ‘openpyxl.chart.data_source.NumDataSource’>

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.chart.series module
    * `Series`
      * `Series.bubble3D`
      * `Series.bubbleSize`
      * `Series.cat`
      * `Series.dLbls`
      * `Series.dPt`
      * `Series.data_points`
      * `Series.errBars`
      * `Series.explosion`
      * `Series.extLst`
      * `Series.graphicalProperties`
      * `Series.identifiers`
      * `Series.idx`
      * `Series.invertIfNegative`
      * `Series.labels`
      * `Series.marker`
      * `Series.order`
      * `Series.pictureOptions`
      * `Series.shape`
      * `Series.smooth`
      * `Series.spPr`
      * `Series.tagname`
      * `Series.title`
      * `Series.to_tree()`
      * `Series.trendline`
      * `Series.tx`
      * `Series.val`
      * `Series.xVal`
      * `Series.yVal`
      * `Series.zVal`
    * `SeriesLabel`
      * `SeriesLabel.strRef`
      * `SeriesLabel.tagname`
      * `SeriesLabel.v`
      * `SeriesLabel.value`
    * `XYSeries`
      * `XYSeries.bubble3D`
      * `XYSeries.bubbleSize`
      * `XYSeries.dLbls`
      * `XYSeries.dPt`
      * `XYSeries.errBars`
      * `XYSeries.idx`
      * `XYSeries.invertIfNegative`
      * `XYSeries.marker`
      * `XYSeries.order`
      * `XYSeries.smooth`
      * `XYSeries.spPr`
      * `XYSeries.trendline`
      * `XYSeries.tx`
      * `XYSeries.xVal`
      * `XYSeries.yVal`



#### Previous topic

[openpyxl.chart.scatter_chart module](openpyxl.chart.scatter_chart.html "previous chapter")

#### Next topic

[openpyxl.chart.series_factory module](openpyxl.chart.series_factory.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.chart.series.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chart.series_factory.html "openpyxl.chart.series_factory module") |
  * [previous](openpyxl.chart.scatter_chart.html "openpyxl.chart.scatter_chart module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.chart package](openpyxl.chart.html) »
  * [openpyxl.chart.series module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
