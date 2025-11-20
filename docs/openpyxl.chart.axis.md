### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chart.bar_chart.html "openpyxl.chart.bar_chart module") |
  * [previous](openpyxl.chart.area_chart.html "openpyxl.chart.area_chart module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.chart package](openpyxl.chart.html) »
  * [openpyxl.chart.axis module]()



# openpyxl.chart.axis module

_class _openpyxl.chart.axis.ChartLines(_spPr =None_)[[source]](../_modules/openpyxl/chart/axis.html#ChartLines)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

graphicalProperties
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

spPr
    

Values must be of type <class ‘openpyxl.chart.shapes.GraphicalProperties’>

tagname _ = 'chartLines'_
    

_class _openpyxl.chart.axis.DateAxis(_auto =None_, _lblOffset =None_, _baseTimeUnit =None_, _majorUnit =None_, _majorTimeUnit =None_, _minorUnit =None_, _minorTimeUnit =None_, _extLst =None_, _** kw_)[[source]](../_modules/openpyxl/chart/axis.html#DateAxis)
    

Bases: `TextAxis`

auto
    

Values must be of type <class ‘bool’>

axId
    

Values must be of type <class ‘int’>

axPos
    

Value must be one of {‘l’, ‘b’, ‘t’, ‘r’}

baseTimeUnit
    

Value must be one of {‘days’, ‘months’, ‘years’}

crossAx
    

Values must be of type <class ‘int’>

crosses
    

Value must be one of {‘autoZero’, ‘max’, ‘min’}

crossesAt
    

Values must be of type <class ‘float’>

delete
    

Values must be of type <class ‘bool’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

lblOffset
    

Values must be of type <class ‘int’>

majorGridlines
    

Values must be of type <class ‘openpyxl.chart.axis.ChartLines’>

majorTickMark
    

Value must be one of {‘cross’, ‘out’, ‘in’}

majorTimeUnit
    

Value must be one of {‘days’, ‘months’, ‘years’}

majorUnit
    

Values must be of type <class ‘float’>

minorGridlines
    

Values must be of type <class ‘openpyxl.chart.axis.ChartLines’>

minorTickMark
    

Value must be one of {‘cross’, ‘out’, ‘in’}

minorTimeUnit
    

Value must be one of {‘days’, ‘months’, ‘years’}

minorUnit
    

Values must be of type <class ‘float’>

numFmt
    

Values must be of type <class ‘openpyxl.chart.data_source.NumFmt’>

scaling
    

Values must be of type <class ‘openpyxl.chart.axis.Scaling’>

spPr
    

Values must be of type <class ‘openpyxl.chart.shapes.GraphicalProperties’>

tagname _ = 'dateAx'_
    

tickLblPos
    

Value must be one of {‘high’, ‘nextTo’, ‘low’}

title
    

Values must be of type <class ‘openpyxl.chart.title.Title’>

txPr
    

Values must be of type <class ‘openpyxl.chart.text.RichText’>

_class _openpyxl.chart.axis.DisplayUnitsLabel(_layout =None_, _tx =None_, _spPr =None_, _txPr =None_)[[source]](../_modules/openpyxl/chart/axis.html#DisplayUnitsLabel)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

graphicalProperties
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

layout
    

Values must be of type <class ‘openpyxl.chart.layout.Layout’>

spPr
    

Values must be of type <class ‘openpyxl.chart.shapes.GraphicalProperties’>

tagname _ = 'dispUnitsLbl'_
    

text
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

textPropertes
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

tx
    

Values must be of type <class ‘openpyxl.chart.text.Text’>

txPr
    

Values must be of type <class ‘openpyxl.chart.text.RichText’>

_class _openpyxl.chart.axis.DisplayUnitsLabelList(_custUnit =None_, _builtInUnit =None_, _dispUnitsLbl =None_, _extLst =None_)[[source]](../_modules/openpyxl/chart/axis.html#DisplayUnitsLabelList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

builtInUnit
    

Value must be one of {‘tenThousands’, ‘trillions’, ‘hundredMillions’, ‘thousands’, ‘millions’, ‘hundredThousands’, ‘tenMillions’, ‘hundreds’, ‘billions’}

custUnit
    

Values must be of type <class ‘float’>

dispUnitsLbl
    

Values must be of type <class ‘openpyxl.chart.axis.DisplayUnitsLabel’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

tagname _ = 'dispUnits'_
    

_class _openpyxl.chart.axis.NumericAxis(_crossBetween =None_, _majorUnit =None_, _minorUnit =None_, _dispUnits =None_, _extLst =None_, _** kw_)[[source]](../_modules/openpyxl/chart/axis.html#NumericAxis)
    

Bases: `_BaseAxis`

axId
    

Values must be of type <class ‘int’>

axPos
    

Value must be one of {‘l’, ‘b’, ‘t’, ‘r’}

crossAx
    

Values must be of type <class ‘int’>

crossBetween
    

Value must be one of {‘between’, ‘midCat’}

crosses
    

Value must be one of {‘autoZero’, ‘max’, ‘min’}

crossesAt
    

Values must be of type <class ‘float’>

delete
    

Values must be of type <class ‘bool’>

dispUnits
    

Values must be of type <class ‘openpyxl.chart.axis.DisplayUnitsLabelList’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

_classmethod _from_tree(_node_)[[source]](../_modules/openpyxl/chart/axis.html#NumericAxis.from_tree)
    

Special case value axes with no gridlines

majorGridlines
    

Values must be of type <class ‘openpyxl.chart.axis.ChartLines’>

majorTickMark
    

Value must be one of {‘cross’, ‘out’, ‘in’}

majorUnit
    

Values must be of type <class ‘float’>

minorGridlines
    

Values must be of type <class ‘openpyxl.chart.axis.ChartLines’>

minorTickMark
    

Value must be one of {‘cross’, ‘out’, ‘in’}

minorUnit
    

Values must be of type <class ‘float’>

numFmt
    

Values must be of type <class ‘openpyxl.chart.data_source.NumFmt’>

scaling
    

Values must be of type <class ‘openpyxl.chart.axis.Scaling’>

spPr
    

Values must be of type <class ‘openpyxl.chart.shapes.GraphicalProperties’>

tagname _ = 'valAx'_
    

tickLblPos
    

Value must be one of {‘high’, ‘nextTo’, ‘low’}

title
    

Values must be of type <class ‘openpyxl.chart.title.Title’>

txPr
    

Values must be of type <class ‘openpyxl.chart.text.RichText’>

_class _openpyxl.chart.axis.Scaling(_logBase =None_, _orientation ='minMax'_, _max =None_, _min =None_, _extLst =None_)[[source]](../_modules/openpyxl/chart/axis.html#Scaling)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

logBase
    

Values must be of type <class ‘float’>

max
    

Values must be of type <class ‘float’>

min
    

Values must be of type <class ‘float’>

orientation
    

Value must be one of {‘minMax’, ‘maxMin’}

tagname _ = 'scaling'_
    

_class _openpyxl.chart.axis.SeriesAxis(_tickLblSkip =None_, _tickMarkSkip =None_, _extLst =None_, _** kw_)[[source]](../_modules/openpyxl/chart/axis.html#SeriesAxis)
    

Bases: `_BaseAxis`

axId
    

Values must be of type <class ‘int’>

axPos
    

Value must be one of {‘l’, ‘b’, ‘t’, ‘r’}

crossAx
    

Values must be of type <class ‘int’>

crosses
    

Value must be one of {‘autoZero’, ‘max’, ‘min’}

crossesAt
    

Values must be of type <class ‘float’>

delete
    

Values must be of type <class ‘bool’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

majorGridlines
    

Values must be of type <class ‘openpyxl.chart.axis.ChartLines’>

majorTickMark
    

Value must be one of {‘cross’, ‘out’, ‘in’}

minorGridlines
    

Values must be of type <class ‘openpyxl.chart.axis.ChartLines’>

minorTickMark
    

Value must be one of {‘cross’, ‘out’, ‘in’}

numFmt
    

Values must be of type <class ‘openpyxl.chart.data_source.NumFmt’>

scaling
    

Values must be of type <class ‘openpyxl.chart.axis.Scaling’>

spPr
    

Values must be of type <class ‘openpyxl.chart.shapes.GraphicalProperties’>

tagname _ = 'serAx'_
    

tickLblPos
    

Value must be one of {‘high’, ‘nextTo’, ‘low’}

tickLblSkip
    

Values must be of type <class ‘int’>

tickMarkSkip
    

Values must be of type <class ‘int’>

title
    

Values must be of type <class ‘openpyxl.chart.title.Title’>

txPr
    

Values must be of type <class ‘openpyxl.chart.text.RichText’>

_class _openpyxl.chart.axis.TextAxis(_auto =None_, _lblAlgn =None_, _lblOffset =100_, _tickLblSkip =None_, _tickMarkSkip =None_, _noMultiLvlLbl =None_, _extLst =None_, _** kw_)[[source]](../_modules/openpyxl/chart/axis.html#TextAxis)
    

Bases: `_BaseAxis`

auto
    

Values must be of type <class ‘bool’>

axId
    

Values must be of type <class ‘int’>

axPos
    

Value must be one of {‘l’, ‘b’, ‘t’, ‘r’}

crossAx
    

Values must be of type <class ‘int’>

crosses
    

Value must be one of {‘autoZero’, ‘max’, ‘min’}

crossesAt
    

Values must be of type <class ‘float’>

delete
    

Values must be of type <class ‘bool’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

lblAlgn
    

Value must be one of {‘l’, ‘ctr’, ‘r’}

lblOffset
    

Values must be of type <class ‘float’>

majorGridlines
    

Values must be of type <class ‘openpyxl.chart.axis.ChartLines’>

majorTickMark
    

Value must be one of {‘cross’, ‘out’, ‘in’}

minorGridlines
    

Values must be of type <class ‘openpyxl.chart.axis.ChartLines’>

minorTickMark
    

Value must be one of {‘cross’, ‘out’, ‘in’}

noMultiLvlLbl
    

Values must be of type <class ‘bool’>

numFmt
    

Values must be of type <class ‘openpyxl.chart.data_source.NumFmt’>

scaling
    

Values must be of type <class ‘openpyxl.chart.axis.Scaling’>

spPr
    

Values must be of type <class ‘openpyxl.chart.shapes.GraphicalProperties’>

tagname _ = 'catAx'_
    

tickLblPos
    

Value must be one of {‘high’, ‘nextTo’, ‘low’}

tickLblSkip
    

Values must be of type <class ‘int’>

tickMarkSkip
    

Values must be of type <class ‘int’>

title
    

Values must be of type <class ‘openpyxl.chart.title.Title’>

txPr
    

Values must be of type <class ‘openpyxl.chart.text.RichText’>

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.chart.axis module
    * `ChartLines`
      * `ChartLines.graphicalProperties`
      * `ChartLines.spPr`
      * `ChartLines.tagname`
    * `DateAxis`
      * `DateAxis.auto`
      * `DateAxis.axId`
      * `DateAxis.axPos`
      * `DateAxis.baseTimeUnit`
      * `DateAxis.crossAx`
      * `DateAxis.crosses`
      * `DateAxis.crossesAt`
      * `DateAxis.delete`
      * `DateAxis.extLst`
      * `DateAxis.lblOffset`
      * `DateAxis.majorGridlines`
      * `DateAxis.majorTickMark`
      * `DateAxis.majorTimeUnit`
      * `DateAxis.majorUnit`
      * `DateAxis.minorGridlines`
      * `DateAxis.minorTickMark`
      * `DateAxis.minorTimeUnit`
      * `DateAxis.minorUnit`
      * `DateAxis.numFmt`
      * `DateAxis.scaling`
      * `DateAxis.spPr`
      * `DateAxis.tagname`
      * `DateAxis.tickLblPos`
      * `DateAxis.title`
      * `DateAxis.txPr`
    * `DisplayUnitsLabel`
      * `DisplayUnitsLabel.graphicalProperties`
      * `DisplayUnitsLabel.layout`
      * `DisplayUnitsLabel.spPr`
      * `DisplayUnitsLabel.tagname`
      * `DisplayUnitsLabel.text`
      * `DisplayUnitsLabel.textPropertes`
      * `DisplayUnitsLabel.tx`
      * `DisplayUnitsLabel.txPr`
    * `DisplayUnitsLabelList`
      * `DisplayUnitsLabelList.builtInUnit`
      * `DisplayUnitsLabelList.custUnit`
      * `DisplayUnitsLabelList.dispUnitsLbl`
      * `DisplayUnitsLabelList.extLst`
      * `DisplayUnitsLabelList.tagname`
    * `NumericAxis`
      * `NumericAxis.axId`
      * `NumericAxis.axPos`
      * `NumericAxis.crossAx`
      * `NumericAxis.crossBetween`
      * `NumericAxis.crosses`
      * `NumericAxis.crossesAt`
      * `NumericAxis.delete`
      * `NumericAxis.dispUnits`
      * `NumericAxis.extLst`
      * `NumericAxis.from_tree()`
      * `NumericAxis.majorGridlines`
      * `NumericAxis.majorTickMark`
      * `NumericAxis.majorUnit`
      * `NumericAxis.minorGridlines`
      * `NumericAxis.minorTickMark`
      * `NumericAxis.minorUnit`
      * `NumericAxis.numFmt`
      * `NumericAxis.scaling`
      * `NumericAxis.spPr`
      * `NumericAxis.tagname`
      * `NumericAxis.tickLblPos`
      * `NumericAxis.title`
      * `NumericAxis.txPr`
    * `Scaling`
      * `Scaling.extLst`
      * `Scaling.logBase`
      * `Scaling.max`
      * `Scaling.min`
      * `Scaling.orientation`
      * `Scaling.tagname`
    * `SeriesAxis`
      * `SeriesAxis.axId`
      * `SeriesAxis.axPos`
      * `SeriesAxis.crossAx`
      * `SeriesAxis.crosses`
      * `SeriesAxis.crossesAt`
      * `SeriesAxis.delete`
      * `SeriesAxis.extLst`
      * `SeriesAxis.majorGridlines`
      * `SeriesAxis.majorTickMark`
      * `SeriesAxis.minorGridlines`
      * `SeriesAxis.minorTickMark`
      * `SeriesAxis.numFmt`
      * `SeriesAxis.scaling`
      * `SeriesAxis.spPr`
      * `SeriesAxis.tagname`
      * `SeriesAxis.tickLblPos`
      * `SeriesAxis.tickLblSkip`
      * `SeriesAxis.tickMarkSkip`
      * `SeriesAxis.title`
      * `SeriesAxis.txPr`
    * `TextAxis`
      * `TextAxis.auto`
      * `TextAxis.axId`
      * `TextAxis.axPos`
      * `TextAxis.crossAx`
      * `TextAxis.crosses`
      * `TextAxis.crossesAt`
      * `TextAxis.delete`
      * `TextAxis.extLst`
      * `TextAxis.lblAlgn`
      * `TextAxis.lblOffset`
      * `TextAxis.majorGridlines`
      * `TextAxis.majorTickMark`
      * `TextAxis.minorGridlines`
      * `TextAxis.minorTickMark`
      * `TextAxis.noMultiLvlLbl`
      * `TextAxis.numFmt`
      * `TextAxis.scaling`
      * `TextAxis.spPr`
      * `TextAxis.tagname`
      * `TextAxis.tickLblPos`
      * `TextAxis.tickLblSkip`
      * `TextAxis.tickMarkSkip`
      * `TextAxis.title`
      * `TextAxis.txPr`



#### Previous topic

[openpyxl.chart.area_chart module](openpyxl.chart.area_chart.html "previous chapter")

#### Next topic

[openpyxl.chart.bar_chart module](openpyxl.chart.bar_chart.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.chart.axis.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chart.bar_chart.html "openpyxl.chart.bar_chart module") |
  * [previous](openpyxl.chart.area_chart.html "openpyxl.chart.area_chart module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.chart package](openpyxl.chart.html) »
  * [openpyxl.chart.axis module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
