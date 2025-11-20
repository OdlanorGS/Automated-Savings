### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.styles.protection.html "openpyxl.styles.protection module") |
  * [previous](openpyxl.styles.named_styles.html "openpyxl.styles.named_styles module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.styles package](openpyxl.styles.html) »
  * [openpyxl.styles.numbers module]()



# openpyxl.styles.numbers module

_class _openpyxl.styles.numbers.NumberFormat(_numFmtId =None_, _formatCode =None_)[[source]](../_modules/openpyxl/styles/numbers.html#NumberFormat)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

formatCode
    

Values must be of type <class ‘str’>

numFmtId
    

Values must be of type <class ‘int’>

_class _openpyxl.styles.numbers.NumberFormatDescriptor(_* args_, _** kw_)[[source]](../_modules/openpyxl/styles/numbers.html#NumberFormatDescriptor)
    

Bases: [`String`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.String "openpyxl.descriptors.base.String")

_class _openpyxl.styles.numbers.NumberFormatList(_count =None_, _numFmt =()_)[[source]](../_modules/openpyxl/styles/numbers.html#NumberFormatList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

_property _count
    

numFmt
    

A sequence (list or tuple) that may only contain objects of the declared type

openpyxl.styles.numbers.builtin_format_code(_index_)[[source]](../_modules/openpyxl/styles/numbers.html#builtin_format_code)
    

Return one of the standard format codes by index.

openpyxl.styles.numbers.builtin_format_id(_fmt_)[[source]](../_modules/openpyxl/styles/numbers.html#builtin_format_id)
    

Return the id of a standard style.

openpyxl.styles.numbers.is_builtin(_fmt_)[[source]](../_modules/openpyxl/styles/numbers.html#is_builtin)
    

openpyxl.styles.numbers.is_date_format(_fmt_)[[source]](../_modules/openpyxl/styles/numbers.html#is_date_format)
    

openpyxl.styles.numbers.is_datetime(_fmt_)[[source]](../_modules/openpyxl/styles/numbers.html#is_datetime)
    

Return date, time or datetime

openpyxl.styles.numbers.is_timedelta_format(_fmt_)[[source]](../_modules/openpyxl/styles/numbers.html#is_timedelta_format)
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.styles.numbers module
    * `NumberFormat`
      * `NumberFormat.formatCode`
      * `NumberFormat.numFmtId`
    * `NumberFormatDescriptor`
    * `NumberFormatList`
      * `NumberFormatList.count`
      * `NumberFormatList.numFmt`
    * `builtin_format_code()`
    * `builtin_format_id()`
    * `is_builtin()`
    * `is_date_format()`
    * `is_datetime()`
    * `is_timedelta_format()`



#### Previous topic

[openpyxl.styles.named_styles module](openpyxl.styles.named_styles.html "previous chapter")

#### Next topic

[openpyxl.styles.protection module](openpyxl.styles.protection.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.styles.numbers.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.styles.protection.html "openpyxl.styles.protection module") |
  * [previous](openpyxl.styles.named_styles.html "openpyxl.styles.named_styles module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.styles package](openpyxl.styles.html) »
  * [openpyxl.styles.numbers module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
