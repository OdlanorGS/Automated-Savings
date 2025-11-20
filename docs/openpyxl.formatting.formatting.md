### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.formatting.rule.html "openpyxl.formatting.rule module") |
  * [previous](openpyxl.formatting.html "openpyxl.formatting package") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.formatting package](openpyxl.formatting.html) »
  * [openpyxl.formatting.formatting module]()



# openpyxl.formatting.formatting module

_class _openpyxl.formatting.formatting.ConditionalFormatting(_sqref =()_, _pivot =None_, _cfRule =()_, _extLst =None_)[[source]](../_modules/openpyxl/formatting/formatting.html#ConditionalFormatting)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

cells
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

cfRule
    

A sequence (list or tuple) that may only contain objects of the declared type

pivot
    

Values must be of type <class ‘bool’>

rules
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

sqref
    

Values must be of type <class ‘openpyxl.worksheet.cell_range.MultiCellRange’>

tagname _ = 'conditionalFormatting'_
    

_class _openpyxl.formatting.formatting.ConditionalFormattingList[[source]](../_modules/openpyxl/formatting/formatting.html#ConditionalFormattingList)
    

Bases: `object`

Conditional formatting rules.

add(_range_string_ , _cfRule_)[[source]](../_modules/openpyxl/formatting/formatting.html#ConditionalFormattingList.add)
    

Add a rule such as ColorScaleRule, FormulaRule or CellIsRule

The priority will be added automatically.

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.formatting.formatting module
    * `ConditionalFormatting`
      * `ConditionalFormatting.cells`
      * `ConditionalFormatting.cfRule`
      * `ConditionalFormatting.pivot`
      * `ConditionalFormatting.rules`
      * `ConditionalFormatting.sqref`
      * `ConditionalFormatting.tagname`
    * `ConditionalFormattingList`
      * `ConditionalFormattingList.add()`



#### Previous topic

[openpyxl.formatting package](openpyxl.formatting.html "previous chapter")

#### Next topic

[openpyxl.formatting.rule module](openpyxl.formatting.rule.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.formatting.formatting.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.formatting.rule.html "openpyxl.formatting.rule module") |
  * [previous](openpyxl.formatting.html "openpyxl.formatting package") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.formatting package](openpyxl.formatting.html) »
  * [openpyxl.formatting.formatting module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
