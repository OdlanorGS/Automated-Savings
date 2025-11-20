### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.formatting.formatting.html "openpyxl.formatting.formatting module") |
  * [previous](openpyxl.drawing.xdr.html "openpyxl.drawing.xdr module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.formatting package]()



# openpyxl.formatting package

## Submodules

  * [openpyxl.formatting.formatting module](openpyxl.formatting.formatting.html)
    * [`ConditionalFormatting`](openpyxl.formatting.formatting.html#openpyxl.formatting.formatting.ConditionalFormatting)
      * [`ConditionalFormatting.cells`](openpyxl.formatting.formatting.html#openpyxl.formatting.formatting.ConditionalFormatting.cells)
      * [`ConditionalFormatting.cfRule`](openpyxl.formatting.formatting.html#openpyxl.formatting.formatting.ConditionalFormatting.cfRule)
      * [`ConditionalFormatting.pivot`](openpyxl.formatting.formatting.html#openpyxl.formatting.formatting.ConditionalFormatting.pivot)
      * [`ConditionalFormatting.rules`](openpyxl.formatting.formatting.html#openpyxl.formatting.formatting.ConditionalFormatting.rules)
      * [`ConditionalFormatting.sqref`](openpyxl.formatting.formatting.html#openpyxl.formatting.formatting.ConditionalFormatting.sqref)
      * [`ConditionalFormatting.tagname`](openpyxl.formatting.formatting.html#openpyxl.formatting.formatting.ConditionalFormatting.tagname)
    * [`ConditionalFormattingList`](openpyxl.formatting.formatting.html#openpyxl.formatting.formatting.ConditionalFormattingList)
      * [`ConditionalFormattingList.add()`](openpyxl.formatting.formatting.html#openpyxl.formatting.formatting.ConditionalFormattingList.add)
  * [openpyxl.formatting.rule module](openpyxl.formatting.rule.html)
    * [`CellIsRule()`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.CellIsRule)
    * [`ColorScale`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.ColorScale)
      * [`ColorScale.color`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.ColorScale.color)
      * [`ColorScale.tagname`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.ColorScale.tagname)
    * [`ColorScaleRule()`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.ColorScaleRule)
    * [`DataBar`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.DataBar)
      * [`DataBar.color`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.DataBar.color)
      * [`DataBar.maxLength`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.DataBar.maxLength)
      * [`DataBar.minLength`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.DataBar.minLength)
      * [`DataBar.showValue`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.DataBar.showValue)
      * [`DataBar.tagname`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.DataBar.tagname)
    * [`DataBarRule()`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.DataBarRule)
    * [`FormatObject`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.FormatObject)
      * [`FormatObject.extLst`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.FormatObject.extLst)
      * [`FormatObject.gte`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.FormatObject.gte)
      * [`FormatObject.tagname`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.FormatObject.tagname)
      * [`FormatObject.type`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.FormatObject.type)
      * [`FormatObject.val`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.FormatObject.val)
    * [`FormulaRule()`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.FormulaRule)
    * [`IconSet`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.IconSet)
      * [`IconSet.iconSet`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.IconSet.iconSet)
      * [`IconSet.percent`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.IconSet.percent)
      * [`IconSet.reverse`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.IconSet.reverse)
      * [`IconSet.showValue`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.IconSet.showValue)
      * [`IconSet.tagname`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.IconSet.tagname)
    * [`IconSetRule()`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.IconSetRule)
    * [`Rule`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.Rule)
      * [`Rule.aboveAverage`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.Rule.aboveAverage)
      * [`Rule.bottom`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.Rule.bottom)
      * [`Rule.colorScale`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.Rule.colorScale)
      * [`Rule.dataBar`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.Rule.dataBar)
      * [`Rule.dxf`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.Rule.dxf)
      * [`Rule.dxfId`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.Rule.dxfId)
      * [`Rule.equalAverage`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.Rule.equalAverage)
      * [`Rule.extLst`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.Rule.extLst)
      * [`Rule.formula`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.Rule.formula)
      * [`Rule.iconSet`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.Rule.iconSet)
      * [`Rule.operator`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.Rule.operator)
      * [`Rule.percent`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.Rule.percent)
      * [`Rule.priority`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.Rule.priority)
      * [`Rule.rank`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.Rule.rank)
      * [`Rule.stdDev`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.Rule.stdDev)
      * [`Rule.stopIfTrue`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.Rule.stopIfTrue)
      * [`Rule.tagname`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.Rule.tagname)
      * [`Rule.text`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.Rule.text)
      * [`Rule.timePeriod`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.Rule.timePeriod)
      * [`Rule.type`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.Rule.type)
    * [`RuleType`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.RuleType)
      * [`RuleType.cfvo`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.RuleType.cfvo)
    * [`ValueDescriptor`](openpyxl.formatting.rule.html#openpyxl.formatting.rule.ValueDescriptor)



[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.formatting package
    * Submodules



#### Previous topic

[openpyxl.drawing.xdr module](openpyxl.drawing.xdr.html "previous chapter")

#### Next topic

[openpyxl.formatting.formatting module](openpyxl.formatting.formatting.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.formatting.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.formatting.formatting.html "openpyxl.formatting.formatting module") |
  * [previous](openpyxl.drawing.xdr.html "openpyxl.drawing.xdr module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.formatting package]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
