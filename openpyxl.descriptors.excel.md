### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.descriptors.namespace.html "openpyxl.descriptors.namespace module") |
  * [previous](openpyxl.descriptors.container.html "openpyxl.descriptors.container module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.descriptors package](openpyxl.descriptors.html) »
  * [openpyxl.descriptors.excel module]()



# openpyxl.descriptors.excel module

Excel specific descriptors

_class _openpyxl.descriptors.excel.Base64Binary(_name =None_, _** kw_)[[source]](../_modules/openpyxl/descriptors/excel.html#Base64Binary)
    

Bases: [`MatchPattern`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.MatchPattern "openpyxl.descriptors.base.MatchPattern")

pattern _ = '^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{4})$'_
    

_class _openpyxl.descriptors.excel.CellRange(_name =None_, _** kw_)[[source]](../_modules/openpyxl/descriptors/excel.html#CellRange)
    

Bases: [`MatchPattern`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.MatchPattern "openpyxl.descriptors.base.MatchPattern")

allow_none _ = True_
    

pattern _ = '^[$]?([A-Za-z]{1,3})[$]?(\\\d+)(:[$]?([A-Za-z]{1,3})[$]?(\\\d+)?)?$|^[A-Za-z]{1,3}:[A-Za-z]{1,3}$'_
    

_class _openpyxl.descriptors.excel.Extension(_uri =None_)[[source]](../_modules/openpyxl/descriptors/excel.html#Extension)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

uri
    

Values must be of type <class ‘str’>

_class _openpyxl.descriptors.excel.ExtensionList(_ext =()_)[[source]](../_modules/openpyxl/descriptors/excel.html#ExtensionList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

ext
    

A sequence (list or tuple) that may only contain objects of the declared type

_class _openpyxl.descriptors.excel.Guid(_name =None_, _** kw_)[[source]](../_modules/openpyxl/descriptors/excel.html#Guid)
    

Bases: [`MatchPattern`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.MatchPattern "openpyxl.descriptors.base.MatchPattern")

pattern _ = '{[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}\\\\}'_
    

_class _openpyxl.descriptors.excel.HexBinary(_name =None_, _** kw_)[[source]](../_modules/openpyxl/descriptors/excel.html#HexBinary)
    

Bases: [`MatchPattern`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.MatchPattern "openpyxl.descriptors.base.MatchPattern")

pattern _ = '[0-9a-fA-F]+$'_
    

_class _openpyxl.descriptors.excel.Percentage(_** kw_)[[source]](../_modules/openpyxl/descriptors/excel.html#Percentage)
    

Bases: [`MinMax`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.MinMax "openpyxl.descriptors.base.MinMax")

max _ = 1000000_
    

min _ = -1000000_
    

pattern _ = '((100)|([0-9][0-9]?))(\\\\.[0-9][0-9]?)?%'_
    

_class _openpyxl.descriptors.excel.Relation(_* args_, _** kw_)[[source]](../_modules/openpyxl/descriptors/excel.html#Relation)
    

Bases: [`String`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.String "openpyxl.descriptors.base.String")

allow_none _ = True_
    

namespace _ = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'_
    

_class _openpyxl.descriptors.excel.TextPoint(_** kw_)[[source]](../_modules/openpyxl/descriptors/excel.html#TextPoint)
    

Bases: [`MinMax`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.MinMax "openpyxl.descriptors.base.MinMax")

Size in hundredths of points. In theory other units of measurement can be used but these are unbounded

expected_type
    

alias of `int`

max _ = 400000_
    

min _ = -400000_
    

_class _openpyxl.descriptors.excel.UniversalMeasure(_name =None_, _** kw_)[[source]](../_modules/openpyxl/descriptors/excel.html#UniversalMeasure)
    

Bases: [`MatchPattern`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.MatchPattern "openpyxl.descriptors.base.MatchPattern")

pattern _ = '[0-9]+(\\\\.[0-9]+)?(mm|cm|in|pt|pc|pi)'_
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.descriptors.excel module
    * `Base64Binary`
      * `Base64Binary.pattern`
    * `CellRange`
      * `CellRange.allow_none`
      * `CellRange.pattern`
    * `Extension`
      * `Extension.uri`
    * `ExtensionList`
      * `ExtensionList.ext`
    * `Guid`
      * `Guid.pattern`
    * `HexBinary`
      * `HexBinary.pattern`
    * `Percentage`
      * `Percentage.max`
      * `Percentage.min`
      * `Percentage.pattern`
    * `Relation`
      * `Relation.allow_none`
      * `Relation.namespace`
    * `TextPoint`
      * `TextPoint.expected_type`
      * `TextPoint.max`
      * `TextPoint.min`
    * `UniversalMeasure`
      * `UniversalMeasure.pattern`



#### Previous topic

[openpyxl.descriptors.container module](openpyxl.descriptors.container.html "previous chapter")

#### Next topic

[openpyxl.descriptors.namespace module](openpyxl.descriptors.namespace.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.descriptors.excel.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.descriptors.namespace.html "openpyxl.descriptors.namespace module") |
  * [previous](openpyxl.descriptors.container.html "openpyxl.descriptors.container module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.descriptors package](openpyxl.descriptors.html) »
  * [openpyxl.descriptors.excel module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
