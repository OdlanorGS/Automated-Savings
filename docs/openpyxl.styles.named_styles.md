### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.styles.numbers.html "openpyxl.styles.numbers module") |
  * [previous](openpyxl.styles.fonts.html "openpyxl.styles.fonts module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.styles package](openpyxl.styles.html) »
  * [openpyxl.styles.named_styles module]()



# openpyxl.styles.named_styles module

_class _openpyxl.styles.named_styles.NamedStyle(_name ='Normal'_, _font =None_, _fill =None_, _border =None_, _alignment =None_, _number_format =None_, _protection =None_, _builtinId =None_, _hidden =False_, _xfId =None_)[[source]](../_modules/openpyxl/styles/named_styles.html#NamedStyle)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

Named and editable styles

alignment
    

Values must be of type <class ‘openpyxl.styles.alignment.Alignment’>

as_name()[[source]](../_modules/openpyxl/styles/named_styles.html#NamedStyle.as_name)
    

Return relevant named style

as_tuple()[[source]](../_modules/openpyxl/styles/named_styles.html#NamedStyle.as_tuple)
    

Return a style array representing the current style

as_xf()[[source]](../_modules/openpyxl/styles/named_styles.html#NamedStyle.as_xf)
    

Return equivalent XfStyle

bind(_wb_)[[source]](../_modules/openpyxl/styles/named_styles.html#NamedStyle.bind)
    

Bind a named style to a workbook

border
    

Values must be of type <class ‘openpyxl.styles.borders.Border’>

builtinId
    

Values must be of type <class ‘int’>

fill
    

Values must be of type <class ‘openpyxl.styles.fills.Fill’>

font
    

Values must be of type <class ‘openpyxl.styles.fonts.Font’>

hidden
    

Values must be of type <class ‘bool’>

name
    

Values must be of type <class ‘str’>

number_format
    

Values must be of type <class ‘str’>

protection
    

Values must be of type <class ‘openpyxl.styles.protection.Protection’>

xfId
    

Values must be of type <class ‘int’>

_class _openpyxl.styles.named_styles.NamedStyleList(_iterable =()_, _/_)[[source]](../_modules/openpyxl/styles/named_styles.html#NamedStyleList)
    

Bases: `list`

Named styles are editable and can be applied to multiple objects

As only the index is stored in referencing objects the order mus be preserved.

Returns a list of NamedStyles

append(_style_)[[source]](../_modules/openpyxl/styles/named_styles.html#NamedStyleList.append)
    

Append object to the end of the list.

_property _names
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.styles.named_styles module
    * `NamedStyle`
      * `NamedStyle.alignment`
      * `NamedStyle.as_name()`
      * `NamedStyle.as_tuple()`
      * `NamedStyle.as_xf()`
      * `NamedStyle.bind()`
      * `NamedStyle.border`
      * `NamedStyle.builtinId`
      * `NamedStyle.fill`
      * `NamedStyle.font`
      * `NamedStyle.hidden`
      * `NamedStyle.name`
      * `NamedStyle.number_format`
      * `NamedStyle.protection`
      * `NamedStyle.xfId`
    * `NamedStyleList`
      * `NamedStyleList.append()`
      * `NamedStyleList.names`



#### Previous topic

[openpyxl.styles.fonts module](openpyxl.styles.fonts.html "previous chapter")

#### Next topic

[openpyxl.styles.numbers module](openpyxl.styles.numbers.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.styles.named_styles.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.styles.numbers.html "openpyxl.styles.numbers module") |
  * [previous](openpyxl.styles.fonts.html "openpyxl.styles.fonts module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.styles package](openpyxl.styles.html) »
  * [openpyxl.styles.named_styles module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
