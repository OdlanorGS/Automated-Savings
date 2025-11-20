### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chart.title.html "openpyxl.chart.title module") |
  * [previous](openpyxl.chart.surface_chart.html "openpyxl.chart.surface_chart module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.chart package](openpyxl.chart.html) »
  * [openpyxl.chart.text module]()



# openpyxl.chart.text module

_class _openpyxl.chart.text.RichText(_bodyPr =None_, _lstStyle =None_, _p =None_)[[source]](../_modules/openpyxl/chart/text.html#RichText)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

From the specification: 21.2.2.216

This element specifies text formatting. The lstStyle element is not supported.

bodyPr
    

Values must be of type <class ‘openpyxl.drawing.text.RichTextProperties’>

lstStyle
    

Values must be of type <class ‘openpyxl.drawing.text.ListStyle’>

p
    

A sequence (list or tuple) that may only contain objects of the declared type

paragraphs
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

properties
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

tagname _ = 'rich'_
    

_class _openpyxl.chart.text.Text(_strRef =None_, _rich =None_)[[source]](../_modules/openpyxl/chart/text.html#Text)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

The value can be either a cell reference or a text element If both are present then the reference will be used.

rich
    

Values must be of type <class ‘openpyxl.chart.text.RichText’>

strRef
    

Values must be of type <class ‘openpyxl.chart.data_source.StrRef’>

tagname _ = 'tx'_
    

to_tree(_tagname =None_, _idx =None_, _namespace =None_)[[source]](../_modules/openpyxl/chart/text.html#Text.to_tree)
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.chart.text module
    * `RichText`
      * `RichText.bodyPr`
      * `RichText.lstStyle`
      * `RichText.p`
      * `RichText.paragraphs`
      * `RichText.properties`
      * `RichText.tagname`
    * `Text`
      * `Text.rich`
      * `Text.strRef`
      * `Text.tagname`
      * `Text.to_tree()`



#### Previous topic

[openpyxl.chart.surface_chart module](openpyxl.chart.surface_chart.html "previous chapter")

#### Next topic

[openpyxl.chart.title module](openpyxl.chart.title.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.chart.text.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chart.title.html "openpyxl.chart.title module") |
  * [previous](openpyxl.chart.surface_chart.html "openpyxl.chart.surface_chart module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.chart package](openpyxl.chart.html) »
  * [openpyxl.chart.text module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
