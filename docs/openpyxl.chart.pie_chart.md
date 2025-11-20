### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chart.pivot.html "openpyxl.chart.pivot module") |
  * [previous](openpyxl.chart.picture.html "openpyxl.chart.picture module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.chart package](openpyxl.chart.html) »
  * [openpyxl.chart.pie_chart module]()



# openpyxl.chart.pie_chart module

_class _openpyxl.chart.pie_chart.CustomSplit(_secondPiePt =()_)[[source]](../_modules/openpyxl/chart/pie_chart.html#CustomSplit)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

secondPiePt
    

A sequence of primitive types that are stored as a single attribute. “val” is the default attribute

tagname _ = 'custSplit'_
    

_class _openpyxl.chart.pie_chart.DoughnutChart(_firstSliceAng =0_, _holeSize =10_, _extLst =None_, _** kw_)[[source]](../_modules/openpyxl/chart/pie_chart.html#DoughnutChart)
    

Bases: `_PieChartBase`

dLbls
    

Values must be of type <class ‘openpyxl.chart.label.DataLabelList’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

firstSliceAng
    

Values must be of type <class ‘float’>

holeSize
    

Values must be of type <class ‘float’>

ser
    

A sequence (list or tuple) that may only contain objects of the declared type

tagname _ = 'doughnutChart'_
    

varyColors
    

Values must be of type <class ‘bool’>

_class _openpyxl.chart.pie_chart.PieChart(_firstSliceAng =0_, _extLst =None_, _** kw_)[[source]](../_modules/openpyxl/chart/pie_chart.html#PieChart)
    

Bases: `_PieChartBase`

dLbls
    

Values must be of type <class ‘openpyxl.chart.label.DataLabelList’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

firstSliceAng
    

Values must be of type <class ‘float’>

ser
    

A sequence (list or tuple) that may only contain objects of the declared type

tagname _ = 'pieChart'_
    

varyColors
    

Values must be of type <class ‘bool’>

_class _openpyxl.chart.pie_chart.PieChart3D(_varyColors =True_, _ser =()_, _dLbls =None_)[[source]](../_modules/openpyxl/chart/pie_chart.html#PieChart3D)
    

Bases: `_PieChartBase`

dLbls
    

Values must be of type <class ‘openpyxl.chart.label.DataLabelList’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

ser
    

A sequence (list or tuple) that may only contain objects of the declared type

tagname _ = 'pie3DChart'_
    

varyColors
    

Values must be of type <class ‘bool’>

_class _openpyxl.chart.pie_chart.ProjectedPieChart(_ofPieType ='pie'_, _gapWidth =None_, _splitType ='auto'_, _splitPos =None_, _custSplit =None_, _secondPieSize =75_, _serLines =None_, _extLst =None_, _** kw_)[[source]](../_modules/openpyxl/chart/pie_chart.html#ProjectedPieChart)
    

Bases: `_PieChartBase`

From the spec 21.2.2.126

This element contains the pie of pie or bar of pie series on this chart. Only the first series shall be displayed. The splitType element shall determine whether the splitPos and custSplit elements apply.

custSplit
    

Values must be of type <class ‘openpyxl.chart.pie_chart.CustomSplit’>

dLbls
    

Values must be of type <class ‘openpyxl.chart.label.DataLabelList’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

gapWidth
    

Values must be of type <class ‘float’>

join_lines
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

ofPieType
    

Value must be one of {‘pie’, ‘bar’}

secondPieSize
    

Values must be of type <class ‘float’>

ser
    

A sequence (list or tuple) that may only contain objects of the declared type

serLines
    

Values must be of type <class ‘openpyxl.chart.axis.ChartLines’>

splitPos
    

Values must be of type <class ‘float’>

splitType
    

Value must be one of {‘cust’, ‘pos’, ‘percent’, ‘val’, ‘auto’}

tagname _ = 'ofPieChart'_
    

type
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

varyColors
    

Values must be of type <class ‘bool’>

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.chart.pie_chart module
    * `CustomSplit`
      * `CustomSplit.secondPiePt`
      * `CustomSplit.tagname`
    * `DoughnutChart`
      * `DoughnutChart.dLbls`
      * `DoughnutChart.extLst`
      * `DoughnutChart.firstSliceAng`
      * `DoughnutChart.holeSize`
      * `DoughnutChart.ser`
      * `DoughnutChart.tagname`
      * `DoughnutChart.varyColors`
    * `PieChart`
      * `PieChart.dLbls`
      * `PieChart.extLst`
      * `PieChart.firstSliceAng`
      * `PieChart.ser`
      * `PieChart.tagname`
      * `PieChart.varyColors`
    * `PieChart3D`
      * `PieChart3D.dLbls`
      * `PieChart3D.extLst`
      * `PieChart3D.ser`
      * `PieChart3D.tagname`
      * `PieChart3D.varyColors`
    * `ProjectedPieChart`
      * `ProjectedPieChart.custSplit`
      * `ProjectedPieChart.dLbls`
      * `ProjectedPieChart.extLst`
      * `ProjectedPieChart.gapWidth`
      * `ProjectedPieChart.join_lines`
      * `ProjectedPieChart.ofPieType`
      * `ProjectedPieChart.secondPieSize`
      * `ProjectedPieChart.ser`
      * `ProjectedPieChart.serLines`
      * `ProjectedPieChart.splitPos`
      * `ProjectedPieChart.splitType`
      * `ProjectedPieChart.tagname`
      * `ProjectedPieChart.type`
      * `ProjectedPieChart.varyColors`



#### Previous topic

[openpyxl.chart.picture module](openpyxl.chart.picture.html "previous chapter")

#### Next topic

[openpyxl.chart.pivot module](openpyxl.chart.pivot.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.chart.pie_chart.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chart.pivot.html "openpyxl.chart.pivot module") |
  * [previous](openpyxl.chart.picture.html "openpyxl.chart.picture module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.chart package](openpyxl.chart.html) »
  * [openpyxl.chart.pie_chart module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
