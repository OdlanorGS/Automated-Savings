### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.styles.fills.html "openpyxl.styles.fills module") |
  * [previous](openpyxl.styles.colors.html "openpyxl.styles.colors module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.styles package](openpyxl.styles.html) »
  * [openpyxl.styles.differential module]()



# openpyxl.styles.differential module

_class _openpyxl.styles.differential.DifferentialStyle(_font =None_, _numFmt =None_, _fill =None_, _alignment =None_, _border =None_, _protection =None_, _extLst =None_)[[source]](../_modules/openpyxl/styles/differential.html#DifferentialStyle)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

alignment
    

Values must be of type <class ‘openpyxl.styles.alignment.Alignment’>

border
    

Values must be of type <class ‘openpyxl.styles.borders.Border’>

fill
    

Values must be of type <class ‘openpyxl.styles.fills.Fill’>

font
    

Values must be of type <class ‘openpyxl.styles.fonts.Font’>

numFmt
    

Values must be of type <class ‘openpyxl.styles.numbers.NumberFormat’>

protection
    

Values must be of type <class ‘openpyxl.styles.protection.Protection’>

tagname _ = 'dxf'_
    

_class _openpyxl.styles.differential.DifferentialStyleList(_dxf =()_, _count =None_)[[source]](../_modules/openpyxl/styles/differential.html#DifferentialStyleList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

Dedupable container for differential styles.

add(_dxf_)[[source]](../_modules/openpyxl/styles/differential.html#DifferentialStyleList.add)
    

Add a differential style and return its index

append(_dxf_)[[source]](../_modules/openpyxl/styles/differential.html#DifferentialStyleList.append)
    

Check to see whether style already exists and append it if does not.

_property _count
    

dxf
    

A sequence (list or tuple) that may only contain objects of the declared type

styles
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

tagname _ = 'dxfs'_
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.styles.differential module
    * `DifferentialStyle`
      * `DifferentialStyle.alignment`
      * `DifferentialStyle.border`
      * `DifferentialStyle.fill`
      * `DifferentialStyle.font`
      * `DifferentialStyle.numFmt`
      * `DifferentialStyle.protection`
      * `DifferentialStyle.tagname`
    * `DifferentialStyleList`
      * `DifferentialStyleList.add()`
      * `DifferentialStyleList.append()`
      * `DifferentialStyleList.count`
      * `DifferentialStyleList.dxf`
      * `DifferentialStyleList.styles`
      * `DifferentialStyleList.tagname`



#### Previous topic

[openpyxl.styles.colors module](openpyxl.styles.colors.html "previous chapter")

#### Next topic

[openpyxl.styles.fills module](openpyxl.styles.fills.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.styles.differential.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.styles.fills.html "openpyxl.styles.fills module") |
  * [previous](openpyxl.styles.colors.html "openpyxl.styles.colors module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.styles package](openpyxl.styles.html) »
  * [openpyxl.styles.differential module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
