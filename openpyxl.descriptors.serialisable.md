### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.html "openpyxl.drawing package") |
  * [previous](openpyxl.descriptors.sequence.html "openpyxl.descriptors.sequence module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.descriptors package](openpyxl.descriptors.html) »
  * [openpyxl.descriptors.serialisable module]()



# openpyxl.descriptors.serialisable module

_class _openpyxl.descriptors.serialisable.Serialisable[[source]](../_modules/openpyxl/descriptors/serialisable.html#Serialisable)
    

Bases: `object`

Objects can serialise to XML their attributes and child objects. The following class attributes are created by the metaclass at runtime: __attrs__ = attributes __nested__ = single-valued child treated as an attribute __elements__ = child elements

_classmethod _from_tree(_node_)[[source]](../_modules/openpyxl/descriptors/serialisable.html#Serialisable.from_tree)
    

Create object from XML

idx_base _ = 0_
    

namespace _ = None_
    

_property _tagname
    

to_tree(_tagname =None_, _idx =None_, _namespace =None_)[[source]](../_modules/openpyxl/descriptors/serialisable.html#Serialisable.to_tree)
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.descriptors.serialisable module
    * `Serialisable`
      * `Serialisable.from_tree()`
      * `Serialisable.idx_base`
      * `Serialisable.namespace`
      * `Serialisable.tagname`
      * `Serialisable.to_tree()`



#### Previous topic

[openpyxl.descriptors.sequence module](openpyxl.descriptors.sequence.html "previous chapter")

#### Next topic

[openpyxl.drawing package](openpyxl.drawing.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.descriptors.serialisable.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.html "openpyxl.drawing package") |
  * [previous](openpyxl.descriptors.sequence.html "openpyxl.descriptors.sequence module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.descriptors package](openpyxl.descriptors.html) »
  * [openpyxl.descriptors.serialisable module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
