### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.packaging.extended.html "openpyxl.packaging.extended module") |
  * [previous](openpyxl.packaging.core.html "openpyxl.packaging.core module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.packaging package](openpyxl.packaging.html) »
  * [openpyxl.packaging.custom module]()



# openpyxl.packaging.custom module

Implementation of custom properties see § 22.3 in the specification

_class _openpyxl.packaging.custom.BoolProperty(_name_ , _value_)[[source]](../_modules/openpyxl/packaging/custom.html#BoolProperty)
    

Bases: `_TypedProperty`

value
    

Values must be of type <class ‘bool’>

_class _openpyxl.packaging.custom.CustomPropertyList[[source]](../_modules/openpyxl/packaging/custom.html#CustomPropertyList)
    

Bases: [`Strict`](openpyxl.descriptors.html#openpyxl.descriptors.Strict "openpyxl.descriptors.Strict")

append(_prop_)[[source]](../_modules/openpyxl/packaging/custom.html#CustomPropertyList.append)
    

_classmethod _from_tree(_tree_)[[source]](../_modules/openpyxl/packaging/custom.html#CustomPropertyList.from_tree)
    

Create list from OOXML element

_property _names
    

List of property names

props
    

A sequence (list or tuple) that may only contain objects of the declared type

to_tree()[[source]](../_modules/openpyxl/packaging/custom.html#CustomPropertyList.to_tree)
    

_class _openpyxl.packaging.custom.DateTimeProperty(_name_ , _value_)[[source]](../_modules/openpyxl/packaging/custom.html#DateTimeProperty)
    

Bases: `_TypedProperty`

value
    

Values must be of type <class ‘datetime.datetime’>

_class _openpyxl.packaging.custom.FloatProperty(_name_ , _value_)[[source]](../_modules/openpyxl/packaging/custom.html#FloatProperty)
    

Bases: `_TypedProperty`

value
    

Values must be of type <class ‘float’>

_class _openpyxl.packaging.custom.IntProperty(_name_ , _value_)[[source]](../_modules/openpyxl/packaging/custom.html#IntProperty)
    

Bases: `_TypedProperty`

value
    

Values must be of type <class ‘int’>

_class _openpyxl.packaging.custom.LinkProperty(_name_ , _value_)[[source]](../_modules/openpyxl/packaging/custom.html#LinkProperty)
    

Bases: `_TypedProperty`

value
    

Values must be of type <class ‘str’>

_class _openpyxl.packaging.custom.NestedBoolText(_* args_, _** kw_)[[source]](../_modules/openpyxl/packaging/custom.html#NestedBoolText)
    

Bases: [`Bool`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Bool "openpyxl.descriptors.base.Bool"), [`NestedText`](openpyxl.descriptors.nested.html#openpyxl.descriptors.nested.NestedText "openpyxl.descriptors.nested.NestedText")

Descriptor for handling nested elements with the value stored in the text part

_class _openpyxl.packaging.custom.StringProperty(_name_ , _value_)[[source]](../_modules/openpyxl/packaging/custom.html#StringProperty)
    

Bases: `_TypedProperty`

value
    

Values must be of type <class ‘str’>

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.packaging.custom module
    * `BoolProperty`
      * `BoolProperty.value`
    * `CustomPropertyList`
      * `CustomPropertyList.append()`
      * `CustomPropertyList.from_tree()`
      * `CustomPropertyList.names`
      * `CustomPropertyList.props`
      * `CustomPropertyList.to_tree()`
    * `DateTimeProperty`
      * `DateTimeProperty.value`
    * `FloatProperty`
      * `FloatProperty.value`
    * `IntProperty`
      * `IntProperty.value`
    * `LinkProperty`
      * `LinkProperty.value`
    * `NestedBoolText`
    * `StringProperty`
      * `StringProperty.value`



#### Previous topic

[openpyxl.packaging.core module](openpyxl.packaging.core.html "previous chapter")

#### Next topic

[openpyxl.packaging.extended module](openpyxl.packaging.extended.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.packaging.custom.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.packaging.extended.html "openpyxl.packaging.extended module") |
  * [previous](openpyxl.packaging.core.html "openpyxl.packaging.core module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.packaging package](openpyxl.packaging.html) »
  * [openpyxl.packaging.custom module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
