### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chart.data_source.html "openpyxl.chart.data_source module") |
  * [previous](openpyxl.chart.bubble_chart.html "openpyxl.chart.bubble_chart module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.chart package](openpyxl.chart.html) »
  * [openpyxl.chart.chartspace module]()



# openpyxl.chart.chartspace module

Enclosing chart object. The various chart types are actually child objects. Will probably need to call this indirectly

_class _openpyxl.chart.chartspace.ChartContainer(_title =None_, _autoTitleDeleted =None_, _pivotFmts =()_, _view3D =None_, _floor =None_, _sideWall =None_, _backWall =None_, _plotArea =None_, _legend =None_, _plotVisOnly =True_, _dispBlanksAs ='gap'_, _showDLblsOverMax =None_, _extLst =None_)[[source]](../_modules/openpyxl/chart/chartspace.html#ChartContainer)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

autoTitleDeleted
    

Values must be of type <class ‘bool’>

backWall
    

Values must be of type <class ‘openpyxl.chart._3d.Surface’>

dispBlanksAs
    

Value must be one of {‘zero’, ‘gap’, ‘span’}

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

floor
    

Values must be of type <class ‘openpyxl.chart._3d.Surface’>

legend
    

Values must be of type <class ‘openpyxl.chart.legend.Legend’>

pivotFmts
    

Wrap a sequence in an containing object

plotArea
    

Values must be of type <class ‘openpyxl.chart.plotarea.PlotArea’>

plotVisOnly
    

Values must be of type <class ‘bool’>

showDLblsOverMax
    

Values must be of type <class ‘bool’>

sideWall
    

Values must be of type <class ‘openpyxl.chart._3d.Surface’>

tagname _ = 'chart'_
    

title
    

Values must be of type <class ‘openpyxl.chart.title.Title’>

view3D
    

Values must be of type <class ‘openpyxl.chart._3d.View3D’>

_class _openpyxl.chart.chartspace.ChartSpace(_date1904 =None_, _lang =None_, _roundedCorners =None_, _style =None_, _clrMapOvr =None_, _pivotSource =None_, _protection =None_, _chart =None_, _spPr =None_, _txPr =None_, _externalData =None_, _printSettings =None_, _userShapes =None_, _extLst =None_)[[source]](../_modules/openpyxl/chart/chartspace.html#ChartSpace)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

chart
    

Values must be of type <class ‘openpyxl.chart.chartspace.ChartContainer’>

clrMapOvr
    

Values must be of type <class ‘openpyxl.drawing.colors.ColorMapping’>

date1904
    

Values must be of type <class ‘bool’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

externalData
    

Values must be of type <class ‘openpyxl.chart.chartspace.ExternalData’>

graphical_properties
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

lang
    

Values must be of type <class ‘str’>

pivotSource
    

Values must be of type <class ‘openpyxl.chart.pivot.PivotSource’>

printSettings
    

Values must be of type <class ‘openpyxl.chart.print_settings.PrintSettings’>

protection
    

Values must be of type <class ‘openpyxl.chart.chartspace.Protection’>

roundedCorners
    

Values must be of type <class ‘bool’>

spPr
    

Values must be of type <class ‘openpyxl.chart.shapes.GraphicalProperties’>

style
    

Values must be of type <class ‘float’>

tagname _ = 'chartSpace'_
    

textProperties
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

to_tree(_tagname =None_, _idx =None_, _namespace =None_)[[source]](../_modules/openpyxl/chart/chartspace.html#ChartSpace.to_tree)
    

txPr
    

Values must be of type <class ‘openpyxl.chart.text.RichText’>

userShapes
    

Values must be of type <class ‘str’>

_class _openpyxl.chart.chartspace.ExternalData(_autoUpdate =None_, _id =None_)[[source]](../_modules/openpyxl/chart/chartspace.html#ExternalData)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

autoUpdate
    

Values must be of type <class ‘bool’>

id
    

Values must be of type <class ‘str’>

tagname _ = 'externalData'_
    

_class _openpyxl.chart.chartspace.Protection(_chartObject =None_, _data =None_, _formatting =None_, _selection =None_, _userInterface =None_)[[source]](../_modules/openpyxl/chart/chartspace.html#Protection)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

chartObject
    

Values must be of type <class ‘bool’>

data
    

Values must be of type <class ‘bool’>

formatting
    

Values must be of type <class ‘bool’>

selection
    

Values must be of type <class ‘bool’>

tagname _ = 'protection'_
    

userInterface
    

Values must be of type <class ‘bool’>

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.chart.chartspace module
    * `ChartContainer`
      * `ChartContainer.autoTitleDeleted`
      * `ChartContainer.backWall`
      * `ChartContainer.dispBlanksAs`
      * `ChartContainer.extLst`
      * `ChartContainer.floor`
      * `ChartContainer.legend`
      * `ChartContainer.pivotFmts`
      * `ChartContainer.plotArea`
      * `ChartContainer.plotVisOnly`
      * `ChartContainer.showDLblsOverMax`
      * `ChartContainer.sideWall`
      * `ChartContainer.tagname`
      * `ChartContainer.title`
      * `ChartContainer.view3D`
    * `ChartSpace`
      * `ChartSpace.chart`
      * `ChartSpace.clrMapOvr`
      * `ChartSpace.date1904`
      * `ChartSpace.extLst`
      * `ChartSpace.externalData`
      * `ChartSpace.graphical_properties`
      * `ChartSpace.lang`
      * `ChartSpace.pivotSource`
      * `ChartSpace.printSettings`
      * `ChartSpace.protection`
      * `ChartSpace.roundedCorners`
      * `ChartSpace.spPr`
      * `ChartSpace.style`
      * `ChartSpace.tagname`
      * `ChartSpace.textProperties`
      * `ChartSpace.to_tree()`
      * `ChartSpace.txPr`
      * `ChartSpace.userShapes`
    * `ExternalData`
      * `ExternalData.autoUpdate`
      * `ExternalData.id`
      * `ExternalData.tagname`
    * `Protection`
      * `Protection.chartObject`
      * `Protection.data`
      * `Protection.formatting`
      * `Protection.selection`
      * `Protection.tagname`
      * `Protection.userInterface`



#### Previous topic

[openpyxl.chart.bubble_chart module](openpyxl.chart.bubble_chart.html "previous chapter")

#### Next topic

[openpyxl.chart.data_source module](openpyxl.chart.data_source.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.chart.chartspace.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chart.data_source.html "openpyxl.chart.data_source module") |
  * [previous](openpyxl.chart.bubble_chart.html "openpyxl.chart.bubble_chart module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.chart package](openpyxl.chart.html) »
  * [openpyxl.chart.chartspace module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
