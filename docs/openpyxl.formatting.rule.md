### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.packaging.html "openpyxl.packaging package") |
  * [previous](openpyxl.formatting.formatting.html "openpyxl.formatting.formatting module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.formatting package](openpyxl.formatting.html) »
  * [openpyxl.formatting.rule module]()



# openpyxl.formatting.rule module

openpyxl.formatting.rule.CellIsRule(_operator =None_, _formula =None_, _stopIfTrue =None_, _font =None_, _border =None_, _fill =None_)[[source]](../_modules/openpyxl/formatting/rule.html#CellIsRule)
    

Conditional formatting rule based on cell contents.

_class _openpyxl.formatting.rule.ColorScale(_cfvo =None_, _color =None_)[[source]](../_modules/openpyxl/formatting/rule.html#ColorScale)
    

Bases: `RuleType`

color
    

A sequence (list or tuple) that may only contain objects of the declared type

tagname _ = 'colorScale'_
    

openpyxl.formatting.rule.ColorScaleRule(_start_type =None_, _start_value =None_, _start_color =None_, _mid_type =None_, _mid_value =None_, _mid_color =None_, _end_type =None_, _end_value =None_, _end_color =None_)[[source]](../_modules/openpyxl/formatting/rule.html#ColorScaleRule)
    

Backwards compatibility

_class _openpyxl.formatting.rule.DataBar(_minLength =None_, _maxLength =None_, _showValue =None_, _cfvo =None_, _color =None_)[[source]](../_modules/openpyxl/formatting/rule.html#DataBar)
    

Bases: `RuleType`

color
    

Values must be of type <class ‘openpyxl.styles.colors.Color’>

maxLength
    

Values must be of type <class ‘int’>

minLength
    

Values must be of type <class ‘int’>

showValue
    

Values must be of type <class ‘bool’>

tagname _ = 'dataBar'_
    

openpyxl.formatting.rule.DataBarRule(_start_type =None_, _start_value =None_, _end_type =None_, _end_value =None_, _color =None_, _showValue =None_, _minLength =None_, _maxLength =None_)[[source]](../_modules/openpyxl/formatting/rule.html#DataBarRule)
    

_class _openpyxl.formatting.rule.FormatObject(_type_ , _val =None_, _gte =None_, _extLst =None_)[[source]](../_modules/openpyxl/formatting/rule.html#FormatObject)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

gte
    

Values must be of type <class ‘bool’>

tagname _ = 'cfvo'_
    

type
    

Value must be one of {‘min’, ‘formula’, ‘num’, ‘percentile’, ‘max’, ‘percent’}

val
    

Values must be of type <class ‘float’>

openpyxl.formatting.rule.FormulaRule(_formula =None_, _stopIfTrue =None_, _font =None_, _border =None_, _fill =None_)[[source]](../_modules/openpyxl/formatting/rule.html#FormulaRule)
    

Conditional formatting with custom differential style

_class _openpyxl.formatting.rule.IconSet(_iconSet =None_, _showValue =None_, _percent =None_, _reverse =None_, _cfvo =None_)[[source]](../_modules/openpyxl/formatting/rule.html#IconSet)
    

Bases: `RuleType`

iconSet
    

Value must be one of {‘3Symbols’, ‘5Arrows’, ‘3Arrows’, ‘3Flags’, ‘3TrafficLights1’, ‘3Signs’, ‘3Symbols2’, ‘4ArrowsGray’, ‘4RedToBlack’, ‘4TrafficLights’, ‘5ArrowsGray’, ‘5Rating’, ‘3TrafficLights2’, ‘4Arrows’, ‘4Rating’, ‘5Quarters’, ‘3ArrowsGray’}

percent
    

Values must be of type <class ‘bool’>

reverse
    

Values must be of type <class ‘bool’>

showValue
    

Values must be of type <class ‘bool’>

tagname _ = 'iconSet'_
    

openpyxl.formatting.rule.IconSetRule(_icon_style =None_, _type =None_, _values =None_, _showValue =None_, _percent =None_, _reverse =None_)[[source]](../_modules/openpyxl/formatting/rule.html#IconSetRule)
    

Convenience function for creating icon set rules

_class _openpyxl.formatting.rule.Rule(_type_ , _dxfId =None_, _priority =0_, _stopIfTrue =None_, _aboveAverage =None_, _percent =None_, _bottom =None_, _operator =None_, _text =None_, _timePeriod =None_, _rank =None_, _stdDev =None_, _equalAverage =None_, _formula =()_, _colorScale =None_, _dataBar =None_, _iconSet =None_, _extLst =None_, _dxf =None_)[[source]](../_modules/openpyxl/formatting/rule.html#Rule)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

aboveAverage
    

Values must be of type <class ‘bool’>

bottom
    

Values must be of type <class ‘bool’>

colorScale
    

Values must be of type <class ‘openpyxl.formatting.rule.ColorScale’>

dataBar
    

Values must be of type <class ‘openpyxl.formatting.rule.DataBar’>

dxf
    

Values must be of type <class ‘openpyxl.styles.differential.DifferentialStyle’>

dxfId
    

Values must be of type <class ‘int’>

equalAverage
    

Values must be of type <class ‘bool’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

formula
    

A sequence (list or tuple) that may only contain objects of the declared type

iconSet
    

Values must be of type <class ‘openpyxl.formatting.rule.IconSet’>

operator
    

Value must be one of {‘containsText’, ‘lessThanOrEqual’, ‘notBetween’, ‘lessThan’, ‘notContains’, ‘beginsWith’, ‘equal’, ‘greaterThanOrEqual’, ‘between’, ‘endsWith’, ‘notEqual’, ‘greaterThan’}

percent
    

Values must be of type <class ‘bool’>

priority
    

Values must be of type <class ‘int’>

rank
    

Values must be of type <class ‘int’>

stdDev
    

Values must be of type <class ‘int’>

stopIfTrue
    

Values must be of type <class ‘bool’>

tagname _ = 'cfRule'_
    

text
    

Values must be of type <class ‘str’>

timePeriod
    

Value must be one of {‘tomorrow’, ‘last7Days’, ‘nextMonth’, ‘lastWeek’, ‘thisMonth’, ‘today’, ‘thisWeek’, ‘lastMonth’, ‘nextWeek’, ‘yesterday’}

type
    

Value must be one of {‘duplicateValues’, ‘containsText’, ‘notContainsText’, ‘timePeriod’, ‘beginsWith’, ‘endsWith’, ‘aboveAverage’, ‘expression’, ‘top10’, ‘notContainsBlanks’, ‘notContainsErrors’, ‘dataBar’, ‘cellIs’, ‘iconSet’, ‘uniqueValues’, ‘colorScale’, ‘containsErrors’, ‘containsBlanks’}

_class _openpyxl.formatting.rule.RuleType[[source]](../_modules/openpyxl/formatting/rule.html#RuleType)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

cfvo
    

A sequence (list or tuple) that may only contain objects of the declared type

_class _openpyxl.formatting.rule.ValueDescriptor(_* args_, _** kw_)[[source]](../_modules/openpyxl/formatting/rule.html#ValueDescriptor)
    

Bases: [`Float`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Float "openpyxl.descriptors.base.Float")

Expected type depends upon type attribute of parent :-(

Most values should be numeric BUT they can also be cell references

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.formatting.rule module
    * `CellIsRule()`
    * `ColorScale`
      * `ColorScale.color`
      * `ColorScale.tagname`
    * `ColorScaleRule()`
    * `DataBar`
      * `DataBar.color`
      * `DataBar.maxLength`
      * `DataBar.minLength`
      * `DataBar.showValue`
      * `DataBar.tagname`
    * `DataBarRule()`
    * `FormatObject`
      * `FormatObject.extLst`
      * `FormatObject.gte`
      * `FormatObject.tagname`
      * `FormatObject.type`
      * `FormatObject.val`
    * `FormulaRule()`
    * `IconSet`
      * `IconSet.iconSet`
      * `IconSet.percent`
      * `IconSet.reverse`
      * `IconSet.showValue`
      * `IconSet.tagname`
    * `IconSetRule()`
    * `Rule`
      * `Rule.aboveAverage`
      * `Rule.bottom`
      * `Rule.colorScale`
      * `Rule.dataBar`
      * `Rule.dxf`
      * `Rule.dxfId`
      * `Rule.equalAverage`
      * `Rule.extLst`
      * `Rule.formula`
      * `Rule.iconSet`
      * `Rule.operator`
      * `Rule.percent`
      * `Rule.priority`
      * `Rule.rank`
      * `Rule.stdDev`
      * `Rule.stopIfTrue`
      * `Rule.tagname`
      * `Rule.text`
      * `Rule.timePeriod`
      * `Rule.type`
    * `RuleType`
      * `RuleType.cfvo`
    * `ValueDescriptor`



#### Previous topic

[openpyxl.formatting.formatting module](openpyxl.formatting.formatting.html "previous chapter")

#### Next topic

[openpyxl.packaging package](openpyxl.packaging.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.formatting.rule.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.packaging.html "openpyxl.packaging package") |
  * [previous](openpyxl.formatting.formatting.html "openpyxl.formatting.formatting module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.formatting package](openpyxl.formatting.html) »
  * [openpyxl.formatting.rule module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
