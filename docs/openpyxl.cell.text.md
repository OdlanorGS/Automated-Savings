### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chart.html "openpyxl.chart package") |
  * [previous](openpyxl.cell.rich_text.html "openpyxl.cell.rich_text module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.cell package](openpyxl.cell.html) »
  * [openpyxl.cell.text module]()



# openpyxl.cell.text module

Richtext definition

_class _openpyxl.cell.text.InlineFont(_rFont =None_, _charset =None_, _family =None_, _b =None_, _i =None_, _strike =None_, _outline =None_, _shadow =None_, _condense =None_, _extend =None_, _color =None_, _sz =None_, _u =None_, _vertAlign =None_, _scheme =None_)[[source]](../_modules/openpyxl/cell/text.html#InlineFont)
    

Bases: [`Font`](openpyxl.styles.fonts.html#openpyxl.styles.fonts.Font "openpyxl.styles.fonts.Font")

Font for inline text because, yes what you need are different objects with the same elements but different constraints.

b
    

Values must be of type <class ‘bool’>

charset
    

Values must be of type <class ‘int’>

color
    

Values must be of type <class ‘openpyxl.styles.colors.Color’>

condense
    

Values must be of type <class ‘bool’>

extend
    

Values must be of type <class ‘bool’>

family
    

Values must be of type <class ‘float’>

i
    

Values must be of type <class ‘bool’>

outline
    

Values must be of type <class ‘bool’>

rFont
    

Values must be of type <class ‘str’>

scheme
    

Value must be one of {‘minor’, ‘major’}

shadow
    

Values must be of type <class ‘bool’>

strike
    

Values must be of type <class ‘bool’>

sz
    

Values must be of type <class ‘float’>

tagname _ = 'RPrElt'_
    

u
    

Value must be one of {‘single’, ‘double’, ‘doubleAccounting’, ‘singleAccounting’}

vertAlign
    

Value must be one of {‘superscript’, ‘baseline’, ‘subscript’}

_class _openpyxl.cell.text.PhoneticProperties(_fontId =None_, _type =None_, _alignment =None_)[[source]](../_modules/openpyxl/cell/text.html#PhoneticProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

alignment
    

Value must be one of {‘left’, ‘distributed’, ‘noControl’, ‘center’}

fontId
    

Values must be of type <class ‘int’>

tagname _ = 'phoneticPr'_
    

type
    

Value must be one of {‘Hiragana’, ‘fullwidthKatakana’, ‘noConversion’, ‘halfwidthKatakana’}

_class _openpyxl.cell.text.PhoneticText(_sb =None_, _eb =None_, _t =None_)[[source]](../_modules/openpyxl/cell/text.html#PhoneticText)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

eb
    

Values must be of type <class ‘int’>

sb
    

Values must be of type <class ‘int’>

t
    

Values must be of type <class ‘str’>

tagname _ = 'rPh'_
    

text
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

_class _openpyxl.cell.text.RichText(_rPr =None_, _t =None_)[[source]](../_modules/openpyxl/cell/text.html#RichText)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

font
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

rPr
    

Values must be of type <class ‘openpyxl.cell.text.InlineFont’>

t
    

Values must be of type <class ‘str’>

tagname _ = 'RElt'_
    

text
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

_class _openpyxl.cell.text.Text(_t =None_, _r =()_, _rPh =()_, _phoneticPr =None_)[[source]](../_modules/openpyxl/cell/text.html#Text)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

PhoneticProperties
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

_property _content
    

Text stripped of all formatting

formatted
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

phonetic
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

phoneticPr
    

Values must be of type <class ‘openpyxl.cell.text.PhoneticProperties’>

plain
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

r
    

A sequence (list or tuple) that may only contain objects of the declared type

rPh
    

A sequence (list or tuple) that may only contain objects of the declared type

t
    

Values must be of type <class ‘str’>

tagname _ = 'text'_
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.cell.text module
    * `InlineFont`
      * `InlineFont.b`
      * `InlineFont.charset`
      * `InlineFont.color`
      * `InlineFont.condense`
      * `InlineFont.extend`
      * `InlineFont.family`
      * `InlineFont.i`
      * `InlineFont.outline`
      * `InlineFont.rFont`
      * `InlineFont.scheme`
      * `InlineFont.shadow`
      * `InlineFont.strike`
      * `InlineFont.sz`
      * `InlineFont.tagname`
      * `InlineFont.u`
      * `InlineFont.vertAlign`
    * `PhoneticProperties`
      * `PhoneticProperties.alignment`
      * `PhoneticProperties.fontId`
      * `PhoneticProperties.tagname`
      * `PhoneticProperties.type`
    * `PhoneticText`
      * `PhoneticText.eb`
      * `PhoneticText.sb`
      * `PhoneticText.t`
      * `PhoneticText.tagname`
      * `PhoneticText.text`
    * `RichText`
      * `RichText.font`
      * `RichText.rPr`
      * `RichText.t`
      * `RichText.tagname`
      * `RichText.text`
    * `Text`
      * `Text.PhoneticProperties`
      * `Text.content`
      * `Text.formatted`
      * `Text.phonetic`
      * `Text.phoneticPr`
      * `Text.plain`
      * `Text.r`
      * `Text.rPh`
      * `Text.t`
      * `Text.tagname`



#### Previous topic

[openpyxl.cell.rich_text module](openpyxl.cell.rich_text.html "previous chapter")

#### Next topic

[openpyxl.chart package](openpyxl.chart.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.cell.text.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.chart.html "openpyxl.chart package") |
  * [previous](openpyxl.cell.rich_text.html "openpyxl.cell.rich_text module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.cell package](openpyxl.cell.html) »
  * [openpyxl.cell.text module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
