### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chart.descriptors.html "openpyxl.chart.descriptors module") |
  * [previous](openpyxl.chart.chartspace.html "openpyxl.chart.chartspace module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.chart package](openpyxl.chart.html) »
  * [openpyxl.chart.data_source module]()



# openpyxl.chart.data_source module

Collection of utility primitives for charts.

_class _openpyxl.chart.data_source.AxDataSource(_numRef =None_, _numLit =None_, _strRef =None_, _strLit =None_, _multiLvlStrRef =None_)[[source]](../_modules/openpyxl/chart/data_source.html#AxDataSource)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

multiLvlStrRef
    

Values must be of type <class ‘openpyxl.chart.data_source.MultiLevelStrRef’>

numLit
    

Values must be of type <class ‘openpyxl.chart.data_source.NumData’>

numRef
    

Values must be of type <class ‘openpyxl.chart.data_source.NumRef’>

strLit
    

Values must be of type <class ‘openpyxl.chart.data_source.StrData’>

strRef
    

Values must be of type <class ‘openpyxl.chart.data_source.StrRef’>

tagname _ = 'cat'_
    

_class _openpyxl.chart.data_source.Level(_pt =()_)[[source]](../_modules/openpyxl/chart/data_source.html#Level)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

pt
    

A sequence (list or tuple) that may only contain objects of the declared type

tagname _ = 'lvl'_
    

_class _openpyxl.chart.data_source.MultiLevelStrData(_ptCount =None_, _lvl =()_, _extLst =None_)[[source]](../_modules/openpyxl/chart/data_source.html#MultiLevelStrData)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

lvl
    

A sequence (list or tuple) that may only contain objects of the declared type

ptCount
    

Values must be of type <class ‘int’>

tagname _ = 'multiLvlStrData'_
    

_class _openpyxl.chart.data_source.MultiLevelStrRef(_f =None_, _multiLvlStrCache =None_, _extLst =None_)[[source]](../_modules/openpyxl/chart/data_source.html#MultiLevelStrRef)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

f
    

Values must be of type <class ‘str’>

multiLvlStrCache
    

Values must be of type <class ‘openpyxl.chart.data_source.MultiLevelStrData’>

tagname _ = 'multiLvlStrRef'_
    

_class _openpyxl.chart.data_source.NumData(_formatCode =None_, _ptCount =None_, _pt =()_, _extLst =None_)[[source]](../_modules/openpyxl/chart/data_source.html#NumData)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

formatCode
    

Values must be of type <class ‘str’>

pt
    

A sequence (list or tuple) that may only contain objects of the declared type

ptCount
    

Values must be of type <class ‘int’>

_class _openpyxl.chart.data_source.NumDataSource(_numRef =None_, _numLit =None_)[[source]](../_modules/openpyxl/chart/data_source.html#NumDataSource)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

numLit
    

Values must be of type <class ‘openpyxl.chart.data_source.NumData’>

numRef
    

Values must be of type <class ‘openpyxl.chart.data_source.NumRef’>

_class _openpyxl.chart.data_source.NumFmt(_formatCode =None_, _sourceLinked =False_)[[source]](../_modules/openpyxl/chart/data_source.html#NumFmt)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

formatCode
    

Values must be of type <class ‘str’>

sourceLinked
    

Values must be of type <class ‘bool’>

_class _openpyxl.chart.data_source.NumRef(_f =None_, _numCache =None_, _extLst =None_)[[source]](../_modules/openpyxl/chart/data_source.html#NumRef)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

f
    

Values must be of type <class ‘str’>

numCache
    

Values must be of type <class ‘openpyxl.chart.data_source.NumData’>

ref
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

_class _openpyxl.chart.data_source.NumVal(_idx =None_, _formatCode =None_, _v =None_)[[source]](../_modules/openpyxl/chart/data_source.html#NumVal)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

formatCode
    

Values must be of type <class ‘str’>

idx
    

Values must be of type <class ‘int’>

v
    

Values must be of type <class ‘NoneType’>

_class _openpyxl.chart.data_source.NumberValueDescriptor(_* args_, _** kw_)[[source]](../_modules/openpyxl/chart/data_source.html#NumberValueDescriptor)
    

Bases: [`NestedText`](openpyxl.descriptors.nested.html#openpyxl.descriptors.nested.NestedText "openpyxl.descriptors.nested.NestedText")

Data should be numerical but isn’t always :-/

allow_none _ = True_
    

_class _openpyxl.chart.data_source.StrData(_ptCount =None_, _pt =()_, _extLst =None_)[[source]](../_modules/openpyxl/chart/data_source.html#StrData)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

pt
    

A sequence (list or tuple) that may only contain objects of the declared type

ptCount
    

Values must be of type <class ‘int’>

tagname _ = 'strData'_
    

_class _openpyxl.chart.data_source.StrRef(_f =None_, _strCache =None_, _extLst =None_)[[source]](../_modules/openpyxl/chart/data_source.html#StrRef)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

f
    

Values must be of type <class ‘str’>

strCache
    

Values must be of type <class ‘openpyxl.chart.data_source.StrData’>

tagname _ = 'strRef'_
    

_class _openpyxl.chart.data_source.StrVal(_idx =0_, _v =None_)[[source]](../_modules/openpyxl/chart/data_source.html#StrVal)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

idx
    

Values must be of type <class ‘int’>

tagname _ = 'strVal'_
    

v
    

Values must be of type <class ‘str’>

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.chart.data_source module
    * `AxDataSource`
      * `AxDataSource.multiLvlStrRef`
      * `AxDataSource.numLit`
      * `AxDataSource.numRef`
      * `AxDataSource.strLit`
      * `AxDataSource.strRef`
      * `AxDataSource.tagname`
    * `Level`
      * `Level.pt`
      * `Level.tagname`
    * `MultiLevelStrData`
      * `MultiLevelStrData.extLst`
      * `MultiLevelStrData.lvl`
      * `MultiLevelStrData.ptCount`
      * `MultiLevelStrData.tagname`
    * `MultiLevelStrRef`
      * `MultiLevelStrRef.extLst`
      * `MultiLevelStrRef.f`
      * `MultiLevelStrRef.multiLvlStrCache`
      * `MultiLevelStrRef.tagname`
    * `NumData`
      * `NumData.extLst`
      * `NumData.formatCode`
      * `NumData.pt`
      * `NumData.ptCount`
    * `NumDataSource`
      * `NumDataSource.numLit`
      * `NumDataSource.numRef`
    * `NumFmt`
      * `NumFmt.formatCode`
      * `NumFmt.sourceLinked`
    * `NumRef`
      * `NumRef.extLst`
      * `NumRef.f`
      * `NumRef.numCache`
      * `NumRef.ref`
    * `NumVal`
      * `NumVal.formatCode`
      * `NumVal.idx`
      * `NumVal.v`
    * `NumberValueDescriptor`
      * `NumberValueDescriptor.allow_none`
    * `StrData`
      * `StrData.extLst`
      * `StrData.pt`
      * `StrData.ptCount`
      * `StrData.tagname`
    * `StrRef`
      * `StrRef.extLst`
      * `StrRef.f`
      * `StrRef.strCache`
      * `StrRef.tagname`
    * `StrVal`
      * `StrVal.idx`
      * `StrVal.tagname`
      * `StrVal.v`



#### Previous topic

[openpyxl.chart.chartspace module](openpyxl.chart.chartspace.html "previous chapter")

#### Next topic

[openpyxl.chart.descriptors module](openpyxl.chart.descriptors.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.chart.data_source.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chart.descriptors.html "openpyxl.chart.descriptors module") |
  * [previous](openpyxl.chart.chartspace.html "openpyxl.chart.chartspace module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.chart package](openpyxl.chart.html) »
  * [openpyxl.chart.data_source module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
