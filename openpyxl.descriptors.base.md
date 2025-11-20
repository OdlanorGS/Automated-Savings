### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.descriptors.container.html "openpyxl.descriptors.container module") |
  * [previous](openpyxl.descriptors.html "openpyxl.descriptors package") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.descriptors package](openpyxl.descriptors.html) »
  * [openpyxl.descriptors.base module]()



# openpyxl.descriptors.base module

Based on Python Cookbook 3rd Edition, 8.13 <http://chimera.labs.oreilly.com/books/1230000000393/ch08.html#_discussiuncion_130>

_class _openpyxl.descriptors.base.ASCII(_* args_, _** kw_)[[source]](../_modules/openpyxl/descriptors/base.html#ASCII)
    

Bases: `Typed`

expected_type
    

alias of `bytes`

_class _openpyxl.descriptors.base.Alias(_alias_)[[source]](../_modules/openpyxl/descriptors/base.html#Alias)
    

Bases: `Descriptor`

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

_class _openpyxl.descriptors.base.Bool(_* args_, _** kw_)[[source]](../_modules/openpyxl/descriptors/base.html#Bool)
    

Bases: `Convertible`

expected_type
    

alias of `bool`

_class _openpyxl.descriptors.base.Convertible(_* args_, _** kw_)[[source]](../_modules/openpyxl/descriptors/base.html#Convertible)
    

Bases: `Typed`

Values must be convertible to a particular type

_class _openpyxl.descriptors.base.DateTime(_* args_, _** kw_)[[source]](../_modules/openpyxl/descriptors/base.html#DateTime)
    

Bases: `Typed`

expected_type
    

alias of `datetime`

_class _openpyxl.descriptors.base.Default(_name =None_, _** kw_)[[source]](../_modules/openpyxl/descriptors/base.html#Default)
    

Bases: `Typed`

When called returns an instance of the expected type. Additional default values can be passed in to the descriptor

_class _openpyxl.descriptors.base.Descriptor(_name =None_, _** kw_)[[source]](../_modules/openpyxl/descriptors/base.html#Descriptor)
    

Bases: `object`

_class _openpyxl.descriptors.base.Float(_* args_, _** kw_)[[source]](../_modules/openpyxl/descriptors/base.html#Float)
    

Bases: `Convertible`

expected_type
    

alias of `float`

_class _openpyxl.descriptors.base.Integer(_* args_, _** kw_)[[source]](../_modules/openpyxl/descriptors/base.html#Integer)
    

Bases: `Convertible`

expected_type
    

alias of `int`

_class _openpyxl.descriptors.base.Length(_name =None_, _** kw_)[[source]](../_modules/openpyxl/descriptors/base.html#Length)
    

Bases: `Descriptor`

_class _openpyxl.descriptors.base.MatchPattern(_name =None_, _** kw_)[[source]](../_modules/openpyxl/descriptors/base.html#MatchPattern)
    

Bases: `Descriptor`

Values must match a regex pattern

allow_none _ = False_
    

_class _openpyxl.descriptors.base.Max(_** kw_)[[source]](../_modules/openpyxl/descriptors/base.html#Max)
    

Bases: `Convertible`

Values must be less than a max value

allow_none _ = False_
    

expected_type
    

alias of `float`

_class _openpyxl.descriptors.base.Min(_** kw_)[[source]](../_modules/openpyxl/descriptors/base.html#Min)
    

Bases: `Convertible`

Values must be greater than a min value

allow_none _ = False_
    

expected_type
    

alias of `float`

_class _openpyxl.descriptors.base.MinMax(_** kw_)[[source]](../_modules/openpyxl/descriptors/base.html#MinMax)
    

Bases: `Min`, `Max`

Values must be greater than min value and less than a max one

_class _openpyxl.descriptors.base.NoneSet(_name =None_, _** kw_)[[source]](../_modules/openpyxl/descriptors/base.html#NoneSet)
    

Bases: `Set`

‘none’ will be treated as None

_class _openpyxl.descriptors.base.Set(_name =None_, _** kw_)[[source]](../_modules/openpyxl/descriptors/base.html#Set)
    

Bases: `Descriptor`

Value can only be from a set of know values

_class _openpyxl.descriptors.base.String(_* args_, _** kw_)[[source]](../_modules/openpyxl/descriptors/base.html#String)
    

Bases: `Typed`

expected_type
    

alias of `str`

_class _openpyxl.descriptors.base.Text(_* args_, _** kw_)[[source]](../_modules/openpyxl/descriptors/base.html#Text)
    

Bases: `String`, `Convertible`

_class _openpyxl.descriptors.base.Tuple(_* args_, _** kw_)[[source]](../_modules/openpyxl/descriptors/base.html#Tuple)
    

Bases: `Typed`

expected_type
    

alias of `tuple`

_class _openpyxl.descriptors.base.Typed(_* args_, _** kw_)[[source]](../_modules/openpyxl/descriptors/base.html#Typed)
    

Bases: `Descriptor`

Values must of a particular type

allow_none _ = False_
    

expected_type
    

alias of `None`

nested _ = False_
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.descriptors.base module
    * `ASCII`
      * `ASCII.expected_type`
    * `Alias`
    * `Bool`
      * `Bool.expected_type`
    * `Convertible`
    * `DateTime`
      * `DateTime.expected_type`
    * `Default`
    * `Descriptor`
    * `Float`
      * `Float.expected_type`
    * `Integer`
      * `Integer.expected_type`
    * `Length`
    * `MatchPattern`
      * `MatchPattern.allow_none`
    * `Max`
      * `Max.allow_none`
      * `Max.expected_type`
    * `Min`
      * `Min.allow_none`
      * `Min.expected_type`
    * `MinMax`
    * `NoneSet`
    * `Set`
    * `String`
      * `String.expected_type`
    * `Text`
    * `Tuple`
      * `Tuple.expected_type`
    * `Typed`
      * `Typed.allow_none`
      * `Typed.expected_type`
      * `Typed.nested`



#### Previous topic

[openpyxl.descriptors package](openpyxl.descriptors.html "previous chapter")

#### Next topic

[openpyxl.descriptors.container module](openpyxl.descriptors.container.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.descriptors.base.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.descriptors.container.html "openpyxl.descriptors.container module") |
  * [previous](openpyxl.descriptors.html "openpyxl.descriptors package") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.descriptors package](openpyxl.descriptors.html) »
  * [openpyxl.descriptors.base module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
