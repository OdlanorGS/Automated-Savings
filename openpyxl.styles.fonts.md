### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.styles.named_styles.html "openpyxl.styles.named_styles module") |
  * [previous](openpyxl.styles.fills.html "openpyxl.styles.fills module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.styles package](openpyxl.styles.html) »
  * [openpyxl.styles.fonts module]()



# openpyxl.styles.fonts module

_class _openpyxl.styles.fonts.Font(_name =None_, _sz =None_, _b =None_, _i =None_, _charset =None_, _u =None_, _strike =None_, _color =None_, _scheme =None_, _family =None_, _size =None_, _bold =None_, _italic =None_, _strikethrough =None_, _underline =None_, _vertAlign =None_, _outline =None_, _shadow =None_, _condense =None_, _extend =None_)[[source]](../_modules/openpyxl/styles/fonts.html#Font)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

Font options used in styles.

UNDERLINE_DOUBLE _ = 'double'_
    

UNDERLINE_DOUBLE_ACCOUNTING _ = 'doubleAccounting'_
    

UNDERLINE_SINGLE _ = 'single'_
    

UNDERLINE_SINGLE_ACCOUNTING _ = 'singleAccounting'_
    

b
    

Values must be of type <class ‘bool’>

bold
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

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

_classmethod _from_tree(_node_)[[source]](../_modules/openpyxl/styles/fonts.html#Font.from_tree)
    

Set default value for underline if child element is present

i
    

Values must be of type <class ‘bool’>

italic
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

name
    

Values must be of type <class ‘str’>

outline
    

Values must be of type <class ‘bool’>

scheme
    

Value must be one of {‘minor’, ‘major’}

shadow
    

Values must be of type <class ‘bool’>

size
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

strike
    

Values must be of type <class ‘bool’>

strikethrough
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

sz
    

Values must be of type <class ‘float’>

tagname _ = 'font'_
    

u
    

Value must be one of {‘single’, ‘double’, ‘doubleAccounting’, ‘singleAccounting’}

underline
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

vertAlign
    

Value must be one of {‘superscript’, ‘baseline’, ‘subscript’}

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.styles.fonts module
    * `Font`
      * `Font.UNDERLINE_DOUBLE`
      * `Font.UNDERLINE_DOUBLE_ACCOUNTING`
      * `Font.UNDERLINE_SINGLE`
      * `Font.UNDERLINE_SINGLE_ACCOUNTING`
      * `Font.b`
      * `Font.bold`
      * `Font.charset`
      * `Font.color`
      * `Font.condense`
      * `Font.extend`
      * `Font.family`
      * `Font.from_tree()`
      * `Font.i`
      * `Font.italic`
      * `Font.name`
      * `Font.outline`
      * `Font.scheme`
      * `Font.shadow`
      * `Font.size`
      * `Font.strike`
      * `Font.strikethrough`
      * `Font.sz`
      * `Font.tagname`
      * `Font.u`
      * `Font.underline`
      * `Font.vertAlign`



#### Previous topic

[openpyxl.styles.fills module](openpyxl.styles.fills.html "previous chapter")

#### Next topic

[openpyxl.styles.named_styles module](openpyxl.styles.named_styles.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.styles.fonts.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.styles.named_styles.html "openpyxl.styles.named_styles module") |
  * [previous](openpyxl.styles.fills.html "openpyxl.styles.fills module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.styles package](openpyxl.styles.html) »
  * [openpyxl.styles.fonts module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
