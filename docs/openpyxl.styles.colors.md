### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.styles.differential.html "openpyxl.styles.differential module") |
  * [previous](openpyxl.styles.cell_style.html "openpyxl.styles.cell_style module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.styles package](openpyxl.styles.html) »
  * [openpyxl.styles.colors module]()



# openpyxl.styles.colors module

_class _openpyxl.styles.colors.Color(_rgb ='00000000'_, _indexed =None_, _auto =None_, _theme =None_, _tint =0.0_, _index =None_, _type ='rgb'_)[[source]](../_modules/openpyxl/styles/colors.html#Color)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

Named colors for use in styles.

auto
    

Values must be of type <class ‘bool’>

_property _index
    

indexed
    

Values must be of type <class ‘int’>

rgb
    

Values must be of type <class ‘str’>

tagname _ = 'color'_
    

theme
    

Values must be of type <class ‘int’>

tint
    

Values must be of type <class ‘float’>

type
    

Values must be of type <class ‘str’>

_property _value
    

_class _openpyxl.styles.colors.ColorDescriptor(_* args_, _** kw_)[[source]](../_modules/openpyxl/styles/colors.html#ColorDescriptor)
    

Bases: [`Typed`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Typed "openpyxl.descriptors.base.Typed")

expected_type
    

alias of `Color`

_class _openpyxl.styles.colors.ColorList(_indexedColors =()_, _mruColors =()_)[[source]](../_modules/openpyxl/styles/colors.html#ColorList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

_property _index
    

indexedColors
    

Wrap a sequence in an containing object

mruColors
    

Wrap a sequence in an containing object

tagname _ = 'colors'_
    

_class _openpyxl.styles.colors.RGB(_* args_, _** kw_)[[source]](../_modules/openpyxl/styles/colors.html#RGB)
    

Bases: [`Typed`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Typed "openpyxl.descriptors.base.Typed")

Descriptor for aRGB values If not supplied alpha is 00

expected_type
    

alias of `str`

_class _openpyxl.styles.colors.RgbColor(_rgb =None_)[[source]](../_modules/openpyxl/styles/colors.html#RgbColor)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

rgb
    

Values must be of type <class ‘str’>

tagname _ = 'rgbColor'_
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.styles.colors module
    * `Color`
      * `Color.auto`
      * `Color.index`
      * `Color.indexed`
      * `Color.rgb`
      * `Color.tagname`
      * `Color.theme`
      * `Color.tint`
      * `Color.type`
      * `Color.value`
    * `ColorDescriptor`
      * `ColorDescriptor.expected_type`
    * `ColorList`
      * `ColorList.index`
      * `ColorList.indexedColors`
      * `ColorList.mruColors`
      * `ColorList.tagname`
    * `RGB`
      * `RGB.expected_type`
    * `RgbColor`
      * `RgbColor.rgb`
      * `RgbColor.tagname`



#### Previous topic

[openpyxl.styles.cell_style module](openpyxl.styles.cell_style.html "previous chapter")

#### Next topic

[openpyxl.styles.differential module](openpyxl.styles.differential.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.styles.colors.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.styles.differential.html "openpyxl.styles.differential module") |
  * [previous](openpyxl.styles.cell_style.html "openpyxl.styles.cell_style module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.styles package](openpyxl.styles.html) »
  * [openpyxl.styles.colors module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
