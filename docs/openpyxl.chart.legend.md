### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chart.line_chart.html "openpyxl.chart.line_chart module") |
  * [previous](openpyxl.chart.layout.html "openpyxl.chart.layout module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.chart package](openpyxl.chart.html) »
  * [openpyxl.chart.legend module]()



# openpyxl.chart.legend module

_class _openpyxl.chart.legend.Legend(_legendPos ='r'_, _legendEntry =()_, _layout =None_, _overlay =None_, _spPr =None_, _txPr =None_, _extLst =None_)[[source]](../_modules/openpyxl/chart/legend.html#Legend)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

graphicalProperties
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

layout
    

Values must be of type <class ‘openpyxl.chart.layout.Layout’>

legendEntry
    

A sequence (list or tuple) that may only contain objects of the declared type

legendPos
    

Value must be one of {‘l’, ‘t’, ‘r’, ‘b’, ‘tr’}

overlay
    

Values must be of type <class ‘bool’>

position
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

spPr
    

Values must be of type <class ‘openpyxl.chart.shapes.GraphicalProperties’>

tagname _ = 'legend'_
    

textProperties
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

txPr
    

Values must be of type <class ‘openpyxl.chart.text.RichText’>

_class _openpyxl.chart.legend.LegendEntry(_idx =0_, _delete =False_, _txPr =None_, _extLst =None_)[[source]](../_modules/openpyxl/chart/legend.html#LegendEntry)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

delete
    

Values must be of type <class ‘bool’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

idx
    

Values must be of type <class ‘int’>

tagname _ = 'legendEntry'_
    

txPr
    

Values must be of type <class ‘openpyxl.chart.text.RichText’>

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.chart.legend module
    * `Legend`
      * `Legend.extLst`
      * `Legend.graphicalProperties`
      * `Legend.layout`
      * `Legend.legendEntry`
      * `Legend.legendPos`
      * `Legend.overlay`
      * `Legend.position`
      * `Legend.spPr`
      * `Legend.tagname`
      * `Legend.textProperties`
      * `Legend.txPr`
    * `LegendEntry`
      * `LegendEntry.delete`
      * `LegendEntry.extLst`
      * `LegendEntry.idx`
      * `LegendEntry.tagname`
      * `LegendEntry.txPr`



#### Previous topic

[openpyxl.chart.layout module](openpyxl.chart.layout.html "previous chapter")

#### Next topic

[openpyxl.chart.line_chart module](openpyxl.chart.line_chart.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.chart.legend.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chart.line_chart.html "openpyxl.chart.line_chart module") |
  * [previous](openpyxl.chart.layout.html "openpyxl.chart.layout module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.chart package](openpyxl.chart.html) »
  * [openpyxl.chart.legend module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
