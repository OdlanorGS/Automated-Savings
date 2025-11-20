### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chart.print_settings.html "openpyxl.chart.print_settings module") |
  * [previous](openpyxl.chart.pivot.html "openpyxl.chart.pivot module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.chart package](openpyxl.chart.html) »
  * [openpyxl.chart.plotarea module]()



# openpyxl.chart.plotarea module

_class _openpyxl.chart.plotarea.DataTable(_showHorzBorder =None_, _showVertBorder =None_, _showOutline =None_, _showKeys =None_, _spPr =None_, _txPr =None_, _extLst =None_)[[source]](../_modules/openpyxl/chart/plotarea.html#DataTable)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

graphicalProperties
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

showHorzBorder
    

Values must be of type <class ‘bool’>

showKeys
    

Values must be of type <class ‘bool’>

showOutline
    

Values must be of type <class ‘bool’>

showVertBorder
    

Values must be of type <class ‘bool’>

spPr
    

Values must be of type <class ‘openpyxl.chart.shapes.GraphicalProperties’>

tagname _ = 'dTable'_
    

txPr
    

Values must be of type <class ‘openpyxl.chart.text.RichText’>

_class _openpyxl.chart.plotarea.PlotArea(_layout =None_, _dTable =None_, _spPr =None_, __charts =()_, __axes =()_, _extLst =None_)[[source]](../_modules/openpyxl/chart/plotarea.html#PlotArea)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

area3DChart
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

areaChart
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

bar3DChart
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

barChart
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

bubbleChart
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

catAx
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

dTable
    

Values must be of type <class ‘openpyxl.chart.plotarea.DataTable’>

dateAx
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

doughnutChart
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

_classmethod _from_tree(_node_)[[source]](../_modules/openpyxl/chart/plotarea.html#PlotArea.from_tree)
    

Create object from XML

graphicalProperties
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

layout
    

Values must be of type <class ‘openpyxl.chart.layout.Layout’>

line3DChart
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

lineChart
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

ofPieChart
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

pie3DChart
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

pieChart
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

radarChart
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

scatterChart
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

serAx
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

spPr
    

Values must be of type <class ‘openpyxl.chart.shapes.GraphicalProperties’>

stockChart
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

surface3DChart
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

surfaceChart
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

tagname _ = 'plotArea'_
    

to_tree(_tagname =None_, _idx =None_, _namespace =None_)[[source]](../_modules/openpyxl/chart/plotarea.html#PlotArea.to_tree)
    

valAx
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.chart.plotarea module
    * `DataTable`
      * `DataTable.extLst`
      * `DataTable.graphicalProperties`
      * `DataTable.showHorzBorder`
      * `DataTable.showKeys`
      * `DataTable.showOutline`
      * `DataTable.showVertBorder`
      * `DataTable.spPr`
      * `DataTable.tagname`
      * `DataTable.txPr`
    * `PlotArea`
      * `PlotArea.area3DChart`
      * `PlotArea.areaChart`
      * `PlotArea.bar3DChart`
      * `PlotArea.barChart`
      * `PlotArea.bubbleChart`
      * `PlotArea.catAx`
      * `PlotArea.dTable`
      * `PlotArea.dateAx`
      * `PlotArea.doughnutChart`
      * `PlotArea.extLst`
      * `PlotArea.from_tree()`
      * `PlotArea.graphicalProperties`
      * `PlotArea.layout`
      * `PlotArea.line3DChart`
      * `PlotArea.lineChart`
      * `PlotArea.ofPieChart`
      * `PlotArea.pie3DChart`
      * `PlotArea.pieChart`
      * `PlotArea.radarChart`
      * `PlotArea.scatterChart`
      * `PlotArea.serAx`
      * `PlotArea.spPr`
      * `PlotArea.stockChart`
      * `PlotArea.surface3DChart`
      * `PlotArea.surfaceChart`
      * `PlotArea.tagname`
      * `PlotArea.to_tree()`
      * `PlotArea.valAx`



#### Previous topic

[openpyxl.chart.pivot module](openpyxl.chart.pivot.html "previous chapter")

#### Next topic

[openpyxl.chart.print_settings module](openpyxl.chart.print_settings.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.chart.plotarea.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chart.print_settings.html "openpyxl.chart.print_settings module") |
  * [previous](openpyxl.chart.pivot.html "openpyxl.chart.pivot module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.chart package](openpyxl.chart.html) »
  * [openpyxl.chart.plotarea module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
