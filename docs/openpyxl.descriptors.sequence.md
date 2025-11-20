### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.descriptors.serialisable.html "openpyxl.descriptors.serialisable module") |
  * [previous](openpyxl.descriptors.nested.html "openpyxl.descriptors.nested module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.descriptors package](openpyxl.descriptors.html) »
  * [openpyxl.descriptors.sequence module]()



# openpyxl.descriptors.sequence module

_class _openpyxl.descriptors.sequence.MultiSequence(_name =None_, _** kw_)[[source]](../_modules/openpyxl/descriptors/sequence.html#MultiSequence)
    

Bases: `Sequence`

Sequences can contain objects with different tags

to_tree(_tagname_ , _obj_ , _namespace =None_)[[source]](../_modules/openpyxl/descriptors/sequence.html#MultiSequence.to_tree)
    

Convert the sequence represented by the descriptor to an XML element

_class _openpyxl.descriptors.sequence.MultiSequencePart(_expected_type_ , _store_)[[source]](../_modules/openpyxl/descriptors/sequence.html#MultiSequencePart)
    

Bases: [`Alias`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Alias "openpyxl.descriptors.base.Alias")

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

_class _openpyxl.descriptors.sequence.NestedSequence(_name =None_, _** kw_)[[source]](../_modules/openpyxl/descriptors/sequence.html#NestedSequence)
    

Bases: `Sequence`

Wrap a sequence in an containing object

count _ = False_
    

from_tree(_node_)[[source]](../_modules/openpyxl/descriptors/sequence.html#NestedSequence.from_tree)
    

to_tree(_tagname_ , _obj_ , _namespace =None_)[[source]](../_modules/openpyxl/descriptors/sequence.html#NestedSequence.to_tree)
    

Convert the sequence represented by the descriptor to an XML element

_class _openpyxl.descriptors.sequence.Sequence(_name =None_, _** kw_)[[source]](../_modules/openpyxl/descriptors/sequence.html#Sequence)
    

Bases: [`Descriptor`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Descriptor "openpyxl.descriptors.base.Descriptor")

A sequence (list or tuple) that may only contain objects of the declared type

container
    

alias of `list`

expected_type
    

alias of `None`

idx_base _ = 0_
    

seq_types _ = (<class 'list'>, <class 'tuple'>)_
    

to_tree(_tagname_ , _obj_ , _namespace =None_)[[source]](../_modules/openpyxl/descriptors/sequence.html#Sequence.to_tree)
    

Convert the sequence represented by the descriptor to an XML element

unique _ = False_
    

_class _openpyxl.descriptors.sequence.UniqueSequence(_name =None_, _** kw_)[[source]](../_modules/openpyxl/descriptors/sequence.html#UniqueSequence)
    

Bases: `Sequence`

Use a set to keep values unique

container
    

alias of `set`

seq_types _ = (<class 'list'>, <class 'tuple'>, <class 'set'>)_
    

_class _openpyxl.descriptors.sequence.ValueSequence(_name =None_, _** kw_)[[source]](../_modules/openpyxl/descriptors/sequence.html#ValueSequence)
    

Bases: `Sequence`

A sequence of primitive types that are stored as a single attribute. “val” is the default attribute

attribute _ = 'val'_
    

from_tree(_node_)[[source]](../_modules/openpyxl/descriptors/sequence.html#ValueSequence.from_tree)
    

to_tree(_tagname_ , _obj_ , _namespace =None_)[[source]](../_modules/openpyxl/descriptors/sequence.html#ValueSequence.to_tree)
    

Convert the sequence represented by the descriptor to an XML element

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.descriptors.sequence module
    * `MultiSequence`
      * `MultiSequence.to_tree()`
    * `MultiSequencePart`
    * `NestedSequence`
      * `NestedSequence.count`
      * `NestedSequence.from_tree()`
      * `NestedSequence.to_tree()`
    * `Sequence`
      * `Sequence.container`
      * `Sequence.expected_type`
      * `Sequence.idx_base`
      * `Sequence.seq_types`
      * `Sequence.to_tree()`
      * `Sequence.unique`
    * `UniqueSequence`
      * `UniqueSequence.container`
      * `UniqueSequence.seq_types`
    * `ValueSequence`
      * `ValueSequence.attribute`
      * `ValueSequence.from_tree()`
      * `ValueSequence.to_tree()`



#### Previous topic

[openpyxl.descriptors.nested module](openpyxl.descriptors.nested.html "previous chapter")

#### Next topic

[openpyxl.descriptors.serialisable module](openpyxl.descriptors.serialisable.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.descriptors.sequence.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.descriptors.serialisable.html "openpyxl.descriptors.serialisable module") |
  * [previous](openpyxl.descriptors.nested.html "openpyxl.descriptors.nested module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.descriptors package](openpyxl.descriptors.html) »
  * [openpyxl.descriptors.sequence module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
