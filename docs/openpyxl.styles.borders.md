### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.styles.builtins.html "openpyxl.styles.builtins module") |
  * [previous](openpyxl.styles.alignment.html "openpyxl.styles.alignment module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.styles package](openpyxl.styles.html) »
  * [openpyxl.styles.borders module]()



# openpyxl.styles.borders module

_class _openpyxl.styles.borders.Border(_left =None_, _right =None_, _top =None_, _bottom =None_, _diagonal =None_, _diagonal_direction =None_, _vertical =None_, _horizontal =None_, _diagonalUp =False_, _diagonalDown =False_, _outline =True_, _start =None_, _end =None_)[[source]](../_modules/openpyxl/styles/borders.html#Border)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

Border positioning for use in styles.

bottom
    

Values must be of type <class ‘openpyxl.styles.borders.Side’>

diagonal
    

Values must be of type <class ‘openpyxl.styles.borders.Side’>

diagonalDown
    

Values must be of type <class ‘bool’>

diagonalUp
    

Values must be of type <class ‘bool’>

end
    

Values must be of type <class ‘openpyxl.styles.borders.Side’>

horizontal
    

Values must be of type <class ‘openpyxl.styles.borders.Side’>

left
    

Values must be of type <class ‘openpyxl.styles.borders.Side’>

outline
    

Values must be of type <class ‘bool’>

right
    

Values must be of type <class ‘openpyxl.styles.borders.Side’>

start
    

Values must be of type <class ‘openpyxl.styles.borders.Side’>

tagname _ = 'border'_
    

top
    

Values must be of type <class ‘openpyxl.styles.borders.Side’>

vertical
    

Values must be of type <class ‘openpyxl.styles.borders.Side’>

_class _openpyxl.styles.borders.Side(_style =None_, _color =None_, _border_style =None_)[[source]](../_modules/openpyxl/styles/borders.html#Side)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

Border options for use in styles. Caution: if you do not specify a border_style, other attributes will have no effect !

border_style
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

color
    

Values must be of type <class ‘openpyxl.styles.colors.Color’>

style
    

Value must be one of {‘dotted’, ‘medium’, ‘dashed’, ‘mediumDashDot’, ‘hair’, ‘thin’, ‘double’, ‘slantDashDot’, ‘thick’, ‘dashDot’, ‘mediumDashed’, ‘dashDotDot’, ‘mediumDashDotDot’}

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.styles.borders module
    * `Border`
      * `Border.bottom`
      * `Border.diagonal`
      * `Border.diagonalDown`
      * `Border.diagonalUp`
      * `Border.end`
      * `Border.horizontal`
      * `Border.left`
      * `Border.outline`
      * `Border.right`
      * `Border.start`
      * `Border.tagname`
      * `Border.top`
      * `Border.vertical`
    * `Side`
      * `Side.border_style`
      * `Side.color`
      * `Side.style`



#### Previous topic

[openpyxl.styles.alignment module](openpyxl.styles.alignment.html "previous chapter")

#### Next topic

[openpyxl.styles.builtins module](openpyxl.styles.builtins.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.styles.borders.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.styles.builtins.html "openpyxl.styles.builtins module") |
  * [previous](openpyxl.styles.alignment.html "openpyxl.styles.alignment module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.styles package](openpyxl.styles.html) »
  * [openpyxl.styles.borders module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
