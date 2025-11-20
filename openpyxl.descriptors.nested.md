### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.descriptors.sequence.html "openpyxl.descriptors.sequence module") |
  * [previous](openpyxl.descriptors.namespace.html "openpyxl.descriptors.namespace module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.descriptors package](openpyxl.descriptors.html) »
  * [openpyxl.descriptors.nested module]()



# openpyxl.descriptors.nested module

Generic serialisable classes

_class _openpyxl.descriptors.nested.EmptyTag(_* args_, _** kw_)[[source]](../_modules/openpyxl/descriptors/nested.html#EmptyTag)
    

Bases: `Nested`, [`Bool`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Bool "openpyxl.descriptors.base.Bool")

Boolean if a tag exists or not.

from_tree(_node_)[[source]](../_modules/openpyxl/descriptors/nested.html#EmptyTag.from_tree)
    

to_tree(_tagname =None_, _value =None_, _namespace =None_)[[source]](../_modules/openpyxl/descriptors/nested.html#EmptyTag.to_tree)
    

_class _openpyxl.descriptors.nested.Nested(_name =None_, _** kw_)[[source]](../_modules/openpyxl/descriptors/nested.html#Nested)
    

Bases: [`Descriptor`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Descriptor "openpyxl.descriptors.base.Descriptor")

attribute _ = 'val'_
    

from_tree(_node_)[[source]](../_modules/openpyxl/descriptors/nested.html#Nested.from_tree)
    

nested _ = True_
    

to_tree(_tagname =None_, _value =None_, _namespace =None_)[[source]](../_modules/openpyxl/descriptors/nested.html#Nested.to_tree)
    

_class _openpyxl.descriptors.nested.NestedBool(_* args_, _** kw_)[[source]](../_modules/openpyxl/descriptors/nested.html#NestedBool)
    

Bases: `NestedValue`, [`Bool`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Bool "openpyxl.descriptors.base.Bool")

from_tree(_node_)[[source]](../_modules/openpyxl/descriptors/nested.html#NestedBool.from_tree)
    

_class _openpyxl.descriptors.nested.NestedFloat(_* args_, _** kw_)[[source]](../_modules/openpyxl/descriptors/nested.html#NestedFloat)
    

Bases: `NestedValue`, [`Float`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Float "openpyxl.descriptors.base.Float")

_class _openpyxl.descriptors.nested.NestedInteger(_* args_, _** kw_)[[source]](../_modules/openpyxl/descriptors/nested.html#NestedInteger)
    

Bases: `NestedValue`, [`Integer`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Integer "openpyxl.descriptors.base.Integer")

_class _openpyxl.descriptors.nested.NestedMinMax(_** kw_)[[source]](../_modules/openpyxl/descriptors/nested.html#NestedMinMax)
    

Bases: `Nested`, [`MinMax`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.MinMax "openpyxl.descriptors.base.MinMax")

_class _openpyxl.descriptors.nested.NestedNoneSet(_name =None_, _** kw_)[[source]](../_modules/openpyxl/descriptors/nested.html#NestedNoneSet)
    

Bases: `Nested`, [`NoneSet`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.NoneSet "openpyxl.descriptors.base.NoneSet")

_class _openpyxl.descriptors.nested.NestedSet(_name =None_, _** kw_)[[source]](../_modules/openpyxl/descriptors/nested.html#NestedSet)
    

Bases: `Nested`, [`Set`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Set "openpyxl.descriptors.base.Set")

_class _openpyxl.descriptors.nested.NestedString(_* args_, _** kw_)[[source]](../_modules/openpyxl/descriptors/nested.html#NestedString)
    

Bases: `NestedValue`, [`String`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.String "openpyxl.descriptors.base.String")

_class _openpyxl.descriptors.nested.NestedText(_* args_, _** kw_)[[source]](../_modules/openpyxl/descriptors/nested.html#NestedText)
    

Bases: `NestedValue`

Represents any nested tag with the value as the contents of the tag

from_tree(_node_)[[source]](../_modules/openpyxl/descriptors/nested.html#NestedText.from_tree)
    

to_tree(_tagname =None_, _value =None_, _namespace =None_)[[source]](../_modules/openpyxl/descriptors/nested.html#NestedText.to_tree)
    

_class _openpyxl.descriptors.nested.NestedValue(_* args_, _** kw_)[[source]](../_modules/openpyxl/descriptors/nested.html#NestedValue)
    

Bases: `Nested`, [`Convertible`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Convertible "openpyxl.descriptors.base.Convertible")

Nested tag storing the value on the ‘val’ attribute

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.descriptors.nested module
    * `EmptyTag`
      * `EmptyTag.from_tree()`
      * `EmptyTag.to_tree()`
    * `Nested`
      * `Nested.attribute`
      * `Nested.from_tree()`
      * `Nested.nested`
      * `Nested.to_tree()`
    * `NestedBool`
      * `NestedBool.from_tree()`
    * `NestedFloat`
    * `NestedInteger`
    * `NestedMinMax`
    * `NestedNoneSet`
    * `NestedSet`
    * `NestedString`
    * `NestedText`
      * `NestedText.from_tree()`
      * `NestedText.to_tree()`
    * `NestedValue`



#### Previous topic

[openpyxl.descriptors.namespace module](openpyxl.descriptors.namespace.html "previous chapter")

#### Next topic

[openpyxl.descriptors.sequence module](openpyxl.descriptors.sequence.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.descriptors.nested.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.descriptors.sequence.html "openpyxl.descriptors.sequence module") |
  * [previous](openpyxl.descriptors.namespace.html "openpyxl.descriptors.namespace module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.descriptors package](openpyxl.descriptors.html) »
  * [openpyxl.descriptors.nested module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
