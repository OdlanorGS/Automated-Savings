### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.styles.fonts.html "openpyxl.styles.fonts module") |
  * [previous](openpyxl.styles.differential.html "openpyxl.styles.differential module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.styles package](openpyxl.styles.html) »
  * [openpyxl.styles.fills module]()



# openpyxl.styles.fills module

_class _openpyxl.styles.fills.Fill[[source]](../_modules/openpyxl/styles/fills.html#Fill)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

Base class

_classmethod _from_tree(_el_)[[source]](../_modules/openpyxl/styles/fills.html#Fill.from_tree)
    

Create object from XML

tagname _ = 'fill'_
    

_class _openpyxl.styles.fills.GradientFill(_type ='linear'_, _degree =0_, _left =0_, _right =0_, _top =0_, _bottom =0_, _stop =()_)[[source]](../_modules/openpyxl/styles/fills.html#GradientFill)
    

Bases: `Fill`

Fill areas with gradient

Two types of gradient fill are supported:

>   * A type=’linear’ gradient interpolates colours between a set of specified Stops, across the length of an area. The gradient is left-to-right by default, but this orientation can be modified with the degree attribute. A list of Colors can be provided instead and they will be positioned with equal distance between them.
> 
>   * A type=’path’ gradient applies a linear gradient from each edge of the area. Attributes top, right, bottom, left specify the extent of fill from the respective borders. Thus top=”0.2” will fill the top 20% of the cell.
> 
> 


bottom
    

Values must be of type <class ‘float’>

degree
    

Values must be of type <class ‘float’>

fill_type
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

left
    

Values must be of type <class ‘float’>

right
    

Values must be of type <class ‘float’>

stop
    

tagname _ = 'gradientFill'_
    

to_tree(_tagname =None_, _namespace =None_, _idx =None_)[[source]](../_modules/openpyxl/styles/fills.html#GradientFill.to_tree)
    

top
    

Values must be of type <class ‘float’>

type
    

Value must be one of {‘linear’, ‘path’}

_class _openpyxl.styles.fills.PatternFill(_patternType=None_ , _fgColor= <openpyxl.styles.colors.Color object> Parameters: rgb='00000000'_, _indexed=None_ , _auto=None_ , _theme=None_ , _tint=0.0_ , _type='rgb'_ , _bgColor= <openpyxl.styles.colors.Color object> Parameters: rgb='00000000'_, _indexed=None_ , _auto=None_ , _theme=None_ , _tint=0.0_ , _type='rgb'_ , _fill_type=None_ , _start_color=None_ , _end_color=None_)[[source]](../_modules/openpyxl/styles/fills.html#PatternFill)
    

Bases: `Fill`

Area fill patterns for use in styles. Caution: if you do not specify a fill_type, other attributes will have no effect !

bgColor
    

Values must be of type <class ‘openpyxl.styles.colors.Color’>

end_color
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

fgColor
    

Values must be of type <class ‘openpyxl.styles.colors.Color’>

fill_type
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

patternType
    

Value must be one of {‘solid’, ‘gray125’, ‘darkGrid’, ‘darkVertical’, ‘gray0625’, ‘lightHorizontal’, ‘lightDown’, ‘lightUp’, ‘darkGray’, ‘darkHorizontal’, ‘lightGray’, ‘lightTrellis’, ‘darkUp’, ‘mediumGray’, ‘lightGrid’, ‘darkDown’, ‘darkTrellis’, ‘lightVertical’}

start_color
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

tagname _ = 'patternFill'_
    

to_tree(_tagname =None_, _idx =None_)[[source]](../_modules/openpyxl/styles/fills.html#PatternFill.to_tree)
    

_class _openpyxl.styles.fills.Stop(_color_ , _position_)[[source]](../_modules/openpyxl/styles/fills.html#Stop)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

color
    

Values must be of type <class ‘openpyxl.styles.colors.Color’>

position
    

Values must be of type <class ‘float’>

tagname _ = 'stop'_
    

_class _openpyxl.styles.fills.StopList(_name =None_, _** kw_)[[source]](../_modules/openpyxl/styles/fills.html#StopList)
    

Bases: [`Sequence`](openpyxl.descriptors.sequence.html#openpyxl.descriptors.sequence.Sequence "openpyxl.descriptors.sequence.Sequence")

expected_type
    

alias of `Stop`

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.styles.fills module
    * `Fill`
      * `Fill.from_tree()`
      * `Fill.tagname`
    * `GradientFill`
      * `GradientFill.bottom`
      * `GradientFill.degree`
      * `GradientFill.fill_type`
      * `GradientFill.left`
      * `GradientFill.right`
      * `GradientFill.stop`
      * `GradientFill.tagname`
      * `GradientFill.to_tree()`
      * `GradientFill.top`
      * `GradientFill.type`
    * `PatternFill`
      * `PatternFill.bgColor`
      * `PatternFill.end_color`
      * `PatternFill.fgColor`
      * `PatternFill.fill_type`
      * `PatternFill.patternType`
      * `PatternFill.start_color`
      * `PatternFill.tagname`
      * `PatternFill.to_tree()`
    * `Stop`
      * `Stop.color`
      * `Stop.position`
      * `Stop.tagname`
    * `StopList`
      * `StopList.expected_type`



#### Previous topic

[openpyxl.styles.differential module](openpyxl.styles.differential.html "previous chapter")

#### Next topic

[openpyxl.styles.fonts module](openpyxl.styles.fonts.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.styles.fills.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.styles.fonts.html "openpyxl.styles.fonts module") |
  * [previous](openpyxl.styles.differential.html "openpyxl.styles.differential module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.styles package](openpyxl.styles.html) »
  * [openpyxl.styles.fills module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
